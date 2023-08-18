from tkinter import *
import math

window = Tk()

window.title("Equation de degre 2")
window.geometry("450x300")
window.minsize(450, 300)
window.config(background="skyblue")
entrer = Entry(window, width=20)




def resolution():
    a = box1.get()
    b = box2.get()
    c = box3.get()
    d = ((int(b) * int(b)) - (4 * int(a) * int(c)))
    global label_text1
    global label_text2
    global label_text3


    if int(a) == 0 and int(b) == 0:


        label_text1 = Label(window, text="il ne sagit pas \nd'une equation de degré 2", bg="skyblue",
                           fg="white", font=("truetypefont", 26), bd=1)
        label_text1.place(x=20, y=300)

    else:
        if int(d) < 0:

            sceen1 = Tk()
            sceen1.title("soluce")
            sceen1.geometry("500x150")
            sceen1.config(background="green")

            label_text2 = Label(sceen1, text="lequation n'admet aucune solution \ndans R", bg="green",
                               fg="white", font=("truetypefont", 25), bd=1)
            label_text2.place(x=10, y=20)

        elif int(d) == 0:

            sceen2 = Tk()
            sceen2.title("soluce")
            sceen2.geometry("500x150")
            sceen2.config(background="green")

            X = (-int(b) / (2 * int(a)))

            label_text3 = Label(sceen2, text="lequation admet une solution double\n X = "+ str(X), bg="green",
                               fg="white", font=("truetypefont", 20), bd=1)
            label_text3.place(x=10, y=20)


        else:

            sceen3 = Tk()
            sceen3.title("soluce")
            sceen3.geometry("400x200")
            sceen3.config(background="green")

            X1 = (-int(b) - math.sqrt(int(d))) / (2 * int(a))
            X2 = (-int(b) + math.sqrt(d)) / (2 * int(a))


            label_text4 = Label(sceen3, text="Les solutions sont:\n X1 = " + str(X1)+" \nX2 = "+ str(X2), bg="green",
                               fg="white", font=("truetypefont", 20), bd=1)
            label_text4.place(x=8, y=20)






box1 = Entry(window,width=3, bg="white", fg="green",font=("truetypefont",20), bd=1)
box1.place(x=50, y=150)

box2 = Entry(window,width=3, bg="white", fg="green",font=("truetypefont",20), bd=1)
box2.place(x=150, y=150)

box3 = Entry(window,width=3, bg="white", fg="green",font=("truetypefont",20), bd=1)
box3.place(x=230, y=150)

label_equation = Label(window,text="soit lequation ax^2 + bx + C = 0",bg="skyblue",font=("courrier",20))
label_equation.place(x=50,y=50)

label_equation = Label(window,text="Entrer a,b et c",bg="skyblue",font=("courrier",20))
label_equation.place(x=50,y=100)

label_equation = Label(window,text="x^2",bg="skyblue",font=("courrier",20))
label_equation.place(x=100,y=150)

label_equation = Label(window,text="x",bg="skyblue",font=("courrier",20))
label_equation.place(x=200,y=150)

label_equation = Label(window,text="= 0",bg="skyblue",font=("courrier",20))
label_equation.place(x=290,y=150)

result_boutton = Button(window,text="Resulta", font=("helvetica", 20), bg="green", width=20, fg="white",command=resolution).place(x=50,y=200)


window.mainloop()