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



from ui.ui_dtmfdlg import Ui_dtmfDlg
from PyQt4 import QtCore, QtGui
from dtmfdlg_c import DtmfDlgController

class dtmfDlgWindow(QtGui.QDialog):
    """ Class for starting the DTMF tone window.
    """

    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.ui = Ui_dtmfDlg()
        self.ui.setupUi(self)
        self.controller = DtmfDlgController()

        QtCore.QObject.connect(self.ui.oneBtn, QtCore.SIGNAL("clicked()"), lambda d="1": self.controller.send_dtmf(d))
        QtCore.QObject.connect(self.ui.twoBtn, QtCore.SIGNAL("clicked()"), lambda d="2": self.controller.send_dtmf(d))
        QtCore.QObject.connect(self.ui.threeBtn, QtCore.SIGNAL("clicked()"), lambda d="3": self.controller.send_dtmf(d))
        QtCore.QObject.connect(self.ui.fourBtn, QtCore.SIGNAL("clicked()"), lambda d="4": self.controller.send_dtmf(d))
        QtCore.QObject.connect(self.ui.fiveBtn, QtCore.SIGNAL("clicked()"), lambda d="5": self.controller.send_dtmf(d))
        QtCore.QObject.connect(self.ui.sixBtn, QtCore.SIGNAL("clicked()"), lambda d="6": self.controller.send_dtmf(d))
        QtCore.QObject.connect(self.ui.sevenBtn, QtCore.SIGNAL("clicked()"), lambda d="7": self.controller.send_dtmf(d))
        QtCore.QObject.connect(self.ui.eightBtn, QtCore.SIGNAL("clicked()"), lambda d="8": self.controller.send_dtmf(d))
        QtCore.QObject.connect(self.ui.nineBtn, QtCore.SIGNAL("clicked()"), lambda d="9": self.controller.send_dtmf(d))
        QtCore.QObject.connect(self.ui.zeroBtn, QtCore.SIGNAL("clicked()"), lambda d="0": self.controller.send_dtmf(d))
        QtCore.QObject.connect(self.ui.astBtn, QtCore.SIGNAL("clicked()"), lambda d="*": self.controller.send_dtmf(d))
        QtCore.QObject.connect(self.ui.poundBtn, QtCore.SIGNAL("clicked()"), lambda d="#": self.controller.send_dtmf(d))

if __name__ == "__main__":
    pass

