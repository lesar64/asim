# Importing tkinter to make gui in python
from tkinter import *

# Importing tkPDFViewer to place pdf file in gui.
# In tkPDFViewer library there is
# an tkPDFViewer module. That I have imported as pdf
from tkPDFViewer import tkPDFViewer as pdf

# Initializing tk
root = Tk()

# Set the width and height of our root window.
root.geometry("550x750")

# creating object of ShowPdf from tkPDFViewer.
v1 = pdf.ShowPdf()

# Adding pdf location and width and height.
path = r"..\DATA\Exposé_GPT-3.pdf"

v2 = v1.pdf_view(root,
                 pdf_location=path,
                 width=100, height=120)

# Placing Pdf in my gui.
v2.pack()
root.mainloop()