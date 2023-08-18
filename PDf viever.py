import tkinter
from tkinter import*
from tkinter import filedialog
import os
import PyPDF2
import pyaudio
import wave


window = Tk()
window.config(bg="white")
window.geometry("620x680")
window.title("pdf reader")

def browserfile():
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),title="select pdf file",filetypes=(("mp3 File",".mp3"),("Wave File",".wav"),("All file",".mp3")))
    v1= open(filename, "rb")


    v2 = PyPDF2.PdfReader(v1)
    num_page = v2.getNumPages()









open_bouton = Button(window,text="open",command=browserfile,width=40,font="centurygotyc",bd=4).pack()


window.mainloop()