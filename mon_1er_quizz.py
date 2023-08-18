import sqlite3
from random import *
from tkinter import *


def questionnaire():
    conn = sqlite3.connect("questionnaire.db")
    cur = conn.cursor()
    req = "select*from quere"
    result = cur.execute(req)

    for row in result:
        label_questions.configure(text=row[1])

def result():
    conn = sqlite3.connect("questionnaire.db")
    cur = conn.cursor()
    req = "select*from quere"
    result = cur.execute(req)
    for row in result:
        label_questions.configure(text=row[1])
    a = 0
    r = result_entry.get()
    r = r.lower()
    if (r == row[2]):
        a += 1
    print("votre score est de ", a)

window = Tk()
window.config(bg="orange")
window.title("Quizz")
window.geometry("500x500")

label_questions = Label(window,text="moi")
label_questions.pack()
start_button = Button(window,command=questionnaire,text="suivant")
start_button.pack()
result_entry = Entry(window)
result_entry.pack()
next_button = Button(window,command=result,text="suivant")
next_button.pack()

'''''
update quere set reponses = 'city hunter' where id='4'
'''''
'''''

req = "select*from quere"
a = 0
result = cur.execute(req)

for row in result:
    print(row[0], row[1])
    r = str(input(""))
    r = r.lower()
    if (r == row[2]):
        a += 1
print("votre score est de ",a)


'''''
window.mainloop()
