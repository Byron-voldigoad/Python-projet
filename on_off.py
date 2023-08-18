from tkinter import *
from math import*


window = Tk()

window.title("calculator")
window.geometry("450x545")
window.minsize(450, 545)
window.config(background="black")
entrer = Entry(window, width=20)

frame = Frame(window, bg="black")
frame.pack(expand="yes")

ECRAN = Entry(window, width=28, bg="black",justify=RIGHT, fg="green",font=("truetypefont",18), bd=35)
ECRAN.place(x=6, y=5)

BOUTONON = Button(frame, text="ON", font=("arial black",50), command=lambda :__import__("calculatrice_scientifique"), width="4", height="1", bg="red", fg="white")
BOUTONON.pack()


window.mainloop()