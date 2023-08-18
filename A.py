import threading

# Verrou
verrou = threading.Lock()
a = 0
# Fonction 1
def fonction1():
    with verrou:
        global a
        a = a + 1

# Fonction 2
def fonction2():
    with verrou:
        global a
        a = a + 1

def fonction3():
        global a
        a = a + 1

# Création des threads
thread1 = threading.Thread(target=fonction1)
thread2 = threading.Thread(target=fonction2)
thread3 = threading.Thread(target=fonction3)

# Démarrage des threads
thread1.start()
thread2.start()
thread3.start()

# Attente de la fin des threads
thread1.join()
thread2.join()
thread3.join()

print(a)

'''''''''''''''
    # ***************************frame[1][1]***********************************************
    for row in range(3):
        for column in range(3):
            b = random.choice(nbr_list)
            row2.append(b)
            for i in range(len(row2)):
                if row1[i] == row2[i]:
                    row2.remove(b)
                    b = random.choice(nbr_list)
                    row2.append(b)
            btn1_1[row][column]["text"] = b
            nbr_list.remove(b)
    nbr_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#**********************ligne 1***************************
    for i in range(3):
        if row1[0] == row2[i]:
            rl1 = btn1_1[0][i]["text"]
            btn1_1[0][i]["text"] = btn1_1[2][i]["text"]
            btn1_1[2][i]["text"]= rl1
        elif row1[1] == row2[i] :
            rl1 = btn1_1[0][i]["text"]
            btn1_1[0][i]["text"] = btn1_1[2][i]["text"]
            btn1_1[2][i]["text"]= rl1
        elif row1[2] == row2[i]:
            rl1 = btn1_1[0][i]["text"]
            btn1_1[0][i]["text"] = btn1_1[2][i]["text"]
            btn1_1[2][i]["text"]= rl1
    # **********************ligne 2***************************
    if row1[3] == row2[3] or row1[4] == row2[3] or row1[5] == row2[3]:
        print(row2[3])
        btn1_1[1][0]["text"] = ""
    elif row1[3] == row2[4] or row1[4] == row2[4] or row1[5] == row2[4]:
        print(row2[4])
        btn1_1[1][1]["text"] = ""
    elif row1[3] == row2[5] or row1[4] == row2[5] or row1[5] == row2[5]:
        print(row2[5])
        btn1_1[1][2]["text"] = ""

        # **********************ligne 3***************************
    if row1[6] == row2[6] or row1[7] == row2[6] or row1[8] == row2[6]:
        print(row2[3])
        btn1_1[2][0]["text"] = ""
    elif row1[6] == row2[7] or row1[7] == row2[7] or row1[8] == row2[7]:
        print(row2[4])
        btn1_1[2][1]["text"] = ""
    elif row1[6] == row2[8] or row1[7] == row2[8] or row1[8] == row2[8]:
        print(row2[5])
        btn1_1[2][2]["text"] = ""

    nbr_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # ***************************************************************
    # ***************************frame[1][2]***********************************************
    for row in range(3):
        for column in range(3):
            b = random.choice(nbr_list)
            row3.append(b)
            for i in range(len(row3)):
                if row1[i] == row3[i]:
                    row3.remove(b)
                    b = random.choice(nbr_list)
                    row3.append(b)
            btn2[row][column]["text"] = b
            nbr_list.remove(b)
    nbr_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # **********************ligne 1***************************
    if row1[0] == row3[0] or row1[3] == row3[0] or row1[6] == row3[0]:
            print(row3[0])
            btn2[0][0]["text"] = ""
    elif row1[0] == row3[3] or row1[3] == row3[3] or row1[6] == row3[3]:
            print(row3[3])
            btn2[1][0]["text"] = ""
    elif row1[0] == row3[6] or row1[3] == row3[6] or row1[6] == row3[6]:
            print(row3[6])
            btn2[2][0]["text"] = ""
    nbr_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # ***************************************************************
'''''''''''
