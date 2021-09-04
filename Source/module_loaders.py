from os import path as p
from sys import path as pyPath
from glob import glob
from errors import error

class Option:
    option_file = "Source\\options.dat"
    autoup = False
    module_folder = ["Source\\modules"]
    show_warning = False
    ask_for_default = True
    default_ui = None

    def __init__(self):
        pass

    def __str__(self):
        return "autoup : " + str(self.autoup) + "\n" + "show_warning : " + str(self.show_warning) + "\n" + "ask_for_default : " + str(self.ask_for_default) + "\n" + "default_ui : " + str(self.default_ui) + "\n"

def simplify(o):
    new_o = ''
    o = str(o)

    take = 0
    for letter in o:
        if letter == ' ':
            if take == 1:
                take = -1
        elif letter == "=":
            take = 0
            new_o += letter
        elif take != -1:
            new_o += letter
            if take == 0:
                take = 1


    return new_o.split('=')

def getContent(path):
    if not(p.exists(path)):
        error(0, 3, 1, path + " not found")
        return None
    if not(p.isfile(path)):
        error(0, 4, 1, path + " not readble")
        return None

    file = open(path, "r")
    content = file.read()
    file.close()

    return content

def read_opt(path):
    opt = Option()
    content = getContent(path)
    if content == None:
        return opt

    lines = content.split('\n')
    for l in lines:
        if len(l) > 0 and l[0] != '#':
            o = simplify(l)
            if len(o) >= 2 and o[1] != '':
                if o[0] == "overide_file":
                    opt.option_file = o[1]
                    over_opt = read_opt(o[1])
                    return over_opt
                elif o[0] == "autoup":
                    if o[1][0] == "t" or o[1][0] == "T" or o[1][0] == "1":
                        opt.autoup = True
                    else:
                        opt.autoup = False
                elif o[0] == "module_folder":
                    list = o[1].split(",")
                    for ele in list:
                        if not(ele in opt.module_folder):
                            opt.module_folder += ele
                elif o[0] == "show_warnings":
                    if o[1][0] == "t" or o[1][0] == "T" or o[1][0] == "1":
                        opt.show_warning = True
                    else:
                        opt.show_warning = False
                elif o[0] == "ask_for_default":
                    if o[1][0] == "f" or o[1][0] == "F" or o[1][0] == "0":
                        opt.ask_for_default = False
                    else:
                        opt.ask_for_default = True
                elif o[0] == "default_ui":
                    opt.default_ui = o[1]
                else:
                    error(0, 5, 0, "unkown option : " + o[0])
            else:
                if len(o) < 2:
                    error(0, 6, 0)

    return opt

def getModules(opt = Option()):
    list = {"path": [], 
            "name": []}
    for path in opt.module_folder:
        list["path"] += glob(path + "\\*")
    for i in range(len(list["path"])):
        if p.isfile(list["path"][i]):
            error(0, 7, 0, list["path"][i] + " is not a module")
            del list["path"][i]
        else:
            list["name"].append(list["path"][i].split("\\")[-1])
    return list

def launch_ui(opt, list):
    loaded = False
    if opt.default_ui != None:
        if opt.default_ui in list["name"]:
            path = list["path"][list["name"].index(opt.default_ui)]
            content = getContent(path + "\\lib.info").split('\n')
            if "main_ui" in content:
                loader(opt.default_ui, "main_ui", path)()
                loaded = True
            else:
                error(0, 8, 1, opt.default_ui + " is not a ui module")
        else:
            error(0, 9, 1, opt.default_ui + " is not installed")
    if not loaded:
        ui_modules = {"name": [],
                      "path": []}
        for i in range(len(list["name"])):
            content = getContent(list["path"][i] + "\\lib.info").split('\n')
            if "main_ui" in content:
                ui_modules["path"].append(list["path"][i])
                ui_modules["name"].append(list["name"][i])
        l = len(ui_modules["path"])
        if l == 1 or (l > 1 and not opt.ask_for_default):
            loader(ui_modules["name"][0], "main_ui", ui_modules["path"][0])()
            loaded = True
        elif l != 0:
            index = 0
            print("Multiple ui modules have been founded, which one do you want to use :\n")
            for i in range(len(ui_modules["name"])):
                print("[" + str(i+1) + "] - " + ui_modules["name"][i] + "\n")
            index = int(input()) - 1
            if not 0 <= index < len(ui_modules["name"]):
                print("\nInvalid Input, taking the first UI module as default")
                index = 0
            print("\n\nDo you want to make" + ui_modules["name"][index] + "your default ui ? (Y/N)")
            answer = input()
            if(answer == "Y" or answer == 'y'):
                setDefaultUI(opt, ui_modules["name"][index])
            loader(ui_modules["name"][index], "main_ui", ui_modules["path"][index])()
            loaded = True

    return loaded

def setDefaultUI(opt, ui_module):
    content = getContent(opt.option_file).split('\n')
    if content == None:
        return False
    finded = False
    for i in range(len(content)):
        buffer = 0
        while buffer < len(content[i]) and content[i][buffer] == ' ':
            buffer += 1
        if len(content[i]) >= 10 + buffer:
            if content[i][buffer:buffer+10] == "default_ui":
                finded = True
                content[i] = "default_ui=" + ui_module
    if not finded:
        content.append("default_ui=" + ui_module)
    
    content = "\n".join(content)
    file = open(opt.option_file, "w")
    file.write(content)
    file.close()
    return True



# from package import name as loader(package, name)
# loader(package, name)(<vars>) will execute name with <vars>
# a = loader(package, name) will allow a(<vars>) to execute name with <vars>
# why don't we learn that and have to find this... beautiful thing by ourselves ;--;
def loader(package, name, path = ''):
    if path != '':
        pyPath.append(path)
    return getattr(__import__(package, fromlist=[name]), name)


def auto_update():
    return True
