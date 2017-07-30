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



from ui.ui_historydlg import Ui_historyDlg
from PyQt4 import QtCore, QtGui
from historydlg_c import HistoryDlgController

class historyDlgWindow(QtGui.QDialog):
    """ Class for starting the Call history window.
    """

    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.ui = Ui_historyDlg()
        self.ui.setupUi(self)
        self.controller = HistoryDlgController(self)
        QtCore.QObject.connect(self.ui.btnBox.button(QtGui.QDialogButtonBox.Reset), QtCore.SIGNAL("clicked()"), self.controller.reset_data)

if __name__ == "__main__":
    pass

