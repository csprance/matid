#!/usr/bin/env python
################################################################################
#
# matid_ui.py
# Description: The Qt GUI for csMatID
# Usage:
# Author: Chris Sprance Entrada Interactive
#
################################################################################

import lx
import lxifc
import lxu.command
import PySide
from PySide.QtGui import *
import modo
import os


# Custom View Class
class OpenMatIDPalette(lxifc.CustomView):
    def __init__(self):
        lx.out('Initializing csMatID')
        self.layout = PySide.QtGui.QFormLayout()
        self.scriptdir = os.path.normpath(lx.eval('query platformservice alias ? {kit_csprance_matid:}'))
        # create the parent layout

    def customview_Init(self, pane):
        lx.out('Initializing custom view')
        if pane is None:
            return False
        custPane = lx.object.CustomPane(pane)
        if custPane.test() is False:
            return False
        # get the parent object
        parent = custPane.GetParent()
        # convert to PySide QWidget
        p = lx.getQWidget(parent)
        # Check that it suceeds
        if p is not None:
            # connect all the buttons to the onClicked function
            # and add it to the layout
            self.layout.setContentsMargins(2, 2, 2, 2)
            p.setLayout(self.layout)
            return True
        return False


# final little bit is to bless the commands needed for csMatID
lx.bless(OpenMatIDPalette, "csMatID")
