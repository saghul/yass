# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addbuddydlg.ui'
#
# Created: Sat Aug 23 11:20:05 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_addbuddyDlg(object):
    def setupUi(self, addbuddyDlg):
        addbuddyDlg.setObjectName("addbuddyDlg")
        addbuddyDlg.resize(375,135)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(addbuddyDlg.sizePolicy().hasHeightForWidth())
        addbuddyDlg.setSizePolicy(sizePolicy)
        addbuddyDlg.setMaximumSize(QtCore.QSize(375,135))
        self.verticalLayout = QtGui.QVBoxLayout(addbuddyDlg)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.nameLabel = QtGui.QLabel(addbuddyDlg)
        self.nameLabel.setObjectName("nameLabel")
        self.gridLayout.addWidget(self.nameLabel,0,0,1,1)
        self.nameText = QtGui.QLineEdit(addbuddyDlg)
        self.nameText.setObjectName("nameText")
        self.gridLayout.addWidget(self.nameText,0,1,1,1)
        self.uriLabel = QtGui.QLabel(addbuddyDlg)
        self.uriLabel.setObjectName("uriLabel")
        self.gridLayout.addWidget(self.uriLabel,1,0,1,1)
        self.uriText = QtGui.QLineEdit(addbuddyDlg)
        self.uriText.setObjectName("uriText")
        self.gridLayout.addWidget(self.uriText,1,1,1,1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.addBtn = QtGui.QPushButton(addbuddyDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addBtn.sizePolicy().hasHeightForWidth())
        self.addBtn.setSizePolicy(sizePolicy)
        self.addBtn.setMaximumSize(QtCore.QSize(100,28))
        self.addBtn.setObjectName("addBtn")
        self.horizontalLayout.addWidget(self.addBtn)
        self.cancelBtn = QtGui.QPushButton(addbuddyDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancelBtn.sizePolicy().hasHeightForWidth())
        self.cancelBtn.setSizePolicy(sizePolicy)
        self.cancelBtn.setMaximumSize(QtCore.QSize(100,28))
        self.cancelBtn.setObjectName("cancelBtn")
        self.horizontalLayout.addWidget(self.cancelBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(addbuddyDlg)
        QtCore.QObject.connect(self.cancelBtn,QtCore.SIGNAL("clicked()"),addbuddyDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(addbuddyDlg)

    def retranslateUi(self, addbuddyDlg):
        addbuddyDlg.setWindowTitle(QtGui.QApplication.translate("addbuddyDlg", "Add Buddy", None, QtGui.QApplication.UnicodeUTF8))
        self.nameLabel.setText(QtGui.QApplication.translate("addbuddyDlg", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.uriLabel.setText(QtGui.QApplication.translate("addbuddyDlg", "URI", None, QtGui.QApplication.UnicodeUTF8))
        self.addBtn.setText(QtGui.QApplication.translate("addbuddyDlg", "Add Buddy", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelBtn.setText(QtGui.QApplication.translate("addbuddyDlg", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

