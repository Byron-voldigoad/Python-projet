'''''''''
import sqlite3
from random import *

conn = sqlite3.connect("mydb.db")
cur = conn.cursor()

req = "select * from students"
resulte = cur.execute(req)
i = 0
for row in resulte:
    for a in range(randint(1,2)):
        print(row[1])

from tkinter import *
import time

root = Tk()
root.geometry("200x50")

label = Label(root,text='BYRON',font=("century",20))
label.pack(side=LEFT)
a = label.winfo_x()
print(label.winfo_x())
while True:
    if (a ==0):
        label.place(x=label.winfo_x()-1)
        root.update()
        time.sleep(0.05)
        print(label.winfo_x())
    if (label.winfo_x() == -100):
        while True:
            label.place(x=label.winfo_x() + 1)
            root.update()
            time.sleep(0.05)
            print(label.winfo_x())
            a = 1
            if (label.winfo_x() == 100):
                a = 0
                break

import time

start_time = time.time()
a = 0
while a != 10:
    current_time = time.time()
    elapsed_time = current_time - start_time
    minutes = int(elapsed_time / 60)
    seconds = int(elapsed_time % 60)
    milliseconds = int((elapsed_time - seconds) * 1000)
    print(f"{minutes:02d}:{seconds:02d}:{milliseconds:03d}", end="\n")
    time.sleep(0.001)
    a += 1
    
def triangle(n):
    for i in range(1,n+1):
        print(" " * (n - i) + " *" * (i))
print("\t +")
triangle(5)

from random import shuffle

anime = ["A","B","C","CH","D","DD","E","F","G","H","K","M","O","T","Y"]
print(anime)
nb_lig = 5
nb_col = 6
nb_carte = nb_col*nb_lig//2
print(nb_carte)
cartes = list(range(nb_carte))*2
print(cartes)

shuffle(cartes)
print(cartes)

plateau =[]
k = 0
for lig in range(nb_lig):
    l = []
    for col in range(nb_col):
        l.append(cartes[k])
        k = k + 1
    plateau.append(l)

print()
print(plateau)
print()



for lig in range(nb_lig):
    for col in range(nb_col):
        nro = plateau[lig][col]
        lang = anime[nro]
        print(lang, end=" ")
    print()
    print()
'''''

import time

start_time = time.time()

while True:
    current_time = time.time()
    elapsed_time = current_time - start_time
    minutes = int(elapsed_time / 60)
    seconds = int(elapsed_time % 60)
    milliseconds = int((elapsed_time - seconds) * 1000)
    print(f"{minutes:02d}:{seconds:02d}:{milliseconds:03d}", end="")
    print()
    time.sleep(0.001)