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

class ImDlgController(object):
    """ Controller class for Instant Messaging.
    """

    def __init__(self, ui, uri="", msg=""):
        self.window = ui
        self.core = yass_core()
        self.delete = False
        self.uri = uri
        if uri:
            self.window.setWindowTitle(uri)
            self.window.ui.uriText.setText(uri)
            self.window.ui.uriText.setReadOnly(True)
            if msg:
                self.window.ui.msgText.appendHtml("<b>%s: </b>%s" % (sip_utils.get_user_from_uri(uri), unicode(msg, "utf-8")))
            self.window.ui.msgsendText.setFocus()
        else:
            self.window.ui.uriText.setFocus()

    def send_message(self):
        if not self.uri:
            if len(self.window.ui.uriText.text()) == 0:
                QtGui.QMessageBox.critical(self.window, "Error", "You need to specify a URI.")
                return
            else:
                uri = sip_utils.make_uri(str(self.window.ui.uriText.text()), self.core.cfg.acc.acc.acc_domain)
                if self.window.parentWidget().search_imdlg(uri):
                    self.delete = True
                    QtGui.QMessageBox.critical(self.window, "Error", "There is already an open conversation with that URI.")
                    return
                self.uri = uri
                self.window.setWindowTitle(self.uri)
                self.window.ui.uriText.setText(self.uri)
                self.window.ui.uriText.setReadOnly(True)
        try:
            msg = str(self.window.ui.msgsendText.document().toPlainText())
            self.core.send_message(self.uri, msg)
            self.window.ui.msgText.appendHtml("<b>me: </b>%s" % unicode(msg, "utf-8"))
            self.window.ui.msgsendText.clear()
            self.window.ui.msgsendText.setFocus()
        except YassException, e:
            QtGui.QMessageBox.critical(self.window, "Error", str(e))

    def incoming_msg(self, msg):
        self.window.ui.msgText.appendHtml(msg)
        
if __name__ == "__main__":
    pass

