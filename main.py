from io import StringIO
import json
import os
from colorama import init, Fore, Style, Cursor
import argparse



isdebug = False
pkgjson = 'package.json'
#ispkgjson = False
debugc = Fore.BLUE + "[" + Fore.LIGHTBLUE_EX + \
    "DEBUG" + Fore.BLUE + "] - " + Fore.RESET

#variables to store the info
rproject_name = ''
rproject_version = ''
rproject_description = ''
rproject_dependencies = ''
rproject_scripts = []
rproject_author = ''
rproject_repository = ''
rproject_website = ''
rproject_license = ''



mainbanner = Fore.LIGHTBLUE_EX + R"""
        '||'''|, '||''''|      /.\      '||'''|. '||\   /||` '||''''| 
         ||   ||  ||   .      // \\      ||   ||  ||\\.//||   ||   .  
         ||...|'  ||'''|     //...\\     ||   ||  ||     ||   ||'''|  
         || \\    ||        //     \\    ||   ||  ||     ||   ||      
        .||  \\. .||....| .//       \\. .||...|' .||     ||. .||....| 
""" + Fore.RESET
mainbannerc = "                           Made By: imxnoobx.xyz\n\n"

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def checkPackageDotJson():
    global rproject_name
    global rproject_version
    global rproject_description
    global rproject_dependencies
    global rproject_scripts
    global rproject_author
    global rproject_repository
    global rproject_website
    global rproject_license
    if os.path.isfile(pkgjson):
        #ispkgjson = True
        if isdebug: print(debugc + Fore.LIGHTMAGENTA_EX +
            'Package.json found, getting info!' + Fore.RESET)
        with open(pkgjson) as json_file:
            pkg = json.load(json_file)
            if "name" in pkg:
                if isdebug: print(debugc + "Key 'name' exist in JSON data, value: " + pkg['name'])
                rproject_name = pkg['name']
            if "description" in pkg:
                if isdebug: print(debugc + "Key 'description' exist in JSON data, value: " + pkg['description'])
                rproject_description = pkg['description']
            if "version" in pkg:
                if isdebug: print(debugc + "Key 'version' exist in JSON data, value: " + pkg['version'])
                rproject_version = pkg['version']



            if "author" in pkg:
                if isdebug: print(debugc + "Key 'scripts' exist in JSON data, value: " + pkg['author'])
                rproject_author = pkg['author']
            if "license" in pkg:
                if isdebug: print(debugc + "Key 'scripts' exist in JSON data, value: " + pkg['license'])
                rproject_license = pkg['license']
            if "homepage" in pkg:
                if isdebug: print(debugc + "Key 'scripts' exist in JSON data, value: " + pkg['homepage'])
                rproject_repository = pkg['homepage']
            if "scripts" in pkg:
                asd = 0
                for sc in pkg['scripts']:
                    if isdebug: print(debugc + "Key 'scripts' (" + str(asd) + ") exist in JSON data, value: " + pkg['scripts'][sc])
                    rproject_scripts = pkg['scripts'][sc].join(rproject_scripts)
                    print(rproject_scripts)
                    asd = asd + 1



        return True
    else: return False
    


def generateReadmeDotMd():
    checkPackageDotJson()
    name = input("Project Name: " + rproject_name)
















#init

parser = argparse.ArgumentParser(description='The App description. if i forgot to fill this plis tell me')
parser.add_argument('init', type=str,
                    help='initialise riadme programthat programsthe ridme')

parser.add_argument('-d', '--debug', action='store_true',
                    help='Will log every action done by the program')

args = parser.parse_args()


if args.init == '-d' or '--debug': 
    isdebug = True
    if isdebug: print(debugc + "Debug mode enabled!")

if args.init == 'init':
    clear()
    print(mainbanner)
    print(mainbannerc)
    generateReadmeDotMd()

