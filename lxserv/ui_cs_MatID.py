#!/usr/bin/env python
################################################################################
#
# ui_cs_MatID.py
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
import json
from colours import Color
from functools import partial


# Custom View Class
class OpenMatIDPalette(lxifc.CustomView):
    def __init__(self):
        lx.out('Initializing csMatID')
        self.layout = PySide.QtGui.QFormLayout()
        self.scriptdir = os.path.normpath(lx.eval('query platformservice alias ? {kit_csprance_matid:}'))
        # create the parent layout
        self.get_swatch_buttons()

    @staticmethod
    def on_swatch_clicked(swatch_color='1.01.01.0'):
        lx.eval('csMatID.apply %s' % swatch_color)

    @staticmethod
    def split_string_to_rgb(string_to_split):
        return (float(string_to_split[0:3]),
                float(string_to_split[3:6]),
                float(string_to_split[6:9]))

    def customview_Init(self, pane):
        lx.out('Initializing cs_MatID panel')
        if pane is None:
            return False
        custPane = lx.object.CustomPane(pane)
        if custPane.test() is False:
            return False
        # get the parent object
        parent = custPane.GetParent()
        # convert to PySide QWidget
        p = lx.getQWidget(parent)
        # Check that it succeeds
        if p is not None:
            # connect all the buttons to the onClicked function
            # and add it to the layout
            self.layout.setContentsMargins(1, 1, 1, 1)
            p.setLayout(self.layout)
            return True
        return False

    def get_swatch_buttons(self):
        for color in json.load(open(os.path.join(self.scriptdir, "cs_matid", "swatch_list.json"))):
            self.create_button_from_color(color['color'])

    def create_button_from_color(self, color):
        button = QPushButton('')
        button.setStyleSheet('background-color:%s' % Color(
                rgb=self.split_string_to_rgb(color)))
        button.clicked.connect(partial(self.on_swatch_clicked, swatch_color=color))
        self.add_button_to_layout(button)

    def add_button_to_layout(self, button):
        self.layout.addWidget(button)


# final little bit is to bless the commands needed for csMatID
lx.bless(OpenMatIDPalette, "csMatID")
