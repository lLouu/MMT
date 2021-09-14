# Import
from module_loaders import loader
App = loader("default_ui", "App", "Source\\modules\\default_ui")


# Global var
input = None
output = None
graph = None


# Getter
def get_input_object(parrent, entry=None):
    pass

def get_output_object(parrent, entry=None):
    pass

def get_graph_object(parrent, entry=None):
    pass


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

