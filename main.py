from io import StringIO
import json
import os
from colorama import init, Fore, Style, Cursor
import argparse
import sys
import time
import datetime

import buildReadme
import checkFileExist

# Define everything. ik this isnt the best way to do, if you think you have a better way to do, pls pull a reques with your changes :D
isdebug = False
scriptPath = os.path.dirname(os.path.realpath(sys.argv[0]))
pkgjson = 'package.json'
debugc = Fore.BLUE + "[" + Fore.LIGHTBLUE_EX + \
    "DEBUG" + Fore.BLUE + "] - " + Fore.RESET

# variables to store the info

rproject_name = ''
rproject_version = ''
rproject_description = ''
rproject_dependencies = ''
rproject_scripts = []
rproject_author = ''
rproject_githubusr = ''
rproject_url = ''
rproject_repository = ''
rproject_website = ''
rproject_license = ''
prName = ''
prVersion = ''
prDescription = ''
prHomePage = ''
prDoscsUrl = ''
prAuthorName = ''
prGithubUsername = ''
prWebSite = ''
prLicenseName = ''
prLicenseUrl = ''
prIssuesUrl = ''
finalReadme = ''

now = datetime.datetime.now()


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
    
def animated_loading(text, times): #jeejj im not that clever xd: https://stackoverflow.com/questions/22029562/python-how-to-make-simple-animated-loading-while-process-is-running
    if isdebug: print(debugc + f"Called function 'animated_loading({text}, {times})'")
    chars = "/—\|" 
    for i in range(times):
        for char in chars:
            sys.stdout.write(f'\r{text} {char}')
            time.sleep(.1)
            sys.stdout.flush()

def getGithubUsername(url):
        if isdebug: print(debugc + f"Called function 'getGithubUsername({url})'")
        afterGH = url.partition("github.com/")[2] #imagin url is: https://github.com/IMXNOOBX/snooby#readme
        if isdebug: print(debugc + f"function 'getGithubUsername(url)' cleaned the first part of the url, result: {afterGH}") #it will delete 'https://github.com/' and you will have left 'IMXNOOBX/snooby#readme'
        cleanedUsrName = afterGH.partition("/")[0] #and this will remove the rest: from: ''IMXNOOBX/snooby#readme' to 'IMXNOOBX'
        if isdebug: print(debugc + f"function 'getGithubUsername(url)' cleaned the github username, result: {cleanedUsrName}") 
        return cleanedUsrName

def getGithubRepo(url):
        if isdebug: print(debugc + f"Called function 'getGithubRepo({url})'")
        cleanedRepoUrl = url.partition(f"#")[0]
        if isdebug: print(debugc + f"function 'getGithubUsername(url)' cleaned the github url, result: {cleanedRepoUrl}") 
        return cleanedRepoUrl
def getLicenseBadgeThing(url):
        if isdebug: print(debugc + f"Called function 'getLicenseBadgeThing({url})'")
        cleanedRepoUrl = url.partition(f"github.com/")[2]
        if isdebug: print(debugc + f"function 'getLicenseBadgeThing(url)' cleaned the github badge, result: {cleanedRepoUrl}") 
        return cleanedRepoUrl

def previewValues(string):
    finalPreview = ''
    if isdebug: print(debugc + f"Called function 'checkPackageDotJson({string})'")
    if string != '':
        finalPreview = Fore.LIGHTBLACK_EX + '(' + string + ') ' + Fore.RESET
    if isdebug: print(debugc + f"Preview Fuction returned: {finalPreview}")
    return finalPreview
    
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

def generateReadmeDotMd():
    global prName
    global prVersion
    global prDescription
    global prHomePage
    global prDoscsUrl
    global prAuthorName
    global prGithubUsername
    global prWebSite
    global prLicenseName
    global prLicenseUrl
    global prIssuesUrl
    global rproject_url
    getPackageDotJson()
    prName = input(f"√ [🍭] Project name: {previewValues(rproject_name)}")
    if prName == '' and rproject_name != '':
        prName = rproject_name
    prVersion = input(f"√ [🔖] Project version: {previewValues(rproject_version)}")
    if prVersion == '' and rproject_version != '':
        prVersion = rproject_version
    prDescription = input(f"√ [📘] Project description: {previewValues(rproject_description)}")
    if prDescription == '' and rproject_description != '':
        prDescription = rproject_description
    prHomePage = input(f"√ [🏡] Project home page: {previewValues(rproject_repository)}")
    if prHomePage == '' and rproject_repository != '':
        prHomePage = rproject_repository
    elif rproject_repository == '':
        rproject_url = getGithubRepo(prHomePage)
    prDoscsUrl = input(f"√ [🌠] Project documentation url/page: {previewValues(rproject_url)}")
    if prDoscsUrl == '' and rproject_url != '':
        prDoscsUrl = rproject_url
    prAuthorName = input(f"√ [🌍] Project Author name: {previewValues(rproject_author)}")
    if prAuthorName == '' and rproject_author != '':
        prAuthorName = rproject_author
    prGithubUsername = input(f"√ [👤] Project Author GitHub username: {previewValues(rproject_githubusr)}")
    if prGithubUsername == '' and rproject_githubusr != '':
        prGithubUsername = rproject_githubusr
    prWebSite = input(f"√ [💡] Project/Author web site: {previewValues('')}")

    prLicenseName = input(f"√ [📝] Project license: {previewValues(rproject_license)}")
    if prLicenseName == '' and rproject_license != '':
        prLicenseName = rproject_license
    prLicenseUrl = input(f"√ [📝] Project license url: {previewValues('')}")

    prIssuesUrl = input(f"√ [📬] Project issues url: {previewValues('')}")

    animated_loading('Loading the readme.md', 10)
    buildReadme.buildReadmeDotMd()















#init
def main():
    clear()
    parser = argparse.ArgumentParser(description='The App description. if i forgot to fill this plis tell me')
    parser.add_argument('init', type=str,
                        help='Initialize the readme generator program')

    parser.add_argument('-d', '--debug', action='store_true',
                        help='Will log every action done by the program')

    args = parser.parse_args()

    if args.debug: #fixed xd
        global isdebug # cause if not it won be reachable from the outside world :D
        isdebug = True
        if isdebug: print(debugc + f"Debug mode: {isdebug}!")

    if args.init == 'init':
        if isdebug: print(debugc + f"Script started in: {scriptPath}")
        if checkFileExist.checkFileExists('readme.md'):
            print('[❌] - Readme file found! it will be overwritten if you continue')
            input()
        print(mainbanner)
        print(mainbannerc)
        generateReadmeDotMd()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        if isdebug: print(debugc + "Detected exception 'KeyboardInterrupt'")
        print('[❌] - Cancelled by KeyboardInterrupt')
        try:
            if isdebug: print(debugc + "Trying to execute 'sys.exit(0)'")
            sys.exit(0)
        except SystemExit:
            if isdebug: print(debugc + "Detected exception 'SystemExit' executing 'os._exit(0)'")
            os._exit(0)