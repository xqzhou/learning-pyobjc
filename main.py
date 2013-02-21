from PyObjCTools import AppHelper
from Foundation import *
from AppKit import *


class MainDelegate(NSObject):

    compareWindowController = objc.IBOutlet()

    @objc.IBAction
    def openFile_(self, button):
        self.compareWindowController.showWindow_()


class CompareWindowController(NSWindowController):

    def init(self):
        self = super(NSWindowController, self).init()
        NSBundle.loadNibNamed_owner_("CompareWindow", self)
        return self


if __name__ == "__main__":
    AppHelper.runEventLoop()