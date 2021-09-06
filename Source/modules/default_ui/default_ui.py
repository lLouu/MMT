from tkinter import *
from json import *
from module_loaders import *

class App():

    def __init__(self, winPath="Source/modules/default_ui/appWindow.json", compoPath="Source/modules/default_ui/appCompo.json", propertiesPath="Source/modules/default_ui/appProperties.json"):
        self.setup(winPath, compoPath, propertiesPath)
        self.load()
    
    def setup(self, winPath, compoPath, propertiesPath):
        self.window = self.new_win(self.load_json(winPath))
        self.compo = self.load_json(compoPath)
        self.properties = self.load_json(propertiesPath)

    def new_win(self, json):
        win = Tk()
        keys = list(json.keys())
        if "dim" in keys : win.geometry(json["dim"])
        if "min_dim" in keys : win.minsize(json["min_dim"][0], json["min_dim"][1])
        if "title" in keys : win.title(json["title"])
        return win
    
    def load_json(self, path):
        content = getContent(path)
        if content == None:
            content = '{}'
        try:
            json = loads(content)
        except:
            error(1, 1, 1, "json file can't be read")
            json = loads('{}')
        return json
    
    def load(self):
        self.construct(self.compo, self.window)
        self.pack(self.compo, self.properties)
    
    def construct(self, dic, parrent):
        keys = list(dic.keys())
        if "type" in keys:
            if dic["type"] == "Label":
                obj = Label(parrent)
            elif dic["type"] == "Button":
                obj = Button(parrent)
            elif dic["type"] == "Entry":
                obj = Entry(parrent)
            elif dic["type"] == "Radio":
                obj = Radiobutton(parrent)
            elif dic["type"] == "Check":
                obj = Checkbutton(parrent)
            elif dic["type"] == "Scale":
                obj = Scale(parrent)
            elif dic["type"] == "Text":
                obj = Text(parrent)
            elif dic["type"] == "LabelFrame":
                obj = LabelFrame(parrent)
            elif dic["type"] == "Canvas":
                obj = Canvas(parrent)
            elif dic["type"] == "Listbox":
                obj = Listbox(parrent)
            elif dic["type"] == "Menu":
                obj = Menu(parrent)
            else:
                obj = Frame(parrent,
                            bg="white" if not "bg" in keys else dic["bg"],
                            width=0 if not "width" in keys else dic["width"],
                            height=0 if not "height" in keys else dic["height"])
        else:
            obj = Frame(parrent,
                        bg="white" if not "bg" in keys else dic["bg"],
                        width=10 if not "width" in keys else dic["width"],
                        height=10 if not "height" in keys else dic["height"])
        
        dic["obj"] = obj

        if "include" in keys:
            for index in list(dic["include"].keys()):
                self.construct(dic["include"][index], obj)

    def pack(self, obj, pack):
        keys = list(pack.keys())
        if "include" in keys:
            for index in list(obj["include"].keys()):
                self.pack(obj["include"][index], pack["include"][index])
        obj["obj"].pack(expand=NO if not "expand" in keys else pack["expand"],
                        fill=NONE if not "fill" in keys else pack["fill"],
                        side=TOP if not "side" in keys else pack["side"])

    def run(self):
        self.window.mainloop()


def main_ui():
    app = App()
    app.run()
