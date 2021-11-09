#Chargement du module tkinter
from tkinter import *
from tkinter import font
from tkinter import messagebox
from tkinter import Toplevel
from tkinter import Image
#from tkinter import filedialog

import math
from math import *

#Pour trouver le chemin de l'image logo_hp.ico, qui doit rester dans le dossier du fichier python
import os,sys
chemin=os.path.dirname(sys.argv[0])

#----------Liste----------#
liste_init=["$","$","$","$"]
liste_file=["*","*","*","*","*","*","*","*"]

#Indicateur pour les fenêtres Toplevel d'aide (?) et skins
skin_open=False
aide_open=False


def win_queue(fen_choix):
    fen_choix.destroy()

    def show_file():
        texte['state']=NORMAL
        texte.delete("0.0",END)
        texte.insert(END,f"Nombre d'éléments : {liste_file[0]}\n")
        texte.insert(END,f"Indice du premier élement : {liste_file[1]}\n")
        texte.insert(END,f"indice de la première case vide : {liste_file[2]}\n\n")
        texte.insert(END,"File : \n")
        for i in range(3,8):
            texte.insert(END,"|")
            if liste_file[i]=="*":
                texte.insert(END," ")
            else:
                texte.insert(END,liste_file[i])
            if i==7:
                texte.insert(END,"|")
        texte.insert(END,"\n\n\n File complète : \n[")
        for i in range(8):
            if not i==7:
                texte.insert(END,f"{liste_file[i]},")
            else:
                texte.insert(END,f"{liste_file[i]}]")
        texte['state']=DISABLED
        

    def fct_file():
        #Nombre d'élements :
        liste_file[0]=len(liste_file)-liste_file.count("*")-3
        #Indice du premier élement :
        if not file_empty(liste_file):
            for i in range(3,8):
                if liste_file[i]!="*":
                    liste_file[1]=i
                    break
        else:
            liste_file[1]=3
        #Indice du premier élement vide :
        for i in range(3,8):
            if liste_file[i]=="*":
                liste_file[2]=i
                break
            else:
                liste_file[2]="*"
        show_file()

    def file_empty(liste):
        empty=True
        for i in range(3,8):
            if liste[i]=="*":
                empty=True
            else:
                empty=False
                break
        return empty

    def file_full(liste):
        full=False
        for i in range(-1, -6, -1):
            if liste[i]=="*":
                full=False
                break
            else:
                full=True
        return full

    def enqueue():
        if saisie.get():
            nouveau=saisie.get()
            saisie.delete("0",END)
            if not file_full(liste_file):
                for i in range (first(),8):
                    if liste_file[i]=="*":
                        liste_file[i]=nouveau
                        break
        fct_file()

    def enqueue_clavier(elem):
        if saisie.get():
            nouveau=saisie.get()
            saisie.delete("0",END)
            if not file_full(liste_file):
                for i in range (first(),8):
                    if liste_file[i]=="*":
                        liste_file[i]=nouveau
                        break
        fct_file()
    def first():
        return liste_file[1]

    def dequeue():
        liste_file[first()]="*"
        fct_file()

    fen_file=Tk()
    fen_file.title("File")
    fen_file.iconbitmap(f"{chemin}/../assets/logo_hp.ico")
    fen_file.configure(background="#32394B")
    fen_file.iconbitmap(f"{chemin}/logo_hp.ico")
    texte= Text(fen_file,width = 35, height = 10,background="#BDC2A4", selectbackground="#BDC2A4", selectforeground="black")
    texte.grid(row=0,column=0,columnspan=6)
    saisie=Entry(fen_file,width = 15,background="#BDC2A4")
    saisie.grid(row=1,column=0, columnspan=5)
    fct_file()
    fct_file()

    bouton_enqueue = Button(fen_file,text="enqueue", relief=GROOVE, command=lambda x="": enqueue())
    bouton_enqueue.grid(row=2,column=0)

    bouton_dequeue = Button(fen_file,text="dequeue", relief=GROOVE, command=lambda x="": dequeue())
    bouton_dequeue.grid(row=2,column=1)

    def quitter():                                                      #Afficher le message d'erreur avec de quitter
        reponse=messagebox.askokcancel("Quitter", "Etes-vous sûr de vouloir quitter ?")
        if reponse:
            fen_file.destroy()

    bouton_quitter = Button(fen_file,text="Quitter", relief=GROOVE, command=lambda x="": quitter())
    bouton_quitter.grid(row=2,column=2)
    fen_file.bind('<Return>',enqueue_clavier) #Entrée normale
    fen_file.bind('<KP_Enter>',enqueue_clavier) #Entrée sur le pavé numérique

    fen_file.mainloop()



if __name__ == '__main__':
    fen_choix = Tk()
    win_queue(fen_choix)