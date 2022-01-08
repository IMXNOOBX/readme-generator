import main
import os

def checkFileExists(filename):
    if main.isdebug: print(main.debugc + f"Called function 'checkPackageDotJson()' to check if '{filename}' exist")
    if os.path.isfile(filename):
        return True
    else: return False