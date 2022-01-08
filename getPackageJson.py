from main import *
import checkFileExist

def getPackageDotJson():
    global rproject_name
    global rproject_version
    global rproject_description
    global rproject_dependencies
    global rproject_scripts
    global rproject_author
    global rproject_githubusr
    global rproject_url
    global rproject_repository
    global rproject_website
    global rproject_license
    if checkFileExist.checkFileExists(pkgjson):
        if isdebug: print(debugc + Fore.LIGHTMAGENTA_EX +
            'Package.json found, getting info!' + Fore.RESET)
        with open(pkgjson) as json_file:
            pkg = json.load(json_file)
            if "name" in pkg:
                if isdebug: print(debugc + "Key 'name' exist in JSON data, value: " + pkg['name'])
                rproject_name = pkg['name']
            if "version" in pkg:
                if isdebug: print(debugc + "Key 'version' exist in JSON data, value: " + pkg['version'])
                rproject_version = pkg['version']
            if "description" in pkg:
                if isdebug: print(debugc + "Key 'description' exist in JSON data, value: " + pkg['description'])
                rproject_description = pkg['description']
            if "homepage" in pkg: #Two birds with one shot 
                if isdebug: print(debugc + "Key 'homepage' exist in JSON data, value: " + pkg['homepage'])
                rproject_repository = pkg['homepage']
                rproject_githubusr = getGithubUsername(rproject_repository)
                rproject_url = getGithubRepo(rproject_repository)

            if "author" in pkg:
                if isdebug: print(debugc + "Key 'author' exist in JSON data, value: " + pkg['author'])
                rproject_author = pkg['author']
            if "license" in pkg:
                if isdebug: print(debugc + "Key 'license' exist in JSON data, value: " + pkg['license'])
                rproject_license = pkg['license']
            if "scripts" in pkg:
                asd = 0
                for sc in pkg['scripts']:
                    if isdebug: print(debugc + "Key 'scripts' (" + str(asd) + ") exist in JSON data, value: " + pkg['scripts'][sc])
                    #rproject_scripts = pkg['scripts'][sc].join(rproject_scripts)
                    #print(rproject_scripts)
                    asd = asd + 1