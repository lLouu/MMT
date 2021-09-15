# Import
from module_loaders import loader
App = loader("default_ui", "App", "Source\\modules\\default_ui")


# Global var
input = None
output = None
graph = None


# Getter
def get_input_object(parrent, entry="Solutions"):
    global input
    input = App(parrent, "Source\\modules\\ui_content_manager\\json\\input\\" + entry + "\\appCompo.json", "Source\\modules\\ui_content_manager\\json\\input\\" + entry + "\\appProperties.json")

def get_output_object(parrent, entry=None):
    global output
    output = App(parrent, "Source\\modules\\ui_content_manager\\json\\output\\appCompo.json", "Source\\modules\\ui_content_manager\\json\\output\\appProperties.json")

def get_graph_object(parrent, entry=None):
    global graph
    graph = App(parrent, "Source\\modules\\ui_content_manager\\json\\graph\\appCompo.json", "Source\\modules\\ui_content_manager\\json\\graph\\appProperties.json")


# Updater
def up_input_content(app, option):
    pass

def up_output_content(app, option):
    pass

def up_graph_content(app, option):
    pass


# Generator
def gen_popup(app, option):
    pass

