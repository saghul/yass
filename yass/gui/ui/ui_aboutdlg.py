# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutdlg.ui'
#
# Created: Tue Aug 19 20:36:32 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_aboutDlg(object):
    def setupUi(self, aboutDlg):
        aboutDlg.setObjectName("aboutDlg")
        aboutDlg.resize(330,185)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(aboutDlg.sizePolicy().hasHeightForWidth())
        aboutDlg.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(aboutDlg)
        self.verticalLayout.setObjectName("verticalLayout")
        self.aboutLabel = QtGui.QLabel(aboutDlg)
        self.aboutLabel.setObjectName("aboutLabel")
        self.verticalLayout.addWidget(self.aboutLabel)
        self.okBtn = QtGui.QDialogButtonBox(aboutDlg)
        self.okBtn.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.okBtn.setCenterButtons(True)
        self.okBtn.setObjectName("okBtn")
        self.verticalLayout.addWidget(self.okBtn)

        self.retranslateUi(aboutDlg)
        QtCore.QObject.connect(self.okBtn,QtCore.SIGNAL("clicked(QAbstractButton*)"),aboutDlg.accept)
        QtCore.QMetaObject.connectSlotsByName(aboutDlg)

    def retranslateUi(self, aboutDlg):
        aboutDlg.setWindowTitle(QtGui.QApplication.translate("aboutDlg", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.aboutLabel.setText(QtGui.QApplication.translate("aboutDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; text-decoration: underline;\">YASS - Yet Another SIP Softphone</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; text-decoration: underline;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">YASS is Yet Another SIP Softphone based on </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">PJSIP libraries (http://www.pjsip.org)</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Big thanks to 01g4 for her paticence over long </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">nights of development.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

