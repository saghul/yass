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



from ui.ui_configdlg import Ui_configDlg
from PyQt4 import QtCore, QtGui
from configdlg_c import ConfigDlgController

class configDlgWindow(QtGui.QDialog):
    """ Class for starting the Configuration Dialog.
    """

    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.ui = Ui_configDlg()
        self.ui.setupUi(self)
        self.controller = ConfigDlgController(self)
        QtCore.QObject.connect(self.ui.buttonBox.button(QtGui.QDialogButtonBox.Ok), QtCore.SIGNAL("clicked()"), self.controller.apply)
        QtCore.QObject.connect(self.ui.rightBtn, QtCore.SIGNAL("clicked()"), self.controller.enable_codec)
        QtCore.QObject.connect(self.ui.leftBtn, QtCore.SIGNAL("clicked()"), self.controller.disable_codec)
        QtCore.QObject.connect(self.ui.testBtn, QtCore.SIGNAL("clicked()"), self.controller.test_devices)

        QtCore.QObject.connect(self.ui.presenceBox, QtCore.SIGNAL("stateChanged(int)"), self.controller.set_restart_acc)
        QtCore.QObject.connect(self.ui.regtimeNum, QtCore.SIGNAL("valueChanged(int)"), self.controller.set_restart_acc)
        QtCore.QObject.connect(self.ui.vadBox, QtCore.SIGNAL("stateChanged(int)"), self.controller.set_restart_core)
        QtCore.QObject.connect(self.ui.framelenBox, QtCore.SIGNAL("valueChanged(int)"), self.controller.set_restart_core)
        QtCore.QObject.connect(self.ui.qualityBox, QtCore.SIGNAL("valueChanged(int)"), self.controller.set_restart_core)
        QtCore.QObject.connect(self.ui.dtmfmodeBox, QtCore.SIGNAL("activated(int)"), self.controller.set_restart_core)
        QtCore.QObject.connect(self.ui.levelBox, QtCore.SIGNAL("valueChanged(int)"), self.controller.set_restart_core)
        QtCore.QObject.connect(self.ui.msgBox, QtCore.SIGNAL("stateChanged(int)"), self.controller.set_restart_core)
        QtCore.QObject.connect(self.ui.portBox, QtCore.SIGNAL("valueChanged(int)"), self.controller.set_restart_core)
        QtCore.QObject.connect(self.ui.transportBox, QtCore.SIGNAL("activated(int)"), self.controller.set_restart_core)


if __name__ == "__main__":
    pass

