# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Thu Aug 27 00:04:01 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_YassMainWindow(object):
    def setupUi(self, YassMainWindow):
        YassMainWindow.setObjectName("YassMainWindow")
        YassMainWindow.resize(700, 550)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        YassMainWindow.setFont(font)
        self.centralFrame = QtGui.QWidget(YassMainWindow)
        self.centralFrame.setObjectName("centralFrame")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralFrame)
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.buddyList = QtGui.QTreeWidget(self.centralFrame)
        self.buddyList.setEnabled(True)
        self.buddyList.setMinimumSize(QtCore.QSize(200, 0))
        self.buddyList.setMaximumSize(QtCore.QSize(200, 16777215))
        self.buddyList.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.buddyList.setObjectName("buddyList")
        self.horizontalLayout_2.addWidget(self.buddyList)
        self.linesFrame = QtGui.QWidget(self.centralFrame)
        self.linesFrame.setObjectName("linesFrame")
        self.verticalLayout = QtGui.QVBoxLayout(self.linesFrame)
        self.verticalLayout.setContentsMargins(-1, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dialFrame = QtGui.QWidget(self.linesFrame)
        self.dialFrame.setObjectName("dialFrame")
        self.gridLayout = QtGui.QGridLayout(self.dialFrame)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName("gridLayout")
        self.dialBtn = QtGui.QPushButton(self.dialFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dialBtn.sizePolicy().hasHeightForWidth())
        self.dialBtn.setSizePolicy(sizePolicy)
        self.dialBtn.setObjectName("dialBtn")
        self.gridLayout.addWidget(self.dialBtn, 0, 1, 1, 1)
        self.dialText = QtGui.QComboBox(self.dialFrame)
        self.dialText.setEditable(True)
        self.dialText.setMaxVisibleItems(5)
        self.dialText.setMaxCount(15)
        self.dialText.setInsertPolicy(QtGui.QComboBox.InsertBeforeCurrent)
        self.dialText.setDuplicatesEnabled(True)
        self.dialText.setFrame(True)
        self.dialText.setObjectName("dialText")
        self.gridLayout.addWidget(self.dialText, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.dialFrame)
        self.linesTabs = QtGui.QTabWidget(self.linesFrame)
        self.linesTabs.setTabShape(QtGui.QTabWidget.Rounded)
        self.linesTabs.setObjectName("linesTabs")
        self.lineTab1 = QtGui.QWidget()
        self.lineTab1.setObjectName("lineTab1")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.lineTab1)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.line1Text = QtGui.QTextEdit(self.lineTab1)
        self.line1Text.setUndoRedoEnabled(False)
        self.line1Text.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.line1Text.setReadOnly(True)
        self.line1Text.setObjectName("line1Text")
        self.verticalLayout_2.addWidget(self.line1Text)
        self.linesTabs.addTab(self.lineTab1, "")
        self.verticalLayout.addWidget(self.linesTabs)
        self.horizontalLayout_2.addWidget(self.linesFrame)
        YassMainWindow.setCentralWidget(self.centralFrame)
        self.menubar = QtGui.QMenuBar(YassMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        YassMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(YassMainWindow)
        self.statusbar.setObjectName("statusbar")
        YassMainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(YassMainWindow)
        self.toolBar.setMinimumSize(QtCore.QSize(0, 0))
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QtCore.QSize(32, 32))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setFloatable(False)
        self.toolBar.setObjectName("toolBar")
        YassMainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionQuit = QtGui.QAction(YassMainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout = QtGui.QAction(YassMainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAnswer = QtGui.QAction(YassMainWindow)
        self.actionAnswer.setEnabled(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/toolbar/icons/toolbar/answer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAnswer.setIcon(icon)
        self.actionAnswer.setObjectName("actionAnswer")
        self.actionHangup = QtGui.QAction(YassMainWindow)
        self.actionHangup.setEnabled(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/toolbar/icons/toolbar/hangup.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHangup.setIcon(icon1)
        self.actionHangup.setObjectName("actionHangup")
        self.actionReject = QtGui.QAction(YassMainWindow)
        self.actionReject.setEnabled(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/toolbar/icons/toolbar/reject.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReject.setIcon(icon2)
        self.actionReject.setObjectName("actionReject")
        self.actionXfer = QtGui.QAction(YassMainWindow)
        self.actionXfer.setEnabled(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/toolbar/icons/toolbar/xfer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionXfer.setIcon(icon3)
        self.actionXfer.setObjectName("actionXfer")
        self.actionHold = QtGui.QAction(YassMainWindow)
        self.actionHold.setCheckable(True)
        self.actionHold.setChecked(False)
        self.actionHold.setEnabled(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/toolbar/icons/toolbar/hold.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHold.setIcon(icon4)
        self.actionHold.setObjectName("actionHold")
        self.actionDtmf = QtGui.QAction(YassMainWindow)
        self.actionDtmf.setEnabled(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/toolbar/icons/toolbar/dtmf.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDtmf.setIcon(icon5)
        self.actionDtmf.setObjectName("actionDtmf")
        self.actionHistory = QtGui.QAction(YassMainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/toolbar/icons/toolbar/history.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHistory.setIcon(icon6)
        self.actionHistory.setObjectName("actionHistory")
        self.actionVoicemail = QtGui.QAction(YassMainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/toolbar/icons/toolbar/voicemail.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionVoicemail.setIcon(icon7)
        self.actionVoicemail.setObjectName("actionVoicemail")
        self.actionConfiguration = QtGui.QAction(YassMainWindow)
        self.actionConfiguration.setObjectName("actionConfiguration")
        self.actionCall = QtGui.QAction(YassMainWindow)
        self.actionCall.setObjectName("actionCall")
        self.actionMessage = QtGui.QAction(YassMainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/toolbar/icons/toolbar/message.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMessage.setIcon(icon8)
        self.actionMessage.setObjectName("actionMessage")
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuEdit.addAction(self.actionConfiguration)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionHangup)
        self.toolBar.addAction(self.actionAnswer)
        self.toolBar.addAction(self.actionReject)
        self.toolBar.addAction(self.actionXfer)
        self.toolBar.addAction(self.actionHold)
        self.toolBar.addAction(self.actionDtmf)
        self.toolBar.addAction(self.actionHistory)
        self.toolBar.addAction(self.actionVoicemail)
        self.toolBar.addAction(self.actionMessage)

        self.retranslateUi(YassMainWindow)
        self.linesTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(YassMainWindow)

    def retranslateUi(self, YassMainWindow):
        YassMainWindow.setWindowTitle(QtGui.QApplication.translate("YassMainWindow", "YASS", None, QtGui.QApplication.UnicodeUTF8))
        self.buddyList.headerItem().setText(0, QtGui.QApplication.translate("YassMainWindow", "Friends", None, QtGui.QApplication.UnicodeUTF8))
        self.dialBtn.setText(QtGui.QApplication.translate("YassMainWindow", "Dial", None, QtGui.QApplication.UnicodeUTF8))
        self.linesTabs.setTabText(self.linesTabs.indexOf(self.lineTab1), QtGui.QApplication.translate("YassMainWindow", "Line 1", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("YassMainWindow", "YASS", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("YassMainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("YassMainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("YassMainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("YassMainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("YassMainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAnswer.setText(QtGui.QApplication.translate("YassMainWindow", "answer", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHangup.setText(QtGui.QApplication.translate("YassMainWindow", "hangup", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReject.setText(QtGui.QApplication.translate("YassMainWindow", "reject", None, QtGui.QApplication.UnicodeUTF8))
        self.actionXfer.setText(QtGui.QApplication.translate("YassMainWindow", "xfer", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHold.setText(QtGui.QApplication.translate("YassMainWindow", "hold", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDtmf.setText(QtGui.QApplication.translate("YassMainWindow", "dtmf", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHistory.setText(QtGui.QApplication.translate("YassMainWindow", "history", None, QtGui.QApplication.UnicodeUTF8))
        self.actionVoicemail.setText(QtGui.QApplication.translate("YassMainWindow", "voicemail", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConfiguration.setText(QtGui.QApplication.translate("YassMainWindow", "Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCall.setText(QtGui.QApplication.translate("YassMainWindow", "call", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMessage.setText(QtGui.QApplication.translate("YassMainWindow", "message", None, QtGui.QApplication.UnicodeUTF8))

import toolbar_icons_rc
