import datetime
import tkinter
from tkinter import *
from tkinter import ttk



Name = 0
other_name = 0
phone_number = 0
born_day = []
password = 0
password_confirme = 0
i = 0



def recupere():
        global Name
        global other_name
        global phone_number
        global born_day
        global born_month
        global born_years
        global password
        global password_confirme

        Name = BOX.get()
        other_name = BOX1.get()
        phone_number = BOX2.get()
        #************************** recupere les infos de la naisaissance *******************
        born_day = listecombo_days.get()
        born_month = listecombo_month.get()
        born_years = listecombo_years.get()
        #  ************************************************************************************
        password = BOX3.get()
        password_confirme = BOX4.get()





        window.destroy()

        def supp():
            screen.destroy()


        global A
        screen = Tk()
        A = screen
        screen.title("my application")
        screen.geometry("600x420")
        screen.minsize(300, 300)
        screen.config(background="#d3d3d3")
        screen.attributes("-fullscreen", True)

        label_print_name = Label(screen, text="Nom :", font=("helvetica", 20), bg="#d3d3d3", fg="black")
        label_print_name.place(x="5", y="5")
        if Name != "":
                label_print_name = Label(screen, text=Name, font=("helvetica", 20), bg="#d3d3d3", fg="black")
                label_print_name.place(x="100", y="5")
        else:
                label_print_name = Label(screen, text="Vous devez entrer un nom !!!!", font=("helvetica", 20), bg="#d3d3d3", fg="red")
                label_print_name.place(x="100", y="5")

        label_print_name = Label(screen, text="Prenom :", font=("helvetica", 20), bg="#d3d3d3", fg="black")
        label_print_name.place(x="5", y="50")

        label_print_name = Label(screen, text=other_name, font=("helvetica", 20), bg="#d3d3d3", fg="black")
        label_print_name.place(x="120", y="50")

        label_print_name = Label(screen, text="Numero :", font=("helvetica", 20), bg="#d3d3d3", fg="black")
        label_print_name.place(x="5", y="100")

        try:
                phone_number = float(phone_number)
                label_print_name = Label(screen, text=phone_number, font=("helvetica", 20), bg="#d3d3d3", fg="black")
                label_print_name.place(x="130", y="100")
        except:
                label_print_name = Label(screen, text="Vous devez entrer un numero de telephone correct !!!!",
                                         font=("helvetica", 20), bg="#d3d3d3", fg="red")
                label_print_name.place(x="130", y="100")


        label_print_name = Label(screen, text="date de naissance :", font=("helvetica", 20), bg="#d3d3d3", fg="black")
        label_print_name.place(x="5", y="150")


        label_print_name = Label(screen, text=(born_day,"-", born_month, "-",born_years ), font=("helvetica", 20), bg="#d3d3d3", fg="black")
        label_print_name.place(x="250", y="150")


        label_print_name = Label(screen, text="mot de passe :", font=("helvetica", 20), bg="#d3d3d3", fg="black")
        label_print_name.place(x="5", y="200")

        def checbutton2():
                label_print_name = Label(screen, text=password, font=("helvetica", 20), bg="#d3d3d3", fg="black")
                label_print_name.place(x="240", y="200")

        if len((password)) >= 8 and password_confirme == password :
                label_print_name_hide = Label(screen, font=("helvetica", 20),bg="#d3d3d3",width=12,fg="black")
                label_print_name_hide.place(x="240", y="200")

                c2 = Checkbutton(screen, text="Cacher le mot de passe", height=1, width=20, bg="#d3d3d3", onvalue=1,
                                 offvalue=0, state=ACTIVE, command=checbutton2)
                c2.place(x="1000", y="230")
        else:
                label_print_name = Label(screen, text="Mot de passe incorect!!!", font=("helvetica", 20), bg="#d3d3d3", fg="red")
                label_print_name.place(x="240", y="200")



        next_button = Button(screen, text="Next", font=("helvetica", 20), bg="gray", width=20, fg="white",command=last_supp)
        next_button.place(x="700", y="600")

        destroy_button = Button(screen, text="Annule", font=("helvetica", 20), bg="gray", width=20, fg="white",
                                command=supp)
        destroy_button.place(x="300", y="600")

def last_supp():
        global i
        A.destroy()
        new_screen = Tk()

        new_screen.title("my application")
        new_screen.geometry("600x420")
        new_screen.minsize(300, 300)
        new_screen.config(background="#d3d3d3")
        new_screen.attributes("-fullscreen", True)

        if len(password) > 8 and password_confirme == password and phone_number != "":

                final_label = Label(new_screen, text="Inscription reusite!!!", font=("elphant", 100), bg="#d3d3d3",fg="green")
                final_label.pack(expand="yes")

                with open("formulaire_donnees.txt", "a+") as file:
                        file.write("nom:"+Name + ", ")
                        file.write("prenom:"+other_name + ", ")
                        file.write("numero:"+str(phone_number) + ", ")
                        file.write("né le:"+born_day + ", ")
                        file.write(+born_month + ", ")
                        file.write(+ born_years + ", ")
                        file.write("Mot de passe:"+password + "\n")


        else:
                final_label = Label(new_screen, text="Echec de l'inscription", font=("elphant", 100), bg="#d3d3d3",
                                    fg="red")
                final_label.pack(expand="yes")



        destroy_button = Button(new_screen, text="Terminé", font=("helvetica", 20), bg="gray", width=20, fg="white",
                                command=new_screen.destroy)
        destroy_button.place(x="500", y="600")


def destroy():
    window.destroy()





window = Tk()

window.title("my application")
window.geometry("2200x1080")
window.minsize(300, 300)
window.config(background="#d3d3d3")
window.attributes("-fullscreen",True)

# ******************************* born day box****************************************************************************

jour = []
for ii in range(1,32):
        jour.append(ii)

mois = ["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Aout","Septembre","Octobre","Novembre","Décembre" ]
anne = datetime.date.year


annee_max = datetime.MAXYEAR - 7899
annee_min = datetime.MINYEAR + 1899
b = []
for i in range(annee_min, annee_max):
                b.append(i)


listecombo_years = ttk.Combobox(window,values = b)
listecombo_years.place(x="850",y="350")
listecombo_years.current(123)

listecombo_days = ttk.Combobox(window,values=jour)
listecombo_days.place(x="450",y="350")
listecombo_days.current(0)

listecombo_month = ttk.Combobox(window,values = mois)
listecombo_month.place(x="650",y="350")
listecombo_month.current(0)

#********************************** Autre box ***************************************************************************

BOX = Entry(window, width=81, bg="white",textvariable=StringVar, fg="green",font=("truetypefont",18), bd=1)
BOX.place(x="250",y="110")

BOX1 = Entry(window, width=80, bg="white",textvariable=StringVar, fg="green",font=("truetypefont",18), bd=1)
BOX1.place(x="262",y="185")

BOX2 = Entry(window, width=67, bg="white",textvariable=StringVar, fg="green",font=("truetypefont",18), bd=1)
BOX2.place(x="430",y="267")

BOX3 = Entry(window, width=75, bg="white",textvariable=StringVar, fg="green",font=("truetypefont",18), bd=1,show="*")
BOX3.place(x="330",y="425")

BOX4 = Entry(window, width=75, bg="white",textvariable=StringVar, fg="green",font=("truetypefont",18), bd=1,show="*")
BOX4.place(x="330",y="495")



label_title = Label(window, text="FORMULAIRE D'INSCRIPTION", font=("arial blac", 40), bg="#d3d3d3", fg="black").place(x="300", y="10")
label_name = Label(window, text="Entrer votre nom:", font=("elephant", 20), bg="#d3d3d3", fg="black").place(x="1", y="100")
label_other_name = Label(window, text="Entrer votre prenom:", font=("elephant", 18), bg="#d3d3d3", fg="black").place(x="1", y="180")
label_number = Label(window, text="Entrer votre numero de telephone:", font=("elephant", 18), bg="#d3d3d3", fg="black").place(x="1", y="260")
label_born_day = Label(window, text="Entrer votre date de naissance:", font=("elephant", 18), bg="#d3d3d3", fg="black").place(x="1", y="340")
label_password = Label(window, text="Entrer votre mot de passe:", font=("elephant", 18), bg="#d3d3d3", fg="black").place(x="1", y="420")
label_password = Label(window, text="Confirmer le mot de passe:", font=("elephant", 18), bg="#d3d3d3", fg="black").place(x="1", y="490")
label_password = Label(window, text="(le mot de passe doit avoir au moins 8 caractères)", font=("calibri", 18), bg="#d3d3d3", fg="red").place(x="1", y="540")

var = tkinter.BooleanVar()
a=var.get()
print(a)

def checbutton():
                BOX3.configure(show="")
                BOX4.configure(show="")


c1 = Checkbutton(window,text="Cacher le mot de passe",variable=var,height=1,width=20,bg="#d3d3d3",onvalue=1,offvalue=0,command=checbutton)
c1.place(x="1140",y="465")

next_button = Button(window, text="Next", font=("helvetica", 20), bg="gray",width=20, fg="white", command=recupere)
next_button.place(x="700", y="600")

destroy_button = Button(window, text="Annule", font=("helvetica", 20), bg="gray",width=20, fg="white", command=destroy)
destroy_button.place(x="300", y="600")


window.mainloop()