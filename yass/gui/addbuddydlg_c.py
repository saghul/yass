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



import yass.util.sip as sip_utils
from yass.core.core import yass_core
from yass.core.error import YassException
from PyQt4 import QtCore, QtGui

class AddbuddyDlgController(object):
    """ Controller class for adding new buddies.
    """

    def add_buddy(self):
        if len(str(self.window.ui.nameText.text())) == 0 or len(str(self.window.ui.uriText.text())) == 0:
            QtGui.QMessageBox.information(self.window, "Info", "You need to specify the buddy name and the URI.")
        else:
            try:
                buddy = str(self.window.ui.nameText.text())
                uri = str(self.window.ui.uriText.text())
                self.core.add_buddy(buddy, uri)
                self.window.emit(QtCore.SIGNAL("add_buddy"), buddy)
            except YassException, e:
                QtGui.QMessageBox.warning(self.window, "Error", str(e))
                self.window.close()
            else:
                self.window.close()

    def __init__(self, ui):
        self.window = ui
        try:
            self.core = yass_core()
        except YassException, e:
            QtGui.QMessageBox.critical(self.window, "Error", str(e))

if __name__ == "__main__":
    pass

