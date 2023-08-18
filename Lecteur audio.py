import time
from tkinter import *
import tkinter
from tkinter import filedialog
import os
import fnmatch

import pygame.mixer
from pygame import mixer

canvas = tkinter.Tk()
canvas.title("Byron player")
canvas.geometry("600x500")
canvas.configure(bg="white")
pygame.init()
pygame.mixer.init()

rootpath = "C:/Users/RAY/Desktop/azerty/son/nouveau dossier"

#rootpath.replace("/","\\")
#print(rootpath)


def ouvrir():
    label.config(text=listbox.get('anchor'))
    mixer.music.load(rootpath+"\\"+listbox.get('anchor'))
    listbox.insert(END, rootpath)
    mixer.music.play()
    slider.config()
    barre.config(command=listbox.yview)


def lecture():
    pygame.mixer.music.play()

def pause():
    if pause_button["text"] == "pause":
        mixer.music.pause()
        pause_button["text"] = "play"
    else:
        pygame.mixer.music.unpause()
        pause_button["text"] = "pause"
compteur = 0
def suiv():
    next_song = listbox.curselection()
    next_song = next_song[compteur]+1
    next_song_name = listbox.get(next_song)
    label.config(text=next_song_name)
    mixer.music.load(rootpath+"\\"+next_song_name)
    mixer.music.play()
    listbox.select_clear(0,'end')
    listbox.activate(next_song)
    listbox.select_set(next_song)



def prec():
    prec_song = listbox.curselection()
    prec_song = prec_song[compteur]-1
    prec_song_name = listbox.get(prec_song)
    label.config(text=prec_song_name)
    mixer.music.load(rootpath + "\\" + prec_song_name)
    mixer.music.play()
    listbox.select_clear(-1,'end')
    listbox.activate(prec_song)
    listbox.select_set(prec_song)


def volume():
    canvas.after(100,volume)
    vol1 = volume_button.get()
    mixer.music.set_volume(vol1*.100)


def fermer():
    mixer.music.stop()
    listbox.select_clear('active')

def sliders(x):
    pass

barre = Scrollbar(canvas,bd=2,bg="orange")
barre.pack(side=RIGHT,fill=Y)

listbox = tkinter.Listbox(canvas,fg='cyan',bg="black",width=100,font=("poppin",14))
listbox.pack(padx=15,pady=15)

with os.scandir(rootpath) as fichiers:
    for fichier in fichiers:
        if fichier.is_file() and (fichier.name.endswith(".mp3") or fichier.name.endswith(".wav")):
            listbox.insert(tkinter.END,fichier.name)



label = tkinter.Label(canvas,text="",bg="white",fg='black',font=("poppin",14))
label.pack(pady=15)

value = tkinter.DoubleVar()
slider = tkinter.Scale(canvas, from_=0, to=100, variable=value,orient=HORIZONTAL,command=sliders,length=520)
slider.pack()


frame = tkinter.Frame(canvas,bg='white')
frame.pack(padx=10,pady=5,anchor='center')

pre_button = tkinter.Button(canvas,text="Preview",font=("centurygotic",12),command=prec,width=10)
pre_button.pack(pady=15,in_=frame,side=LEFT)
stop_button = tkinter.Button(canvas,text="Stop",font=("centurygotic",12),command=fermer,width=10)
stop_button.pack(pady=15,in_=frame,side=LEFT)
open_button = tkinter.Button(canvas,text="Play",font=("centurygotic",12),command=ouvrir,width=10)
open_button.pack(pady=15,in_=frame,side=LEFT)
pause_button = tkinter.Button(canvas,text="pause",font=("centurygotic",12),command=pause,width=10)
pause_button.pack(pady=15,in_=frame,side=LEFT)
next_button = tkinter.Button(canvas,text="Next",font=("centurygotic",12),command=suiv,width=10)
next_button.pack(pady=15,in_=frame,side=LEFT)

volume_button = tkinter.Button(canvas,text="Volume",font=("centurygotic",12),command=volume,width=10)
volume_button.pack(side=LEFT)



canvas.mainloop()