# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xferdlg.ui'
#
# Created: Fri Aug 15 19:49:09 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_xferDlg(object):
    def setupUi(self, xferDlg):
        xferDlg.setObjectName("xferDlg")
        xferDlg.resize(545,210)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(xferDlg.sizePolicy().hasHeightForWidth())
        xferDlg.setSizePolicy(sizePolicy)
        xferDlg.setMaximumSize(QtCore.QSize(545,210))
        self.verticalLayout_2 = QtGui.QVBoxLayout(xferDlg)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.xferBox = QtGui.QGroupBox(xferDlg)
        self.xferBox.setObjectName("xferBox")
        self.verticalLayout = QtGui.QVBoxLayout(self.xferBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.blindRad = QtGui.QRadioButton(self.xferBox)
        self.blindRad.setChecked(True)
        self.blindRad.setObjectName("blindRad")
        self.verticalLayout.addWidget(self.blindRad)
        self.atRad = QtGui.QRadioButton(self.xferBox)
        self.atRad.setCheckable(False)
        self.atRad.setObjectName("atRad")
        self.verticalLayout.addWidget(self.atRad)
        self.verticalLayout_2.addWidget(self.xferBox)
        self.dstW = QtGui.QWidget(xferDlg)
        self.dstW.setObjectName("dstW")
        self.horizontalLayout = QtGui.QHBoxLayout(self.dstW)
        self.horizontalLayout.setContentsMargins(0,-1,0,-1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dstLabel = QtGui.QLabel(self.dstW)
        self.dstLabel.setObjectName("dstLabel")
        self.horizontalLayout.addWidget(self.dstLabel)
        self.dstText = QtGui.QLineEdit(self.dstW)
        self.dstText.setObjectName("dstText")
        self.horizontalLayout.addWidget(self.dstText)
        self.verticalLayout_2.addWidget(self.dstW)
        self.buttonW = QtGui.QWidget(xferDlg)
        self.buttonW.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.buttonW.setObjectName("buttonW")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.buttonW)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cancelBtn = QtGui.QPushButton(self.buttonW)
        self.cancelBtn.setObjectName("cancelBtn")
        self.horizontalLayout_2.addWidget(self.cancelBtn)
        self.xferBtn = QtGui.QPushButton(self.buttonW)
        self.xferBtn.setObjectName("xferBtn")
        self.horizontalLayout_2.addWidget(self.xferBtn)
        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.buttonW)

        self.retranslateUi(xferDlg)
        QtCore.QObject.connect(self.cancelBtn,QtCore.SIGNAL("clicked()"),xferDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(xferDlg)

    def retranslateUi(self, xferDlg):
        xferDlg.setWindowTitle(QtGui.QApplication.translate("xferDlg", "Call Transfer", None, QtGui.QApplication.UnicodeUTF8))
        self.xferBox.setTitle(QtGui.QApplication.translate("xferDlg", "Transfer Type", None, QtGui.QApplication.UnicodeUTF8))
        self.blindRad.setText(QtGui.QApplication.translate("xferDlg", "Blind transfer", None, QtGui.QApplication.UnicodeUTF8))
        self.atRad.setText(QtGui.QApplication.translate("xferDlg", "Attended transfer", None, QtGui.QApplication.UnicodeUTF8))
        self.dstLabel.setText(QtGui.QApplication.translate("xferDlg", "Destination", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelBtn.setText(QtGui.QApplication.translate("xferDlg", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.xferBtn.setText(QtGui.QApplication.translate("xferDlg", "Transfer", None, QtGui.QApplication.UnicodeUTF8))

