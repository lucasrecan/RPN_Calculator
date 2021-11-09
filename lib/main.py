"""
@author : lucas, le 07/12/2020, en python 3.8.2
"""
#Chargement du module tkinter
from tkinter import *
from tkinter import font
from tkinter import messagebox
from tkinter import Toplevel
from tkinter import Image
#from tkinter import filedialog

import math
from math import *

from stack import la_pile
from queue import la_file
#Pour trouver le chemin de l'image logo_hp.ico, qui doit rester dans le dossier du fichier python
import os,sys
chemin=os.path.dirname(sys.argv[0])

#----------Liste----------#
liste_init=["$","$","$","$"]
liste_file=["*","*","*","*","*","*","*","*"]

#Indicateur pour les fenêtres Toplevel d'aide (?) et skins
skin_open=False
aide_open=False

#LIGNES 28 A 995 : CALCULATRICE EN PILE
#LIGNES 997 A 1114 : LA FILE
#LIGNES 1117 A 1128 : PREMIERE FENETRE DE CHOIX

def main_win():
    fen_choix=Tk()
    fen_choix.geometry("500x350")
    fen_choix.title("Choix entre pile et file")
    titre=Label(fen_choix,text="Choisissez entre la calculatrice HP48 en pile et la file",background="#32394B")
    titre.place(relx=0.5, rely=0.4, anchor=CENTER)
    #print("logo_hp.ico")
    fen_choix.iconbitmap(f"{chemin}/logo_hp.ico")

    fen_choix.configure(background="#32394B")
    bouton_pile = Button(fen_choix, text="HP48",width=5, relief=GROOVE, bg="GREY", command=lambda x="": la_pile(fen_choix))
    bouton_pile.place(relx=0.4,rely=0.5,anchor=CENTER)
    bouton_file = Button(fen_choix, text="FILE",width=5, relief=GROOVE, bg="GREY", command=lambda x="": la_file(fen_choix))
    bouton_file.place(relx=0.6,rely=0.5,anchor=CENTER)
    fen_choix.mainloop()


if __name__ =='__main__':
    main_win()