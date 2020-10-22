from tkinter import *
from tkinter.filedialog import *
import PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter
from DragDrop import *

class PDF_Doc():
    def __init__(self, filename):
        self.filename = filename
        self.display = filename.split('/')[-1]
        self.pdf = load_pdf(filename)
        self.pages = self.pdf.getNumPages()
        self.start = 1
        self.end = self.pages
            
    def add_to_writer(pdf, writer):
        for i in range(self.start-1, self.end):
            writer.addPage(self.pdf.getPage(i))


def load_pdf(filename):
    f = open(filename,'rb')
    return PdfFileReader(f)

def load():
    f = askopenfilename(filetypes=(('PDF File','*.pdf'),('All Files','*.*')))
    pdf = PDF_Doc(f)
    listbox.lst += [pdf]
    listbox.insert(END,pdf.display)
    

def save_pdf():
    writer = PdfFileWriter()

    output_filename = asksaveasfilename(filetypes=(('PDF File','*.pdf'),('All files','*.*')))
    output_file = open(output_filename, 'wb')

    for doc in pdf_list:
        doc.add_to_writer(writer)

    writer.write(output_file)
    output_file.close()
    root.quit()

def remove():
    index = int(listbox.curselection()[0])
    pdf_list.pop(index)
    listbox.delete(ANCHOR)
    

def display(*args):
    index = int(listbox.curselection()[0])
    value = listbox.get(index)
    filename.set(value)
    pages.set(pdf_list[index].pages)
    start.set(pdf_list[index].start)
    end.set(pdf_list[index].end)

def set_start(*args):
    index = int(listbox.curselection()[0])
    pdf_list[index].start = int(start.get())

def set_end(*args):
    index = int(listbox.curselection()[0])
    pdf_list[index].end = int(end.get())


pdf_list = []

root = Tk()
root.title('PDF Merger')

filename = StringVar()
pages = StringVar()
start = StringVar()
end = StringVar()

Label(root, text='PDF Manipulator').grid(row=0, column=0,columnspan=4)

Button(root, text='Add PDF',command=load).grid(row=2,column=0)
Button(root,text='Remove PDF',command=remove).grid(row=3,column=0)

listbox = DragDropListbox(root, pdf_list)
listbox.bind('<<ListboxSelect>>', display)
listbox.grid(row=1,rowspan=4, column=1)

Label(root, text='File: ').grid(row=1, column=2)
Label(root, textvariable=filename, width=20).grid(row=1, column=3,sticky=(N, S, E,W))

Label(root, text='Pages: ').grid(row=2, column=2)
Label(root, textvariable=pages).grid(row=2, column=3)

Label(root, text='Start: ').grid(row=3,column=2)
s = Entry(root, textvariable=start, width=3)
s.grid(row=3, column=3)

Label(root, text='End: ').grid(row=4, column=2)
e = Entry(root, textvariable=end,width=3)
e.grid(row=4, column=3)

Button(root, text='Save PDF As: ', command=save_pdf,width=10).grid(row=5,column=0,columnspan=4)

for child in root.winfo_children():
    child.grid(padx=10, pady=10)

start.trace('w',set_start)
end.trace('w',set_end)

root.mainloop()