from module_loaders import read_opt, launch_ui, auto_update, getModules
from errors import error

def main():
    opt = read_opt("Source/options.dat")

    if opt.autoup:
        if not(auto_update()):
            error(0, 1, 1)

    list = getModules(opt)

    if not(launch_ui(opt, list)):
        error(0, 2, 5, "no ui module is installed")

if __name__ == '__main__':
    main()