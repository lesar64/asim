from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QFileDialog, QWidget
from pathlib import Path
sys.path.append("..")
from API.tasks import summarize, ask_question, classify_topic, create_quote
from pdfminer_approach import convert_pdf_to_string


class Ui_Dialog(QWidget):
    def __init__(self):
        super().__init__()

    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.resize(1160, 871)
        self.TextOutput = QtWidgets.QTextBrowser(Dialog)
        self.TextOutput.setGeometry(QtCore.QRect(590, 200, 550, 650))
        self.TextOutput.setObjectName("TextOutput")

        self.TextInput = QtWidgets.QTextEdit(Dialog, acceptRichText=False)
        self.TextInput.setGeometry(QtCore.QRect(20, 30, 550, 741))
        self.TextInput.setObjectName("TextInput")
        self.TextInput.setTextColor(QtGui.QColor('#000000'))

        self.Question_Input = QtWidgets.QTextEdit(Dialog)
        self.Question_Input.setGeometry(QtCore.QRect(20, 810, 550, 41))
        self.Question_Input.setObjectName("Question_Input")

        def update_output(function_type):
            Input_text = self.TextInput.toPlainText()

            if function_type == 'summarize':
                result = summarize(Input_text)
            elif function_type == 'create_quote':
                result = create_quote(Input_text)
            elif function_type == 'classify_topic':
                result = classify_topic(Input_text)
            elif function_type == 'ask_question':
                Question_text = self.Question_Input.toPlainText()
                result = ask_question(Input_text, Question_text)

            self.TextOutput.setText(result)

            return

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 8, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(590, 170, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 780, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")

        # Question
        self.ButtonQuestion = QtWidgets.QPushButton(Dialog)
        self.ButtonQuestion.setGeometry(QtCore.QRect(590, 100, 270, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ButtonQuestion.setFont(font)
        self.ButtonQuestion.setObjectName("ButtonQuestion")
        self.ButtonQuestion.clicked.connect(lambda: update_output('ask_question'))

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

        # File import
        self.ButtonOpenFile = QtWidgets.QPushButton(Dialog)
        self.ButtonOpenFile.setGeometry(QtCore.QRect(100, 10, 135, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.ButtonOpenFile.setFont(font)
        self.ButtonOpenFile.setObjectName("ButtonOpenFile")
        self.ButtonOpenFile.clicked.connect(self.showDialog)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def showDialog(self):

        home_dir = str(Path.home())
        filepath = QFileDialog.getOpenFileName(self, 'Open file', home_dir)

        print(filepath[0])
        fileText = convert_pdf_to_string(filepath[0])
        self.TextInput.setText(fileText)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "GPT-3 supported paper reading"))
        self.label.setText(_translate("Dialog", "Input"))
        self.label_2.setText(_translate("Dialog", "Output"))
        self.label_3.setText(_translate("Dialog", "Question"))
        self.ButtonQuestion.setText(_translate("Dialog", "Question"))
        self.ButtonQuote.setText(_translate("Dialog", "Quote"))
        self.ButtonSummary.setText(_translate("Dialog", "Summary"))
        self.ButtonTopic.setText(_translate("Dialog", "Topic"))
        self.ButtonOpenFile.setText(_translate("Dialog", "Import file"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
