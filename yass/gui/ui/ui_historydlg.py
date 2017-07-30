# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'historydlg.ui'
#
# Created: Tue Aug 19 18:40:54 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_historyDlg(object):
    def setupUi(self, historyDlg):
        historyDlg.setObjectName("historyDlg")
        historyDlg.resize(500,420)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(historyDlg.sizePolicy().hasHeightForWidth())
        historyDlg.setSizePolicy(sizePolicy)
        historyDlg.setMaximumSize(QtCore.QSize(500,420))
        self.verticalLayout = QtGui.QVBoxLayout(historyDlg)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabGrid = QtGui.QTableWidget(historyDlg)
        self.tabGrid.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tabGrid.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tabGrid.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tabGrid.setProperty("showDropIndicator",QtCore.QVariant(False))
        self.tabGrid.setDragDropOverwriteMode(False)
        self.tabGrid.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tabGrid.setSortingEnabled(False)
        self.tabGrid.setWordWrap(True)
        self.tabGrid.setCornerButtonEnabled(False)
        self.tabGrid.setObjectName("tabGrid")
        self.verticalLayout.addWidget(self.tabGrid)
        self.btnBox = QtGui.QDialogButtonBox(historyDlg)
        self.btnBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Reset)
        self.btnBox.setCenterButtons(True)
        self.btnBox.setObjectName("btnBox")
        self.verticalLayout.addWidget(self.btnBox)

        self.retranslateUi(historyDlg)
        QtCore.QObject.connect(self.btnBox,QtCore.SIGNAL("rejected()"),historyDlg.close)
        QtCore.QMetaObject.connectSlotsByName(historyDlg)

    def retranslateUi(self, historyDlg):
        historyDlg.setWindowTitle(QtGui.QApplication.translate("historyDlg", "Call History", None, QtGui.QApplication.UnicodeUTF8))
        self.tabGrid.setRowCount(0)
        self.tabGrid.setColumnCount(3)
        self.tabGrid.clear()
        self.tabGrid.setColumnCount(3)
        self.tabGrid.setRowCount(0)
        headerItem = QtGui.QTableWidgetItem()
        headerItem.setText(QtGui.QApplication.translate("historyDlg", "Number", None, QtGui.QApplication.UnicodeUTF8))
        self.tabGrid.setHorizontalHeaderItem(0,headerItem)
        headerItem1 = QtGui.QTableWidgetItem()
        headerItem1.setText(QtGui.QApplication.translate("historyDlg", "Call Type", None, QtGui.QApplication.UnicodeUTF8))
        self.tabGrid.setHorizontalHeaderItem(1,headerItem1)
        headerItem2 = QtGui.QTableWidgetItem()
        headerItem2.setText(QtGui.QApplication.translate("historyDlg", "Date", None, QtGui.QApplication.UnicodeUTF8))
        self.tabGrid.setHorizontalHeaderItem(2,headerItem2)

