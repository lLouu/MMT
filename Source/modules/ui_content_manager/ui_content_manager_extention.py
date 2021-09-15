from tkinter import Frame
from module_loaders import loader
App = loader("default_ui", "App", "Source\\modules\\default_ui")

point_list = []
point_index = 0

def get_point_index(entry=None):
    global point_index
    return point_index

def add_point(app, entry=None):
    global point_list
    global point_index
    point_list.append([App(app.compo["points"]["include"]["content"]["obj"], "Source\\modules\\ui_content_manager\\json\\input\\Interpolation\\pointCompo.json", "Source\\modules\\ui_content_manager\\json\\input\\Interpolation\\pointProperties.json"), point_index])
    point_index += 1

def reset(app, entry=None):
    global point_list
    global point_index
    app.compo["points"]["include"]["content"]["obj"].destroy()
    app.compo["points"]["include"]["content"]["obj"] = Frame(app.compo["points"]["obj"])
    app.compo["points"]["include"]["content"]["obj"].grid(row=1, sticky="n")
    point_list = []
    point_index = 0

def remove(app, index):
    global point_list
    point_list[index][0].compo["point"]["obj"].destroy()