# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dtmfdlg.ui'
#
# Created: Fri Aug 15 11:35:03 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_dtmfDlg(object):
    def setupUi(self, dtmfDlg):
        dtmfDlg.setObjectName("dtmfDlg")
        dtmfDlg.resize(265,210)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dtmfDlg.sizePolicy().hasHeightForWidth())
        dtmfDlg.setSizePolicy(sizePolicy)
        dtmfDlg.setMaximumSize(QtCore.QSize(265,210))
        dtmfDlg.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.gridLayout = QtGui.QGridLayout(dtmfDlg)
        self.gridLayout.setObjectName("gridLayout")
        self.oneBtn = QtGui.QPushButton(dtmfDlg)
        self.oneBtn.setObjectName("oneBtn")
        self.gridLayout.addWidget(self.oneBtn,0,0,1,1)
        self.twoBtn = QtGui.QPushButton(dtmfDlg)
        self.twoBtn.setObjectName("twoBtn")
        self.gridLayout.addWidget(self.twoBtn,0,1,1,1)
        self.threeBtn = QtGui.QPushButton(dtmfDlg)
        self.threeBtn.setObjectName("threeBtn")
        self.gridLayout.addWidget(self.threeBtn,0,2,1,1)
        self.fourBtn = QtGui.QPushButton(dtmfDlg)
        self.fourBtn.setObjectName("fourBtn")
        self.gridLayout.addWidget(self.fourBtn,1,0,1,1)
        self.fiveBtn = QtGui.QPushButton(dtmfDlg)
        self.fiveBtn.setObjectName("fiveBtn")
        self.gridLayout.addWidget(self.fiveBtn,1,1,1,1)
        self.sixBtn = QtGui.QPushButton(dtmfDlg)
        self.sixBtn.setObjectName("sixBtn")
        self.gridLayout.addWidget(self.sixBtn,1,2,1,1)
        self.sevenBtn = QtGui.QPushButton(dtmfDlg)
        self.sevenBtn.setObjectName("sevenBtn")
        self.gridLayout.addWidget(self.sevenBtn,2,0,1,1)
        self.eightBtn = QtGui.QPushButton(dtmfDlg)
        self.eightBtn.setObjectName("eightBtn")
        self.gridLayout.addWidget(self.eightBtn,2,1,1,1)
        self.nineBtn = QtGui.QPushButton(dtmfDlg)
        self.nineBtn.setObjectName("nineBtn")
        self.gridLayout.addWidget(self.nineBtn,2,2,1,1)
        self.astBtn = QtGui.QPushButton(dtmfDlg)
        self.astBtn.setObjectName("astBtn")
        self.gridLayout.addWidget(self.astBtn,3,0,1,1)
        self.zeroBtn = QtGui.QPushButton(dtmfDlg)
        self.zeroBtn.setObjectName("zeroBtn")
        self.gridLayout.addWidget(self.zeroBtn,3,1,1,1)
        self.poundBtn = QtGui.QPushButton(dtmfDlg)
        self.poundBtn.setObjectName("poundBtn")
        self.gridLayout.addWidget(self.poundBtn,3,2,1,1)

        self.retranslateUi(dtmfDlg)
        QtCore.QMetaObject.connectSlotsByName(dtmfDlg)

    def retranslateUi(self, dtmfDlg):
        dtmfDlg.setWindowTitle(QtGui.QApplication.translate("dtmfDlg", "DTMF", None, QtGui.QApplication.UnicodeUTF8))
        self.oneBtn.setText(QtGui.QApplication.translate("dtmfDlg", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.twoBtn.setText(QtGui.QApplication.translate("dtmfDlg", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.threeBtn.setText(QtGui.QApplication.translate("dtmfDlg", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.fourBtn.setText(QtGui.QApplication.translate("dtmfDlg", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.fiveBtn.setText(QtGui.QApplication.translate("dtmfDlg", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.sixBtn.setText(QtGui.QApplication.translate("dtmfDlg", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.sevenBtn.setText(QtGui.QApplication.translate("dtmfDlg", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.eightBtn.setText(QtGui.QApplication.translate("dtmfDlg", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.nineBtn.setText(QtGui.QApplication.translate("dtmfDlg", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.astBtn.setText(QtGui.QApplication.translate("dtmfDlg", "*", None, QtGui.QApplication.UnicodeUTF8))
        self.zeroBtn.setText(QtGui.QApplication.translate("dtmfDlg", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.poundBtn.setText(QtGui.QApplication.translate("dtmfDlg", "#", None, QtGui.QApplication.UnicodeUTF8))

