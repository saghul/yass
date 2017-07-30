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



from ui.ui_main import Ui_YassMainWindow
from aboutdlg_w import aboutDlgWindow
from configdlg_w import configDlgWindow
from dtmfdlg_w import dtmfDlgWindow
from xferdlg_w import xferDlgWindow
from historydlg_w import historyDlgWindow
from useravaildlg_w import useravailDlgWindow
from addbuddydlg_w import addbuddyDlgWindow
from editbuddydlg_w import editbuddyDlgWindow
from imdlg_w import imDlgWindow
from main_c import MainWindowController
from PyQt4 import QtCore, QtGui
import ui.buddy_icons_rc
import threading

class YassMainWindow(QtGui.QMainWindow):
    """ Class for starting the YASS Main Window.
    """

    def __init__(self, parent=None):

        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_YassMainWindow()
        self.ui.setupUi(self)
        self.center()

        self.ui.buddyList.setMouseTracking(True)
        self.controller = MainWindowController(self)
        QtCore.QObject.connect(self.ui.actionQuit, QtCore.SIGNAL("activated()"), self.close)
        QtCore.QObject.connect(self.ui.actionHangup, QtCore.SIGNAL("activated()"), self.controller.hangup_call)
        QtCore.QObject.connect(self.ui.actionAnswer, QtCore.SIGNAL("activated()"), self.controller.answer_call)
        QtCore.QObject.connect(self.ui.actionReject, QtCore.SIGNAL("activated()"), self.controller.reject_call)
        QtCore.QObject.connect(self.ui.actionXfer, QtCore.SIGNAL("activated()"), self.show_xferdlg)
        QtCore.QObject.connect(self.ui.actionHold, QtCore.SIGNAL("activated()"), self.controller.hold_call)
        QtCore.QObject.connect(self.ui.actionDtmf, QtCore.SIGNAL("activated()"), self.show_dtmfdlg)
        QtCore.QObject.connect(self.ui.actionConfiguration, QtCore.SIGNAL("activated()"), self.show_configdlg)
        QtCore.QObject.connect(self.ui.actionHistory, QtCore.SIGNAL("activated()"), self.show_historydlg)
        QtCore.QObject.connect(self.ui.actionVoicemail, QtCore.SIGNAL("activated()"), self.controller.check_voicemail)
        QtCore.QObject.connect(self.ui.actionMessage, QtCore.SIGNAL("activated()"), self.show_newimdlg)
        
        QtCore.QObject.connect(self.ui.buddyList, QtCore.SIGNAL("customContextMenuRequested(QPoint)"), self.controller.friendsPopupMenu)
        QtCore.QObject.connect(self.ui.buddyList, QtCore.SIGNAL("buddy_icon"), self.set_buddy_icon)
        QtCore.QObject.connect(self.ui.actionAbout, QtCore.SIGNAL("activated()"), self.show_aboutdlg)
        QtCore.QObject.connect(self.ui.dialBtn, QtCore.SIGNAL("clicked()"), self.controller.make_call)
        QtCore.QObject.connect(self.ui.dialText, QtCore.SIGNAL("activated(int)"), self.controller.make_call)
        QtCore.QObject.connect(self.ui.statusbar, QtCore.SIGNAL("update_text"), self.status_message)
        QtCore.QObject.connect(self, QtCore.SIGNAL("error_msg"), self.error_msg)
        QtCore.QObject.connect(self, QtCore.SIGNAL("close_imdlg"), self.close_imdlg)
        QtCore.QObject.connect(self, QtCore.SIGNAL("new_msg"), self.show_newimdlg)
        self.ui.statusbar.showMessage("YASS is ready to rock!")
        
            
    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

    def show_aboutdlg(self):
        about = aboutDlgWindow(self)
        about.exec_()

    def show_configdlg(self):
        config = configDlgWindow(self)
        config.exec_()

    def show_dtmfdlg(self):
        dtmf = dtmfDlgWindow(self)
        dtmf.exec_()
        
    def show_xferdlg(self):
        xfer = xferDlgWindow(self)
        xfer.exec_()

    def show_historydlg(self):
        history = historyDlgWindow(self)
        history.exec_()

    def show_useravaildlg(self):
        useravail = useravailDlgWindow(self)
        useravail.exec_()

    def show_addbuddydlg(self):
        addbuddy = addbuddyDlgWindow(self)
        QtCore.QObject.connect(addbuddy, QtCore.SIGNAL("add_buddy"), self.add_buddy)
        addbuddy.exec_()
    
    def show_editbuddydlg(self, buddy):
        editbuddy = editbuddyDlgWindow(self, buddy)
        editbuddy.exec_()

    def show_imdlg(self, uri):
        if not self.search_imdlg(uri):
            imdlg = imDlgWindow(self, uri)
            imdlg.show()
            self.controller.imDlgs.append(imdlg)

    def show_newimdlg(self, uri="", msg=""):
        if not self.search_imdlg(uri):
            imdlg = imDlgWindow(self, uri, msg)
            imdlg.show()
            self.controller.imDlgs.append(imdlg)

    def close_imdlg(self, uri):
        lock = threading.Lock()
        lock.acquire(True)
        for dlg in self.controller.imDlgs:
            if dlg.controller.delete or dlg.controller.uri == uri:
                try:
                    self.controller.imDlgs.remove(dlg)
                    break
                except ValueError:
                    pass
                finally:
                    lock.release()

    def search_imdlg(self, uri):
        lock = threading.Lock()
        lock.acquire(True)
        for dlg in self.controller.imDlgs:
            if dlg.controller.uri == uri:
                lock.release()
                return True
        lock.release()
        return False

    def status_message(self, msg):
        self.ui.statusbar.showMessage(msg)

    def error_msg(self, msg):
        QtGui.QMessageBox.critical(self, "Error", msg)

    def add_buddy(self, buddy):
        item = QtGui.QTreeWidgetItem()
        item.setIcon(0, QtGui.QIcon(":buddy/icons/buddylist/offline.png"))
        item.setText(0, buddy)
        self.ui.buddyList.addTopLevelItem(item)

    def set_buddy_icon(self, data):
        items = self.ui.buddyList.findItems(data[0], QtCore.Qt.MatchCaseSensitive, 0)
        if len(items) == 1:
            if data[1]:
                items[0].setIcon(0, QtGui.QIcon(":buddy/icons/buddylist/online.png"))
            else:
                items[0].setIcon(0, QtGui.QIcon(":buddy/icons/buddylist/offline.png"))
            tooltip = "%s\n%s" % (data[2], data[3])
            items[0].setToolTip(0, tooltip)

    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message', "Are you sure to quit?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
            self.setCursor(QtCore.Qt.WaitCursor)
            self.controller.core.stop()
            self.close()
        else:
            event.ignore()


if __name__ == "__main__":
    pass

