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



from yass.core.error import YassException
from PyQt4 import QtCore, QtGui
from pysqlite2 import dbapi2 as sqlite
import yass.modules.callhistory as mod_callhistory

class HistoryDlgController(object):
    """ Controller class for loading Call History data.
    """

    def load_table_data(self):
        history = mod_callhistory.get_history_data()
        for data in history:
            rownum = self.window.ui.tabGrid.rowCount()
            self.window.ui.tabGrid.insertRow(rownum)
            item = QtGui.QTableWidgetItem(data[0])
            self.window.ui.tabGrid.setItem(rownum, 0, item)
            item = QtGui.QTableWidgetItem(data[1])
            self.window.ui.tabGrid.setItem(rownum, 1, item)
            item = QtGui.QTableWidgetItem(data[2])
            self.window.ui.tabGrid.setItem(rownum, 2, item)
        self.window.ui.tabGrid.setSortingEnabled(True)
        self.window.ui.tabGrid.sortItems(2, QtCore.Qt.DescendingOrder)
        self.window.ui.tabGrid.update()

    def _adjust_width(self):
        self.window.ui.tabGrid.setColumnWidth(0, 175)
        self.window.ui.tabGrid.setColumnWidth(1, 101)
        self.window.ui.tabGrid.setColumnWidth(2, 165)

    def reset_data(self):
        try:
            mod_callhistory.delete_history()
        except YassException, e:
            QtGui.QMessageBox.warning(self.window, "Error", str(e))
        else:
            self.window.ui.tabGrid.clearContents()
            self.window.ui.tabGrid.setRowCount(0)
            QtGui.QMessageBox.information(self.window, "Info", "Call history data has been reset.")
            self.window.close()

    def __init__(self, ui):
        self.window = ui
        self._adjust_width()
        try:
            self.load_table_data()
        except YassException, e:
            QtGui.QMessageBox.warning(self.window, "Error", str(e))

if __name__ == "__main__":
    pass

