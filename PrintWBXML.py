#!/usr/bin/python

import lldb
import fbchisellldbbase as fb
import os, sys, inspect
import datetime

cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

from PyWBXMLDecoder import ASCommandResponse


def lldbcommands():
    return [PrintWBXML()]


class PrintWBXML(fb.FBCommand):
    def name(self):
        return 'pwbxml'

    def description(self):
        return 'prints pwbxml'

    def run(self, arguments, options):
        WBXMLVariable = arguments[0]

        # byteWBXML = fb.evaluateExpressionValue("(NSString*)[[NSString alloc] initWithData:URLRequest.HTTPBody encoding:4]").GetObjectDescription()
        # going through tmp file is dirty hack but so far I failed to get utf8 string from fb api

        try:
            open("/tmp/whatever", 'w').close() # make sure file is there and is empty
        except OSError:
            pass

        # this will work only on sim as it writes to local device /tmp file.
        fb.evaluateExpressionValue(
            "(void)[%(wbxmlvar)s writeToURL:(NSURL*)[NSURL URLWithString:@\"file:///tmp/whatever\"] atomically:YES]" % {
                'wbxmlvar': WBXMLVariable});
        byteWBXML = open("/tmp/whatever", "rb").read()

        instance = ASCommandResponse.ASCommandResponse(byteWBXML)

        if instance.getXMLString():
            out = instance.getXMLString()

        else:
            out = "RAW WBXML"
            out += "\n" + byteWBXML

        print(out)

        with open("/tmp/wbxml.log", "a") as f:
            f.write( str(datetime.datetime.now()) + "\n" )
            f.write( out )
            f.write( "\n____________________________\n" )
            f.close()
