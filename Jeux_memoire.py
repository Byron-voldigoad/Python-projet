from tkinter import*
from random import*
from tkinter import messagebox


anime = ["B","C","CH","DD","E","HC","HE","MU","O","ST","T","Y"]
nb_lig = 4
nb_col = 6
nb_carte = nb_col*nb_lig//2


def melange_grille():
    cartes = list(range(nb_carte)) * 2
    shuffle(cartes)

    p = []
    k = 0
    for lig in range(nb_lig):
        l = []
        for col in range(nb_col):
            l.append(cartes[k])
            k = k + 1
        p.append(l)

    return p


larg = 1000
haut = 700
cote = 150
pad = 10
side = cote+2*pad
couples = 0
xo = yo = side/2

def creer_logo():
    #liste des cartes
    logos = []

    for lang in anime:
        fichier = "image/"+ lang +".png"
        logo = PhotoImage(file=fichier).zoom(x=6, y=6).subsample(40)
        logos.append(logo)
    return logos


def remplire(plateau):
    id_covers = []
    #placement des images
    for ling in range(4):
        l=[]
        for col in range(6):
            center = (col*side+xo,ling*side+yo)
            i = plateau[ling][col]
            logo = logos[i]
            cnv.create_image(center, image=logo)
            id_cover = cnv.create_image(center, image=imageC)
            l.append(id_cover)

        id_covers.append(l)
    return id_covers


def clic(event):
    if move[1] is not None:
        return
    X, Y = (event.x, event.y)
    col = X//side
    ling = Y//side
    if plateau[ling][col] != -1:
        traiter_clic(ling,col)

def traiter_clic(ling, col):
    global cpt, couples

    item = id_covers[ling][col]
    cnv.delete(item)
    if move[0] is None:
        move[0] = (ling,col)
    else:
        if move[0] == (ling, col):
            return
        cpt = cpt+1
        comp["text"] = cpt
        move[1] = (ling, col)
        i, j = move[0]
        if plateau[i][j] == plateau[ling][col]:
            plateau[i][j] = plateau[ling][col] = -1
            move[0] = move[1] = None

            couples += 1
            if couples == nb_carte:
                messagebox.showinfo("Jeux terminer","Felicitation!!")

        else:
            cnv.after(400, cacher, i , j, ling, col)


def cacher(i, j, ling, col):
    center = (side * j+ xo, side * i + yo)
    id_covers[i][j] = cnv.create_image(center, image=imageC)
    center = (side * col + xo, side * ling + yo)
    id_covers[ling][col] = cnv.create_image(center, image=imageC)

    move[0] = move[1] = None

def init():
    global plateau, id_covers, move,cpt,couples
    plateau = melange_grille()
    id_covers = remplire(plateau)
    move = [None, None]
    cpt = 0
    comp['text']=0
    couples = 0


window = Tk()

window.title('Memoire')
imageC = PhotoImage(file="image/recto_carte.png").zoom(x=6, y=6).subsample(40)

center = (randrange(larg),randrange(haut))
cnv = Canvas(window, width=larg, height=haut, background='gray')
cnv.pack(padx=20, pady=10,side=LEFT)
logos = creer_logo()

btn= Button(window,font=("century",20),text="Nouveau",command=init)
btn.pack(padx=10,pady=10)
comp = Label(window,text=0,font=("courier 20 bold"))
comp.pack()
init()

cnv.bind("<Button>", clic)

window.mainloop()