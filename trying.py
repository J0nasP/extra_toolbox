import tkinter 
from tkinter import *
from tkinter import filedialog
import PyPDF2
from PyPDF2 import PdfFileReader
from DragDrop import *

class PDF_Doc():

    def __init__(self, filename):
        self.filename = filename
        self.display = filename.split('/')[-1]
        self.pdf = load_pdf(filename)
        self.pages = self.pdf.getNumPages()
        self.start = 1
        self.end = self.pages

    def add_to_writer(pdf, writer, start, end):
    for i in range(start-1, end):
        writer.addPage(pdf.getPage(i))


def load_pdf(filename):
    f = open(filename,'rb')
    return PdfFileReader(f)



def load1():
    f1 = tkinter.filedialog.askopenfilename(filetypes=(('PDF File', '*.pdf'),('All Files','*.*')))

    pdf1 = PDF_Doc(f1)
    filename1.set(pdf1.display)
    pages1.set(pdf1.pages)
    start1.set(pdf1.start)
    end1.set(pdf1.end)

    pdf_list.append(f1)

def load2():
    f2 = tkinter.filedialog.askopenfilename(filetypes=(('PDF File', '*.pdf'),('All Files','*.*')))

    pdf2 = PDF_Doc(f2)
    filename2.set(pdf2.display)
    pages2.set(pdf2.pages)
    start2.set(pdf2.start)
    end2.set(pdf2.end)

    pdf_list.append(f2)

def save_pdf():
    writer = PdfFileWriter()

    output_filename = filedialog.asksaveasfilename(filetypes=(('PDF File', '*.pdf'),('All Files','*.*')))
    output_file = open(output_filename, 'wb')

    add_to_writer(pdf_list[0].pdf, writer, int(s1.get()), int(e1.get()))
    add_to_writer(pdf_list[1].pdf, writer, int(s2.get()), int(e2.get()))

    writer.write(output_file)
    output_file.close()
    root.quit()


pdf_list = []

root = tkinter.Tk()
root.title("Wuhu DnD")

filename1 = StringVar()
pages1 = StringVar()
start1 = StringVar()
end1 = StringVar()

filename2 = StringVar()
pages2 = StringVar()
start2 = StringVar()
end2 = StringVar()

Label(root, text="PDF Manipulator").grid(row=0, column=2, sticky=E)

Button(root, text='Add pdf', command=load1).grid(row=1, column=0)
Label(root, textvariable=filename1, width = 30).grid(row=1, column=1, sticky=(N, S, E, W))

Label(root, text='Pages: ').grid(row=1,column=2)
Label(root, textvariable=pages1, width = 3).grid(row=1, column=3, sticky=(N, S, E, W))

Label(root, text='Start: ').grid(row=1, column=4)
s1 = Entry(root, textvariable=start1, width = 3)
s1.grid(row=1, column=5)

Label(root, text='End: ').grid(row=1,column=6)
e1 = Entry(root, textvariable=end1, width = 3)
e1.grid(row=1, column=7)

Button(root, text='Add pdf', command=load2).grid(row=2, column=0)
Label(root, textvariable=filename2, width = 20).grid(row=2, column=1, sticky=(N, S, E, W))

Label(root, text='Pages: ').grid(row=2,column=2)
Label(root, textvariable=pages2, width=3).grid(row=2, column=3, sticky=(N, S, E, W))

Label(root, text='Start: ').grid(row=2, column=4)
s2 = Entry(root, textvariable=start2, width = 3)
s2.grid(row=2, column=5)

Label(root, text='End: ').grid(row=2,column=6)
e2 = Entry(root, textvariable=end2, width=3)
e2.grid(row=2, column=7)


Button(root,text='Save PDF as', command=save_pdf, width=10).grid(row=3, column=2, sticky=E)

for child in root.winfo_children():
    child.grid_configure(padx=10, pady=10)

root.mainloop()
