# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imdlg.ui'
#
# Created: Wed Aug 26 21:43:35 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_imDlg(object):
    def setupUi(self, imDlg):
        imDlg.setObjectName("imDlg")
        imDlg.resize(468, 338)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(imDlg.sizePolicy().hasHeightForWidth())
        imDlg.setSizePolicy(sizePolicy)
        imDlg.setMaximumSize(QtCore.QSize(468, 338))
        self.gridLayoutWidget = QtGui.QWidget(imDlg)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 451, 231))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.uriLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.uriLabel.setObjectName("uriLabel")
        self.gridLayout.addWidget(self.uriLabel, 0, 1, 1, 1)
        self.uriText = QtGui.QLineEdit(self.gridLayoutWidget)
        self.uriText.setObjectName("uriText")
        self.gridLayout.addWidget(self.uriText, 0, 2, 1, 1)
        self.msgText = QtGui.QPlainTextEdit(self.gridLayoutWidget)
        self.msgText.setReadOnly(True)
        self.msgText.setObjectName("msgText")
        self.gridLayout.addWidget(self.msgText, 1, 1, 1, 2)
        self.gridLayoutWidget_2 = QtGui.QWidget(imDlg)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 249, 451, 81))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.msgsendText = QtGui.QPlainTextEdit(self.gridLayoutWidget_2)
        self.msgsendText.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.msgsendText.setTabChangesFocus(True)
        self.msgsendText.setObjectName("msgsendText")
        self.gridLayout_2.addWidget(self.msgsendText, 0, 0, 1, 1)
        self.sendBtn = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.sendBtn.setObjectName("sendBtn")
        self.gridLayout_2.addWidget(self.sendBtn, 0, 1, 1, 1)

        self.retranslateUi(imDlg)
        QtCore.QMetaObject.connectSlotsByName(imDlg)

    def retranslateUi(self, imDlg):
        imDlg.setWindowTitle(QtGui.QApplication.translate("imDlg", "Instant Messaging", None, QtGui.QApplication.UnicodeUTF8))
        self.uriLabel.setText(QtGui.QApplication.translate("imDlg", "URI", None, QtGui.QApplication.UnicodeUTF8))
        self.sendBtn.setText(QtGui.QApplication.translate("imDlg", "Send", None, QtGui.QApplication.UnicodeUTF8))

