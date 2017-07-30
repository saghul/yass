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



from yass.core.core import yass_core
from yass.core.error import YassException
from PyQt4 import QtCore, QtGui
import ui.buddy_icons_rc
import yass.util.sip as sip_utils
import threading

class MainWindowController(object):
    """ Controller class for the Main Window. It handles all the events produced by the interaction of the user with
        the window.
    """

    def make_call(self):
        num = str(self.window.ui.dialText.currentText()) 
        if len(num) > 0:
            try:
                self.core.make_call(num)
            except YassException, e:
                QtGui.QMessageBox.critical(self.window, "Error", str(e))
            else:
                msg = "Calling..."
                self.window.ui.statusbar.emit(QtCore.SIGNAL("update_text"), msg)
                if self.window.ui.dialText.count() == self.window.ui.dialText.maxCount():
                    self.window.ui.dialText.removeItem(0)
                self.window.ui.dialText.insertItem(-1, num)

    def hangup_call(self):
        try:
            self.core.hangup_call(self.core.calls.current)
        except YassException, e:
            QtGui.QMessageBox.critical(self.window, "Error", str(e))

    def answer_call(self):
        try:
            self.core.answer_call(self.core.calls.current)
        except YassException, e:
            QtGui.QMessageBox.critical(self.window, "Error", str(e))
    
    def reject_call(self):
        try:
            self.core.reject_call(self.core.calls.current)
        except YassException, e:
            QtGui.QMessageBox.critical(self.window, "Error", str(e))

    def hold_call(self):
        try:
            if self.holding:
                self.window.ui.actionHold.setText("hold")
                self.holding = False
                self.core.unhold_call(self.core.calls.current)
            else:
                self.window.ui.actionHold.setText("unhold")
                self.holding = True
                self.core.hold_call(self.core.calls.current)
        except YassException, e:
            QtGui.QMessageBox.critical(self.window, "Error", str(e))

    def check_voicemail(self):
        try:
            vmexten = self.core.cfg.acc.acc.voicemail_exten
            self.core.make_call(vmexten)
        except YassException, e:
            QtGui.QMessageBox.critical(self.window, "Error", str(e))

    def friendsPopupMenu(self, point):
        menu = QtGui.QMenu(self.window.ui.buddyList)
        addFriend = QtGui.QAction("Add Friend", menu)
        changeAvail = QtGui.QAction("Change Availability", menu)
        callFriend = QtGui.QAction("Call", menu)
        delFriend = QtGui.QAction("Delete", menu)
        editFriend = QtGui.QAction("Edit", menu)
        changeSubs = QtGui.QAction("Subscribe", menu)
        im = QtGui.QAction("Instant Message", menu)
        menu.addAction(addFriend)
        menu.addAction(changeAvail)
        menu.addAction(callFriend)
        menu.addAction(delFriend)
        menu.addAction(editFriend)
        menu.addAction(changeSubs)
        menu.addAction(im)
        QtCore.QObject.connect(addFriend, QtCore.SIGNAL("activated()"), self._popup_addFriend)
        QtCore.QObject.connect(changeAvail, QtCore.SIGNAL("activated()"), self._popup_changeAvail)
        QtCore.QObject.connect(callFriend, QtCore.SIGNAL("activated()"), self._popup_callFriend)
        QtCore.QObject.connect(delFriend, QtCore.SIGNAL("activated()"), self._popup_delFriend)
        QtCore.QObject.connect(editFriend, QtCore.SIGNAL("activated()"), self._popup_editFriend)
        QtCore.QObject.connect(changeSubs, QtCore.SIGNAL("activated()"), self._popup_changeSubs)
        QtCore.QObject.connect(im, QtCore.SIGNAL("activated()"), self._popup_im)
        
        item = self.window.ui.buddyList.itemAt(point)
        if item is not None:
            buddy = self.core.cfg.find_buddy(item.text(0))
            if self._check_buddy_subscription(buddy):
                changeSubs.setText("Unsubscribe")
            addFriend.setVisible(False)
            changeAvail.setVisible(False)
        else:
            callFriend.setVisible(False)
            delFriend.setVisible(False)
            editFriend.setVisible(False)
            changeSubs.setVisible(False)
            im.setVisible(False)
        menu.exec_(self.window.ui.buddyList.mapToGlobal(point))

    def _check_buddy_subscription(self, buddy):
        if buddy is not None:
            return buddy.subscribed
        else:
            return False

    def _popup_addFriend(self):
        self.window.show_addbuddydlg()

    def _popup_changeAvail(self):
        self.window.show_useravaildlg()
    
    def _popup_callFriend(self):
        name = self.window.ui.buddyList.currentItem().text(0)
        buddy = self.core.cfg.find_buddy(name)
        if buddy is not None:
            try:
                self.core.make_call(buddy.uri)
            except YassException, e:
                QtGui.QMessageBox.critical(self.window, "Error", str(e))

    def _popup_delFriend(self):
        try:
            item = self.window.ui.buddyList.currentItem()
            self.core.delete_buddy(item.text(0))
            self.window.ui.buddyList.removeItemWidget(item, 0)
        except YassException, e:
            QtGui.QMessageBox.critical(self.window, "Error", str(e))

    def _popup_editFriend(self):
        name = self.window.ui.buddyList.currentItem().text(0)
        buddy = self.core.cfg.find_buddy(name)
        if buddy is not None:
            self.window.show_editbuddydlg(buddy)

    def _popup_changeSubs(self):
        name = self.window.ui.buddyList.currentItem().text(0)
        buddy = self.core.cfg.find_buddy(name)
        if buddy is not None:
            self.core.toggle_subscription(buddy)

    def _popup_im(self):
        name = self.window.ui.buddyList.currentItem().text(0)
        buddy = self.core.cfg.find_buddy(name)
        if buddy is not None:
            self.window.show_imdlg(buddy.uri)

    def load_buddies(self):
        for b in self.core.cfg.buddies:
            item = QtGui.QTreeWidgetItem()
            status = b.status()
            if status[0] == 1:
                # Buddy is online
                item.setIcon(0, QtGui.QIcon(":buddy/icons/buddylist/online.png"))
            else:
                item.setIcon(0, QtGui.QIcon(":buddy/icons/buddylist/offline.png"))
            item.setText(0, b.name)
            item.setToolTip(0, b.uri)
            self.window.ui.buddyList.addTopLevelItem(item)
        

    #### Callback functions ###

    def call_state_cb(self, state):
        self.window.ui.line1Text.append(str(state))
        self.window.ui.line1Text.ensureCursorVisible()
        msg = None
        if state.state == "EARLY" or state.state == "CALLING":
            self.window.ui.actionHangup.setEnabled(True)

        if state.state == "CONFIRMED":
            msg = "On call..."
            self.window.ui.actionHangup.setEnabled(True)
            self.window.ui.actionAnswer.setEnabled(False)
            self.window.ui.actionReject.setEnabled(False)
            self.window.ui.actionXfer.setEnabled(True)
            self.window.ui.actionHold.setEnabled(True)
            self.window.ui.actionDtmf.setEnabled(True)
            self.window.ui.actionHistory.setEnabled(False)
            self.window.ui.actionVoicemail.setEnabled(False)
            
        if state.state == "DISCONNCTD":
            msg = "YASS is ready to rock!"
            self.window.ui.actionHangup.setEnabled(False)
            self.window.ui.actionAnswer.setEnabled(False)
            self.window.ui.actionReject.setEnabled(False)
            self.window.ui.actionXfer.setEnabled(False)
            if self.holding:
                self.holding = False
                self.window.ui.actionHold.setText("hold")
                self.window.ui.actionHold.setChecked(False)
            self.window.ui.actionHold.setEnabled(False)
            self.window.ui.actionDtmf.setEnabled(False)
            self.window.ui.actionHistory.setEnabled(True)
            self.window.ui.actionVoicemail.setEnabled(True)
        if msg is not None:
            self.window.ui.statusbar.emit(QtCore.SIGNAL("update_text"), msg)

    def regstate_cb(self, state):
        self.window.ui.line1Text.append(str(state))
        self.window.ui.line1Text.ensureCursorVisible()
        if state.code == "200":
            msg = "Register OK."
        else:
            msg = "Register failed."
        self.window.ui.statusbar.emit(QtCore.SIGNAL("update_text"), msg)

    def incoming_call_cb(self, info, error):
        if error:
            msg = "Could NOT set sound device, using NULL device instead."
            self.window.emit(QtCore.SIGNAL("error_msg"), msg)
            
        msg = "INCOMING CALL: \nURI: %s\n" % info.uri
        self.window.ui.line1Text.append(str(msg))
        self.window.ui.line1Text.ensureCursorVisible()
        msg = "Incoming call from %s" % info.uri
        self.window.ui.statusbar.emit(QtCore.SIGNAL("update_text"), msg)
        self.window.ui.actionHangup.setEnabled(False)
        self.window.ui.actionAnswer.setEnabled(True)
        self.window.ui.actionReject.setEnabled(True)
        self.window.ui.actionHistory.setEnabled(False)
        self.window.ui.actionVoicemail.setEnabled(False)

    def incoming_message_cb(self, msg):
        uri = sip_utils.make_uri(sip_utils.get_user_from_uri(msg.from_uri), sip_utils.get_domain_from_uri(msg.from_uri)) 
        sent = False
        lock = threading.Lock()
        lock.acquire(True)
        for dlg in self.imDlgs:
            if dlg.windowTitle() == uri:
                msg = "<b>%s: </b>%s" % (sip_utils.get_user_from_uri(msg.from_uri), unicode(msg.body, "utf-8"))
                dlg.emit(QtCore.SIGNAL("incoming_msg"), msg)
                sent = True
                break
        lock.release()
        if not sent:
            self.window.emit(QtCore.SIGNAL("new_msg"), uri, msg.body)

    def buddystate_cb(self, state):
        data_online = (state.name, True, state.online_text, state.uri)
        data_offline = (state.name, False, state.online_text, state.uri)
        if state.subscribed:
            if state.online_status == 1:
                self.window.ui.buddyList.emit(QtCore.SIGNAL("buddy_icon"), data_online)
            else:
                self.window.ui.buddyList.emit(QtCore.SIGNAL("buddy_icon"), data_offline)
        else:
            self.window.ui.buddyList.emit(QtCore.SIGNAL("buddy_icon"), data_offline)

    ### ---------- ###

    def __init__(self, ui):
        self.window = ui
        self.imDlgs = []
        try:
            self.core = yass_core()
            self.holding = False
            self.core.cb.set_cb_callstate(self.call_state_cb)
            self.core.cb.set_cb_regstate(self.regstate_cb)
            self.core.cb.set_cb_incoming_call(self.incoming_call_cb)
            self.core.cb.set_cb_buddystate(self.buddystate_cb)
            self.core.cb.set_cb_incoming_message(self.incoming_message_cb)
            self.core.start()
            self.load_buddies()
            self.window.ui.dialText.setFocus()
        except YassException, e:
            QtGui.QMessageBox.critical(self.window, "Error", str(e))

if __name__ == "__main__":
    pass

