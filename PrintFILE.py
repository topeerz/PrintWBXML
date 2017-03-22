#!/usr/bin/python

import lldb
import fblldbbase as fb
import os, sys, inspect
import datetime

cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

def lldbcommands():
    return [PrintFile()]


class PrintFile(fb.FBCommand):
    def name(self):
        return 'pfile'

    def description(self):
        return 'prints evaluated value to file'

    def run(self, arguments, options):
        inputData = arguments[0]

        try:
            open("/tmp/whatever", 'w').close() # make sure file is there and is empty
        except OSError:
            pass

        fb.evaluateExpressionValue(
            "(void)[%(wbxmlvar)s writeToURL:(NSURL*)[NSURL URLWithString:@\"file:///tmp/whatever\"] atomically:YES]" % {
                'wbxmlvar': inputData});
        out = open("/tmp/whatever", "rb").read()

        print out

        with open("/tmp/wbxml.log", "a") as f:
            f.write( str(datetime.datetime.now()) + "\n" )
            f.write( out )
            f.write( "\n____________________________\n" )
            f.close()
