from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from math import *
import matplotlib.pyplot as plt
import  numpy as np

#******variables pour le discrete***********************************
M = 0
M1 = 0
i = 1
fi = 1
f = []
data = []
datav = []
datav2 = []
datav2a = []
data2 = []
data3 = []
data4 = []
dataf1 = []
dataf2 = []

#******************************************************************
#***************variable pour les continues************************

Mc = 0
Mc1 = 0
ic = 1
fic = 1
fc= []
datac = []
datacv = []
datacvcv = []
datacv2 = []
datacv2a = []
datac2 = []
datac3 = []
datac4 = []
datacf1 = []
datacf2 = []
datacci = []
datacai = []
datacdi = []
x = []
y = []

def reset():
    global M ,M1,i,fi,f,data,datav,datav2,datav2a,data2,data3,data4,dataf1,dataf2,Mc,Mc1,ic,fic,fc,datac,datacv,datacvcv,datacv2,datacv2a,datac2,datac3,datac4,datacf1,datacf2,datacci,datacai,datacdi,x,y,data,datav,datav2,datav2a,data2,data3,data4,dataf1,dataf2
    i_entry2.delete(0,END)
    i_entry.delete(0,END)
    i_entryc.delete(0,END)
    i_entryc2.delete(0,END)
    M = 0
    M1 = 0
    i = 1
    fi = 1
    f = []
    data = []
    datav = []
    datav2 = []
    datav2a = []
    data2 = []
    data3 = []
    data4 = []
    dataf1 = []
    dataf2 = []
    Mc = 0
    Mc1 = 0
    ic = 1
    fic = 1
    fc = []
    datac = []
    datacv = []
    datacvcv = []
    datacv2 = []
    datacv2a = []
    datac2 = []
    datac3 = []
    datac4 = []
    datacf1 = []
    datacf2 = []
    datacci = []
    datacai = []
    datacdi = []
    x = []
    y = []
    data = []
    datav = []
    datav2 = []
    datav2a = []
    data2 = []
    data3 = []
    data4 = []
    dataf1 = []
    dataf2 = []

    # ******************************************************************
    for item in table.get_children():
        table.delete(item)
    for item in table2.get_children():
        table2.delete(item)
    for item in table3.get_children():
        table3.delete(item)
#*************************************************************************************************************************************

def quantitative_discrete():
    global M1, i
    try:
        table.insert("", 0, values=(i_entry.get(), i_entry2.get(), ""))
        M1 = M1 + int(i_entry2.get())
        i += 1
    except:
        messagebox.showerror("Erreur de charactere", "Vous devez entrer des valeurs numeriques")

def quantitative_continue():
    table.insert("", 0, values=(i_entryc.get(), i_entryc2.get(), ""))

def calcul_qc():
    global Mc1, ic, f, Mc
    fh = ["1,2,5,4,8"]
    # ******stocke les effectifs et variable dans des tableaux*************
    for itemc in table.get_children():
        val_col1 = table.item(itemc, "values")[1]
        val_col11 = table.item(itemc, "values")[0]
        datac.append(val_col1)
        datacv.append(val_col11)
        datacvcv.append(val_col11)
        table.delete(itemc)
        a = len(datac)
        av = len(datacv)
    for c in range(len(datacv)):
        datacvcv[c] = datacv[c].split("-")

    # ********************************************************************
    val_col3 = 0
    val_col4 = 0
    val_col11a1 = 0
    datacp = []
    datac2p = []
    # *********frequence*******ECC******et**********ECD****************
    for dp in range(len(datac) - 1, -1, -1):
        datacp.append(datac[dp])

    for i in datacp:
        val_col4 = val_col4 + int(i)
        datac4.append(val_col4)
    datac4.reverse()
    for i in datac:
        val_col2 = int(i) / a
        val_col2 = round(val_col2, 2)
        val_col3 = val_col3 + int(i)
        val_col3 = round(val_col3, 2)
        datac2.append(val_col2)
        datac3.append(val_col3)

    # **************************************************************************

    #** ** ** ** *FCC ** ** ** et ** ** ** ** ** FCD ** ** ** ** ** ** ** *

    for dp2 in range(len(datac2) - 1, -1, -1):
        datac2p.append(datac2[dp2])
    val_colf1 = 0
    val_colf2 = 0
    for i in datac2p:
        val_colf2 = round(val_colf2 + float(i), 2)
        datacf2.append(val_colf2)
    datacf2.reverse()
    for i in datac2:
        val_colf1 = round(val_colf1 + float(i), 2)
        datacf1.append(val_colf1)

    # ******************************************************************
    # **********ci****************ai**************di*****************
    nici = 0
    for i in range(len(datacvcv)):
        ci = float(float(datacvcv[i][0])+float(datacvcv[i][1]))/2
        ai = float(float(datacvcv[i][1]) - float(datacvcv[i][0]))
        nici = nici + (float(datac[i])*ci)
        nici2 = nici * ci
        datacci.append(ci)
        datacai.append(ai)
    for i in range(len(datac2)):
        di = float(float(datac2[i])/float(datacai[i]))
        di = round(di, 2)
        datacdi.append(di)
    # ******************************************************************
    # *****Mode**********************Mediane*************************
    cm = datacv[0]
    mni = datac[0]
    mni2 = datac[0]
    mni3 = datac[0]

    for i in range(len(datac)):
        if (datac[i] > mni) :
            mni = datac[i]
            cm = datacv[i]
            i = i+1
            mni2 = datac[i]
            i = i - 2
            mni3 = datac[i]

        elif (datac[0] < datac[-1]):
            mni = datac[-1]
            cm = datacv[-1]
            mni2 = 0
            i = i - 2
            mni3 = datac[i]
        elif (datac[0] > datac[-1]):
            mni = datac[0]
            cm = datacv[0]
            mni3 = 0
            mni2 = datac[1]

    mni2 = float(mni) - float(mni2)
    mni3 = float(mni) -float(mni3)
    cm2 = cm.split("-")
    mode1 = float(mni2)+float(mni3)
    mode2 =float(cm2[1])-float(cm2[0])
    mode3 = mode2/mode1
    mode = (float(cm2[1])+mni2*mode3)

    me2 = []
    me3 = []
    med = float(datacf2[0])/2
    for i in range(len(datacf2)):
        if (datacf2[i]<=med):
            me2.append(datacf2[i])
            me3.append(datacv[i])
    me4 = me3[0].split("-")
    med1 = (0.5-float(me2[1]))
    med2 = (float(me4[-1])-float(me4[0]))
    med3 = (float(me2[0])-float(me2[1]))
    med4 = (med1*med2)/med3
    mediane = float(me4[0]) + med4
    # ******************************************************************
    # ***Moyenne*********variance**********ecart type*********etendue********cv******************

    for i in range(len(datac)):
        Mc1= Mc1 + float(datac[i])
    Mc = nici/Mc1
    v = nici2/Mc1
    ec = sqrt(v)
    e = float(float(datacvcv[-1][1]) - float(datacvcv[0][0]))
    cv = ec/Mc
    # ******************************************************************
    #************ arondit a 2 chiffres apres la virgule****************
    Mc= round(Mc, 2)
    v = round(v, 2)
    ec = round(ec, 2)
    e = round(e, 2)
    cv = round(cv, 2)
    mode = round(mode, 2)
    mediane = round(mediane, 2)
    #**************************************************************
    # **********ajustement des treeview******************************
    entete3 = ["Variable (xi)", "Effectif (ni)", "Frequence (fi)", "ECC", "ECD", "FCC", "FCD", "ci", "ai","di"]
    table.configure(columns=(1, 2, 3, 4, 5, 6, 7, 8, 9,10))
    for ia in range(0, 10):
        table.heading(ia + 1, text=entete3[ia], anchor='center')

    for ai in range(1, 10):
        table.column(ai, anchor='center', width=200)
        table.place_configure(width=862)

    entete22 = ["Moyenne", "Variance", "Ecart type", "Etendue", "CV", "Mode", "Mediane", "Classe modale", "ni.xi²"]
    for ia in range(0, 8):
        table2.heading(ia + 1, text=entete22[ia], anchor='center')

    table3.configure(columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

    for ai in range(1, 11):
        table3.column(ai, anchor='center', width=200)
        table3.place_configure(width=862)
    # ******************************************************************
    ii = 0
    for row in (datac2):
        table.insert('', 0, values=(datacv[ii], datac[ii], row, datac4[ii], datac3[ii], datacf2[ii],datacf1[ii],datacci[ii],datacai[ii],datacdi[ii]))
        ii += 1

    table2.insert('', 0, values=(Mc,v,ec,e,cv,mode,mediane,cm))
    table3.insert('', 0, values=("Total", Mc1, datacf2[0], "///", "///","///", "///",))
#**********************************************************************************************************************************************
def calcul_qd():
    global M1, i, f,M
    M = M1 / (i - 1)
    count = 0
    #******stocke les effectifs et variable dans des tableaux*************
    for item in table.get_children():
        val_col1 = table.item(item, "values")[1]
        val_col11 = table.item(item, "values")[0]
        data.append(val_col1)
        datav.append(val_col11)
        table.delete(item)
    #***************************************************************
        a = len(data)
        av = len(datav)
    val_col3 = 0
    val_col4 = 0
    val_col11a1 = 0
    datap = []
    data2p = []
    # *********frequence*******ECC******et**********ECD***************
    for dp in range(len(data) - 1, -1, -1):
        datap.append(data[dp])

    for i in datap:
        val_col4 = val_col4 + int(i)
        data4.append(val_col4)
    data4.reverse()
    for i in data:
        val_col2 = int(i) / M1
        val_col2 = round(val_col2, 2)
        val_col3 = val_col3 + int(i)
        val_col3 = round(val_col3, 2)
        data2.append(val_col2)
        data3.append(val_col3)

    # ***************************************************
    # ***********FCC******et**********FCD***************

    for dp2 in range(len(data2) - 1, -1, -1):
        data2p.append(data2[dp2])
    val_colf1 = 0
    val_colf2 = 0
    for i in data2p:
        val_colf2 = round(val_colf2 + float(i), 2)
        dataf2.append(val_colf2)
    dataf2.reverse()
    for i in data2:
        val_colf1 = round(val_colf1 + float(i), 2)
        dataf1.append(val_colf1)

    #*********************************************************
    # *****************xi*ni********xi²*ni**************************
    ni = 0
    xi = 0
    for i in datav:
        val_colf11 = float(data[count]) * float(i)
        val_colf11a = float(data[count]) * float(i) * float(i)
        ni = ni = val_colf11
        xi = xi = val_colf11a
        datav2.append(val_colf11)
        datav2a.append(val_colf11a)
        count += 1

    for i in datav2a:
        val_col11a1 = val_col11a1 + float(i)
    val_col11a1 = val_col11a1 / a
    val_col11a1 = val_col11a1 - M
    val_col11a1e = sqrt(val_col11a1)
    e = float(datav[0]) - float(datav[-1])
    cv = val_col11a1e / M
    # ***************************************************

    #************ arondit a 2 chiffres apres la virgule****************
    M = round(M, 2)
    val_col11a1 = round(val_col11a1, 2)
    val_col11a1e = round(val_col11a1e, 2)
    e = round(e, 2)
    cv = round(cv, 2)
    #**************************************************************
    #*************Mediane et mode*********************************
    c = []
    for i in range(len(datav)):
        for j in range(int(data[i])):
            c.append(datav[i])
    c.sort()
    a2 = len(c)
    med = a2%2
    if med == 1:
        a2 = a2+1
        n = a2 / 2
        mediane = c[int(n - 1)]
    else:
        n1 = a2 / 2
        n2 = a2/2 +1
        d1 = int(c[int(n1-1)])
        d2 = int(c[int(n2-1)])
        mediane = (d1+d2)/2

    mode = data[0]
    for i in range(len(data)):
        if data[i] > mode :
            mode = data[i]
            i += 1
        else:
            i += 1
    #****************************************************************

    table2.insert('', 0, values=(M, val_col11a1, val_col11a1e, e, cv,mode,mediane))
    ii = 0
    for row in (data2):
        table.insert('', 0, values=(datav[ii], data[ii], row, data4[ii], data3[ii], dataf2[ii], dataf1[ii], datav2[ii], datav2a[ii]))
        ii += 1

    table3.insert('', 0, values=("Total", M1, dataf2[0], "////", "////", "////", "////", ni, xi))
    x = np.array(data)
    y = np.array(datav)

def g():
    x = np.array(data)
    y = np.array(datav)
    x.sort()
    y.sort()
    plt.bar(x,y)
    plt.plot(x, y, color='green', lw = 3)
    plt.title("Polygone des effectif et diagrame en baton")
    plt.xlabel("ni")
    plt.ylabel('xi')
    plt.show()
    plt.close()

xdata = []

def g_c():
    for i in range(len((datacvcv))):
        print(datacvcv[i][1])
        xdata.append(datacvcv[i][0])
    x = np.array(xdata)
    y = np.array(datacv)
    x.sort()
    y.sort()
    plt.hist(x, bins=5)
    plt.title("Histogramme")
    plt.xlabel("ni")
    plt.ylabel('xi')
    plt.show()
    plt.close()

#********************************************************************************************************************************************************
fen = Tk()
fen.geometry("880x660")
fen.configure(background='gray')


#*******************Variable quantitative discrète**********************************************************
frame_qd = Frame(fen,background='darkgray',width=350,height=115)
frame_qd.place(x=10,y=2)

label_qd = Label(frame_qd,text="Variable quantitative discrète",background='darkgray',font=("century", 15))
label_qd.place(x=30,y=0)

i_entry = Entry(frame_qd, width=30)
i_entry.place(x=150, y=30)
lb_entry = Label(frame_qd,text='xi',background='darkgray')
lb_entry.place(x=130, y=30)

i_entry2 = Entry(frame_qd, width=30)
i_entry2.place(x=150, y=70)
lb_entry2 = Label(frame_qd,text='ni',background='darkgray')
lb_entry2.place(x=130, y=70)

btn2 = Button(frame_qd, text="Ajout d'effectifs", command=quantitative_discrete)
btn2.place(x=30, y=50)

btn4 = Button(frame_qd, text="Calcul", command=calcul_qd)
btn4.place(x=30, y=90)

btng = Button(frame_qd,text="courbe", command=g)
btng.place(x=90, y=90)

#*******************Variable quantitative continue*******************************************************
frame_qc = Frame(fen,background='darkgray',width=350,height=115)
frame_qc.place(x=520,y=2)

label_qc = Label(frame_qc,text="Variable quantitative continue",background='darkgray',font=("century", 15))
label_qc.place(x=30,y=0)

i_entryc = Entry(frame_qc, width=30)
i_entryc.place(x=150, y=30)
lb_entryc = Label(frame_qc,text='xi',background='darkgray')
lb_entryc.place(x=130, y=30)

i_entryc2 = Entry(frame_qc, width=30)
i_entryc2.place(x=150, y=70)
lb_entryc = Label(frame_qc,text='ni',background='darkgray')
lb_entryc.place(x=130, y=70)

btnc2 = Button(frame_qc, text="Ajout d'effectifs", command=quantitative_continue)
btnc2.place(x=30, y=50)

btnc4 = Button(frame_qc, text="Calcul", command=lambda :calcul_qc())
btnc4.place(x=30, y=90)

btng = Button(frame_qc,text="courbe", command=g_c)
btng.place(x=90, y=90)
btng.config(activebackground="blue")

#***************treeview***************************************************************************
table3 = ttk.Treeview(fen, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9), height=1)
table3.place(x=10, y=483)

table = ttk.Treeview(fen, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9), height=18, show='headings')
table.place(x=10, y=120)

entete = ["Variable (xi)", "Effectif (ni)", "Frequence (fi)", "ECC", "ECD", "FCC", "FCD", "ni.xi", "ni.xi²"]
for ia in range(0, 9):
    table.heading(ia + 1, text=entete[ia], anchor='center')

table.column(1, anchor='center', width=80)
table.column(2, anchor='center', width=80)
for ai in range(3, 10):
    table.column(ai, anchor='center', width=100)

table2 = ttk.Treeview(fen, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9), height=1, show='headings')
table2.place(x=10, y=560)

entete2 = ["Moyenne", "Variance", "Ecart type", "Etendue", "CV", "Mode", "Mediane", "Classe modale", "ni.xi²"]
for ia in range(0, 7):
    table2.heading(ia + 1, text=entete2[ia], anchor='center')
for ai in range(1, 10):
    table2.column(ai, anchor='center', width=95)


table3.column("#0", anchor='center', width=0,stretch=NO)
table3.column(1, anchor='center', width=80)
table3.column(2, anchor='center', width=80)
for ai in range(3, 10):
    table3.column(ai, anchor='center', width=100)


reset_btn = Button(fen,text='Reset',background='darkgray',command=reset)
reset_btn.pack(pady=10)
'''''''''
table.bindtags((str(table), "ttk", "all"))
table.bind_class("Treeview", "<Button-1>", lambda event : "break")
'''''''''

fen.mainloop()
