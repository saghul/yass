# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configdlg.ui'
#
# Created: Sat Aug 22 03:12:42 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_configDlg(object):
    def setupUi(self, configDlg):
        configDlg.setObjectName("configDlg")
        configDlg.resize(430, 350)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(configDlg.sizePolicy().hasHeightForWidth())
        configDlg.setSizePolicy(sizePolicy)
        configDlg.setMaximumSize(QtCore.QSize(430, 350))
        self.verticalLayout = QtGui.QVBoxLayout(configDlg)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cfgTabs = QtGui.QTabWidget(configDlg)
        self.cfgTabs.setObjectName("cfgTabs")
        self.accTab = QtGui.QWidget()
        self.accTab.setObjectName("accTab")
        self.gridLayout = QtGui.QGridLayout(self.accTab)
        self.gridLayout.setObjectName("gridLayout")
        self.userLabel = QtGui.QLabel(self.accTab)
        self.userLabel.setObjectName("userLabel")
        self.gridLayout.addWidget(self.userLabel, 0, 0, 1, 1)
        self.userText = QtGui.QLineEdit(self.accTab)
        self.userText.setObjectName("userText")
        self.gridLayout.addWidget(self.userText, 0, 1, 1, 1)
        self.passLabel = QtGui.QLabel(self.accTab)
        self.passLabel.setObjectName("passLabel")
        self.gridLayout.addWidget(self.passLabel, 1, 0, 1, 1)
        self.passwordText = QtGui.QLineEdit(self.accTab)
        self.passwordText.setEchoMode(QtGui.QLineEdit.PasswordEchoOnEdit)
        self.passwordText.setObjectName("passwordText")
        self.gridLayout.addWidget(self.passwordText, 1, 1, 1, 1)
        self.domainLabel = QtGui.QLabel(self.accTab)
        self.domainLabel.setObjectName("domainLabel")
        self.gridLayout.addWidget(self.domainLabel, 2, 0, 1, 1)
        self.domainText = QtGui.QLineEdit(self.accTab)
        self.domainText.setObjectName("domainText")
        self.gridLayout.addWidget(self.domainText, 2, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 7, 1, 1, 1)
        self.regtimeNum = QtGui.QSpinBox(self.accTab)
        self.regtimeNum.setMaximum(3600)
        self.regtimeNum.setProperty("value", QtCore.QVariant(3600))
        self.regtimeNum.setObjectName("regtimeNum")
        self.gridLayout.addWidget(self.regtimeNum, 3, 1, 1, 1)
        self.regtimeLabel = QtGui.QLabel(self.accTab)
        self.regtimeLabel.setObjectName("regtimeLabel")
        self.gridLayout.addWidget(self.regtimeLabel, 3, 0, 1, 1)
        self.stunText = QtGui.QLineEdit(self.accTab)
        self.stunText.setObjectName("stunText")
        self.gridLayout.addWidget(self.stunText, 4, 1, 1, 1)
        self.stunLabel = QtGui.QLabel(self.accTab)
        self.stunLabel.setObjectName("stunLabel")
        self.gridLayout.addWidget(self.stunLabel, 4, 0, 1, 1)
        self.presenceBox = QtGui.QCheckBox(self.accTab)
        self.presenceBox.setObjectName("presenceBox")
        self.gridLayout.addWidget(self.presenceBox, 5, 1, 1, 1)
        self.presenceLabel = QtGui.QLabel(self.accTab)
        self.presenceLabel.setObjectName("presenceLabel")
        self.gridLayout.addWidget(self.presenceLabel, 5, 0, 1, 1)
        self.vmextenLabel = QtGui.QLabel(self.accTab)
        self.vmextenLabel.setObjectName("vmextenLabel")
        self.gridLayout.addWidget(self.vmextenLabel, 6, 0, 1, 1)
        self.vmextenText = QtGui.QLineEdit(self.accTab)
        self.vmextenText.setObjectName("vmextenText")
        self.gridLayout.addWidget(self.vmextenText, 6, 1, 1, 1)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/configuration/icons/configuration/acc.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cfgTabs.addTab(self.accTab, icon, "")
        self.mediaTab = QtGui.QWidget()
        self.mediaTab.setObjectName("mediaTab")
        self.gridLayout_2 = QtGui.QGridLayout(self.mediaTab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.vadLable = QtGui.QLabel(self.mediaTab)
        self.vadLable.setObjectName("vadLable")
        self.gridLayout_2.addWidget(self.vadLable, 0, 0, 1, 1)
        self.vadBox = QtGui.QCheckBox(self.mediaTab)
        self.vadBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.vadBox.setObjectName("vadBox")
        self.gridLayout_2.addWidget(self.vadBox, 0, 1, 1, 1)
        self.framelenLabel = QtGui.QLabel(self.mediaTab)
        self.framelenLabel.setObjectName("framelenLabel")
        self.gridLayout_2.addWidget(self.framelenLabel, 1, 0, 1, 1)
        self.framelenBox = QtGui.QSpinBox(self.mediaTab)
        self.framelenBox.setMinimum(20)
        self.framelenBox.setMaximum(100)
        self.framelenBox.setSingleStep(10)
        self.framelenBox.setProperty("value", QtCore.QVariant(20))
        self.framelenBox.setObjectName("framelenBox")
        self.gridLayout_2.addWidget(self.framelenBox, 1, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 4, 0, 1, 1)
        self.qualityLabel = QtGui.QLabel(self.mediaTab)
        self.qualityLabel.setObjectName("qualityLabel")
        self.gridLayout_2.addWidget(self.qualityLabel, 2, 0, 1, 1)
        self.qualityBox = QtGui.QSlider(self.mediaTab)
        self.qualityBox.setMinimum(1)
        self.qualityBox.setMaximum(10)
        self.qualityBox.setProperty("value", QtCore.QVariant(6))
        self.qualityBox.setOrientation(QtCore.Qt.Horizontal)
        self.qualityBox.setTickPosition(QtGui.QSlider.TicksBelow)
        self.qualityBox.setTickInterval(1)
        self.qualityBox.setObjectName("qualityBox")
        self.gridLayout_2.addWidget(self.qualityBox, 2, 1, 1, 1)
        self.dtmfmodeLabel = QtGui.QLabel(self.mediaTab)
        self.dtmfmodeLabel.setObjectName("dtmfmodeLabel")
        self.gridLayout_2.addWidget(self.dtmfmodeLabel, 3, 0, 1, 1)
        self.dtmfmodeBox = QtGui.QComboBox(self.mediaTab)
        self.dtmfmodeBox.setObjectName("dtmfmodeBox")
        self.dtmfmodeBox.addItem(QtCore.QString())
        self.dtmfmodeBox.addItem(QtCore.QString())
        self.gridLayout_2.addWidget(self.dtmfmodeBox, 3, 1, 1, 1)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/configuration/icons/configuration/media.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cfgTabs.addTab(self.mediaTab, icon1, "")
        self.codecTab = QtGui.QWidget()
        self.codecTab.setObjectName("codecTab")
        self.horizontalLayout = QtGui.QHBoxLayout(self.codecTab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.enaList = QtGui.QListWidget(self.codecTab)
        self.enaList.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.enaList.setDragEnabled(True)
        self.enaList.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        self.enaList.setMovement(QtGui.QListView.Free)
        self.enaList.setObjectName("enaList")
        self.verticalLayout_3.addWidget(self.enaList)
        self.enaLabel = QtGui.QLabel(self.codecTab)
        self.enaLabel.setObjectName("enaLabel")
        self.verticalLayout_3.addWidget(self.enaLabel)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.arrowFrame = QtGui.QWidget(self.codecTab)
        self.arrowFrame.setObjectName("arrowFrame")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.arrowFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.rightBtn = QtGui.QPushButton(self.arrowFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightBtn.sizePolicy().hasHeightForWidth())
        self.rightBtn.setSizePolicy(sizePolicy)
        self.rightBtn.setMaximumSize(QtCore.QSize(28, 28))
        self.rightBtn.setObjectName("rightBtn")
        self.verticalLayout_2.addWidget(self.rightBtn)
        self.leftBtn = QtGui.QPushButton(self.arrowFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftBtn.sizePolicy().hasHeightForWidth())
        self.leftBtn.setSizePolicy(sizePolicy)
        self.leftBtn.setMaximumSize(QtCore.QSize(28, 28))
        self.leftBtn.setObjectName("leftBtn")
        self.verticalLayout_2.addWidget(self.leftBtn)
        self.horizontalLayout.addWidget(self.arrowFrame)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.disList = QtGui.QListWidget(self.codecTab)
        self.disList.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.disList.setDragEnabled(True)
        self.disList.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        self.disList.setMovement(QtGui.QListView.Free)
        self.disList.setObjectName("disList")
        self.verticalLayout_4.addWidget(self.disList)
        self.disLabel = QtGui.QLabel(self.codecTab)
        self.disLabel.setObjectName("disLabel")
        self.verticalLayout_4.addWidget(self.disLabel)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/configuration/icons/configuration/codecs.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cfgTabs.addTab(self.codecTab, icon2, "")
        self.logTab = QtGui.QWidget()
        self.logTab.setObjectName("logTab")
        self.gridLayout_3 = QtGui.QGridLayout(self.logTab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.levelLabel = QtGui.QLabel(self.logTab)
        self.levelLabel.setObjectName("levelLabel")
        self.gridLayout_3.addWidget(self.levelLabel, 0, 0, 1, 1)
        self.levelBox = QtGui.QSpinBox(self.logTab)
        self.levelBox.setMaximum(9)
        self.levelBox.setProperty("value", QtCore.QVariant(9))
        self.levelBox.setObjectName("levelBox")
        self.gridLayout_3.addWidget(self.levelBox, 0, 1, 1, 1)
        self.fileLabel = QtGui.QLabel(self.logTab)
        self.fileLabel.setObjectName("fileLabel")
        self.gridLayout_3.addWidget(self.fileLabel, 1, 0, 1, 1)
        self.msgLabel = QtGui.QLabel(self.logTab)
        self.msgLabel.setObjectName("msgLabel")
        self.gridLayout_3.addWidget(self.msgLabel, 2, 0, 1, 1)
        self.msgBox = QtGui.QCheckBox(self.logTab)
        self.msgBox.setObjectName("msgBox")
        self.gridLayout_3.addWidget(self.msgBox, 2, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 3, 0, 1, 1)
        self.fileText = QtGui.QLineEdit(self.logTab)
        self.fileText.setObjectName("fileText")
        self.gridLayout_3.addWidget(self.fileText, 1, 1, 1, 1)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/configuration/icons/configuration/log.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cfgTabs.addTab(self.logTab, icon3, "")
        self.sysTab = QtGui.QWidget()
        self.sysTab.setEnabled(True)
        self.sysTab.setObjectName("sysTab")
        self.gridLayout_4 = QtGui.QGridLayout(self.sysTab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.devLabel = QtGui.QLabel(self.sysTab)
        self.devLabel.setObjectName("devLabel")
        self.gridLayout_4.addWidget(self.devLabel, 0, 0, 1, 1)
        self.portLabel = QtGui.QLabel(self.sysTab)
        self.portLabel.setObjectName("portLabel")
        self.gridLayout_4.addWidget(self.portLabel, 3, 0, 1, 1)
        self.portBox = QtGui.QSpinBox(self.sysTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.portBox.sizePolicy().hasHeightForWidth())
        self.portBox.setSizePolicy(sizePolicy)
        self.portBox.setMinimum(1025)
        self.portBox.setMaximum(65535)
        self.portBox.setProperty("value", QtCore.QVariant(5060))
        self.portBox.setObjectName("portBox")
        self.gridLayout_4.addWidget(self.portBox, 3, 1, 1, 1)
        self.playbackdevBox = QtGui.QComboBox(self.sysTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playbackdevBox.sizePolicy().hasHeightForWidth())
        self.playbackdevBox.setSizePolicy(sizePolicy)
        self.playbackdevBox.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContentsOnFirstShow)
        self.playbackdevBox.setObjectName("playbackdevBox")
        self.gridLayout_4.addWidget(self.playbackdevBox, 0, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem3, 6, 0, 1, 1)
        self.capturedevLabel = QtGui.QLabel(self.sysTab)
        self.capturedevLabel.setObjectName("capturedevLabel")
        self.gridLayout_4.addWidget(self.capturedevLabel, 1, 0, 1, 1)
        self.capturedevBox = QtGui.QComboBox(self.sysTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.capturedevBox.sizePolicy().hasHeightForWidth())
        self.capturedevBox.setSizePolicy(sizePolicy)
        self.capturedevBox.setObjectName("capturedevBox")
        self.gridLayout_4.addWidget(self.capturedevBox, 1, 1, 1, 1)
        self.testBtn = QtGui.QPushButton(self.sysTab)
        self.testBtn.setObjectName("testBtn")
        self.gridLayout_4.addWidget(self.testBtn, 2, 0, 1, 2)
        self.transportLabel = QtGui.QLabel(self.sysTab)
        self.transportLabel.setObjectName("transportLabel")
        self.gridLayout_4.addWidget(self.transportLabel, 4, 0, 1, 1)
        self.transportBox = QtGui.QComboBox(self.sysTab)
        self.transportBox.setObjectName("transportBox")
        self.transportBox.addItem(QtCore.QString())
        self.transportBox.addItem(QtCore.QString())
        self.gridLayout_4.addWidget(self.transportBox, 4, 1, 1, 1)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/configuration/icons/configuration/cfg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cfgTabs.addTab(self.sysTab, icon4, "")
        self.verticalLayout.addWidget(self.cfgTabs)
        self.buttonBox = QtGui.QDialogButtonBox(configDlg)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.userLabel.setBuddy(self.userText)
        self.passLabel.setBuddy(self.passwordText)
        self.domainLabel.setBuddy(self.domainText)
        self.regtimeLabel.setBuddy(self.regtimeNum)
        self.stunLabel.setBuddy(self.stunText)
        self.presenceLabel.setBuddy(self.presenceBox)
        self.vmextenLabel.setBuddy(self.vmextenText)
        self.vadLable.setBuddy(self.vadBox)
        self.framelenLabel.setBuddy(self.framelenBox)
        self.qualityLabel.setBuddy(self.qualityBox)
        self.dtmfmodeLabel.setBuddy(self.dtmfmodeBox)
        self.levelLabel.setBuddy(self.levelBox)
        self.fileLabel.setBuddy(self.fileText)
        self.msgLabel.setBuddy(self.msgBox)
        self.devLabel.setBuddy(self.playbackdevBox)
        self.portLabel.setBuddy(self.portBox)
        self.capturedevLabel.setBuddy(self.capturedevBox)

        self.retranslateUi(configDlg)
        self.cfgTabs.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), configDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(configDlg)

    def retranslateUi(self, configDlg):
        configDlg.setWindowTitle(QtGui.QApplication.translate("configDlg", "Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.userLabel.setText(QtGui.QApplication.translate("configDlg", "Username", None, QtGui.QApplication.UnicodeUTF8))
        self.passLabel.setText(QtGui.QApplication.translate("configDlg", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.domainLabel.setText(QtGui.QApplication.translate("configDlg", "Domain", None, QtGui.QApplication.UnicodeUTF8))
        self.regtimeLabel.setText(QtGui.QApplication.translate("configDlg", "RegistryTimeout", None, QtGui.QApplication.UnicodeUTF8))
        self.stunLabel.setText(QtGui.QApplication.translate("configDlg", "STUN server", None, QtGui.QApplication.UnicodeUTF8))
        self.presenceLabel.setText(QtGui.QApplication.translate("configDlg", "Publish Presence", None, QtGui.QApplication.UnicodeUTF8))
        self.vmextenLabel.setText(QtGui.QApplication.translate("configDlg", "Voicemail Extension", None, QtGui.QApplication.UnicodeUTF8))
        self.cfgTabs.setTabText(self.cfgTabs.indexOf(self.accTab), QtGui.QApplication.translate("configDlg", "Account", None, QtGui.QApplication.UnicodeUTF8))
        self.vadLable.setText(QtGui.QApplication.translate("configDlg", "Enable VAD", None, QtGui.QApplication.UnicodeUTF8))
        self.framelenLabel.setText(QtGui.QApplication.translate("configDlg", "Audio frames length(ms)", None, QtGui.QApplication.UnicodeUTF8))
        self.qualityLabel.setText(QtGui.QApplication.translate("configDlg", "Audio quality", None, QtGui.QApplication.UnicodeUTF8))
        self.dtmfmodeLabel.setText(QtGui.QApplication.translate("configDlg", "DTMF transport", None, QtGui.QApplication.UnicodeUTF8))
        self.dtmfmodeBox.setItemText(0, QtGui.QApplication.translate("configDlg", "RFC2833", None, QtGui.QApplication.UnicodeUTF8))
        self.dtmfmodeBox.setItemText(1, QtGui.QApplication.translate("configDlg", "SIP INFO", None, QtGui.QApplication.UnicodeUTF8))
        self.cfgTabs.setTabText(self.cfgTabs.indexOf(self.mediaTab), QtGui.QApplication.translate("configDlg", "Media", None, QtGui.QApplication.UnicodeUTF8))
        self.enaLabel.setText(QtGui.QApplication.translate("configDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Enabled Codecs</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.rightBtn.setText(QtGui.QApplication.translate("configDlg", "->", None, QtGui.QApplication.UnicodeUTF8))
        self.leftBtn.setText(QtGui.QApplication.translate("configDlg", "<-", None, QtGui.QApplication.UnicodeUTF8))
        self.disLabel.setText(QtGui.QApplication.translate("configDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Disabled Codecs</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.cfgTabs.setTabText(self.cfgTabs.indexOf(self.codecTab), QtGui.QApplication.translate("configDlg", "Codecs", None, QtGui.QApplication.UnicodeUTF8))
        self.levelLabel.setText(QtGui.QApplication.translate("configDlg", "Log level", None, QtGui.QApplication.UnicodeUTF8))
        self.fileLabel.setText(QtGui.QApplication.translate("configDlg", "Log filename", None, QtGui.QApplication.UnicodeUTF8))
        self.msgLabel.setText(QtGui.QApplication.translate("configDlg", "Log SIP messages", None, QtGui.QApplication.UnicodeUTF8))
        self.cfgTabs.setTabText(self.cfgTabs.indexOf(self.logTab), QtGui.QApplication.translate("configDlg", "Log", None, QtGui.QApplication.UnicodeUTF8))
        self.devLabel.setText(QtGui.QApplication.translate("configDlg", "Sound Playback Device", None, QtGui.QApplication.UnicodeUTF8))
        self.portLabel.setText(QtGui.QApplication.translate("configDlg", "SIP port", None, QtGui.QApplication.UnicodeUTF8))
        self.capturedevLabel.setText(QtGui.QApplication.translate("configDlg", "Sound Capture Device", None, QtGui.QApplication.UnicodeUTF8))
        self.testBtn.setText(QtGui.QApplication.translate("configDlg", "Test sound devices", None, QtGui.QApplication.UnicodeUTF8))
        self.transportLabel.setText(QtGui.QApplication.translate("configDlg", "Transport type", None, QtGui.QApplication.UnicodeUTF8))
        self.transportBox.setItemText(0, QtGui.QApplication.translate("configDlg", "UDP", None, QtGui.QApplication.UnicodeUTF8))
        self.transportBox.setItemText(1, QtGui.QApplication.translate("configDlg", "TCP", None, QtGui.QApplication.UnicodeUTF8))
        self.cfgTabs.setTabText(self.cfgTabs.indexOf(self.sysTab), QtGui.QApplication.translate("configDlg", "System", None, QtGui.QApplication.UnicodeUTF8))

import configuration_icons_rc
