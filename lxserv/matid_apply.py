#!/usr/bin/env python
################################################################################
#
# matid_apply.py
# Description: The class used for applying a swatch color material to the selected polygons
# Usage:
# Explosivo.toggle - toggles the explode map on the selected meshes
# Explosivo.toggle other_explode_morph_name - toggles the explode on the selected meshes
# but uses a custom named morph map
# Explosivo.delete removes the morphs on all meshes instead of toggling them
# Explosivo.delete other_explode_morph_name - removes morph on all meshes with special morph name
# Author: Chris Sprance Entrada Interactive
# csMatID.apply 1.01.01.0
################################################################################

import lx
import lxifc
import lxu.command
import modo
import cs_matid


class MatIDApply(lxu.command.BasicCommand):
    def __init__(self):
        lxu.command.BasicCommand.__init__(self)
        reload(cs_matid)
        self.dyna_Add('swatch_color', lx.symbol.sTYPE_STRING)

    def cmd_Flags(self):
        return lx.symbol.fCMD_MODEL | lx.symbol.fCMD_UNDO

    def basic_Enable(self, msg):
        return True

    def cmd_Interact(self):
        pass

    def basic_Execute(self, msg, flags):
        if self.dyna_IsSet(0):
            matid = cs_matid.MatIDApplyClass(self.dyna_String(0, '1.01.01.0'))
            matid.create_material()

    def cmd_Query(self, index, vaQuery):
        lx.notimpl()


lx.bless(MatIDApply, "csMatID.apply")
