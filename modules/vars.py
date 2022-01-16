import os
import sys
from colorama import Fore

# variables to store the info
mainbanner = Fore.LIGHTBLUE_EX + R"""
        '||'''|, '||''''|      /.\      '||'''|. '||\   /||` '||''''| 
         ||   ||  ||   .      // \\      ||   ||  ||\\.//||   ||   .  
         ||...|'  ||'''|     //...\\     ||   ||  ||     ||   ||'''|  
         || \\    ||        //     \\    ||   ||  ||     ||   ||      
        .||  \\. .||....| .//       \\. .||...|' .||     ||. .||....| 
""" + Fore.RESET+"                           Made By: imxnoobx.xyz\n\n"


scriptPath = os.path.dirname(os.path.realpath(sys.argv[0]))
pkgjson = 'package.json'

isdebug = False

debugc = Fore.BLUE + "[" + Fore.LIGHTBLUE_EX + \
    "DEBUG" + Fore.BLUE + "] - " + Fore.RESET

greenTick = Fore.GREEN + "√" + Fore.RESET

rproject_name = ''
rproject_version = ''
rproject_description = ''
rproject_dependencies = ''
#rproject_scripts = []
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
finalLicense = ''
finalIssues = ''
finalPulls = ''