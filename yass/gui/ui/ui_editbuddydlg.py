# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editbuddydlg.ui'
#
# Created: Tue Aug  4 17:47:48 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_editbuddyDlg(object):
    def setupUi(self, editbuddyDlg):
        editbuddyDlg.setObjectName("editbuddyDlg")
        editbuddyDlg.resize(375, 135)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(editbuddyDlg.sizePolicy().hasHeightForWidth())
        editbuddyDlg.setSizePolicy(sizePolicy)
        editbuddyDlg.setMaximumSize(QtCore.QSize(375, 135))
        self.verticalLayout = QtGui.QVBoxLayout(editbuddyDlg)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.nameLabel = QtGui.QLabel(editbuddyDlg)
        self.nameLabel.setObjectName("nameLabel")
        self.gridLayout.addWidget(self.nameLabel, 0, 0, 1, 1)
        self.nameText = QtGui.QLineEdit(editbuddyDlg)
        self.nameText.setEnabled(False)
        self.nameText.setObjectName("nameText")
        self.gridLayout.addWidget(self.nameText, 0, 1, 1, 1)
        self.uriLabel = QtGui.QLabel(editbuddyDlg)
        self.uriLabel.setObjectName("uriLabel")
        self.gridLayout.addWidget(self.uriLabel, 1, 0, 1, 1)
        self.uriText = QtGui.QLineEdit(editbuddyDlg)
        self.uriText.setObjectName("uriText")
        self.gridLayout.addWidget(self.uriText, 1, 1, 1, 1)
        self.subsBox = QtGui.QCheckBox(editbuddyDlg)
        self.subsBox.setObjectName("subsBox")
        self.gridLayout.addWidget(self.subsBox, 2, 1, 1, 1)
        self.subsLabel = QtGui.QLabel(editbuddyDlg)
        self.subsLabel.setObjectName("subsLabel")
        self.gridLayout.addWidget(self.subsLabel, 2, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.buttonBox = QtGui.QDialogButtonBox(editbuddyDlg)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(editbuddyDlg)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), editbuddyDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(editbuddyDlg)

    def retranslateUi(self, editbuddyDlg):
        editbuddyDlg.setWindowTitle(QtGui.QApplication.translate("editbuddyDlg", "Edit Buddy", None, QtGui.QApplication.UnicodeUTF8))
        self.nameLabel.setText(QtGui.QApplication.translate("editbuddyDlg", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.uriLabel.setText(QtGui.QApplication.translate("editbuddyDlg", "URI", None, QtGui.QApplication.UnicodeUTF8))
        self.subsLabel.setText(QtGui.QApplication.translate("editbuddyDlg", "Subscribed", None, QtGui.QApplication.UnicodeUTF8))

