import datetime
import time
from timeit import *
from tkinter import *

def updatetime():
    now = default_timer() - start
    minutes,seconds = divmod(now,60)
    hours, minutes = divmod(minutes, 60)
    str_time = "%d:%02d:%02d" % (hours,minutes,seconds)
    canvas.itemconfigure(text_clock,text=str_time)
    window.after(1000, updatetime)


def pause():
    pass



window = Tk()
window.title("Chronometre")
window.geometry("360x240")
window.config(background="blue")



start_btn = Button(window,font=("courier",20),width="6",text="lancer",command=updatetime).place(x="15",y="100")
end_btn = Button(window,font=("courier",20),width="6",text="quiter",command=window.destroy).place(x="250",y="100")
pause_btn = Button(window,font=("courier",20),width="6",text="pause",command=pause).place(x="130",y="100")

canvas = Canvas(window,width=180,height=50)
canvas.place(x="80",y="12")

start = default_timer()
text_clock = canvas.create_text(100,20)


window.mainloop()