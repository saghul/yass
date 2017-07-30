# -*- coding: utf-8 -*-

# Copyright 2008, 2009 Saúl Ibarra <saghul@gmail.com>
# This file is part of YASS.
# 
# YASS is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# YASS is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with YASS.  If not, see <http://www.gnu.org/licenses/>.



from yass.core.core import yass_core
from yass.core.error import YassException
from PyQt4 import QtCore, QtGui

class XferDlgController(object):
    """ Controller class for the Xfer Window dialog. It implements blind transfers and attended transfers.
    """

    def xfer_call(self):
        dst = self.window.ui.dstText.text()
        if self.window.ui.blindRad.isChecked():
            self.blind_xfer(dst)
        else:
            self.attended_xfer(dst)

    def blind_xfer(self, dst):
        try:
            self.core.blind_xfer(self.core.calls.current, dst)
            self.window.close()
        except YassException, e:
            QtGui.QMessageBox.critical(self.window, "Error", str(e))

    def attended_xfer(self, dst):
        pass

    def __init__(self, ui):
        self.window = ui
        try:
            self.core = yass_core()
        except YassException, e:
            QtGui.QMessageBox.critical(self.window, "Error", str(e))

if __name__ == "__main__":
    pass

