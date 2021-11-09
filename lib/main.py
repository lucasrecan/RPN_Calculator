#Loading the tkinter library
from tkinter import *
from tkinter import Toplevel
from tkinter import Image

#Loading the math library
from math import *

#Loading the stack and the queue from the other files
from stack import win_stack
from queue import win_queue

# The two following lines are for finding the icon for the windows
import os,sys
chemin=os.path.dirname(sys.argv[0])

# Initialization of the list for the stack and the queue
liste_init=["$","$","$","$"]
liste_file=["*","*","*","*","*","*","*","*"]

# Booleans to control if the windows for choosing skin and getting help are open or not
skin_open=False
aide_open=False

def main_win():
    fen_choix = Tk()
    fen_choix.geometry("500x350")
    fen_choix.title("Choix entre pile et file")
    titre = Label(fen_choix,text="Choisissez entre la calculatrice HP48 en pile et la file",background="#32394B")
    titre.place(relx=0.5, rely=0.4, anchor=CENTER)
    fen_choix.iconbitmap(f"{chemin}/../assets/logo_hp.ico")

    fen_choix.configure(background="#32394B")
    bouton_pile = Button(fen_choix, text="HP48",width=5, relief=GROOVE, bg="GREY", command=lambda x="": win_stack(fen_choix))
    bouton_pile.place(relx=0.4,rely=0.5,anchor=CENTER)
    bouton_file = Button(fen_choix, text="FILE",width=5, relief=GROOVE, bg="GREY", command=lambda x="": win_queue(fen_choix))
    bouton_file.place(relx=0.6,rely=0.5,anchor=CENTER)
    fen_choix.mainloop()


if __name__ =='__main__':
    main_win()