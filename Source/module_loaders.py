from os import path as p, remove
from glob import glob
from errors import error

class Option:
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

def read_opt(path):
    opt = Option()
    if not(p.exists(path)):
        error(0, 3, 1, path + " not found")
        return opt
    if not(p.isfile(path)):
        error(0, 4, 1, path + " not readble")
        return opt

    file = open(path, "r")
    content = file.read()
    file.close()

    lines = content.split('\n')
    for l in lines:
        if len(l) > 0 and l[0] != '#':
            o = simplify(l)
            if len(o) >= 2 and o[1] != '':
                if o[0] == "overide_file":
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
                    # need a validation
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
        list["path"] += glob(path + "\*")
    for i in range(len(list["path"])):
        if p.isfile(list["path"][i]):
            error(0, 7, 0, list["path"][i] + " is not a module")
            del list["path"][i]
        else:
            list["name"] += [list["path"][i].split("\\")[-1]]
    return list

def launch_ui(opt):
    return True

def auto_update():
    return True

def loader():
    pass
