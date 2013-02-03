from PyObjCTools import AppHelper
from Foundation import *


class MainDelegate(NSObject):
    fileName = objc.IBOutlet()
    fileContent = objc.IBOutlet()

    @objc.IBAction
    def openFile_(self, button):
    	fileToOpen = self.fileName.stringValue()
    	self.fileContent.setStringValue_(fileToOpen)


if __name__ == "__main__":
    AppHelper.runEventLoop()