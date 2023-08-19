
from tkinter import*
import random


nbr_list1 = [1,2,3,4,5,6,7,8,9]
nbr_list = []
for i in range(len(nbr_list1)):
    nbr_list.append(nbr_list1[i])

row1 = []
row11 = []
row2 = []
row12 = []
row3 = []
row13 = []
a = 0
m = True
def table_clear():
    row1.clear()
    row11.clear()
    row2.clear()
    row12.clear()
    row3.clear()
    row13.clear()

def verifier_tableau(nbr_list):
    chiffres = set(range(1, 10)) # ensemble des chiffres de 1 à 9
    for chiffre in chiffres:
        if nbr_list.count(chiffre) > 1: # si le chiffre est présent plus d'une fois
            manquant = chiffres - set(nbr_list) # on calcule le chiffre manquant
            nbr_list[nbr_list.index(chiffre)] = manquant.pop() # on remplace le chiffre répété par le chiffre manquant
            break # on sort de la boucle car on a trouvé un chiffre répété et l'a remplacé
    return nbr_list

def remplisage1():
    global nbr_list, a
    for row in range(3):
        for column in range(3):
            a = random.choice(nbr_list)
            row1.append(a)
            verifier_tableau(row1)
    for i in range(3):
        row11a = []
        for j in range(3):
            if row1:
                row11a.append(row1.pop(0))
        row11.append(row11a)

def remplisage2():
    global nbr_list, a
    nbr_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for row in range(3):
        for column in range(3):
            a = random.choice(nbr_list)
            row2.append(a)
            verifier_tableau(row2)
    for i in range(3):
        row12a = []
        for j in range(3):
            if row2:
                row12a.append(row2.pop(0))
        row12.append(row12a)

def remplisage3():
    global nbr_list, a
    for row in range(3):
        for column in range(3):
            a = random.choice(nbr_list)
            row3.append(a)
            verifier_tableau(row3)
    for i in range(3):
        row13a = []
        for j in range(3):
            if row3:
                row13a.append(row3.pop(0))
        row13.append(row13a)


def similaire1_2():
    for i in range(3):
        # verification de la premiere ligne
        if row12[0][i] == row11[0][0] or row12[0][i] == row12[0][0]:
            # print("f1_2_1=" + str(row12[0][i]))
            return False
        elif row12[0][i] == row11[0][1]:
            # print("f1_2_2=" + str(row12[0][i]))
            return False
        elif row12[0][i] == row11[0][2]:
            # print("f1_2_3=" + str(row12[0][i]))
            return False

        # verification de la deuxieme ligne
        if row12[1][i] == row11[1][0]:
            # print("f1_2_1=" + str(row12[1][i]))
            return False
        elif row12[1][i] == row11[1][1]:
            # print("f1_2_2=" + str(row12[1][i]))
            return False
        elif row12[1][i] == row11[1][2]:
            # print("f1_2_3=" + str(row12[1][i]))
            return False

        # verification de la deuxieme ligne
        if row12[2][i] == row11[2][0]:
            # print("f1_2_1=" + str(row12[2][i]))
            return False
        elif row12[2][i] == row11[2][1]:
            # print("f1_2_2=" + str(row12[2][i]))
            return False
        elif row12[2][i] == row11[2][2]:
            # print("f1_2_3=" + str(row12[2][i]))
            return False
    return True

def similaire1_3():
    for i in range(3):
        # verification de la premiere ligne
        if row13[0][i] == row11[0][0]:
            # print("f1_3_1=" + str(row13[0][i]))
            return False
        elif row13[0][i] == row11[0][1]:
            # print("f1_3_2=" + str(row13[0][i]))
            return False
        elif row13[0][i] == row11[0][2]:
            # print("f1_3_3=" + str(row13[0][i]))
            return False

        # verification de la deuxieme ligne
        if row13[1][i] == row11[1][0]:
            # print("f1_3_1=" + str(row13[1][i]))
            return False
        elif row13[1][i] == row11[1][1]:
            # print("f1_3_2=" + str(row13[1][i]))
            return False
        elif row13[1][i] == row11[1][2]:
            # print("f1_3_3=" + str(row13[1][i]))
            return False

        # verification de la deuxieme ligne
        if row13[2][i] == row11[2][0]:
            # print("f1_3_1=" + str(row13[2][i]))
            return False
        elif row13[2][i] == row11[2][1]:
            # print("f1_3_2=" + str(row13[2][i]))
            return False
        elif row13[2][i] == row11[2][2]:
            # print("f1_3_3=" + str(row13[2][i]))
            return False
    return True

def similaire2_3():
    for i in range(3):
        # verification de la premiere ligne
        if row13[0][i] == row12[0][0]:
            # print("f2_3_1=" + str(row13[0][i]))
            return False
        elif row13[0][i] == row12[0][1]:
            # print("f2_3_2=" + str(row13[0][i]))
            return False
        elif row13[0][i] == row12[0][2]:
            # print("f2_3_3=" + str(row13[0][i]))
            return False

        # verification de la deuxieme ligne
        if row13[1][i] == row12[1][0]:
            # print("f2_3_1=" + str(row13[1][i]))
            return False
        elif row13[1][i] == row12[1][1]:
            # print("f2_3_2=" + str(row13[1][i]))
            return False
        elif row13[1][i] == row12[1][2]:
            # print("f2_3_3=" + str(row13[1][i]))
            return False

        # verification de la deuxieme ligne
        if row13[2][i] == row12[2][0]:
            # print("f2_3_1=" + str(row13[2][i]))
            return False
        elif row13[2][i] == row12[2][1]:
            # print("f2_3_2=" + str(row13[2][i]))
            return False
        elif row13[2][i] == row12[2][2]:
            # print("f2_3_3=" + str(row13[2][i]))
            return False
    return True


def sudoku_start():
    global nbr_list,a
    #***************************frame[1][0]*********************************************
    remplisage1()
    #***************************frame[1][1]*********************************************
    remplisage2()
    # ***************************frame[1][2]*********************************************
    remplisage3()

    def melanger_tableau(tableau):
        random.shuffle(tableau)
        return tableau
    while not similaire1_2() :
        melanger_tableau(row12)
        remplisage2()
        #verifier_tableau(row12)
        print(similaire1_2())
    for i in range(9):
        btn1[i // 3][i % 3]["text"] = row11[i // 3][i % 3]
        btn1_1[i//3][i%3]["text"] = row12[i//3][i%3]
        btn1_2[i // 3][i % 3]["text"] = row13[i // 3][i % 3]

    nbr_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    #***************************************************************
    for i in range(9):
        if btn1_1[i//3][i % 3]["text"] == 1:
                btn1_1[i//3][i % 3]["bg"] = color[0][0]
        if btn1_1[i//3][i % 3]["text"] == 2:
            btn1_1[i//3][i % 3]["bg"] = color[0][1]
        if btn1_1[i//3][i % 3]["text"] == 3 :
            btn1_1[i//3][i % 3]["bg"] = color[0][2]
        if btn1_1[i//3][i % 3]["text"] == 4:
            btn1_1[i//3][i % 3]["bg"] = color[1][0]
        if btn1_1[i//3][i % 3]["text"] == 5:
            btn1_1[i//3][i % 3]["bg"] = color[1][1]
        if btn1_1[i//3][i % 3]["text"] == 6:
            btn1_1[i//3][i % 3]["bg"] = color[1][2]
        if btn1_1[i//3][i % 3]["text"] == 7:
            btn1_1[i//3][i % 3]["bg"] = color[2][0]
        if btn1_1[i//3][i % 3]["text"] == 8:
            btn1_1[i//3][i % 3]["bg"] = color[2][1]
        if btn1_1[i//3][i % 3]["text"] == 9:
            btn1_1[i//3][i % 3]["bg"] = color[2][2]
        if btn1[i//3][i % 3]["text"] == 1:
            btn1[i//3][i % 3]["bg"] = color[0][0]
        if btn1[i//3][i % 3]["text"] == 2:
            btn1[i//3][i % 3]["bg"] = color[0][1]
        if btn1[i // 3][i % 3]["text"] == 3:
            btn1[i // 3][i % 3]["bg"] = color[0][2]
        if btn1[i // 3][i % 3]["text"] == 4:
            btn1[i // 3][i % 3]["bg"] = color[1][0]
        if btn1[i // 3][i % 3]["text"] == 5:
            btn1[i // 3][i % 3]["bg"] = color[1][1]
        if btn1[i // 3][i % 3]["text"] == 6:
            btn1[i // 3][i % 3]["bg"] = color[1][2]
        if btn1[i // 3][i % 3]["text"] == 7:
            btn1[i // 3][i % 3]["bg"] = color[2][0]
        if btn1[i // 3][i % 3]["text"] == 8:
            btn1[i // 3][i % 3]["bg"] = color[2][1]
        if btn1[i // 3][i % 3]["text"] == 9:
            btn1[i // 3][i % 3]["bg"] = color[2][2]
        if btn1_2[i//3][i % 3]["text"] == 1:
            btn1_2[i//3][i % 3]["bg"] = color[0][0]
        if btn1_2[i//3][i % 3]["text"] == 2:
            btn1_2[i//3][i % 3]["bg"] = color[0][1]
        if btn1_2[i//3][i % 3]["text"] == 3 :
            btn1_2[i//3][i % 3]["bg"] = color[0][2]
        if btn1_2[i//3][i % 3]["text"] == 4:
            btn1_2[i//3][i % 3]["bg"] = color[1][0]
        if btn1_2[i//3][i % 3]["text"] == 5:
            btn1_2[i//3][i % 3]["bg"] = color[1][1]
        if btn1_2[i//3][i % 3]["text"] == 6:
            btn1_2[i//3][i % 3]["bg"] = color[1][2]
        if btn1_2[i//3][i % 3]["text"] == 7:
            btn1_2[i//3][i % 3]["bg"] = color[2][0]
        if btn1_2[i//3][i % 3]["text"] == 8:
            btn1_2[i//3][i % 3]["bg"] = color[2][1]
        if btn1_2[i//3][i % 3]["text"] == 9:
            btn1_2[i//3][i % 3]["bg"] = color[2][2]

    ii = 0
    ii1 = 0
    ii2 = 0


    table_clear()
    '''''''''''
    row12a.clear()
    row13a.clear()
     '''''



    nbr_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]



window = Tk()

window.geometry("516x700")
window.configure(background="orange")

color = [["green","red","yellow"],["gray","brown","pink"],["purple","blue","darkblue"]]

#*********** row 1 *****************************************************
btn1 = [[0,0,0],[0,0,0],[0,0,0]]
btn1_1 = [[0,0,0],[0,0,0],[0,0,0]]
btn1_2 = [[0,0,0],[0,0,0],[0,0,0]]
#*********** row 2 *****************************************************
btn2 = [[0,0,0],[0,0,0],[0,0,0]]
btn2_2 = [[0,0,0],[0,0,0],[0,0,0]]
btn2_1 = [[0,0,0],[0,0,0],[0,0,0]]
#*********** row 3 *****************************************************
btn3 = [[0,0,0],[0,0,0],[0,0,0]]
btn3_2 = [[0,0,0],[0,0,0],[0,0,0]]
btn3_1 = [[0,0,0],[0,0,0],[0,0,0]]

frame = Frame(window,width=150,height=150)
frame.grid(row=0,column=2)

btn_start = Button(window,text="Comencer",command=sudoku_start)
btn_start.place(x=12,y=12)

frame= [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

for row in range(1,4):
     for column in range(3):
        frame[row][column] = Frame(window,width=166.5,height=166.5,highlightbackground="black",highlightthickness=2)
        frame[row][column].grid(row=row,column=column)

#*********** row 1 *****************************************************
for row in range(3):
     for column in range(3):
        btn1 [row][column] = Button(frame[1][0],width=6,height=3)
        btn1[row][column].grid(row=row,column=column)
for row in range(3):
     for column in range(3):
        btn1_1 [row][column] = Button(frame[1][1],width=6,height=3)
        btn1_1 [row][column].grid(row=row,column=column)
for row in range(3):
     for column in range(3):
        btn1_2 [row][column] = Button(frame[1][2],width=6,height=3)
        btn1_2 [row][column].grid(row=row,column=column)
#*************************************************************************

#*********** row 2 ****************************************************
for row in range(3):
     for column in range(3):
        btn2 [row][column] = Button(frame[2][0],width=6,height=3)
        btn2 [row][column].grid(row=row,column=column)
for row in range(3):
     for column in range(3):
        btn2_1 [row][column] = Button(frame[2][1],width=6,height=3)
        btn2_1 [row][column].grid(row=row,column=column)
for row in range(3):
     for column in range(3):
        btn2_2 [row][column] = Button(frame[2][2],width=6,height=3)
        btn2_2 [row][column].grid(row=row,column=column)
#*************************************************************************

#*********** row 3 ********************************************************
for row in range(3):
     for column in range(3):
        btn3 [row][column] = Button(frame[3][0],width=6,height=3)
        btn3 [row][column].grid(row=row,column=column)
for row in range(3):
     for column in range(3):
        btn3_1 [row][column] = Button(frame[3][1],width=6,height=3)
        btn3_1 [row][column].grid(row=row,column=column)
for row in range(3):
     for column in range(3):
        btn3_2 [row][column] = Button(frame[3][2],width=6,height=3)
        btn3_2 [row][column].grid(row=row,column=column)
#*************************************************************************


window.mainloop()