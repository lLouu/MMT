class Option:
    autoup = False
    show_warning = False
    ask_for_default = True
    default_ui = None

    def __init__(self):
        pass

def GetEmptyOpt():
    return Option()

def read_opt():
    return GetEmptyOpt()

def launch_ui(opt):
    return True

def auto_update():
    return True

def loader():
    pass
