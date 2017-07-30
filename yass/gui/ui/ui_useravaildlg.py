# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'useravaildlg.ui'
#
# Created: Sun Aug  9 23:54:47 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_useravailDlg(object):
    def setupUi(self, useravailDlg):
        useravailDlg.setObjectName("useravailDlg")
        useravailDlg.resize(330, 210)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(useravailDlg.sizePolicy().hasHeightForWidth())
        useravailDlg.setSizePolicy(sizePolicy)
        useravailDlg.setMaximumSize(QtCore.QSize(330, 210))
        self.verticalLayout_2 = QtGui.QVBoxLayout(useravailDlg)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.availBox = QtGui.QGroupBox(useravailDlg)
        self.availBox.setObjectName("availBox")
        self.verticalLayout = QtGui.QVBoxLayout(self.availBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.onRad = QtGui.QRadioButton(self.availBox)
        self.onRad.setChecked(True)
        self.onRad.setObjectName("onRad")
        self.verticalLayout.addWidget(self.onRad)
        self.offRad = QtGui.QRadioButton(self.availBox)
        self.offRad.setCheckable(True)
        self.offRad.setObjectName("offRad")
        self.verticalLayout.addWidget(self.offRad)
        self.verticalLayout_2.addWidget(self.availBox)
        self.descrW = QtGui.QWidget(useravailDlg)
        self.descrW.setObjectName("descrW")
        self.horizontalLayout = QtGui.QHBoxLayout(self.descrW)
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.descrLabel = QtGui.QLabel(self.descrW)
        self.descrLabel.setObjectName("descrLabel")
        self.horizontalLayout.addWidget(self.descrLabel)
        self.descrText = QtGui.QLineEdit(self.descrW)
        self.descrText.setObjectName("descrText")
        self.horizontalLayout.addWidget(self.descrText)
        self.verticalLayout_2.addWidget(self.descrW)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(useravailDlg)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Apply|QtGui.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(useravailDlg)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), useravailDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(useravailDlg)

    def retranslateUi(self, useravailDlg):
        useravailDlg.setWindowTitle(QtGui.QApplication.translate("useravailDlg", "Change User Availability", None, QtGui.QApplication.UnicodeUTF8))
        self.availBox.setTitle(QtGui.QApplication.translate("useravailDlg", "Availability", None, QtGui.QApplication.UnicodeUTF8))
        self.onRad.setText(QtGui.QApplication.translate("useravailDlg", "Online", None, QtGui.QApplication.UnicodeUTF8))
        self.offRad.setText(QtGui.QApplication.translate("useravailDlg", "Offline", None, QtGui.QApplication.UnicodeUTF8))
        self.descrLabel.setText(QtGui.QApplication.translate("useravailDlg", "Description", None, QtGui.QApplication.UnicodeUTF8))

