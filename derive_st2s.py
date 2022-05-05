#import Latex
import exFonction
from Exercice import *
from random import random, randint, choice, shuffle
#from Tools import randomValue

def run():
    content = ""

    ex = Exercice(exFonction.getExerciceDerivePoly(onlyInt=True, nbRacine=2))
    content += str(ex)

    ex = Exercice(exFonction.getExerciceDerivePoly(onlyInt=True))
    content += str(ex)

    ex = Exercice(exFonction.getExerciceDerivePoly(nbRacine=2))
    content += str(ex)

    ex = Exercice(exFonction.getExerciceDerivePoly())
    content += str(ex)

    ex = Exercice(exFonction.getExerciceDerivePoly(onlyInt=True, nbRacine=1))
    content += str(ex)

    ex = Exercice(exFonction.getExerciceDerivePoly(nbRacine=1))
    content += str(ex)

    return content
    """
    print("Compilation du fichier")
    Latex.compileTexFile(fileName)
    print("Fichier compilé")
    """
