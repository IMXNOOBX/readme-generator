import main
import os
import sys
import modules.buildReadme as buildReadme
import json
import time
from colorama import Fore
import modules.functions as func
import modules.vars as vars


def checkFileExists(filename):
    if vars.isdebug:
        print(vars.debugc +
              f"Called function 'checkPackageDotJson()' to check if '{filename}' exist")
    if os.path.isfile(filename):
        return True
    else:
        return False


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# jeejj im not that clever xd: https://stackoverflow.com/questions/22029562/python-how-to-make-simple-animated-loading-while-process-is-running
def animated_loading(text, times):
    if vars.isdebug:
        print(vars.debugc +
              f"Called function 'animated_loading({text}, {times})'")
    chars = "/—\|"
    for i in range(times):
        for char in chars:
            sys.stdout.write(f'\r{text} {char}')
            time.sleep(.1)
            sys.stdout.flush()


def getGithubUsername(url):
    if vars.isdebug:
        print(vars.debugc + f"Called function 'getGithubUsername({url})'")
    # imagin url is: https://github.com/IMXNOOBX/snooby#readme
    afterGH = url.partition("github.com/")[2]
    if vars.isdebug:
        # it will delete 'https://github.com/' and you will have left 'IMXNOOBX/snooby#readme'
        print(
            vars.debugc + f"function 'getGithubUsername(url)' cleaned the first part of the url, result: {afterGH}")
    # and this will remove the rest: from: ''IMXNOOBX/snooby#readme' to 'IMXNOOBX'
    cleanedUsrName = afterGH.partition("/")[0]
    if vars.isdebug:
        print(
            vars.debugc + f"function 'getGithubUsername(url)' cleaned the github username, result: {cleanedUsrName}")
    return cleanedUsrName


def getGithubRepo(url):
    if vars.isdebug:
        print(vars.debugc + f"Called function 'getGithubRepo({url})'")
    cleanedRepoUrl = url.partition(f"#")[0]
    if vars.isdebug:
        print(
            vars.debugc + f"function 'getGithubUsername(url)' cleaned the github url, result: {cleanedRepoUrl}")
    return cleanedRepoUrl


def getLicenseBadgeThing(url):
    if vars.isdebug:
        print(vars.debugc + f"Called function 'getLicenseBadgeThing({url})'")
    cleanedRepoUrl = url.partition(f"github.com/")[2]
    if vars.isdebug:
        print(
            vars.debugc + f"function 'getLicenseBadgeThing(url)' cleaned the github badge, result: {cleanedRepoUrl}")
    return cleanedRepoUrl


def previewValues(string):
    finalPreview = ''
    if vars.isdebug:
        print(vars.debugc + f"Called function 'checkPackageDotJson({string})'")
    if string != '':
        finalPreview = Fore.LIGHTBLACK_EX + '(' + string + ') ' + Fore.RESET
    if vars.isdebug:
        print(vars.debugc + f"Preview Fuction returned: {finalPreview}")
    return finalPreview


def getPackageDotJson():
    if func.checkFileExists(vars.pkgjson):
        if vars.isdebug:
            print(vars.debugc + Fore.LIGHTMAGENTA_EX +
                  'Package.json found, getting info!' + Fore.RESET)
        with open(vars.pkgjson) as json_file:
            pkg = json.load(json_file)
            if "name" in pkg:
                if vars.isdebug:
                    print(
                        vars.debugc + "Key 'name' exist in JSON data, value: " + pkg['name'])
                vars.rproject_name = pkg['name']
            if "version" in pkg:
                if vars.isdebug:
                    print(
                        vars.debugc + "Key 'version' exist in JSON data, value: " + pkg['version'])
                vars.rproject_version = pkg['version']
            if "description" in pkg:
                if vars.isdebug:
                    print(
                        vars.debugc + "Key 'description' exist in JSON data, value: " + pkg['description'])
                vars.rproject_description = pkg['description']
            if "homepage" in pkg:  # Two birds with one shot
                if vars.isdebug:
                    print(
                        vars.debugc + "Key 'homepage' exist in JSON data, value: " + pkg['homepage'])
                vars.rproject_repository = pkg['homepage']
                vars.rproject_githubusr = getGithubUsername(
                    vars.rproject_repository)
                vars.rproject_url = getGithubRepo(vars.rproject_repository)

            if "author" in pkg:
                if vars.isdebug:
                    print(
                        vars.debugc + "Key 'author' exist in JSON data, value: " + pkg['author'])
                vars.rproject_author = pkg['author']
            if "license" in pkg:
                if vars.isdebug:
                    print(
                        vars.debugc + "Key 'license' exist in JSON data, value: " + pkg['license'])
                vars.rproject_license = pkg['license']
            if "scripts" in pkg:
                asd = 0
                for sc in pkg['scripts']:
                    if vars.isdebug:
                        print(vars.debugc + "Key 'scripts' (" + str(asd) +
                              ") exist in JSON data, value: " + pkg['scripts'][sc])
                    #rproject_scripts = pkg['scripts'][sc].join(rproject_scripts)
                    # print(rproject_scripts)
                    asd = asd + 1


def generateReadmeDotMd():
    getPackageDotJson()
    vars.prName = input(
        Fore.GREEN+"√"+Fore.RESET+f" [🍭] Project name: {previewValues(vars.rproject_name)}")
    if vars.prName == '' and vars.rproject_name != '':
        vars.prName = vars.rproject_name
    vars.prVersion = input(
        Fore.GREEN+"√"+Fore.RESET+f" [🔖] Project version: {previewValues(vars.rproject_version)}")
    if vars.prVersion == '' and vars.rproject_version != '':
        vars.prVersion = vars.rproject_version
    vars.prDescription = input(
        Fore.GREEN+"√"+Fore.RESET+f" [📘] Project description: {previewValues(vars.rproject_description)}")
    if vars.prDescription == '' and vars.rproject_description != '':
        vars.prDescription = vars.rproject_description
    vars.prHomePage = input(
        Fore.GREEN+"√"+Fore.RESET+f" [🏡] Project home page: {previewValues(vars.rproject_repository)}")
    if vars.prHomePage == '' and vars.rproject_repository != '':
        vars.prHomePage = vars.rproject_repository
    elif vars.rproject_repository == '':
        vars.rproject_url = getGithubRepo(vars.prHomePage)
    vars.prDoscsUrl = input(
        Fore.GREEN+"√"+Fore.RESET+f" [🌠] Project documentation url/page: {previewValues(vars.rproject_url)}")
    if vars.prDoscsUrl == '' and vars.rproject_url != '':
        vars.prDoscsUrl = vars.rproject_url
    vars.prAuthorName = input(
        Fore.GREEN+"√"+Fore.RESET+f" [🌍] Project Author name: {previewValues(vars.rproject_author)}")
    if vars.prAuthorName == '' and vars.rproject_author != '':
        vars.prAuthorName = vars.rproject_author
    vars.prGithubUsername = input(
        Fore.GREEN+"√"+Fore.RESET+f" [👤] Project Author GitHub username: {previewValues(vars.rproject_githubusr)}")
    if vars.prGithubUsername == '' and vars.rproject_githubusr != '':
        vars.prGithubUsername = vars.rproject_githubusr
    vars.prWebSite = input(
        Fore.GREEN+"√"+Fore.RESET+f" [💡] Project/Author web site: {previewValues('')}")

    vars.prLicenseName = input(
        Fore.GREEN+"√"+Fore.RESET+f" [📝] Project license: {previewValues(vars.rproject_license)}")
    if vars.prLicenseName == '' and vars.rproject_license != '':
        vars.prLicenseName = vars.rproject_license
    vars.prLicenseUrl = input(
        Fore.GREEN+"√"+Fore.RESET+f" [📝] Project license url: {previewValues('')}")

    vars.prIssuesUrl = input(Fore.GREEN+"√"+Fore.RESET+f"[📬] Project issues url: {previewValues('')}")

    animated_loading('Loading the readme.md', 10)
    buildReadme.buildReadmeDotMd()
    print("\r"+Fore.GREEN+"√"+Fore.RESET+" [📖] Readme Successfully Generated!")
