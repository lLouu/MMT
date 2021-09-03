from module_loaders import read_opt, launch_ui, auto_update
from errors import error

def main():
    opt = read_opt()

    if opt.autoup:
        if not(auto_update()):
            error(0, 1, 1)

    if not(launch_ui(opt)):
        error(0, 2, 5)

if __name__ == '__main__':
    main()