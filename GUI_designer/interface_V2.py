# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interface_v2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path.append("..")
from API.tasks import summarize, ask_question, classify_topic, create_quote




class Ui_Dialog(object):
    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.resize(1160, 871)
        self.TextOutput = QtWidgets.QTextBrowser(Dialog)
        self.TextOutput.setGeometry(QtCore.QRect(590, 200, 550, 650))
        self.TextOutput.setObjectName("TextOutput")


        self.TextInput = QtWidgets.QTextEdit(Dialog)
        self.TextInput.setGeometry(QtCore.QRect(20, 30, 550, 820))
        self.TextInput.setObjectName("TextInput")

        def update_output(function_type):
            Input_text = self.TextInput.toPlainText()

            if function_type == 'summarize':
                result = summarize(Input_text)
            elif function_type == 'create_quote':
                result = create_quote(Input_text)
            elif function_type == 'classify_topic':
                result = classify_topic(Input_text)

            self.TextOutput.setText(result)

            return


        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 8, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")


        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(590, 170, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")

        # Question
        self.ButtonQuestion = QtWidgets.QPushButton(Dialog)
        self.ButtonQuestion.setGeometry(QtCore.QRect(590, 100, 270, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ButtonQuestion.setFont(font)
        self.ButtonQuestion.setObjectName("ButtonQuestion")
        question=input()
        # self.ButtonQuestion.clicked.connect(ask_question(input_phrase, question))
        self.ButtonQuestion.clicked.connect(lambda: print(self.TextInput.toPlainText()))

        # Quote
        self.ButtonQuote = QtWidgets.QPushButton(Dialog)
        self.ButtonQuote.setGeometry(QtCore.QRect(870, 100, 270, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ButtonQuote.setFont(font)
        self.ButtonQuote.setObjectName("ButtonQuote")
        self.ButtonQuote.clicked.connect(lambda: update_output('create_quote'))

        # Summary
        self.ButtonSummary = QtWidgets.QPushButton(Dialog)
        self.ButtonSummary.setGeometry(QtCore.QRect(590, 30, 270, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ButtonSummary.setFont(font)
        self.ButtonSummary.setObjectName("ButtonSummary")
        self.ButtonSummary.clicked.connect(lambda: update_output("summarize"))


        # Topic
        self.ButtonTopic = QtWidgets.QPushButton(Dialog)
        self.ButtonTopic.setGeometry(QtCore.QRect(870, 30, 270, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ButtonTopic.setFont(font)
        self.ButtonTopic.setObjectName("ButtonTopic")
        self.ButtonTopic.clicked.connect(lambda: update_output('classify_topic'))


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Input"))
        self.label_2.setText(_translate("Dialog", "Output"))
        self.ButtonQuestion.setText(_translate("Dialog", "Question"))
        self.ButtonQuote.setText(_translate("Dialog", "Quote"))
        self.ButtonSummary.setText(_translate("Dialog", "Summary"))
        self.ButtonTopic.setText(_translate("Dialog", "Topic"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())