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



from pysqlite2 import dbapi2 as sqlite
from PyQt4 import QtCore, QtGui
from yass.util.acc_cfg import yass_acc_cfg
from yass.util.media_cfg import yass_media_cfg
from yass.util.log_cfg import yass_log_cfg
from yass.core.core import yass_core
from yass.core.error import YassException
import yass.core.codecs as codecs
import yass.core.dbconfig as dbconfig
import yass.util.stun as stun_utils


class ConfigDlgController(object):
    """ Controller class for the Configuration Dialog. It controls the loading and application of changes to:
            * Account settings.
            * Media settings.
            * Log settings.
            * System settings.
    """

    def load_acc_cfg(self):
        try:
            con = sqlite.connect(dbconfig.DB_CONFIG)
            acc_cfg = yass_acc_cfg()
            for row in con.execute("SELECT opt, val FROM acc"):
                acc_cfg.__dict__[str(row[0])] = str(row[1])
            for row in con.execute("SELECT opt, val FROM ua WHERE opt LIKE 'stun_%'"):
                acc_cfg.__dict__[str(row[0])] = str(row[1])
            con.close()
            self.window.ui.userText.setText(acc_cfg.acc_user)
            self.window.ui.passwordText.setText(acc_cfg.acc_password)
            self.window.ui.domainText.setText(acc_cfg.acc_domain)
            self.window.ui.regtimeNum.setValue(int(acc_cfg.reg_timeout))
            self.window.ui.stunText.setText(acc_cfg.stun_host)
            self.window.ui.presenceBox.setChecked(False if str(acc_cfg.publish_enabled) == "0" else True)
            self.window.ui.vmextenText.setText(acc_cfg.voicemail_exten)
        except sqlite.Error:
            raise YassException("GUI", "001", "Error loading account settings.")
    
    def load_media_cfg(self):
        try:
            con = sqlite.connect(dbconfig.DB_CONFIG)
            media_cfg = yass_media_cfg()
            for row in con.execute("SELECT opt, val FROM media"):
                media_cfg.__dict__[str(row[0])] = str(row[1])
            con.close()
            dtmfmode = "0" if media_cfg.dtmfmode == "rfc2833" else "1"
            self.window.ui.vadBox.setChecked(True if str(media_cfg.no_vad) == "0" else False)
            self.window.ui.framelenBox.setValue(int(media_cfg.audio_frame_ptime))
            self.window.ui.qualityBox.setValue(int(media_cfg.quality))
            self.window.ui.dtmfmodeBox.setCurrentIndex(int(dtmfmode))
        except sqlite.Error:
            raise YassException("GUI", "002", "Error loading media settings.")

    def load_codecs_cfg(self):
        try:
            con = sqlite.connect(dbconfig.DB_CONFIG)
            for row in con.execute("SELECT codec FROM codecs WHERE priority > -1 ORDER BY priority DESC"):
                self.window.ui.enaList.addItem(str(row[0]))
            for row in con.execute("SELECT codec FROM codecs WHERE priority = -1"):
                self.window.ui.disList.addItem(str(row[0]))
        except sqlite.Error:
            raise YassException("GUI", "009", "Error loading codec settings.")

    def load_log_cfg(self):
        try:
            con = sqlite.connect(dbconfig.DB_CONFIG)
            log_cfg = yass_log_cfg()
            for row in con.execute("SELECT opt, val FROM log"):
                log_cfg.__dict__[str(row[0])] = str(row[1])
            con.close()
            self.window.ui.msgBox.setChecked(True if str(log_cfg.msg_logging) == "1" else False)
            self.window.ui.levelBox.setValue(int(log_cfg.level))
            self.window.ui.fileText.setText(log_cfg.filename)
        except sqlite.Error:
            raise YassException("GUI", "003", "Error loading log settings.")

    def load_sys_cfg(self):
        try:
            list = self.core.dev.list
            for item in list:
                self.window.ui.playbackdevBox.insertItem(item.id, item.name)
                self.window.ui.capturedevBox.insertItem(item.id, item.name)
            current_devs = self.core.dev.get_stored_dev()
            if current_devs[1] != -1:
                self.window.ui.playbackdevBox.setCurrentIndex(current_devs[1])
            if current_devs[0] != -1:
                self.window.ui.capturedevBox.setCurrentIndex(current_devs[0])
            self.window.ui.portBox.setValue(int(self.core.cfg.net.bindport))
            transport = "0" if self.core.cfg.acc.acc.acc_transport == "udp" else "1"
            self.window.ui.transportBox.setCurrentIndex(int(transport))
        except sqlite.Error:
            raise YassException("GUI", "004", "Error loading system settings.")

    def apply(self):
        try:
            self.apply_acc()
            self.apply_media()
            self.apply_codecs()
            self.apply_log()
            self.apply_sys()

            if self.restart_acc and self.restart_core:
                self._restart_core()
            elif self.restart_acc:
                self._restart_acc()
            elif self.restart_core:
                self._restart_core()

        except YassException, e:
            QtGui.QMessageBox.critical(self.window, "Error", str(e))
        else:
            self.window.close()

    def apply_acc(self):
        try:
            if self.window.ui.userText.isModified() or  self.window.ui.passwordText.isModified() or  self.window.ui.domainText.isModified():
                self.restart_acc = True

            if self.window.ui.stunText.isModified():
                self.restart_core = True

            user = self.window.ui.userText.text()
            password = self.window.ui.passwordText.text()
            domain = self.window.ui.domainText.text()
            reg_timeout = str(self.window.ui.regtimeNum.value())
            stun = self.window.ui.stunText.text()
            if stun and not stun_utils.stun_valid_host(stun):
                QtGui.QMessageBox.warning(self.window, "Info", "Invalid STUN host. STUN has been disabled.")
                stun = ""
            presence = "1" if self.window.ui.presenceBox.isChecked() else "0"
            vmexten = self.window.ui.vmextenText.text()
            con = sqlite.connect(dbconfig.DB_CONFIG)
            con.isolation_level = None
            con.execute("UPDATE acc set val='%s' WHERE opt='acc_user'" % user)
            con.execute("UPDATE acc set val='%s' WHERE opt='acc_password'" % password)
            con.execute("UPDATE acc set val='%s' WHERE opt='acc_domain'" % domain)
            con.execute("UPDATE acc set val='%s' WHERE opt='reg_timeout'" % reg_timeout)
            con.execute("UPDATE acc set val='%s' WHERE opt='publish_enabled'" % presence)
            con.execute("UPDATE acc set val='%s' WHERE opt='voicemail_exten'" % vmexten)
            con.execute("UPDATE ua set val='%s' WHERE opt='stun_host'" % stun)
            con.close()
        except sqlite.Error:
            raise YassException("GUI", "005", "Error saving account settings.")

    def apply_media(self):
        try:
            novad = "0" if self.window.ui.vadBox.isChecked() else "1"
            size = str(self.window.ui.framelenBox.value())
            quality = str(self.window.ui.qualityBox.value())
            dtmfmode = "rfc2833" if self.window.ui.dtmfmodeBox.currentIndex() == 0 else "info"
            con = sqlite.connect(dbconfig.DB_CONFIG)
            con.isolation_level = None
            con.execute("UPDATE media set val='%s' WHERE opt='no_vad'" % novad)
            con.execute("UPDATE media set val='%s' WHERE opt='audio_frame_ptime'" % size)
            con.execute("UPDATE media set val='%s' WHERE opt='quality'" % quality)
            con.execute("UPDATE media set val='%s' WHERE opt='dtmfmode'" % dtmfmode)
            con.close()
        except sqlite.Error:
            raise YassException("GUI", "006", "Error saving media settings.")
    
    def apply_codecs(self):
        try:
            con = sqlite.connect(dbconfig.DB_CONFIG)
            con.isolation_level = None
            i = 0
            priority = 200
            while i < self.window.ui.enaList.count():
                item = self.window.ui.enaList.item(i)
                con.execute("UPDATE codecs set priority=%d WHERE codec='%s'" %(priority, item.text()))
                i += 1
                priority -= 10

            i = 0
            while i < self.window.ui.disList.count():
                item = self.window.ui.disList.item(i)
                con.execute("UPDATE codecs set priority = -1 WHERE codec='%s'" %(item.text()))
                i += 1
            con.close()
            codecs.load_codecs()
        except sqlite.Error:
            raise YassException("GUI", "010", "Error saving codec settings.")

    def apply_log(self):
        try:
            if self.window.ui.fileText.isModified():
                self.restart_core = True

            msg = "1" if self.window.ui.msgBox.isChecked() else "0"
            filename = self.window.ui.fileText.text()
            level = str(self.window.ui.levelBox.value())
            con = sqlite.connect(dbconfig.DB_CONFIG)
            con.isolation_level = None
            con.execute("UPDATE log set val='%s' WHERE opt='msg_logging'" % msg)
            con.execute("UPDATE log set val='%s' WHERE opt='filename'" % filename)
            con.execute("UPDATE log set val='%s' WHERE opt='level'" % level)
            con.execute("UPDATE log set val='%s' WHERE opt='console_level'" % level)
            con.close()
        except sqlite.Error:
            raise YassException("GUI", "007", "Error saving log settings.")

    def apply_sys(self):
        try:
            playbackdev = self.window.ui.playbackdevBox.currentIndex()
            capturedev = self.window.ui.capturedevBox.currentIndex()
            """ First argument is capture device and second is playback device """
            if self.core.dev.get_dev() != (capturedev, playbackdev):
                self.core.dev.store_dev(capturedev, playbackdev)
            port = str(self.window.ui.portBox.value())
            transport = "udp" if self.window.ui.transportBox.currentIndex() == 0 else "tcp"
            con = sqlite.connect(dbconfig.DB_CONFIG)
            con.isolation_level = None
            con.execute("UPDATE net set val='%s' WHERE opt='bindport'" % port)
            con.execute("UPDATE acc set val='%s' WHERE opt='acc_transport'" % transport)
            con.close()
        except sqlite.Error:
            raise YassException("GUI", "008", "Error saving system settings.")

    def enable_codec(self):
        row = self.window.ui.enaList.currentRow()
        if row > -1:
            item = self.window.ui.enaList.takeItem(row)
            self.window.ui.disList.addItem(item)
            del item

    def disable_codec(self):
        row = self.window.ui.disList.currentRow()
        if row > -1:
            item = self.window.ui.disList.takeItem(row)
            self.window.ui.enaList.addItem(item)
            del item

    def test_devices(self):
        try:
            playbackdev = self.window.ui.playbackdevBox.currentIndex()
            capturedev = self.window.ui.capturedevBox.currentIndex()
            self.core.dev.set_dev(capturedev, playbackdev)
        except YassException, e:
            QtGui.QMessageBox.critical(self.window, "Error", str(e))
        else:
            QtGui.QMessageBox.information(self.window, "Info", "Devices set OK!")

    def set_restart_acc(self):
        self.restart_acc = True

    def set_restart_core(self):
        self.restart_core = True

    def _restart_core(self):
        self.window.setCursor(QtCore.Qt.WaitCursor)
        self.core.restart_core()
        self.window.unsetCursor()
        self.restart_core = False
        self.restart_acc = False
    
    def _restart_acc(self):
        self.window.setCursor(QtCore.Qt.WaitCursor)
        self.core.restart_acc()
        self.window.unsetCursor()
        self.restart_acc = False

    def __init__(self, ui):
        self.window = ui
        self.restart_acc = False
        self.restart_core = False
        try:
            self.core = yass_core()
            self.load_acc_cfg()
            self.load_media_cfg()
            self.load_codecs_cfg()
            self.load_log_cfg()
            self.load_sys_cfg()
        except YassException, e:
            QtGui.QMessageBox.warning(self.window, "Error", str(e))

if __name__ == "__main__":
    pass

