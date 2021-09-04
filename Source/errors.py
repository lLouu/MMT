class Error:
    def __init__(self):
        pass

def error(file_id, id, weight, message = ''):
    file_id = file_id if 0 <= file_id <= MAX_ID_MODULE else -1
    pass

## Has to be set with the installer
 # Modular section
MAX_ID_MODULE = 0
index = {
        -1 :    "unkown",
        0  :    "main module"
        }