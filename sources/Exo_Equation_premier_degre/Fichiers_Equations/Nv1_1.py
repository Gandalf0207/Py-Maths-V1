from pylatex import *
from pylatex.utils import * 

import random


def pgcd(a,b):
    # pgcd(a,b): calcul du 'Plus Grand Commun Diviseur' entre les 2 nombres entiers a et b
    while b != 0:
        a,b=b,a%b
    return a

### LIGNE DE L'EXO ###
def ligne_exo(doc,nb7,nb8,nb9,nb10,nb_value):

    doc.append(NoEscape("\\begin{align*}"))
    doc.append(NoEscape("\\  \\Leftrightarrow %sx - %s &= %s + %sx \\\\" % (nb7,nb8,nb9,nb10)))
    doc.append(NoEscape("\\end{align*}"))


### CORRECTION DE L'EXO ###
# Toutes les simplification sont faites si possible en fonction (simplification de fraction...)
def correction_exo(doc,nb7,nb8,nb9,nb10,nb_value):

    doc.append(NoEscape("\\ \\text{L'équation à résoudre est : } " % ()))

    doc.append(NoEscape("\\begin{align*}"))
    doc.append(NoEscape("\\  \\Leftrightarrow %sx - %s &= %s + %sx \\\\" % (nb7,nb8,nb9,nb10)))
    doc.append(NoEscape("\\end{align*}"))


    # Etape 1
    doc.append(NoEscape("\\  \\parbox{ 450pt }{ \\textbf{Etape 1} : Regroupons les termes contenant la variable x d’un côté de l’équation et les termes constants de l’autre côté. Retirons %sx des deux côtés et ajoutons %s des deux côtés également : }" % (nb10,nb8)))

    doc.append(NoEscape("\\begin{align*}"))
    doc.append(NoEscape("\\  \\Leftrightarrow %sx - %s + %s -%sx &= %s + %sx -%sx +%s \\\\" % (nb7,nb8,nb9,nb10,nb9,nb10,nb10,nb8)))
    nb = nb9 + nb8
    nbx = nb7 - nb10

    if nbx != 1:
        doc.append(NoEscape("\\  \\Leftrightarrow %sx &= %s \\\\" % (nbx,nb)))
        doc.append(NoEscape("\\end{align*}"))
    else:
        doc.append(NoEscape("\\  \\Leftrightarrow x &= %s \\\\" % (nb)))
        doc.append(NoEscape("\\end{align*}"))



    # Etape 2 
    #que si x != 0

    if nbx != 1:
        doc.append(NoEscape("\\  \\parbox{ 450pt }{ \\textbf{Etape 2} : Divisons les deux côtés de l’équation par %s pour isoler x et simplifions: }" % (nbx)))

        doc.append(NoEscape("\\begin{align*}"))
        doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%sx}{%s} &= \\frac{%s}{%s} \\\\" % (nbx,nbx,nb,nbx)))
        pgcd_frac3 = pgcd(nb,nbx)
        nb = nb//pgcd_frac3
        nbx = nbx//pgcd_frac3
        
        if nbx !=1:
            doc.append(NoEscape("\\  \\Leftrightarrow x &= \\frac{%s}{%s} \\\\" % (nb,nbx)))
            doc.append(NoEscape("\\end{align*}"))
        else:
            doc.append(NoEscape("\\  \\Leftrightarrow x &= %s \\\\" % (nb)))
            doc.append(NoEscape("\\end{align*}"))      





        