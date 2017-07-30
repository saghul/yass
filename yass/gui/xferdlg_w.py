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



from ui.ui_xferdlg import Ui_xferDlg
from PyQt4 import QtCore, QtGui
from xferdlg_c import XferDlgController

class xferDlgWindow(QtGui.QDialog):
    """ Class for starting the Transfer Window dialog.
    """

    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.ui = Ui_xferDlg()
        self.ui.setupUi(self)
        self.controller = XferDlgController(self)

        QtCore.QObject.connect(self.ui.xferBtn, QtCore.SIGNAL("clicked()"), self.controller.xfer_call)

if __name__ == "__main__":
    pass

