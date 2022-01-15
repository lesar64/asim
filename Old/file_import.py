import qpageview

from PyQt5.Qt import *


a = QApplication([])

v = qpageview.View()
v.show()
v.loadPdf(r"C:\Users\Christian\Documents\git\asim\DATA\Exposé_GPT-3.pdf")
