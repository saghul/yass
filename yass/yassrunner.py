#!/usr/bin/python2.5
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



from gui.main_w import YassMainWindow
from PyQt4 import QtCore, QtGui
import gui.ui.splash_images_rc
import sys

def start():
    app = QtGui.QApplication(sys.argv)
    pic = QtGui.QPixmap(":splash/images/splash.png")
    splash = QtGui.QSplashScreen(pic, QtCore.Qt.WindowStaysOnTopHint)
    splash.setMask(pic.mask())
    splash.show()
    mainw = YassMainWindow()
    mainw.show()
    splash.finish(mainw)
    sys.exit(app.exec_())

if __name__ == "__main__":
    pass

