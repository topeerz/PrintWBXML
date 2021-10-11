#!/usr/bin/python

import lldb
import fbchisellldbbase as fb
import os, sys, inspect
import datetime

cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

def lldbcommands():
    return [PrintRawFile()]


class PrintRawFile(fb.FBCommand):
    def name(self):
        return 'prfile'

    def description(self):
        return 'prints raw string file'

    def run(self, arguments, options):
        inputData = arguments[0]

        out = inputData

        print(out)

        with open("/tmp/wbxml.log", "a") as f:
            f.write( str(datetime.datetime.now()) + "\n" )
            f.write( out )
            f.write( "\n____________________________\n" )
            f.close()
