from tkinter import *
import webbrowser

def open_byron_channel():
    webbrowser.open("http://www.youtube.com/@byronlementaliste8624")

window = Tk()

window.title("my application")
window.geometry("720x420")
window.minsize(300, 300)
window.iconbitmap("1065281.ico")
window.config(background="blue")

frame = Frame(window, bg="blue")

label_title = Label(frame, text="bienvenue sur l'application", font=("elephant", 25), bg="blue", fg="white")
label_title.pack()

label_subtitle = Label(frame, text="hey salut a tous c'est byron", font=("elephant", 15), bg="blue", fg="white")
label_subtitle.pack()

yt_button = Button(frame, text="ouvrir youtube", font=("elephant", 15), bg="white", fg="blue", command=open_byron_channel)
yt_button.pack(pady=25, fill=X)

frame.pack(expand="yes")

window.mainloop()
