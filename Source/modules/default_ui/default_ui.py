from tkinter import *
from json import *
from module_loaders import *

class App():

    def __init__(self, winPath="Source/modules/default_ui/appWindow.json", compoPath="Source/modules/default_ui/appCompo.json", propertiesPath="Source/modules/default_ui/appProperties.json"):
        self.setup(winPath, compoPath, propertiesPath)
        self.load()
    
    def setup(self, winPath, compoPath, propertiesPath):
        self.hasMenu = False
        self.menuName = None

        self.window = self.new_win(self.load_json(winPath))
        self.compo = self.load_json(compoPath)
        self.properties = self.load_json(propertiesPath)

    def new_win(self, json):
        win = Tk()
        keys = list(json.keys())
        if "dim" in keys : win.geometry(json["dim"])
        if "min_dim" in keys : win.minsize(json["min_dim"][0], json["min_dim"][1])
        if "title" in keys : win.title(json["title"])
        if "iconbitmap" in keys : win.iconbitmap(json["iconbitmap"])
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
        if self.hasMenu:
            self.setMenu()

        self.window.update_idletasks()

    def empty_method(self, second=None):
        pass

    def get_StrVar(self, dic):
        return loader(dic["package"], dic["name"], '' if not "path" in list(dic.keys()) else dic["path"])(self)
    
    def object(self, st, value):
        if st == "Double":
            return DoubleVar().set(value)
        elif st == "String":
            return StringVar().set(str(value))
        elif st == "Bool":
            return BooleanVar().set(value)
        else:
            return IntVar().set(value)
    

    ## TODO - Scroll bars && Canvas && Menus
    def construct(self, compo, parrent):
        for index in list(compo.keys()):
            dic = compo[index]
            keys = list(dic.keys())
            if "type" in keys:
                if dic["type"] == "Label":
                    obj = Label(parrent,
                                anchor=CENTER if not "anchor" in keys else dic["anchor"],
                                bg="white" if not "bg" in keys else dic["bg"],
                                bitmap="" if not "bitmap" in keys else dic["bitmap"],
                                bd=0 if not "bd" in keys else dic["bd"],
                                cursor="arrow" if not "cursor" in keys else dic["cursor"],
                                font=("Times", "9") if not "font" in keys else dic["font"],
                                fg="black" if not "fg" in keys else dic["fg"],
                                height=0 if not "height" in keys else dic["height"],
                                image="" if not "image" in keys else dic["image"],
                                justify=CENTER if not "justify" in keys else dic["justify"],
                                padx=0 if not "padx" in keys else dic["padx"],
                                pady=0 if not "pady" in keys else dic["pady"],
                                relief=FLAT if not "relief" in keys else dic["relief"],
                                text="" if not "text" in keys else dic["text"],
                                textvariable=None if not "textvariable" in keys else dic["textvariable"],
                                underline=-1 if not "underline" in keys else dic["underline"],
                                width=0 if not "width" in keys else dic["width"],
                                wraplength=0 if not "wraplength" in keys else dic["wraplength"])
                elif dic["type"] == "Button":
                    obj = Button(parrent,
                                activebackground="gray" if not "activebackground" in keys else dic["activebackground"],
                                activeforeground="black" if not "activeforeground" in keys else dic["activeforeground"],
                                bd=1 if not "bd" in keys else dic["bd"],
                                bg="white" if not "bg" in keys else dic["bg"],
                                command=self.empty_method if not "command" in keys else 
                                    lambda: loader(dic["command"]["package"], dic["command"]["name"],
                                        '' if not "path" in list(dic["command"].keys()) else dic["command"]["path"])
                                        (self, None if not "entry" in list(dic["command"].keys()) else dic["command"]["entry"]),
                                font=("Times", "9") if not "font" in keys else dic["font"],
                                fg="black" if not "fg" in keys else dic["fg"],
                                height=0 if not "height" in keys else dic["height"],
                                highlightcolor="white" if not "highlightcolor" in keys else dic["highlightcolor"],
                                image="" if not "image" in keys else dic["image"],
                                justify=CENTER if not "justify" in keys else dic["justify"],
                                padx=0 if not "padx" in keys else dic["padx"],
                                pady=0 if not "pady" in keys else dic["pady"],
                                relief=FLAT if not "relief" in keys else dic["relief"],
                                text="" if not "text" in keys else dic["text"],
                                textvariable=None if not "textvariable" in keys else self.get_StrVar(dic["textvariable"]),
                                state=NORMAL if not "state" in keys else dic["state"],
                                underline=-1 if not "underline" in keys else dic["underline"],
                                width=0 if not "width" in keys else dic["width"],
                                wraplength=0 if not "wraplength" in keys else dic["wraplength"])
                elif dic["type"] == "Entry":
                    obj = Entry(parrent,
                                bd=1 if not "bd" in keys else dic["bd"],
                                bg="white" if not "bg" in keys else dic["bg"],
                                cursor="arrow" if not "cursor" in keys else dic["cursor"],
                                font=("Times", "9") if not "font" in keys else dic["font"],
                                exportselection=0 if not "exportselection" in keys else dic["exportselection"],
                                fg="black" if not "fg" in keys else dic["fg"],
                                highlightcolor="white" if not "highlightcolor" in keys else dic["highlightcolor"],
                                justify=CENTER if not "justify" in keys else dic["justify"],
                                relief=FLAT if not "relief" in keys else dic["relief"],
                                selectbackground="blue" if not "selectbackground" in keys else dic["selectbackground"],
                                selectborderwidth=1 if not "selectborderwidth" in keys else dic["selectbackground"],
                                selectforeground="white" if not "selectforeground" in keys else dic["selectforeground"],
                                show="tree headings" if not "show" in keys else dic["show"],
                                state=NORMAL if not "state" in keys else dic["state"],
                                textvariable=None if not "textvariable" in keys else self.get_StrVar(dic["textvariable"]),
                                width=0 if not "width" in keys else dic["width"])
                elif dic["type"] == "Radio":
                    obj = Radiobutton(parrent,
                                    activebackground="gray" if not "activebackground" in keys else dic["activebackground"],
                                    activeforeground="black" if not "activeforeground" in keys else dic["activeforeground"],
                                    anchor=CENTER if not "anchor" in keys else dic["anchor"],
                                    bg="white" if not "bg" in keys else dic["bg"],
                                    bitmap="" if not "bitmap" in keys else dic["bitmap"],
                                    bd=0 if not "bd" in keys else dic["bd"],
                                    cursor="arrow" if not "cursor" in keys else dic["cursor"],
                                    command=self.empty_method if not "command" in keys else 
                                                lambda: loader(dic["command"]["package"], dic["command"]["name"],
                                                '' if not "path" in list(dic["command"].keys()) else dic["command"]["path"])
                                                (self, None if not "entry" in list(dic["command"].keys()) else dic["command"]["entry"]),
                                    font=("Times", "9") if not "font" in keys else dic["font"],
                                    fg="black" if not "fg" in keys else dic["fg"],
                                    height=0 if not "height" in keys else dic["height"],
                                    highlightbackground="white" if not "highlightbackground" in keys else dic["highlightbackground"],
                                    highlightcolor="white" if not "highlightcolor" in keys else dic["highlightcolor"],
                                    image="" if not "image" in keys else dic["image"],
                                    justify=CENTER if not "justify" in keys else dic["justify"],
                                    padx=0 if not "padx" in keys else dic["padx"],
                                    pady=0 if not "pady" in keys else dic["pady"],
                                    relief=FLAT if not "relief" in keys else dic["relief"],
                                    selectcolor="white" if not "selectcolor" in keys else dic["selectcolor"],
                                    selectimage="" if not "selectimage" in keys else dic["selectimage"],
                                    text="" if not "text" in keys else dic["text"],
                                    textvariable=None if not "textvariable" in keys else self.get_StrVar(dic["textvariable"]),
                                    state=NORMAL if not "state" in keys else dic["state"],
                                    underline=-1 if not "underline" in keys else dic["underline"],
                                    value=0 if not "value" in keys else dic["value"],
                                    variable=IntVar() if not "variable" in keys else loader(dic["variable"]["package"], dic["variable"]["name"], 
                                                                                            '' if not "path" in list(dic["variable"].keys()) else dic["variable"]["path"])
                                                                                            (self, None if not "entry" in list(dic["variable"].keys()) else dic["variable"]["entry"]),
                                    width=0 if not "width" in keys else dic["width"],
                                    wraplength=0 if not "wraplength" in keys else dic["wraplength"])
                elif dic["type"] == "Check":
                    obj = Checkbutton(parrent,
                                    activebackground="gray" if not "activebackground" in keys else dic["activebackground"],
                                    activeforeground="black" if not "activeforeground" in keys else dic["activeforeground"],
                                    bg="white" if not "bg" in keys else dic["bg"],
                                    bitmap="" if not "bitmap" in keys else dic["bitmap"],
                                    bd=0 if not "bd" in keys else dic["bd"],
                                    cursor="arrow" if not "cursor" in keys else dic["cursor"],
                                    command=self.empty_method if not "command" in keys else 
                                                lambda: loader(dic["command"]["package"], dic["command"]["name"],
                                                '' if not "path" in list(dic["command"].keys()) else dic["command"]["path"])
                                                (self, None if not "entry" in list(dic["command"].keys()) else dic["command"]["entry"]),
                                    disabledforeground="gray",
                                    font=("Times", "9") if not "font" in keys else dic["font"],
                                    fg="black" if not "fg" in keys else dic["fg"],
                                    height=0 if not "height" in keys else dic["height"],
                                    highlightcolor="white" if not "highlightcolor" in keys else dic["highlightcolor"],
                                    image="" if not "image" in keys else dic["image"],
                                    justify=CENTER if not "justify" in keys else dic["justify"],
                                    offvalue=0 if not "offvalue" in keys else dic["offvalue"],
                                    onvalue=1 if not "onvalue" in keys else dic["onvalue"],
                                    padx=0 if not "padx" in keys else dic["padx"],
                                    pady=0 if not "pady" in keys else dic["pady"],
                                    relief=FLAT if not "relief" in keys else dic["relief"],
                                    selectcolor="white" if not "selectcolor" in keys else dic["selectcolor"],
                                    selectimage="" if not "selectimage" in keys else dic["selectimage"],
                                    text="" if not "text" in keys else dic["text"],
                                    textvariable=None if not "textvariable" in keys else self.get_StrVar(dic["textvariable"]),
                                    state=NORMAL if not "state" in keys else dic["state"],
                                    underline=-1 if not "underline" in keys else dic["underline"],
                                    variable=IntVar() if not "variable" in keys else loader(dic["variable"]["package"], dic["variable"]["name"], 
                                                                                            '' if not "path" in list(dic["variable"].keys()) else dic["variable"]["path"])
                                                                                            (self, None if not "entry" in list(dic["variable"].keys()) else dic["variable"]["entry"]),
                                    width=0 if not "width" in keys else dic["width"],
                                    wraplength=0 if not "wraplength" in keys else dic["wraplength"])
                elif dic["type"] == "Scale":
                    obj = Scale(parrent,
                                activebackground="gray" if not "activebackground" in keys else dic["activebackground"],
                                bg="white" if not "bg" in keys else dic["bg"],
                                bd=0 if not "bd" in keys else dic["bd"],
                                cursor="arrow" if not "cursor" in keys else dic["cursor"],
                                command=self.empty_method if not "command" in keys else 
                                            lambda: loader(dic["command"]["package"], dic["command"]["name"],
                                            '' if not "path" in list(dic["command"].keys()) else dic["command"]["path"])
                                            (self, None if not "entry" in list(dic["command"].keys()) else dic["command"]["entry"]),
                                digits=IntVar().set(1) if not "digits" in keys else self.object(dic["digits"]["type"], dic["digits"]["value"]),
                                font=("Times", "9") if not "font" in keys else dic["font"],
                                fg="black" if not "fg" in keys else dic["fg"],
                                from_=1 if not "from" in keys else dic["from"],
                                highlightbackground="white" if not "highlightbackground" in keys else dic["highlightbackground"],
                                highlightcolor="white" if not "highlightcolor" in keys else dic["highlightcolor"],
                                label="" if not "label" in keys else dic["label"],
                                length=100 if not "lenght" in keys else dic["lenght"],
                                orient=HORIZONTAL if not "orient" in keys else dic["orient"],
                                relief=FLAT if not "relief" in keys else dic["relief"],
                                repeatdelay=300 if not "repeatdelay" in keys else dic["repeatdelay"],
                                resolution=1 if not "resolution" in keys else dic["resolution"],
                                showvalue=1 if not "showvalue" in keys else dic["showvalue"],
                                sliderlength=30 if not "sliderlenght" in keys else dic["sliderlenght"],
                                state=NORMAL if not "state" in keys else dic["state"],
                                takefocus=1 if not "takefocus" in keys else dic["takefocus"],
                                tickinterval=0 if not "tickinterval" in keys else dic["tickinterval"],
                                to=100 if not "to" in keys else dic["to"],
                                troughcolor="gray" if not "troughcolor" in keys else dic["troughcolor"],
                                variable=IntVar() if not "variable" in keys else loader(dic["variable"]["package"], dic["variable"]["name"], 
                                                                                        '' if not "path" in list(dic["variable"].keys()) else dic["variable"]["path"])
                                                                                        (self, None if not "entry" in list(dic["variable"].keys()) else dic["variable"]["entry"]),
                                width=20 if not "width" in keys else dic["width"])
                elif dic["type"] == "Text":
                    obj = Text(parrent,
                            bg="white" if not "bg" in keys else dic["bg"],
                            bd=0 if not "bd" in keys else dic["bd"],
                            cursor="arrow" if not "cursor" in keys else dic["cursor"],
                            exportselection=0 if not "exportselection" in keys else dic["exportselection"],
                            font=("Times", "9") if not "font" in keys else dic["font"],
                            fg="black" if not "fg" in keys else dic["fg"],
                            height=0 if not "height" in keys else dic["height"],
                            highlightbackground="white" if not "highlightbackground" in keys else dic["highlightbackground"],
                            highlightcolor="white" if not "highlightcolor" in keys else dic["highlightcolor"],
                            highlightthickness=0 if not "highlightthickness" in keys else dic["highlightthickness"],
                            insertbackground="black" if not "insertbackground" in keys else dic["insertbackground"],
                            insertborderwidth=0 if not "insertborderwidth" in keys else dic["insertborderwidth"],
                            insertofftime=300 if not "insertofftime" in keys else dic["insertofftime"],
                            insertontime=600 if not "insertontime" in keys else dic["insertontime"],
                            insertwidth=2 if not "insertwidth" in keys else dic["insertwidth"],
                            padx=0 if not "padx" in keys else dic["padx"],
                            pady=0 if not "pady" in keys else dic["pady"],
                            relief=FLAT if not "relief" in keys else dic["relief"],
                            selectbackground="blue" if not "selectbackground" in keys else dic["selectbackground"],
                            selectborderwidth=1 if not "selectborderwidth" in keys else dic["selectbackground"],
                            spacing1=0 if not "spacing1" in keys else dic["spacing1"],
                            spacing2=0 if not "spacing2" in keys else dic["spacing2"],
                            spacing3=0 if not "spacing3" in keys else dic["spacing3"],
                            state=NORMAL if not "state" in keys else dic["state"],
                            tabs=1 if not "tabs" in keys else dic["tabs"],
                            width=0 if not "width" in keys else dic["width"],
                            wrap=WORD if not "wrap" in keys else dic["wrap"])
                elif dic["type"] == "LabelFrame":
                    obj = LabelFrame(parrent,
                                    bg="white" if not "bg" in keys else dic["bg"],
                                    bd=5 if not "bd" in keys else dic["bd"],
                                    cursor="arrow" if not "cursor" in keys else dic["cursor"],
                                    font=("Times", "9") if not "font" in keys else dic["font"],
                                    height=0 if not "height" in keys else dic["height"],
                                    labelanchor=NW if not "labelancor" in keys else dic["labelancor"],
                                    highlightbackground="white" if not "highlightbackground" in keys else dic["highlightbackground"],
                                    highlightcolor="white" if not "highlightcolor" in keys else dic["highlightcolor"],
                                    highlightthickness=0 if not "highlightthickness" in keys else dic["highlightthickness"],
                                    relief=GROOVE if not "relief" in keys else dic["relief"],
                                    text="" if not "text" in keys else dic["text"],
                                    width=0 if not "width" in keys else dic["width"])
                # elif dic["type"] == "Listbox":
                #     obj = Listbox(parrent)
                # elif dic["type"] == "Canvas":
                #     obj = Canvas(parrent)
                elif dic["type"] == "Menu":
                    obj = Menu(parrent,
                            activebackground="gray" if not "activebackground" in keys else dic["activebackground"],
                            activeborderwidth=0 if not "activeborderwidth" in keys else dic["activeborderwidth"],
                            activeforeground="black" if not "activeforeground" in keys else dic["activeforeground"],
                            bd=0 if not "bd" in keys else dic["bd"],
                            bg="white" if not "bg" in keys else dic["bg"],
                            cursor="arrow" if not "cursor" in keys else dic["cursor"],
                            disabledforeground="gray" if not "disabledforground" in keys else dic["disabledforeground"],
                            font=("Times", "9") if not "font" in keys else dic["font"],
                            fg="black" if not "fg" in keys else dic["fg"],
                            postcommand=self.empty_method if not "command" in keys else 
                                        lambda: loader(dic["command"]["package"], dic["command"]["name"],
                                        '' if not "path" in list(dic["command"].keys()) else dic["command"]["path"]),
                            relief=FLAT if not "relief" in keys else dic["relief"],
                            selectcolor="gray" if not "selectcolor" in keys else dic["selectcolor"],
                            tearoff=0 if not "tearoff" in keys else dic["tearoff"],
                            title="Menu" if not "title" in keys else dic["title"])
                elif dic["type"] == "Data":
                    obj = None
                else:
                    obj = Frame(parrent,
                                bg="white" if not "bg" in keys else dic["bg"],
                                bd=0 if not "bd" in keys else dic["bd"],
                                cursor="arrow" if not "cursor" in keys else dic["cursor"],
                                highlightbackground="white" if not "highlightbackground" in keys else dic["highlightbackground"],
                                highlightcolor="white" if not "highlightcolor" in keys else dic["highlightcolor"],
                                highlightthickness=0 if not "highlightthickness" in keys else dic["highlightthickness"],
                                relief=FLAT if not "relief" in keys else dic["relief"],
                                width=0 if not "width" in keys else dic["width"],
                                height=0 if not "height" in keys else dic["height"])
            else:
                obj = Frame(parrent,
                            bg="white" if not "bg" in keys else dic["bg"],
                            bd=0 if not "bd" in keys else dic["bd"],
                            cursor="arrow" if not "cursor" in keys else dic["cursor"],
                            highlightbackground="white" if not "highlightbackground" in keys else dic["highlightbackground"],
                            highlightcolor="white" if not "highlightcolor" in keys else dic["highlightcolor"],
                            highlightthickness=0 if not "highlightthickness" in keys else dic["highlightthickness"],
                            relief=FLAT if not "relief" in keys else dic["relief"],
                            width=0 if not "width" in keys else dic["width"],
                            height=0 if not "height" in keys else dic["height"])
        
            if "include" in keys:
                self.construct(dic["include"], obj)

            dic["obj"] = obj
            compo[index] = dic

    def pack(self, obj, pack, caller=1):
        for index in list(pack.keys()):
            data = pack[index]
            keys = list(data.keys())
            
            if "type" in list(obj[index].keys()) and obj[index]["type"] == "Menu":
                if caller == 1:
                    self.hasMenu = True
                    self.menuName = index
            else:
                if "include" in keys:
                    self.pack(obj[index]["include"], data["include"], 0)
                
                if "mode" in keys and data["mode"] == "grid":
                    obj[index]["obj"].grid(column=0 if not "column" in keys else data["column"],
                                    columnspan=1 if not "columnspan" in keys else data["columnspan"],
                                    ipadx=0 if not "ipadx" in keys else data["ipadx"],
                                    ipady=0 if not "ipady" in keys else data["ipady"],
                                    padx=0 if not "padx" in keys else data["padx"],
                                    pady=0 if not "pady" in keys else data["pady"],
                                    row=0 if not "row" in keys else data["row"],
                                    rowspan=1 if not "rowspan" in keys else data["rowspan"],
                                    sticky=W if not "sticky" in keys else data["sticky"])
                else:
                    obj[index]["obj"].pack(expand=NO if not "expand" in keys else data["expand"],
                                    fill=NONE if not "fill" in keys else data["fill"],
                                    side=TOP if not "side" in keys else data["side"])

    def setMenu(self):
        if self.menuName in list(self.compo.keys()):
            self.window.config(menu=self.compo[self.menuName]["obj"])
            self.menuConfig(self.compo[self.menuName])
    
    def menuConfig(self, compo):
        menu = compo["obj"]
        if "include" in list(compo.keys()):
            for index in list(compo["include"].keys()):
                ele = compo["include"][index]
                if ele["mode"]["type"] == "command":
                    menu.add_command(label=ele["mode"]["label"],
                                     command=lambda: loader(ele["mode"]["package"], ele["mode"]["name"])
                                     (self, ele["mode"]["content"]))
                elif ele["mode"]["type"] == "cascade":
                    menu.add_cascade(label=ele["mode"]["label"],
                                     menu=ele["obj"])
                    self.menuConfig(ele)
                elif ele["mode"]["type"] == "radiobutton":
                    menu.add_radiobutton(label=ele["mode"]["label"],
                                         value=ele["mode"]["value"],
                                         variable=lambda: loader(ele["mode"]["variable"]["package"], ele["mode"]["variable"]["name"]),
                                         command=lambda: loader(ele["mode"]["command"]["package"], ele["mode"]["command"]["name"]))
                elif ele["mode"]["type"] == "checkbox":
                    menu.add_checkbutton(label=ele["mode"]["label"],
                                         onvalue=ele["mode"]["onvalue"],
                                         offvalue=ele["mode"]["offvalue"],
                                         variable=lambda: loader(ele["mode"]["variable"]["package"], ele["mode"]["variable"]["name"]),
                                         command=lambda: loader(ele["mode"]["command"]["package"], ele["mode"]["command"]["name"]))
                elif ele["mode"]["type"] == "separator":
                    menu.separator()


    def run(self):
        self.window.mainloop()


def main_ui():
    app = App()
    app.run()
