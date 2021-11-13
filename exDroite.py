from Tools import randomValue
import random
from graphique import Graphique, Repere
"""
ATTENTION : Pensez à ajouter un exempel dans la fonction ``sample`` afin de pouvoir données un appercu du résusltat
"""

def samples():
    result = {}
    #result["getRepere()"] = getRepere()
    #result["getRepere(xmin = -2, xmax = 2, ymin=-2.5, ymax = 3.5)"] = getRepere(xmin = -2, xmax = 2, ymin=-2.5, ymax = 3.5)
    #result["getRepere(xStep = .5, yStep = 2)"] = getRepere(xStep = .5, yStep = 2)
    #result["getRepere(xunit = .8, yunit=1.6) (en cm)"] = getRepere(xunit = .8, yunit=1.6)

    #result["getRepereCart()"] = getRepereCart()
    #result["getRepereCart(xmin=-2, xmax = 8, ymin = 0, ymax=5)"] = getRepereCart(xmin=-2, xmax = 8, ymin = 0, ymax=5)
    #result["getRepereCart(xUnitVect=(.5,0), yUnitVect=(-1,1))"] = getRepereCart(xUnitVect=(.5,0), yUnitVect=(-1,1))
    #result["getRepereCart(xStep=.5, yStep=2)"] = getRepereCart(xStep=.5, yStep=2)

    result["getLectureAffine()"] = getLectureAffine()
    return result

"""
Fonctionement de TikZ
http://math.et.info.free.fr/TikZ/bdd/TikZ-Impatient.pdf
"""

def getRepereCart(xmin=-5, xmax = 5, ymin = -3, ymax = 5, xStep = 1, yStep = 1, xUnitVect=(.5,0), yUnitVect=(0,.5)):
    repere = Repere(xmin, xmax, ymin, ymax, xStep, yStep, xUnitVect, yUnitVect)
    repere.cartesien = True
    graph = Graphique()
    graph.repere = repere
    return graph.render()


def getRepere(xmin = -3.5, xmax = 3.5, ymin=-2.5, ymax = 2.5, xStep = 1, yStep = 1, xunit = .5, yunit = .5):
    repere = Repere(xmin, xmax, ymin, ymax, xStep, yStep, (xunit, 0), (0,yunit))
    repere.cartesien = False
    graph = Graphique()
    graph.repere = repere
    return graph.render()


def getLectureAffine(nbDroite = 1 ):
    result = ""
    graph = Graphique()
    graph.addPoint(1,2)
    graph.addDroite(-2,3, -3)
    graph.addAffine(-.5,2)
    graph.addDroite(1,0, 3)
    return graph.render()






