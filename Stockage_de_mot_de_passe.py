from tkinter import *




def create_entrey():
        a = 5
        first_entry = Entry(frame_create_button,font=("courier",20))
        first_entry.place(x=305,y=a)



window = Tk()
window.title("password garder")
window.geometry("700x500")
window.config(bg="skyblue")

welcom_label = Label(window,text="Bien venue veiller ajouter un nouveau mot de passe",font=("century",20),bg="skyblue")
welcom_label.pack()

frame_button = Frame(window,width=800,height=50,bg="skyblue")
frame_button.place(x=0,y=90)
add_button = Button(frame_button,text="Ajouter",font=("arial",15),width=20,command=create_entrey)
add_button.place(x=5,y=5)
delete_button = Button(frame_button,text="Supprimer",font=("arial",15),width=20)
delete_button.place(x=460,y=5)

frame_create_button = Frame(window,width=800,height=500,bg="orange")
frame_create_button.place(x=0,y=150)


window.mainloop()