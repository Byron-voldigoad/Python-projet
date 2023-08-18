import tkinter
from tkinter import *
from math import*


#if op == "!"


#12!*2+1
# fonctions:

def effacer_ecran(a):
    ECRAN.delete(0,a)


def effacer_ecran_tout(a):

    ECRAN.delete(0, a)




def afficher_nbr(a):


    ECRAN.insert(100000000, a)





def eval_calcul():

        op = ECRAN.get()
        op1 = ECRAN.get()

        try:
                result=""
                result2=""
                expressions=["cos","sin","!","log","exp","sqrt","^"]
                elements=[]
                try:
                    try:
                        try:
                            for Exp in expressions:
                                    if Exp in op:
                                        if Exp=="cos":
                                            for o in op:
                                                elements.append(o)

                            nb = elements.index("s") + 1
                            for nb in range(elements.index("s")+1, len(elements)):
                                    result += str(elements[nb])

                            ECRAN.delete(0, END)
                            ECRAN.insert(0, cos(radians(int(result))))
                        except:
                            try:

                                for Exp in expressions:
                                    if Exp in op:
                                        if Exp == "sqrt":
                                            for o in op:
                                                elements.append(o)

                                nb = elements.index("t") + 1
                                for nb in range(elements.index("t") + 1, len(elements)):
                                    result += str(elements[nb])

                                ECRAN.delete(0, END)
                                ECRAN.insert(0, sqrt(int(result)))
                            except:

                                for Exp in expressions:
                                    if Exp in op:
                                        if Exp == "^":
                                            for o in op:
                                                elements.append(o)

                                nb = elements.index("^")+1

                                result1=""
                                for nb in range(elements.index("^") + 1, len(elements)-1):
                                    result += str(elements[nb])


                                nb2 = elements.index("^") + 1
                                for nb2 in range(elements.index("^") + 1, len(elements)):
                                    result2 += str(elements[nb2])


                                for ig in range(0,elements.index("^")-1):
                                    result1+=str(ig)



                                ECRAN.delete(0, END)
                                ECRAN.insert(0, pow(result1,result))
                                print(pow(result1,result))
                    except:
                        try:
                            for Exp in expressions:
                                if Exp in op:
                                    if Exp == "exp":
                                        for o in op:
                                            elements.append(o)

                            nb = elements.index("p") + 1
                            for nb in range(elements.index("p") + 1, len(elements)):
                                result += str(elements[nb])

                            ECRAN.delete(0, END)
                            ECRAN.insert(0, exp(int(result)))
                        except:
                            for Exp in expressions:
                                if Exp in op:
                                    if Exp == "!":
                                        for o in op:
                                            elements.append(o)

                            elements.reverse()
                            nb = elements.index("!") + 1
                            for nb in range(elements.index("!")+1,len(elements)):
                                result += str(elements[nb])



                            ECRAN.delete(0, END)
                            ECRAN.insert(0, factorial(int(result)))
                        print(elements[0])
                        print(elements[len(elements)-1])
                except:
                    try:
                        for Exp in expressions:
                            if Exp in op:
                                if Exp == "log":
                                    for o in op:
                                        elements.append(o)
                                     
                        nb = elements.index("g") + 1
                        for nb in range(elements.index("g") + 1, len(elements)):
                            result += str(elements[nb])

                        ECRAN.delete(0, END)
                        ECRAN.insert(0, log(int(result)))
                    except:
                            for Exp in expressions:
                                if Exp in op:
                                    if Exp == "sin":
                                        for o in op:
                                            elements.append(o)

                            nb = elements.index("n") + 1
                            for nb in range(elements.index("n") + 1, len(elements)):
                                result += str(elements[nb])

                            ECRAN.delete(0, END)
                            ECRAN.insert(0, sin(radians(int(result))))


        except:

                result = eval(op)
                ECRAN.delete(0,END)
                ECRAN.insert(0,result)



window = Tk()

window.title("calculator")
window.geometry("450x545")
window.minsize(450, 545)
window.config(background="black")
entrer = Entry(window, width=20)


#Ecran:

frame = Frame(window, bg="black").place(x="225", y="275")

ECRAN = Entry(frame, width=28, bg="black",justify=RIGHT, fg="green",font=("truetypefont",18), bd=35)
ECRAN.place(x=6, y=5)




label_name = Label(frame, text="scientific calculator",width=17,height=2, font=("courrier", 19), bg="black", fg="white",relief=SUNKEN).place(x=4, y=120)

# boutons:



BOUTON1 = Button(frame, text="1", font=("arial black",20), command=lambda :afficher_nbr(1), width="4", height="1", bg="black", fg="white").place(x="90", y="400")
BOUTON2 = Button(frame, text="2", font=("arial black",20), command=lambda :afficher_nbr(2), width="4", height="1", bg="black", fg="white").place(x="180", y="400")
BOUTON3 = Button(frame, text="3", font=("arial black",20), command=lambda :afficher_nbr(3), width="4", height="1",bg="black", fg="white").place(x="270", y="400")
BOUTON4 = Button(frame, text="4", font=("arial black",20), command=lambda :afficher_nbr(4), width="4", height="1", bg="black", fg="white").place(x="90", y="330")
BOUTON5 = Button(frame, text="5", font=("arial black",20), command=lambda :afficher_nbr(5), width="4", height="1", bg="black", fg="white").place(x="180", y="330")
BOUTON6 = Button(frame, text="6", font=("arial black",20), command=lambda :afficher_nbr(6), width="4", height="1", bg="black", fg="white").place(x="270", y="330")
BOUTON7 = Button(frame, text="7", font=("arial black",20), command=lambda :afficher_nbr(7), width="4", height="1", bg="black", fg="white").place(x="90", y="260")
BOUTON8 = Button(frame, text="8", font=("arial black",20), command=lambda :afficher_nbr(8), width="4", height="1", bg="black", fg="white").place(x="180", y="260")
BOUTON9 = Button(frame, text="9", font=("arial black",20), command=lambda :afficher_nbr(9), width="4", height="1", bg="black", fg="white").place(x="270", y="260")
BOUTON10 = Button(frame, text="0", font=("arial black",20), command=lambda :afficher_nbr(0), width="4", height="1", bg="black", fg="white").place(x="180", y="470")
BOUTON11 = Button(frame, text="+", font=("arial black",20), command=lambda :afficher_nbr("+"), width="4", height="1", bg="black", fg="orange").place(x="359", y="400")
BOUTON12 = Button(frame, text="X", font=("arial black",20), command=lambda :afficher_nbr("*"), width="4", height="1", bg="black", fg="orange").place(x="359", y="260")
BOUTON13 = Button(frame, text="/", font=("arial black",20), command=lambda :afficher_nbr("/"), width="4", height="1", bg="black", fg="orange").place(x="359", y="190")
BOUTON14 = Button(frame, text="-", font=("arial black",20), command=lambda :afficher_nbr("-"), width="4", height="1", bg="black", fg="orange").place(x="359", y="330")
BOUTON15 = Button(frame, text="^", font=("arial black",20), command=lambda :afficher_nbr("^"), width="4", height="1", bg="black", fg="orange").place(x="90", y="470")
BOUTON16 = Button(frame, text="=", font=("arial black",20), command=lambda :eval_calcul(), width="4", height="1", bg="black", fg="orange").place(x="359", y="470")
BOUTON17 = Button(frame, text=",", font=("arial black",20), command=lambda :afficher_nbr(","), width="4", height="1", bg="black", fg="orange").place(x="270", y="470")
BOUTON18 = Button(frame, text="(", font=("arial black",20), command=lambda :afficher_nbr("("), width="4", height="1", bg="black", fg="orange").place(x="2", y="470")
BOUTON19 = Button(frame, text=")", font=("arial black",20), command=lambda :afficher_nbr(")"), width="4", height="1", bg="black", fg="orange").place(x="2", y="400")
BOUTON20 = Button(frame, text="ln", font=("arial black",20), command=lambda :afficher_nbr("log"), width="4", height="1", bg="black", fg="orange").place(x="2", y="330")
BOUTON21 = Button(frame, text="e", font=("arial black",20), command=lambda :afficher_nbr("exp"), width="4", height="1", bg="black", fg="orange").place(x="2", y="260")
BOUTON22 = Button(frame, text="!", font=("arial black",20), command=lambda :afficher_nbr("!"), width="4", height="1", bg="black", fg="orange").place(x="2", y="190")
BOUTON23 = Button(frame, text="sqrt", font=("arial black",20), command=lambda :afficher_nbr("sqrt"), width="4", height="1", bg="black", fg="orange").place(x="180", y="190")
BOUTON24 = Button(frame, text="sin", font=("arial black",20), command=lambda :afficher_nbr("sin"), width="4", height="1", bg="black", fg="orange").place(x="270", y="190")
BOUTON25 = Button(frame, text="cos", font=("arial black",20), command=lambda :afficher_nbr("cos"), width="4", height="1", bg="black", fg="orange").place(x="90", y="190")
BOUTON26 = Button(frame, text="Del", font=("arial black",20), command=lambda :effacer_ecran(1),justify=RIGHT, width="4", height="1", bg="black", fg="orange").place(x="270", y="120")
BOUTON27 = Button(frame, text="C", font=("arial black",20), command=lambda :effacer_ecran_tout(10000000), width="4", height="1", bg="black", fg="orange").place(x="360", y="120")


window.mainloop()