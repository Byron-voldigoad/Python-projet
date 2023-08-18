from tkinter import *
from tkinter import filedialog
import os
import tkinter.font as font

window = Tk()
window.title("lecteur fichiers")
window.geometry("500x500")
window.config(bg="white")

def charge():
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),title="selectionner le fichier",filetypes=(("Document texte",".txt"),("All texte",".txt"),("fichier CBZ",".cbz")))
    with open(filename,"r+") as file:
        v1 = file.readlines()
        liste.insert(END, v1)
        barre.config(command=liste.yview)
        barre2.config(command=liste.xview)
    file.close()



open_button = Button(window,text="ouvrir",font=("centurygotic",20),command=charge,width=100)
open_button.pack()
barre = Scrollbar(window,bd=2,bg="orange")
barre.pack(side=RIGHT,fill=Y)
barre2 = Scrollbar(window,bd=2,repeatdelay=2,bg="orange",orient=HORIZONTAL)
barre2.pack(side=BOTTOM,fill=X)
liste = Listbox(window,yscrollcommand=barre.set,xscrollcommand=barre2.set,font=("centurygotic",50))

liste.pack(side=LEFT,fill=BOTH)
barre.config(command=liste.yview)
barre2.config(command=liste.yview)

window.mainloop()