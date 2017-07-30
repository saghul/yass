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
from PyQt4 import QtCore, QtGui

class EditbuddyDlgController(object):
    """ Controller class for editing buddies.
    """

    def __init__(self, ui, buddy):
        self.window = ui
        self.core = yass_core()
        if buddy:
            self.window.ui.nameText.setText(buddy.name)
            self.window.ui.uriText.setText(buddy.uri)
            self.window.ui.subsBox.setChecked(buddy.subscribed)

    def save_buddy(self):
        close = False
        origsubs = self.core.cfg.find_buddy(str(self.window.ui.nameText.text())).subscribed
        if self.window.ui.uriText.isModified():
            b = self.core.cfg.find_buddy(str(self.window.ui.uriText.text()))
            if b:
                QtGui.QMessageBox.warning(self.window, "Info", "There is another buddy with that URI.")
            else:
                self.core.delete_buddy(str(self.window.ui.nameText.text()))
                self.core.add_buddy(str(self.window.ui.nameText.text()), str(self.window.ui.uriText.text()))
                close = True

        if origsubs ^ self.window.ui.subsBox.isChecked():
            newb = yass_core().cfg.find_buddy(str(self.window.ui.nameText.text()))
            yass_core().toggle_subscription(newb)
            close = True
                
        if close:
            self.window.close()


if __name__ == "__main__":
    pass

