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

def win_stack(fen_choix):
    #Destruction de la fenêtre de choix
    fen_choix.destroy()
    def show():
        """
            Fonction qui fait apparaître la liste dans le widget Text a_afficher
        """
        a_afficher["state"]= NORMAL
        nb=4
        result=[]
        a_afficher.delete("0.0",END)
        for element in liste_init:
            if element=="$":
                if nb==1:
                    result.append(f"{nb}:")  
                else:
                    result.append(f"{nb}: \n")  
            else:
                if nb==1:
                    result.append(f"{nb}: {element}")
                else:
                    result.append(f"{nb}: {element}\n")
            nb-=1
        for i in result:
            a_afficher.insert(END,i)
        a_afficher["state"]= DISABLED

    def empty():   
        """
            Fonction qui renvoie True si la liste est vide, False sinon.
                Entrée : liste_init
                Sortie : empty=True/False
        """
        empty=True
        for element in liste_init:
            if element=="$":
                empty=True
            else:
                empty=False
                break
        return empty
                
    def full():    
        """
            Fonction qui renvoie True si la liste est pleine, False sinon.
                Entrée : liste_init
                Sortie : full=True/False
        """
        full=False
        for element in liste_init:
            if element=="$":
                full=False
                break
            else:
                full=True
        return full

    def top():     
        """
            Fonction qui renvoie le dernier élement de la liste.
                Entrée : liste_init
                Sortie : liste_init[3]
        """
        return liste_init[3]

    def push(nouveau):
        """
            Fonction qui pousse les élements vers le haut et en rajoute un nouveau.
                Entrée : liste_init
                Sortie : liste_init
        """
        if not full():
            liste_init[0]=liste_init[1]
            liste_init[1]=liste_init[2]
            liste_init[2]=liste_init[3]
            liste_init[3]=nouveau
        else:
            entree.insert(END,nouveau)
            ajouter_erreur("The stack is full")

    def nv_elem(valeur):    #pour clavier
        """
            Fonction qui utilise la fonction push() pour rajouter un ou plusieurs nombres présents dans le widget entree de type Entry.
            Appelée en faisant entrer sur le clavier (entrer normal ou celui du pavé numérique).
                Entrée : liste_init et entree
                Sortie : liste_init et a_afficher mis à jour
        """
        vider_erreurs()
        try:
            if entree.get():
                nv=entree.get().split()
                entree.delete(0,END)
                i=0
                for e in nv:
                    nv[i]=float(e)
                    i+=1
                if len(nv)==1 and liste_init[3]=="$":
                    liste_init[3]=nv[0]
                else:
                    for elem in nv:
                        push(elem)
            else:
                ajouter_erreur("Too few arguments")
        except ValueError:
            ajouter_erreur("Not an int or a float")
        show()

    def nv_elem_pourbouton():    
        """
            Fonction qui utilise la fonction push() pour rajouter un ou plusieurs nombres présents dans le widget entree de type Entry.
            Appelée en faisant appuyant sur le bouton ENTER.
                Entrée : liste_init et entree
                Sortie : liste_init et a_afficher mis à jour
        """
        vider_erreurs()
        try:
            if entree.get():
                nv=entree.get().split()
                entree.delete(0,END)
                i=0
                for e in nv:
                    nv[i]=float(e)
                    i+=1
                if len(nv)==1 and liste_init[3]=="$":
                    liste_init[3]=nv[0]
                else:
                    for elem in nv:
                        push(elem)
            else:
                ajouter_erreur("Too few arguments")
        except ValueError:
            ajouter_erreur("Not an int or a float")
        show()

    def pop():     
        """
            Fonction qui supprime le dernier element et décale tout vers le bas
                Entrée : liste_init et entree
                Sortie : liste_init ou l'erreur "too few arguments"
        """
        vider_erreurs()
        if not empty():
            liste_init[3]=liste_init[2]
            liste_init[2]=liste_init[1]
            liste_init[1]=liste_init[0]
            liste_init[0]="$"
        else:
            ajouter_erreur("Too few arguments")
        show()

    def pop_pour_bouton():
        """
            Fonction qui supprime le dernier élément et décale tout vers le bas.
            Si il y a quelque chose dans le widget entree de type Entry, supprime en priorité le contenu de ce widget.
                Entrée : liste_init et entree
                Sortie : liste_init ou l'erreur "too few arguments"
        """
        vider_erreurs()
        if entree.get():
            a=entree.get()
            entree.delete("0",END)
            entree.insert(END,a[:-1])
        elif not empty():
            liste_init[3]=liste_init[2]
            liste_init[2]=liste_init[1]
            liste_init[1]=liste_init[0]
            liste_init[0]="$"
        else:
            ajouter_erreur("Too few arguments")
        show()

    def effacer():
        """
            Fonction qui supprime tous les éléments de la liste.
                Entrée : liste_init
        """
        vider_erreurs()
        if entree.get():
            entree.delete("0",END)
        if not empty():
            liste_init[0]="$"
            liste_init[1]="$"
            liste_init[2]="$"
            liste_init[3]="$"
        show()



    #----------Fonctions opérations----------#

    def plus():                                                    #fonction pour l'addition
        vider_erreurs()
        conver=False
        if not empty():
            a_additionner=top()
            if str(a_additionner)[0]=="#":
                base=a_additionner[-1]
                conver=True
                origine()
                a_additionner=top()
            pop()
            if entree.get():
                    try:
                        nv=float(entree.get())
                        entree.delete("0",END)
                        push(a_additionner+nv)
                        if conver:
                            traitement_base(base)
                    except ValueError:
                        push(a_additionner)
                        entree.delete("0",END)
                        ajouter_erreur("Not an int or a float")
            elif not empty():
                dernier=top()
                if str(dernier)[0]=="#":
                    base=dernier[-1]
                    conver=True
                    origine()
                    dernier=top()
                pop()
                push(dernier+a_additionner)
                if conver:
                    traitement_base(base)
            else:
                push(a_additionner)
                if conver:
                    traitement_base(base)
                ajouter_erreur("Too few arguments")
        else:
            ajouter_erreur("Too few arguments")
        show()

    def moins():                                                   #fonction pour la soustraction
        vider_erreurs()
        conver=False
        if not empty():
            a_soustraire=top()
            if str(a_soustraire)[0]=="#":
                base=a_soustraire[-1]
                conver=True
                origine()
                a_soustraire=top()
            pop()
            if entree.get():
                    try:
                        nv=float(entree.get())
                        entree.delete("0",END)
                        push(a_soustraire-nv)
                        if conver:
                            traitement_base(base)
                    except ValueError:
                        push(a_soustraire)
                        entree.delete("0",END)
                        ajouter_erreur("Not an int or a float")
            elif not empty():
                dernier=top()
                if str(dernier)[0]=="#":
                    base=dernier[-1]
                    conver=True
                    origine()
                    dernier=top()
                pop()
                push(dernier-a_soustraire)
                if conver:
                    traitement_base(base)
            else:
                push(a_soustraire)
                if conver:
                    traitement_base(base)
                ajouter_erreur("Too few arguments")
        else:
            ajouter_erreur("Too few arguments")
        show()

    def fois():                                                    #fonction pour la multiplication
        vider_erreurs()
        conver=False
        if not empty():
            a_multiplier=top()
            if str(a_multiplier)[0]=="#":
                base=a_multiplier[-1]
                conver=True
                origine()
                a_multiplier=top()
            pop()
            if entree.get():
                    try:
                        nv=float(entree.get())
                        entree.delete("0",END)
                        push(a_multiplier*nv)
                        if conver:
                            traitement_base(base)
                    except ValueError:
                        push(a_multiplier)
                        entree.delete("0",END)
                        ajouter_erreur("Not an int or a float")
            elif not empty():
                dernier=top()
                if str(dernier)[0]=="#":
                    base=dernier[-1]
                    conver=True
                    origine()
                    dernier=top()
                pop()
                push(dernier*a_multiplier)
                if conver:
                    traitement_base(base)
            else:
                push(a_multiplier)
                if conver:
                    traitement_base(base)
                ajouter_erreur("Too few arguments")
        else:
            ajouter_erreur("Too few arguments")
        show()

    def diviser():                                                  #fonction division
        vider_erreurs()
        conver=False
        if not empty():
            a_diviser=top()
            if str(a_diviser)[0]=="#":
                base=a_diviser[-1]
                conver=True
                origine()
                a_diviser=top()
            pop()
            if entree.get():
                    try:
                        nv=float(entree.get())
                        entree.delete("0",END)
                        push(a_diviser/nv)
                        if conver:
                            traitement_base(base)
                    except ValueError:
                        push(a_diviser)
                        entree.delete("0",END)
                        ajouter_erreur("Not an int or a float")
            elif not empty():
                dernier=top()
                if str(dernier)[0]=="#":
                    base=dernier[-1]
                    conver=True
                    origine()
                    dernier=top()
                pop()
                push(dernier/a_diviser)
                if conver:
                    traitement_base(base)
            else:
                push(a_diviser)
                if conver:
                    traitement_base(base)
                ajouter_erreur("Too few arguments")
        else:
            ajouter_erreur("Too few arguments")
        show()

    def carré():                                                     #fonction pour le carré
        vider_erreurs()
        try:
            if entree.get():
                try:
                    nv=float(entree.get())
                    entree.delete("0",END)
                    push(nv**2)
                except ValueError:
                    ajouter_erreur("Not an int or a float")
                    entree.delete("0",END)
            elif not empty():
                if str(top())[0]=="#":
                    ajouter_erreur("Bad argument type")
                else:
                    nv=top()
                    pop()
                    push(nv**2)
            else:
                ajouter_erreur("Too few arguments")
            show()
        except OverflowError:
            push(nv)
            show()
            ajouter_erreur("Overflow error")

    def fct_exp():                                                     #fonction pour l'exponentielle
        vider_erreurs()
        try:
            if entree.get():
                try:
                    nv=float(entree.get())
                    entree.delete("0",END)
                    push(math.e**nv)
                except ValueError:
                    ajouter_erreur("Not an int or a float")
                    entree.delete("0",END)
            elif not empty():
                if str(top())[0]=="#":
                    ajouter_erreur("Bad argument type")
                else:
                    nv=top()
                    pop()
                    push(math.e**nv)
            else:
                ajouter_erreur("Too few arguments")
            show()
        except OverflowError:
            push(nv)
            show()
            ajouter_erreur("Overflow error")
            
    def fct_log():                                                     #fonction pour le log
        vider_erreurs()
        if entree.get():
            try:
                nv=float(entree.get())
                if nv>0:
                    entree.delete("0",END)
                    push(math.log(nv,10))
                else:
                    ajouter_erreur("Math domain error")
            except ValueError:
                ajouter_erreur("Not an int or a float")
                entree.delete("0",END)
        elif not empty():
            if str(top())[0]=="#":
                    ajouter_erreur("Bad argument type")
            else:
                nv=top()
                if nv>0:
                    pop()
                    push(math.log(nv,10))
                else:
                    ajouter_erreur("Math domain error")
        else:
            ajouter_erreur("Too few arguments")
        show()

    def fct_pi():                                                     #Fonction pour insérer le chiffre pi
        vider_erreurs()
        if entree.get():
            try:
                nv=float(entree.get())
                push(nv)
                entree.delete("0",END)
            except ValueError:
                entree.delete("0",END)
        vider_erreurs()
        push(math.pi)
        show()

    def plusoumoins():                                                 #Fonction pour changer le signe
        vider_erreurs()
        if entree.get():
            try:
                nv=float(entree.get())
                entree.delete("0",END)
                entree.insert(END,-nv)
            except ValueError:
                ajouter_erreur("Not an int or a float")
                entree.delete("0",END)
        elif not empty():
            if str(top())[0]=="#":
                ajouter_erreur("Bad argument type")
            else:
                nv=top()
                pop()
                push(-nv)
        else:
            ajouter_erreur("Too few arguments")
        show()


    def swap():                                                        #Fonction du bouton swap
        vider_erreurs()
        if not empty():
            un=top()
            pop()
            if entree.get():
                try:
                    deux=float(entree.get())
                    entree.delete("0",END)
                    push(deux)
                    push(un)
                except ValueError:
                    push(un)
                    ajouter_erreur("Not an int or a float")
                    entree.delete("0", END)
            elif not empty():
                deux=top()
                pop()
                push(un)
                push(deux)
            else:
                push(un)
                ajouter_erreur("Too few arguments")
            show()
        else:
            ajouter_erreur("Too few arguments")

    def puissance():                                                   #Fonction du bouton puissance
        vider_erreurs()
        try:
            if not empty():
                if str(top())[0]=="#":
                    ajouter_erreur("Bad argument type")
                else:
                    exposant=top()
                    pop()
                if entree.get():
                        try:
                            nv=float(entree.get())
                            entree.delete("0",END)
                            push(nv**exposant)
                        except ValueError:
                            push(exposant)
                            entree.delete("0",END)
                            ajouter_erreur("Not an int or a float")
                        except OverflowError:
                            entree.insert(END,nv)
                            push(exposant)
                            ajouter_erreur("Overflow error")
                elif not empty():
                    if str(top())[0]=="#":
                        vider_erreurs()
                        ajouter_erreur("Bad argument type")
                    else:
                        nombre=top()
                        pop()
                        push(nombre**exposant)
                else:
                    push(exposant)
                    ajouter_erreur("Too few arguments")
            else:
                ajouter_erreur("Too few arguments")
        except OverflowError:
            push(nombre)
            push(exposant)
            ajouter_erreur("Overflow error")
        show()

    def racine_carrée():                                                  #Fonction du bouton racine carrée
        vider_erreurs()
        if entree.get():
            try:
                nv=float(entree.get())
                if nv>=0:
                    entree.delete("0",END)
                    push(sqrt(nv))
                else:
                    ajouter_erreur("Math domain error")
            except ValueError:
                ajouter_erreur("Not an int or a float")
                entree.delete("0",END)
        elif not empty():
            if str(top())[0]=="#":
                ajouter_erreur("Bad argument type")
            else:
                if top()>=0:
                    nv=top()
                    pop()
                    push(sqrt(nv))
                else:
                    ajouter_erreur("Math domain error")
        else:
            ajouter_erreur("Too few arguments")
        show()

    def fonction_inverse():                                             #Fonction pour le bouton de la fonction inverse
        vider_erreurs()
        if entree.get():
            try:
                nv=float(entree.get())
                if nv==0:
                    ajouter_erreur("Float division by zero")
                else:
                    entree.delete("0",END)
                    push(1/nv)
            except ValueError:
                ajouter_erreur("Not an int or a float")
                entree.delete("0",END)
        elif not empty():
            if str(top())[0]=="#":
                ajouter_erreur("Bad argument type")
            else:
                if top()==0:
                    ajouter_erreur("Float division by zero")
                else:
                    nv=top()
                    pop()
                    push(1/nv)
        else:
            ajouter_erreur("Too few arguments")
        show()

    def fctcos_sin_tan_atan(op):                                                      #Fonction du bouton cosinus, sinus, tan et atan
        vider_erreurs()
        if entree.get():
            try:
                nv=float(entree.get())
                entree.delete("0",END)
                push(op(nv))
            except ValueError:
                ajouter_erreur("Not an int or a float")
                entree.delete("0",END)
        elif not empty():
            if str(top())[0]=="#":
                ajouter_erreur("Bad argument type")
            else:
                nv=top()
                pop()
                push(op(nv))
        else:
            ajouter_erreur("Too few arguments")
        show()

    def fctacos_asin(op):                                                     #Fonction du bouton acosinus et asinus
        vider_erreurs()
        if entree.get():
            try:
                nv=float(entree.get())
                if nv<=1 and nv>=-1:
                    entree.delete("0",END)
                    push(op(nv))
                else:
                    ajouter_erreur("Math domain error")
            except ValueError:
                ajouter_erreur("Not an int or a float")
                entree.delete("0",END)
        elif not empty():
            if str(top())[0]=="#":
                ajouter_erreur("Bad argument type")
            else:
                if top()<=1 and top()>=-1:
                    nv=top()
                    pop()
                    push(op(nv))
                else:
                    ajouter_erreur("Math domain error")
        else:
            ajouter_erreur("Too few arguments")
        show()

    #-------------------Fonctions pour les conversions--------------------#
    def hexa():                                     #Fonction conversion en hexadécimal
        vider_erreurs()
        if not empty():
            nb=top()
            if isinstance(nb,str) and nb[0]=="#":
                base=nb[-1]
                nb=nb[2:]
                nb=nb[:-1]
                if base=="d":
                    nv=hex(int(float(nb)))
                elif base=="b":
                    nb="0b"+nb
                    nv=hex(int(nb,2))
                elif base=="o":
                    nb="0o"+nb
                    nv=hex(int(nb,8))
                elif base=="h":
                    nv=nb
                pop()
                if base!="h":
                    nv=nv[2:]
                push(f"# {nv.upper()}h")
        show()

    def dec():                                      #Fonction conversion en décimal
        vider_erreurs()
        if not empty():
            nb=top()
            if isinstance(nb,str) and nb[0]=="#":
                base=nb[-1]
                nb=nb[2:]
                nb=nb[:-1]
                if base=="h":
                    nb="0x"+nb
                    nv=int(int(nb,16))
                elif base=="d":
                    nv=nb
                elif base=="b":
                    nb="0b"+nb
                    nv=int(int(nb,2))
                elif base=="o":
                    nb="0o"+nb
                    nv=int(int(nb,8))
                pop()
                push(f"# {str(nv).upper()}d")
        show()

    def octal():                                    #Fonction conversion en octal
        vider_erreurs()
        if not empty():
            nb=top()
            if isinstance(nb,str) and nb[0]=="#":
                base=nb[-1]
                nb=nb[2:]
                nb=nb[:-1]
                if base=="h":
                    nb="0x"+nb
                    nv=oct(int(nb,16))
                elif base=="d":
                    nv=oct(int(float(nb)))
                elif base=="b":
                    nb="0b"+nb
                    nv=oct(int(nb,2))
                elif base=="o":
                    nv=nb
                pop()
                if base!="o":
                    nv=nv[2:]
                push(f"# {str(nv).upper()}o")
        show()

    def binaire():                                  #Fonction conversion en binaire
        vider_erreurs()
        if not empty():
            nb=top()
            if isinstance(nb,str) and nb[0]=="#":
                base=nb[-1]
                nb=nb[2:]
                nb=nb[:-1]
                if base=="h":
                    nb="0x"+nb
                    nv=bin(int(nb,16))
                elif base=="d":
                    nv=bin(int(float(nb)))
                elif base=="b":
                    nv=nb
                elif base=="o":
                    nb="0o"+nb
                    nv=bin(int(nb,8))
                pop()
                if base!="b":
                    nv=nv[2:]
                push(f"# {str(nv).upper()}b")
        show()

    def conversion():                               #Fonction qui donne la bonne syntaxe au nombre pour qu'il puisse être converti (avec un # devant)
        vider_erreurs()
        if entree.get():
            try:
                nv=float(entree.get())
            except ValueError:
                ajouter_erreur("Not an int or a float")
            entree.delete("0",END)
            if nv<0:
                push("# 0d")
            else:
                push(f"# {nv}d")
        elif not empty():
            nv=top()
            if str(nv)[0]!="#":
                pop()
                if nv<0:
                    push("# 0d")
                else:
                    push(f"# {nv}d")
        else:
            ajouter_erreur("Too few arguments")
        show()

    def origine():                                  #Fonction qui convertit le nombre en décimal et en float, donc comme d'origine
        vider_erreurs()
        try:
            if not empty():
                dec()
                nv=float(top().rstrip("d").lstrip("# "))
                pop()
                push(nv)
                show()
            else:
                ajouter_erreur("Too few arguments")
        except AttributeError:
            ajouter_erreur("Bad argument type")

    def traitement_base(base):                      #Fonction pour analyser la base d'un nombre et le reconvertir dans sa bonne forme (utilisée dans les opérations)
        if base=="h":
            conversion()
            hexa()
        elif base=="d":
            conversion()
        elif base=="b":
            conversion()
            binaire()
        elif base=="o":
            conversion()
            octal()

    #--------Chiffres et caractères pour l'interface--------#
    def caractères(caractère):
        vider_erreurs()
        entree.insert(END, caractère)

    #-------Gestion d'affichage des erreurs-------#
    def vider_erreurs():                                  
        """
            Fonction qui vide le bandeau où s'affiche les erreurs (affich_erreurs de type Entry)
        """
        affich_erreurs["state"]= NORMAL
        affich_erreurs.delete("0",END)
        affich_erreurs["state"]= DISABLED

    def ajouter_erreur(nouvelle):    
        """
            Fonction pour ajouter une nouvelle erreur dans le bandeau (affich_erreur de type Entry)
                Entrée : nouvelle erreur
        """
        affich_erreurs["state"]= NORMAL
        affich_erreurs.insert(END,nouvelle)
        affich_erreurs["state"]= DISABLED
    #--------------------------------------------#

    def quitter():                                                      #Afficher le message d'erreur avec de quitter
        reponse=messagebox.askokcancel("Quitter", "Etes-vous sûr de vouloir quitter ?")
        if reponse:
            fen.quit()

    #------------------Fenêtres------------------#
    #Initialisation :
    fen=Tk()
    fen.title("HP48")
    fen.configure(background="#32394B")
    fen.resizable(width=False, height=False)
    fontStyle = font.Font(family="Courier", size=15)
    fen.iconbitmap(f"{chemin}/../assets/logo_hp.ico")
    #Affichage des erreurs
    affich_erreurs=Entry(fen,width=23, textvariable="", state="disabled", font=fontStyle,disabledbackground="#BDC2A4", disabledforeground="black")
    affich_erreurs.grid(row=0, column=0, columnspan=6)

    #Ecran d'affichage
    a_afficher=Text(fen,width = 30, height = 4,background="#BDC2A4", font=fontStyle,selectbackground="#BDC2A4", selectforeground="black")
    a_afficher.grid(row=1,column=0,columnspan=6)

    #Zone de saisie
    entree=Entry(fen,width = 16,background="#BDC2A4", font=fontStyle)
    entree.grid(row=2,column=0, columnspan=5)

    #fonction pour afficher l'aide
    def fenêtre_aide():
        global aide_open
        if not aide_open:
            aide_open=True
            aide=Toplevel(fen)
            aide.title("Informations")
            texte=Text(aide,wrap='word', selectbackground="white", selectforeground="black")
            texte.pack()
            texte.insert(END, "-Calculatrice NPI se basant sur les calculatrices HP- \n \n Je me suis servi de l'application Droid48 pour avoir le même comportement qu'une calculatrice HP. \n\n Il est possible d'insérer des nombres, les puissances de 10 (avec e) et les espaces avec le clavier en cliquant sur la zone de saisie sous l'écran (les espaces permettent de mettre des nombres sur plusieurs étages de la pile, comme sur Droid48) \n\n Il est possible de faire les opérations de base (addition, soustraction, multiplication et division) avec des nombres convertis (en hexadécimal, octal, décimal ou binaire).")
            texte["state"]="disabled"
            aide.resizable(width=False, height=False)
            def is_closed():
                    global aide_open
                    aide_open=False
                    aide.destroy()
            aide.protocol("WM_DELETE_WINDOW", is_closed)

    #-----------------Boutons :-----------------#
    #Bouton +
    bouton_plus = Button(fen, text="+",  bg="#545B60",relief=GROOVE, height=2, width=5, command=lambda x="": plus())
    bouton_plus.grid(row=9, column=4)
    #Bouton -
    bouton_moins = Button(fen, text="-",  bg="#545B60",relief=GROOVE,height=2, width=5, command=lambda x="": moins())
    bouton_moins.grid(row=8, column=4)
    #Bouton *
    bouton_fois = Button(fen, text="*",  bg="#545B60",relief=GROOVE,height=2, width=5, command=lambda x="": fois())
    bouton_fois.grid(row=7, column=4)
    #Bouton ÷
    bouton_diviser = Button(fen, text="÷", bg="#545B60", relief=GROOVE,height=2, width=5, command=lambda x="": diviser())
    bouton_diviser.grid(row=6, column=4)
    #Bouton enlever
    bouton_enlever = Button(fen,text="←",relief=GROOVE,bg="#545B60",height=2, width=5, command=lambda x="": pop_pour_bouton())
    bouton_enlever.grid(row=5,column=5)
    #Bouton tout enlever
    bouton_del = Button(fen, text="drop", relief=GROOVE,bg="#545B60",height=2, width=5, command=lambda x="": effacer())
    bouton_del.grid(row=5, column=4)
    #Bouton pour changer le signe
    bouton_plusoumoins = Button(fen, text="+/-",relief=GROOVE,bg="#545B60",height=2, width=5, command=lambda x="": plusoumoins())
    bouton_plusoumoins.grid(row=2, column=0)
    #Bouton x²
    bouton_carré = Button(fen, text="x²",relief=GROOVE, bg="#545B60",height=2, width=5,command=lambda x="": carré())
    bouton_carré.grid(row=6, column=5)
    #Bouton exponentielle
    bouton_exp = Button(fen, text="e^x",relief=GROOVE,bg="#545B60",height=2, width=5, command=lambda x="": fct_exp())
    bouton_exp.grid(row=7, column=5)
    #Bouton swap
    bouton_swap = Button(fen, text="swap",relief=GROOVE,bg="#545B60",height=2, width=5,command=lambda x="": swap())
    bouton_swap.grid(row=2, column=4)
    #Bouton puissance
    bouton_puissance = Button(fen, text="y^x",relief=GROOVE,bg="#545B60", height=2, width=5, command=lambda x="": puissance())
    bouton_puissance.grid(row=4, column=4)
    #Bouton fonction inverse
    bouton_inverse = Button(fen, text="1/x",relief=GROOVE,bg="#545B60",height=2, width=5,command=lambda x="": fonction_inverse())
    bouton_inverse.grid(row=4, column=5)
    #Bouton racine carrée
    bouton_racine = Button(fen, text="√x",relief=GROOVE, bg="#545B60",height=2, width=5, command=lambda x="": racine_carrée())
    bouton_racine.grid(row=4, column=3)
    #Bouton cosinus
    bouton_cos = Button(fen, text="cos", relief=GROOVE,bg="#545B60",height=2, width=5, command=lambda x="": fctcos_sin_tan_atan(cos))
    bouton_cos.grid(row=5, column=0)
    #Bouton acos
    bouton_acos = Button(fen, text="acos",relief=GROOVE, bg="#545B60",height=2, width=5, command=lambda x="": fctacos_asin(acos))
    bouton_acos.grid(row=4, column=0)
    #Bouton sinus
    bouton_sin = Button(fen, text="sin",relief=GROOVE, bg="#545B60",height=2, width=5, command=lambda x="": fctcos_sin_tan_atan(sin))
    bouton_sin.grid(row=5, column=1)
    #Bouton asinus
    bouton_asin = Button(fen, text="asin",relief=GROOVE,bg="#545B60",height=2, width=5,  command=lambda x="": fctacos_asin(asin))
    bouton_asin.grid(row=4, column=1)
    #Bouton tan
    bouton_tan = Button(fen, text="tan",relief=GROOVE, bg="#545B60",height=2, width=5, command=lambda x="": fctcos_sin_tan_atan(tan))
    bouton_tan.grid(row=5, column=2)
    #Bouton atan
    bouton_atan = Button(fen, text="atan",relief=GROOVE, bg="#545B60",height=2, width=5, command=lambda x="": fctcos_sin_tan_atan(atan))
    bouton_atan.grid(row=4, column=2)
    #Bouton puissance de dix
    bouton_puissance_de_dix = Button(fen, text="EEX", relief=GROOVE,bg="#545B60",height=2, width=5, command=lambda x="":caractères("E"))
    bouton_puissance_de_dix.grid(row=5, column=3)

    bouton_log = Button(fen, text="LOG", relief=GROOVE,bg="#545B60",height=2, width=5, command=lambda x="":fct_log())
    bouton_log.grid(row=8, column=0)

    bouton_pi = Button(fen, text="π", relief=GROOVE,bg="#545B60",height=2, width=5, command=lambda x="":fct_pi())
    bouton_pi.grid(row=7, column=0)

    bouton_hex = Button(fen, text="HEX", relief=GROOVE,bg="#545B60",height=2, width=5, command=lambda x="":hexa())
    bouton_hex.grid(row=3, column=0)

    bouton_dec = Button(fen, text="DEC", relief=GROOVE,bg="#545B60",height=2, width=5, command=lambda x="":dec())
    bouton_dec.grid(row=3, column=1)

    bouton_oct = Button(fen, text="OCT", relief=GROOVE,bg="#545B60",height=2, width=5, command=lambda x="":octal())
    bouton_oct.grid(row=3, column=2)

    bouton_bin = Button(fen, text="BIN", relief=GROOVE,bg="#545B60",height=2, width=5, command=lambda x="":binaire())
    bouton_bin.grid(row=3, column=3)

    bouton_conversion = Button(fen, text="R→B", relief=GROOVE,bg="#545B60",height=2, width=5, command=lambda x="":conversion())
    bouton_conversion.grid(row=3, column=4)

    bouton_origine = Button(fen, text="B→R", relief=GROOVE,bg="#545B60",height=2, width=5, command=lambda x="":origine())
    bouton_origine.grid(row=3, column=5)
    #Bouton espace
    bouton_spc = Button(fen, text="SPC",bg="grey", relief=GROOVE,height=2, width=5, command=lambda x="":caractères(" "))
    bouton_spc.grid(row=9, column=3)
    #Bouton 1
    bouton_un = Button(fen, text=" 1 ",bg="grey",relief=GROOVE,height=2, width=5, command=lambda x="" : caractères(1))
    bouton_un.grid(row=8, column=1)
    #Bouton 2
    bouton_deux = Button(fen, text=" 2 ",bg="grey",relief=GROOVE,height=2, width=5, command=lambda x="" : caractères(2))
    bouton_deux.grid(row=8, column=2)
    #Bouton 3
    bouton_trois = Button(fen, text=" 3 ",bg="grey",relief=GROOVE, height=2, width=5, command=lambda x="" : caractères(3))
    bouton_trois.grid(row=8, column=3)
    #Bouton 4
    bouton_quatre = Button(fen, text=" 4 ",bg="grey", relief=GROOVE,height=2, width=5, command=lambda x="" : caractères(4))
    bouton_quatre.grid(row=7, column=1)
    #Bouton 5
    bouton_cinq = Button(fen, text=" 5 ",bg="grey", relief=GROOVE,height=2, width=5, command=lambda x="" : caractères(5))
    bouton_cinq.grid(row=7, column=2)
    #Bouton 6
    bouton_six = Button(fen, text=" 6 ",bg="grey",relief=GROOVE,height=2, width=5, command=lambda x="" : caractères(6))
    bouton_six.grid(row=7, column=3)
    #Bouton 7
    bouton_sept = Button(fen, text=" 7 ",bg="grey",relief=GROOVE,height=2, width=5, command=lambda x="" : caractères(7))
    bouton_sept.grid(row=6, column=1)
    #Bouton 8
    bouton_huit = Button(fen, text=" 8 ",bg="grey",relief=GROOVE,height=2, width=5, command=lambda x="" : caractères(8))
    bouton_huit.grid(row=6, column=2)
    #Bouton 9
    bouton_neuf = Button(fen, text=" 9 ",bg="grey",relief=GROOVE,height=2, width=5, command=lambda x="" : caractères(9))
    bouton_neuf.grid(row=6, column=3)
    #Bouton 0
    bouton_zero = Button(fen, text=" 0 ",bg="grey",relief=GROOVE,height=2, width=5,  command=lambda x="" : caractères(0))
    bouton_zero.grid(row=9, column=1)
    #Bouton ,
    bouton_virgule = Button(fen, text=" . ",bg="grey", relief=GROOVE,height=2, width=5, command=lambda x="" : caractères("."))
    bouton_virgule.grid(row=9, column=2)
    #Bouton entrée
    bouton_entree = Button(fen, text="ENTRER", bg="#545B60", relief=GROOVE,height=2, width=5, command=lambda x="": nv_elem_pourbouton())
    bouton_entree.grid(row=6, column=0)

    #Bouton quitter
    bouton_quitter = Button(fen, text="QUIT", relief=GROOVE,bg="#d71526", height=2, width=5, command=lambda x="": quitter())
    bouton_quitter.grid(row=9, column=0)
    #Bouton aide
    bouton_aide = Button(fen, text="?", relief=GROOVE, bg="#d71526",height=2, width=5,command=lambda x="": fenêtre_aide())
    bouton_aide.grid(row=9, column=5)

    #bouton skin
    def skin():
        global skin_open
        if skin_open==False:
            skin_open=True
            def skin_aero():
                fen.configure(background="#b6d2ec")
                entree.configure(bg="white",fg="black")
                a_afficher.configure(bg="white",fg="black")
                affich_erreurs.configure(disabledbackground="white",disabledforeground="black")
                bouton_plus.configure(bg="#dce6f4",fg="black")
                bouton_moins.configure(bg="#dce6f4",fg="black")
                bouton_fois.configure(bg="#dce6f4",fg="black")
                bouton_diviser.configure(bg="#dce6f4",fg="black")
                bouton_enlever.configure(bg="#dce6f4",fg="black")
                bouton_del.configure(bg="#dce6f4",fg="black")
                bouton_plusoumoins.configure(bg="#dce6f4",fg="black")
                bouton_carré.configure(bg="#dce6f4",fg="black")
                bouton_exp.configure(bg="#dce6f4",fg="black")
                bouton_swap.configure(bg="#dce6f4",fg="black")
                bouton_puissance.configure(bg="#dce6f4",fg="black")
                bouton_inverse.configure(bg="#dce6f4",fg="black")
                bouton_racine.configure(bg="#dce6f4",fg="black")
                bouton_cos.configure(bg="#dce6f4",fg="black")
                bouton_sin.configure(bg="#dce6f4",fg="black")
                bouton_tan.configure(bg="#dce6f4",fg="black")
                bouton_acos.configure(bg="#dce6f4",fg="black")
                bouton_asin.configure(bg="#dce6f4",fg="black")
                bouton_atan.configure(bg="#dce6f4",fg="black")
                bouton_puissance_de_dix.configure(bg="#dce6f4",fg="black")
                bouton_log.configure(bg="#dce6f4",fg="black")
                bouton_pi.configure(bg="#dce6f4",fg="black")
                bouton_hex.configure(bg="#dce6f4",fg="black")
                bouton_dec.configure(bg="#dce6f4",fg="black")
                bouton_bin.configure(bg="#dce6f4",fg="black")
                bouton_oct.configure(bg="#dce6f4",fg="black")
                bouton_conversion.configure(bg="#dce6f4",fg="black")
                bouton_origine.configure(bg="#dce6f4",fg="black")
                bouton_spc.configure(bg="#c5cfdf",fg="black")
                bouton_un.configure(bg="#c5cfdf",fg="black")
                bouton_deux.configure(bg="#c5cfdf",fg="black")
                bouton_trois.configure(bg="#c5cfdf",fg="black")
                bouton_quatre.configure(bg="#c5cfdf",fg="black")
                bouton_cinq.configure(bg="#c5cfdf",fg="black")
                bouton_six.configure(bg="#c5cfdf",fg="black")
                bouton_sept.configure(bg="#c5cfdf",fg="black")
                bouton_huit.configure(bg="#c5cfdf",fg="black")
                bouton_neuf.configure(bg="#c5cfdf",fg="black")
                bouton_zero.configure(bg="#c5cfdf",fg="black")
                bouton_virgule.configure(bg="#c5cfdf",fg="black")
                bouton_entree.configure(bg="#c5cfdf",fg="black")
                bouton_skin.configure(bg="#c5cfdf",fg="black")
                bouton_quitter.configure(bg="#2898C4",fg="white")
                bouton_aide.configure(bg="#2898C4",fg="white")
            def HP_original():
                fen.configure(background="#32394B")
                entree.configure(bg="#BDC2A4",fg="black")
                a_afficher.configure(bg="#BDC2A4",fg="black")
                affich_erreurs.configure(disabledbackground="#BDC2A4",disabledforeground="black")
                bouton_plus.configure(bg="#545B60",fg="black")
                bouton_moins.configure(bg="#545B60",fg="black")
                bouton_fois.configure(bg="#545B60",fg="black")
                bouton_diviser.configure(bg="#545B60",fg="black")
                bouton_enlever.configure(bg="#545B60",fg="black")
                bouton_del.configure(bg="#545B60",fg="black")
                bouton_plusoumoins.configure(bg="#545B60",fg="black")
                bouton_carré.configure(bg="#545B60",fg="black")
                bouton_exp.configure(bg="#545B60",fg="black")
                bouton_swap.configure(bg="#545B60",fg="black")
                bouton_puissance.configure(bg="#545B60",fg="black")
                bouton_inverse.configure(bg="#545B60",fg="black")
                bouton_racine.configure(bg="#545B60",fg="black")
                bouton_cos.configure(bg="#545B60",fg="black")
                bouton_sin.configure(bg="#545B60",fg="black")
                bouton_tan.configure(bg="#545B60",fg="black")
                bouton_acos.configure(bg="#545B60",fg="black")
                bouton_asin.configure(bg="#545B60",fg="black")
                bouton_atan.configure(bg="#545B60",fg="black")
                bouton_puissance_de_dix.configure(bg="#545B60",fg="black")
                bouton_log.configure(bg="#545B60",fg="black")
                bouton_pi.configure(bg="#545B60",fg="black")
                bouton_hex.configure(bg="#545B60",fg="black")
                bouton_dec.configure(bg="#545B60",fg="black")
                bouton_bin.configure(bg="#545B60",fg="black")
                bouton_oct.configure(bg="#545B60",fg="black")
                bouton_conversion.configure(bg="#545B60",fg="black")
                bouton_origine.configure(bg="#545B60",fg="black")
                bouton_spc.configure(bg="grey",fg="black")
                bouton_un.configure(bg="grey",fg="black")
                bouton_deux.configure(bg="grey",fg="black")
                bouton_trois.configure(bg="grey",fg="black")
                bouton_quatre.configure(bg="grey",fg="black")
                bouton_cinq.configure(bg="grey",fg="black")
                bouton_six.configure(bg="grey",fg="black")
                bouton_sept.configure(bg="grey",fg="black")
                bouton_huit.configure(bg="grey",fg="black")
                bouton_neuf.configure(bg="grey",fg="black")
                bouton_zero.configure(bg="grey",fg="black")
                bouton_virgule.configure(bg="grey",fg="black")
                bouton_entree.configure(bg="grey",fg="black")
                bouton_skin.configure(bg="grey",fg="black")
                bouton_quitter.configure(bg="#d71526",fg="black")
                bouton_aide.configure(bg="#d71526",fg="black")
            def light():
                fen.configure(background="#f1f1f1")           
                entree.configure(bg="white",fg="black")
                a_afficher.configure(bg="white",fg="black")
                affich_erreurs.configure(disabledbackground="white",disabledforeground="black")
                bouton_plus.configure(bg="#f9eb4a",fg="black")
                bouton_moins.configure(bg="#f9eb4a",fg="black")
                bouton_fois.configure(bg="#f9eb4a",fg="black")
                bouton_diviser.configure(bg="#f9eb4a",fg="black")
                bouton_enlever.configure(bg="#f9a7a4",fg="black")
                bouton_del.configure(bg="#97a5ff",fg="black")
                bouton_plusoumoins.configure(bg="white",fg="black")
                bouton_carré.configure(bg="white",fg="black")
                bouton_exp.configure(bg="white",fg="black")
                bouton_swap.configure(bg="white",fg="black")
                bouton_puissance.configure(bg="white",fg="black")
                bouton_inverse.configure(bg="white",fg="black")
                bouton_racine.configure(bg="white",fg="black")
                bouton_cos.configure(bg="white",fg="black")
                bouton_sin.configure(bg="white",fg="black")
                bouton_tan.configure(bg="white",fg="black")
                bouton_acos.configure(bg="white",fg="black")
                bouton_asin.configure(bg="white",fg="black")
                bouton_atan.configure(bg="white",fg="black")
                bouton_puissance_de_dix.configure(bg="white",fg="black")
                bouton_log.configure(bg="white",fg="black")
                bouton_pi.configure(bg="white",fg="black")
                bouton_hex.configure(bg="white",fg="black")
                bouton_dec.configure(bg="white",fg="black")
                bouton_bin.configure(bg="white",fg="black")
                bouton_oct.configure(bg="white",fg="black")
                bouton_conversion.configure(bg="white",fg="black")
                bouton_origine.configure(bg="white",fg="black")
                bouton_spc.configure(bg="white",fg="black")
                bouton_un.configure(bg="white",fg="black")
                bouton_deux.configure(bg="white",fg="black")
                bouton_trois.configure(bg="white",fg="black")
                bouton_quatre.configure(bg="white",fg="black")
                bouton_cinq.configure(bg="white",fg="black")
                bouton_six.configure(bg="white",fg="black")
                bouton_sept.configure(bg="white",fg="black")
                bouton_huit.configure(bg="white",fg="black")
                bouton_neuf.configure(bg="white",fg="black")
                bouton_zero.configure(bg="white",fg="black")
                bouton_virgule.configure(bg="white",fg="black")
                bouton_entree.configure(bg="#f9eb4a",fg="black")
                bouton_skin.configure(bg="white",fg="black")
                bouton_quitter.configure(bg="#d71526",fg="black")
                bouton_aide.configure(bg="#d71526",fg="black")
            def dark():
                fen.configure(background="#1e1e1e")
                entree.configure(bg="#3c3c3c",fg="white")
                a_afficher.configure(bg="#3c3c3c",fg="white")
                affich_erreurs.configure(disabledbackground="#3c3c3c",disabledforeground="white")
                bouton_plus.configure(bg="black",fg="white")
                bouton_moins.configure(bg="black",fg="white")
                bouton_fois.configure(bg="black",fg="white")
                bouton_diviser.configure(bg="black",fg="white")
                bouton_enlever.configure(bg="black",fg="white")
                bouton_del.configure(bg="black",fg="white")
                bouton_plusoumoins.configure(bg="black",fg="white")
                bouton_carré.configure(bg="black",fg="white")
                bouton_exp.configure(bg="black",fg="white")
                bouton_swap.configure(bg="black",fg="white")
                bouton_puissance.configure(bg="black",fg="white")
                bouton_inverse.configure(bg="black",fg="white")
                bouton_racine.configure(bg="black",fg="white")
                bouton_cos.configure(bg="black",fg="white")
                bouton_sin.configure(bg="black",fg="white")
                bouton_tan.configure(bg="black",fg="white")
                bouton_acos.configure(bg="black",fg="white")
                bouton_asin.configure(bg="black",fg="white")
                bouton_atan.configure(bg="black",fg="white")
                bouton_puissance_de_dix.configure(bg="black",fg="white")
                bouton_log.configure(bg="black",fg="white")
                bouton_pi.configure(bg="black",fg="white")
                bouton_hex.configure(bg="black",fg="white")
                bouton_dec.configure(bg="black",fg="white")
                bouton_bin.configure(bg="black",fg="white")
                bouton_oct.configure(bg="black",fg="white")
                bouton_conversion.configure(bg="black",fg="white")
                bouton_origine.configure(bg="black",fg="white")
                bouton_spc.configure(bg="#252526",fg="white")
                bouton_un.configure(bg="#252526",fg="white")
                bouton_deux.configure(bg="#252526",fg="white")
                bouton_trois.configure(bg="#252526",fg="white")
                bouton_quatre.configure(bg="#252526",fg="white")
                bouton_cinq.configure(bg="#252526",fg="white")
                bouton_six.configure(bg="#252526",fg="white")
                bouton_sept.configure(bg="#252526",fg="white")
                bouton_huit.configure(bg="#252526",fg="white")
                bouton_neuf.configure(bg="#252526",fg="white")
                bouton_zero.configure(bg="#252526",fg="white")
                bouton_virgule.configure(bg="#252526",fg="white")
                bouton_entree.configure(bg="#252526",fg="white")
                bouton_skin.configure(bg="#252526",fg="white")
                bouton_quitter.configure(bg="#888888",fg="white")
                bouton_aide.configure(bg="#888888",fg="white")
            def blue():
                fen.configure(background="#004052")
                entree.configure(bg="#002b36",fg="white")
                a_afficher.configure(bg="#002b36",fg="white")
                affich_erreurs.configure(disabledbackground="#002b36",disabledforeground="white")
                bouton_plus.configure(bg="#115b84",fg="white")
                bouton_moins.configure(bg="#115b84",fg="white")
                bouton_fois.configure(bg="#115b84",fg="white")
                bouton_diviser.configure(bg="#115b84",fg="white")
                bouton_enlever.configure(bg="#115b84",fg="white")
                bouton_del.configure(bg="#115b84",fg="white")
                bouton_plusoumoins.configure(bg="#115b84",fg="white")
                bouton_carré.configure(bg="#115b84",fg="white")
                bouton_exp.configure(bg="#115b84",fg="white")
                bouton_swap.configure(bg="#115b84",fg="white")
                bouton_puissance.configure(bg="#115b84",fg="white")
                bouton_inverse.configure(bg="#115b84",fg="white")
                bouton_racine.configure(bg="#115b84",fg="white")
                bouton_cos.configure(bg="#115b84",fg="white")
                bouton_sin.configure(bg="#115b84",fg="white")
                bouton_tan.configure(bg="#115b84",fg="white")
                bouton_acos.configure(bg="#115b84",fg="white")
                bouton_asin.configure(bg="#115b84",fg="white")
                bouton_atan.configure(bg="#115b84",fg="white")
                bouton_puissance_de_dix.configure(bg="#115b84",fg="white")
                bouton_log.configure(bg="#115b84",fg="white")
                bouton_pi.configure(bg="#115b84",fg="white")
                bouton_hex.configure(bg="#115b84",fg="white")
                bouton_dec.configure(bg="#115b84",fg="white")
                bouton_bin.configure(bg="#115b84",fg="white")
                bouton_oct.configure(bg="#115b84",fg="white")
                bouton_conversion.configure(bg="#115b84",fg="white")
                bouton_origine.configure(bg="#115b84",fg="white")
                bouton_spc.configure(bg="#57afae",fg="white")
                bouton_un.configure(bg="#57afae",fg="white")
                bouton_deux.configure(bg="#57afae",fg="white")
                bouton_trois.configure(bg="#57afae",fg="white")
                bouton_quatre.configure(bg="#57afae",fg="white")
                bouton_cinq.configure(bg="#57afae",fg="white")
                bouton_six.configure(bg="#57afae",fg="white")
                bouton_sept.configure(bg="#57afae",fg="white")
                bouton_huit.configure(bg="#57afae",fg="white")
                bouton_neuf.configure(bg="#57afae",fg="white")
                bouton_zero.configure(bg="#57afae",fg="white")
                bouton_virgule.configure(bg="#57afae",fg="white")
                bouton_entree.configure(bg="#57afae",fg="white")
                bouton_skin.configure(bg="#57afae",fg="white")
                bouton_quitter.configure(bg="#12356A",fg="white")
                bouton_aide.configure(bg="#12356A",fg="white")
            def sable():
                fen.configure(background="#6d725b")
                entree.configure(bg="#3e3d32",fg="white")
                a_afficher.configure(bg="#3e3d32",fg="white")
                affich_erreurs.configure(disabledbackground="#3e3d32",disabledforeground="white")
                bouton_plus.configure(bg="#272822",fg="white")
                bouton_moins.configure(bg="#272822",fg="white")
                bouton_fois.configure(bg="#272822",fg="white")
                bouton_diviser.configure(bg="#272822",fg="white")
                bouton_enlever.configure(bg="#272822",fg="white")
                bouton_del.configure(bg="#272822",fg="white")
                bouton_plusoumoins.configure(bg="#272822",fg="white")
                bouton_carré.configure(bg="#272822",fg="white")
                bouton_exp.configure(bg="#272822",fg="white")
                bouton_swap.configure(bg="#272822",fg="white")
                bouton_puissance.configure(bg="#272822",fg="white")
                bouton_inverse.configure(bg="#272822",fg="white")
                bouton_racine.configure(bg="#272822",fg="white")
                bouton_cos.configure(bg="#272822",fg="white")
                bouton_sin.configure(bg="#272822",fg="white")
                bouton_tan.configure(bg="#272822",fg="white")
                bouton_acos.configure(bg="#272822",fg="white")
                bouton_asin.configure(bg="#272822",fg="white")
                bouton_atan.configure(bg="#272822",fg="white")
                bouton_puissance_de_dix.configure(bg="#272822",fg="white")
                bouton_log.configure(bg="#272822",fg="white")
                bouton_pi.configure(bg="#272822",fg="white")
                bouton_hex.configure(bg="#272822",fg="white")
                bouton_dec.configure(bg="#272822",fg="white")
                bouton_bin.configure(bg="#272822",fg="white")
                bouton_oct.configure(bg="#272822",fg="white")
                bouton_conversion.configure(bg="#272822",fg="white")
                bouton_origine.configure(bg="#272822",fg="white")
                bouton_spc.configure(bg="#485042",fg="white")
                bouton_un.configure(bg="#485042",fg="white")
                bouton_deux.configure(bg="#485042",fg="white")
                bouton_trois.configure(bg="#485042",fg="white")
                bouton_quatre.configure(bg="#485042",fg="white")
                bouton_cinq.configure(bg="#485042",fg="white")
                bouton_six.configure(bg="#485042",fg="white")
                bouton_sept.configure(bg="#485042",fg="white")
                bouton_huit.configure(bg="#485042",fg="white")
                bouton_neuf.configure(bg="#485042",fg="white")
                bouton_zero.configure(bg="#485042",fg="white")
                bouton_virgule.configure(bg="#485042",fg="white")
                bouton_entree.configure(bg="#485042",fg="white")
                bouton_skin.configure(bg="#485042",fg="white")
                bouton_quitter.configure(bg="#8E835F",fg="black")
                bouton_aide.configure(bg="#8E835F",fg="black")
            skin=Toplevel(fen)
            skin.title(" ")
            skin.configure(background="#32394B")
            label=Label(skin, text="Choisissez un skin à la calculatrice.")
            label.grid(row=0,column=0,columnspan=2)
            bouton_aero=Button(skin, text="aero",width=5, bg="#dce6f4",command=lambda x="": skin_aero())
            bouton_aero.grid(row=1,column=0)
            bouton_hp=Button(skin, text="hp",width=5,bg="#545B60",command=lambda x="": HP_original())
            bouton_hp.grid(row=1,column=1)
            bouton_light=Button(skin, text="light",width=5,bg="#c4b7d7",command=lambda x="": light())
            bouton_light.grid(row=2,column=0)
            bouton_dark=Button(skin, text="dark",width=5,bg="black",fg="white",command=lambda x="": dark())
            bouton_dark.grid(row=2,column=1)
            bouton_blue=Button(skin, text="blue",width=5,bg="#57afae",fg="white",command=lambda x="": blue())
            bouton_blue.grid(row=3,column=0)
            bouton_sable=Button(skin, text="sable",width=5,bg="#485042",fg="white",command=lambda x="": sable())
            bouton_sable.grid(row=3,column=1)
            skin.resizable(width=False, height=False)
            def is_closed():
                global skin_open
                skin_open=False
                skin.destroy()
            skin.protocol("WM_DELETE_WINDOW", is_closed)
    bouton_skin = Button(fen, text="skins", bg="grey", relief=GROOVE,height=2, width=5,command=lambda x="": skin())
    bouton_skin.grid(row=8,column=5)

    #-------Entrée avec le clavier-------#
    fen.bind('<Return>',nv_elem) #Entrée normale
    fen.bind('<KP_Enter>',nv_elem) #Entrée sur le pavé numérique
    #------------------------------------#
    show()
    fen.mainloop()


if __name__ == '__main__':
    fen_choix = Tk()
    win_stack(fen_choix)