from tkinter import *
import string
from  random import*

def generate_password():
    password_min = 8
    password_max = 12
    all_chars = string.ascii_letters + string.digits

    password = "".join(choice(all_chars) for x in range(randint(password_min,password_max)))
    with open("mot de passe.txt","a+") as file:
        file.write(password_entry.get() + "\n")

    password_entry.delete(0, END)
    password_entry.insert(0, password)

window = Tk()

window.title("Generateur de mot de passe")
window.geometry("720x480")
window.minsize(720, 480)
window.iconbitmap("image/1065281.ico")
window.config(background="skyblue")

frame = Frame(window,bg="skyblue")

width = 300
height = 300
image = PhotoImage(file="BackgroundEraser_20221119_165932283 - Copie.png").zoom(x=2, y=2).subsample(32)
canvas = Canvas(frame, width=width, height=height, bg="skyblue", bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0,column=0, sticky=W)

right_frame = Frame(frame, bg="skyblue")

label_title = Label(right_frame, text="mot de passe", font=("helvetica", 20), bg="skyblue", fg="white")
label_title.grid()

password_entry = Entry(right_frame, font=("helvetica", 20), bg="skyblue", fg="white")
password_entry.grid()

generate_password_button = Button(right_frame, text="Generer", font=("helvetica", 20), bg="skyblue", fg="white", command=generate_password)
generate_password_button.grid()


right_frame.grid(row=0,column=1, sticky=W)

frame.pack(expand="yes")

menu_bar = Menu(window)

file_menu = Menu(menu_bar,tearoffcommand=0)
file_menu.add_command(label="Nouveau", command=generate_password)
file_menu.add_command(label="quiter", command=window.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)

window.config(menu=menu_bar)


window.mainloop()