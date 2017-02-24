# PrintWBXML

Chisel command for printing NSData storing WBXML.

This is https://github.com/facebook/chisel function based on https://github.com/davidpshaw/PyWBXMLDecoder
Note: this is just raw notes rather than full instraction. Also this is subject to be changed at some point in future.
Note: Current code is more a draft than anything else.
Note: this is xcode/appcode osx only project.

Installation:
1. Instal chisel
2. Create .lldbinit with content
  command script import /usr/local/opt/chisel/libexec/fblldb.py
  script fblldb.loadCommandsInDirectory('/Users/user/topeerz/.lldb')
3. Clone this archive to latter directory
4. Run xcode and have fun. Don't forget about using logging breakpoints.

Syntax:
pwbxml \<NSData variable\>
