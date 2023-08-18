import random
from tkinter import *

window = Tk()
window.title("Meal propose")
window.geometry("500x300")
window.minsize(500,300)
window.config(background="skyblue")

def propsiton_repas():

        with open("meals.txt","r") as file:
            meal_random_choice = random.choices(file.readlines())
            result_entry.delete(0,END)
            result_entry.insert(0,meal_random_choice)
            file.close()

label_propos1 = Label(window,font=("century",20),text="Proposition de menu",width="30",bg="skyblue")
label_propos1.place(x="11",y="8")

propo_buton = Button(window,text="proposer",width="80",height="3",command=propsiton_repas,font=("cintury gotic",8))
propo_buton.place(x="10",y="230")

result_entry = Entry(window,bg="skyblue",fg="black",font=("century",20),width="30")
result_entry.place(x="12",y="100")


window.mainloop()