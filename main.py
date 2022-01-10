
import os
import argparse
import sys

import datetime


import modules.functions as func
import modules.vars as vars

# Define everything. ik this isnt the best way to do, if you think you have a better way to do, pls pull a reques with your changes :D
now = datetime.datetime.now()

# init


def main():
    func.clear()
    parser = argparse.ArgumentParser(
        description='The App description. if i forgot to fill this plis tell me')
    parser.add_argument('init', type=str,
                        help='Initialize the readme generator program')

    parser.add_argument('-d', '--debug', action='store_true',
                        help='Will log every action done by the program')

    args = parser.parse_args()

    if args.debug:  # fixed xd

        vars.isdebug = True
        if vars.isdebug:
            print(vars.debugc + f"Debug mode: {vars.isdebug}!")

    if args.init == 'init':
        if vars.isdebug:
            print(vars.debugc + f"Script started in: {vars.scriptPath}")
        if func.checkFileExists('readme.md'):
            print('[❌] - Readme file found! it will be overwritten if you continue')
            input("Press Enter to continue...")
        print(vars.mainbanner)
        func.generateReadmeDotMd()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        if vars.isdebug:
            print(vars.debugc + "Detected exception 'KeyboardInterrupt'")
        print('[❌] - Cancelled by KeyboardInterrupt')
        try:
            if vars.isdebug:
                print(vars.debugc + "Trying to execute 'sys.exit(0)'")
            sys.exit(0)
        except SystemExit:
            if vars.isdebug:
                print(vars.debugc +
                      "Detected exception 'SystemExit' executing 'os._exit(0)'")
            os._exit(0)
