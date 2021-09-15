# Import
from module_loaders import loader
App = loader("default_ui", "App", "Source\\modules\\default_ui")


# Global var
input = None
output = None
graph = None
output_text = None


# Getter
def get_input_object(parrent, entry="Solutions"):
    global input
    return input

def get_output_object(parrent, entry=None):
    global output
    return output

def get_output_text(app=None, entry = None):
    global output_text
    return output_text

def get_graph_object(parrent, entry=None):
    global graph
    return graph


# Setter
def set_input_object(parrent, entry="Solutions"):
    global input
    input = App(parrent, "Source\\modules\\ui_content_manager\\json\\input\\" + entry + "\\appCompo.json", "Source\\modules\\ui_content_manager\\json\\input\\" + entry + "\\appProperties.json")

def set_output_object(parrent, entry=None):
    global output
    output = App(parrent, "Source\\modules\\ui_content_manager\\json\\output\\appCompo.json", "Source\\modules\\ui_content_manager\\json\\output\\appProperties.json")

def set_output_text(app, entry = ""):
    global output_text
    output_text = app.get_tk_object("String", entry)
    return output_text

def set_graph_object(parrent, entry=None):
    global graph
    graph = App(parrent, "Source\\modules\\ui_content_manager\\json\\graph\\appCompo.json", "Source\\modules\\ui_content_manager\\json\\graph\\appProperties.json")


# Updater
def up_input_content(app, option):
    global input
    input.reset("Source\\modules\\ui_content_manager\\json\\input\\" + option + "\\appCompo.json", "Source\\modules\\ui_content_manager\\json\\input\\" + option + "\\appProperties.json")

def up_output_content(app, option):
    global output_text
    output_text.set(option)

def up_graph_content(app, option):
    pass


# Generator
def gen_popup(app, option):
    popup = App("Source\\modules\\ui_content_manager\\json\\popup\\appWindow.json", "Source\\modules\\ui_content_manager\\json\\input\\" + option + "\\appCompo.json", "Source\\modules\\ui_content_manager\\json\\input\\" + option + "\\appProperties.json")
    popup.run()

