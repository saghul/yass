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



import yass.core.dbconfig as dbconfig
from pysqlite2 import dbapi2 as sqlite
from yass.core.core import yass_core
from yass.core.error import YassException
from PyQt4 import QtCore, QtGui

class UseravailDlgController(object):
    """ Controller class for the user availability change window.
    """

    def change_availability(self):
        try:
            descr = str(self.window.ui.descrText.text())
            if self.window.ui.onRad.isChecked():
                self.core.set_presence_status(True, descr)
            else:
                self.core.set_presence_status(False, descr)
            online = "1" if self.window.ui.onRad.isChecked() else "0"
            try:
                con = sqlite.connect(dbconfig.DB_CONFIG)
                con.isolation_level = None
                con.execute("UPDATE presentity set val='%s' WHERE opt='p_online'" % online)
                con.execute("UPDATE presentity set val='%s' WHERE opt='p_text'" % descr)
                con.close()
            except sqlite.Error:
                raise YassException("GUI", "012", "Error saving presentity settings.")
        except YassException, e:
            QtGui.QMessageBox.critical(self.window, "Error", str(e))
        else:
            self.window.close()

    def load_status(self):
        try:
            con = sqlite.connect(dbconfig.DB_CONFIG)
            for row in con.execute("SELECT opt, val FROM presentity"):
                if str(row[0]) == "p_online":
                    online = str(row[1])
                    continue
                if str(row[0]) == "p_text":
                    descr = str(row[1])
                    continue
            con.close()
            if bool(int(online)):
                self.window.ui.onRad.setChecked(True)
                self.window.ui.offRad.setChecked(False)
            else:
                self.window.ui.onRad.setChecked(False)
                self.window.ui.offRad.setChecked(True)
            self.window.ui.descrText.setText(descr)
        except sqlite.Error:
            raise YassException("GUI", "011", "Error loading presentity settings.")

    def __init__(self, ui):
        self.window = ui
        try:
            self.core = yass_core()
            self.load_status()
        except YassException, e:
            QtGui.QMessageBox.critical(self.window, "Error", str(e))

if __name__ == "__main__":
    pass


