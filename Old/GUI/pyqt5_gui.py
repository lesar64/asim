# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Interface_V2ClxVrA.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1160, 871)
        self.TextOutput = QTextBrowser(Dialog)
        self.TextOutput.setObjectName(u"TextOutput")
        self.TextOutput.setGeometry(QRect(590, 200, 550, 650))
        self.TextInput = QTextEdit(Dialog)
        self.TextInput.setObjectName(u"TextInput")
        self.TextInput.setGeometry(QRect(20, 30, 550, 820))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 8, 61, 21))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(590, 170, 81, 31))
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.ButtonQuestion = QPushButton(Dialog)
        self.ButtonQuestion.setObjectName(u"ButtonQuestion")
        self.ButtonQuestion.setGeometry(QRect(590, 100, 270, 60))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setWeight(50)
        self.ButtonQuestion.setFont(font1)
        self.ButtonQuote = QPushButton(Dialog)
        self.ButtonQuote.setObjectName(u"ButtonQuote")
        self.ButtonQuote.setGeometry(QRect(870, 100, 270, 60))
        self.ButtonQuote.setFont(font1)
        self.ButtonSummary = QPushButton(Dialog)
        self.ButtonSummary.setObjectName(u"ButtonSummary")
        self.ButtonSummary.setGeometry(QRect(590, 30, 270, 60))
        self.ButtonSummary.setFont(font1)
        self.ButtonTopic = QPushButton(Dialog)
        self.ButtonTopic.setObjectName(u"ButtonTopic")
        self.ButtonTopic.setGeometry(QRect(870, 30, 270, 60))
        self.ButtonTopic.setFont(font1)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Input", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Output", None))
        self.ButtonQuestion.setText(QCoreApplication.translate("Dialog", u"Question", None))
        self.ButtonQuote.setText(QCoreApplication.translate("Dialog", u"Quote", None))
        self.ButtonSummary.setText(QCoreApplication.translate("Dialog", u"Summary", None))
        self.ButtonTopic.setText(QCoreApplication.translate("Dialog", u"Topic", None))
    # retranslateUi

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ui_Dialog()
    sys.exit(Ui_Dialog.exec_())