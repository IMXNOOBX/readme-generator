import os
import argparse
import sys

import datetime


import modules.functions as func
import modules.vars as vars


__author__ = "IMXNOOBX"
__copyright__ = "Copyright 2022, The Readme Generator Project"
__credits__ = ["IMXNOOBX"]
__license__ = "ISC"
__version__ = "1.0.4"
__maintainer__ = "IMXNOOBX"
__email__ = "contact@imxnoobx.xyz"
__status__ = "Production"


now = datetime.datetime.now()

# init


def main():
    func.clear()
    parser = argparse.ArgumentParser(
        description='A Simple Advanced readme generator for your Projects')
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
