from Tools import randomValue
import random
from graphique import Graphique, Repere
"""
ATTENTION : Pensez à ajouter un exempel dans la fonction ``sample`` afin de pouvoir données un appercu du résusltat
"""

def samples():
    result = {}
    result["getRepere()"] = getRepere()
    result["getRepere(xmin = -2, xmax = 2, ymin=-2.5, ymax = 3.5)"] = getRepere(xmin = -2, xmax = 2, ymin=-2.5, ymax = 3.5)
    result["getRepere(xStep = .5, yStep = 2)"] = getRepere(xStep = .5, yStep = 2)
    result["getRepere(xunit = .8, yunit=1.6) (en cm)"] = getRepere(xunit = .8, yunit=1.6)

     #getRepereCart(xmin=-5, xmax = 5, ymin = -3, ymax=5, xUnitVect=(1,0), yUnitVect=(0,1)):
    result["getRepereCart()"] = getRepereCart()
    result["getRepereCart(xmin=-2, xmax = 8, ymin = 0, ymax=5)"] = getRepereCart(xmin=-2, xmax = 8, ymin = 0, ymax=5)
    result["getRepereCart(xUnitVect=(.5,0), yUnitVect=(-1,1))"] = getRepereCart(xUnitVect=(.5,0), yUnitVect=(-1,1))
    result["getRepereCart(xStep=.5, yStep=2)"] = getRepereCart(xStep=.5, yStep=2)
    return result

"""
Fonctionement de TikZ
http://math.et.info.free.fr/TikZ/bdd/TikZ-Impatient.pdf
"""

def getRepereCart(xmin=-5, xmax = 5, xStep = 1, ymin = -3, ymax = 5, yStep = 1, xUnitVect=(1,0), yUnitVect=(0,1)):
    """result=""
    result += "\\begin{tikzpicture}"
    result += "\\begin{axis}[\n"
    result += "axis lines=middle,\n"
    result += "grid=both,\n"
    result += "xtick={"+str(xmin)+","+str(xmin+xStep)+",...,"+str(xmax)+"},\n"
    result += "ytick={"+str(ymin)+","+str(ymin+yStep)+",...,"+str(ymax)+"},\n"
    result += "x={("+str(xUnitVect[0])+"cm, "+str(xUnitVect[1])+"cm)},\n"
    result += "y={("+str(yUnitVect[0])+"cm, "+str(yUnitVect[1])+"cm)},\n"
    result += "xmin="+str(xmin)+",xmax="+str(xmax)+",\n"
    result += "ymin="+str(ymin)+",ymax="+str(ymax)+"\n"
    result += "]\n"
    result += "\\end{axis}\n"
    result += "\\end{tikzpicture}"
    return result"""
    repere = Repere(xmin, xmax, xStep, ymin, ymax, yStep, xUnitVect, yUnitVect)
    repere.cartesien = True
    graph = Graphique()
    graph.repere = repere
    return graph.render()


def getRepere(xmin = -3.5, xmax = 3.5, ymin=-2.5, ymax = 2.5, xStep = 1, yStep = 1, xunit = .5, yunit = .5):
    result ="\\begin{tikzpicture}[x="+str(xunit)+"cm,y="+str(yunit)+"cm]"
    result += "% Dimensions du repere\n"
    result += "\\def\\xmin{"+str(xmin)+"} \\def\\xmax{"+str(xmax)+"} \\def\\ymin{"+str(ymin)+"} \\def\\ymax{"+str(ymax)+"}\n"

    result += "% Styles des axes et de la grille\n"
    result += "\\tikzstyle{axe}=[->,>=stealth']\n"
    result += "\\tikzstyle{grille}= [xstep="+str(xStep)+",ystep="+str(yStep)+",very thin, gray]\n"

    result += "% Grille\n"
    result += "\\draw [grille] (\\xmin,\\ymin) grid (\\xmax,\\ymax);\n"

    result += "% Annotations axes et unites\n"
    result += "\\draw [axe] (\\xmin,0)--(\\xmax,0) node[above left]  {$x$};\n"
    result += "\\draw [axe] (0,\\ymin)--(0,\\ymax) node[below right] {$y$};\n"
    result += "\\draw [axe,thick] (0,0)--(1,0) node[below left]  {$\\vec{i}$};\n"
    result += "\\draw [axe,thick] (0,0)--(0,1) node[below left] {$\\vec{j}$};\n"

    result += "% Clip pour que les figures ne sortent pas du cadre\n"
    result += "\\clip (\\xmin,\\ymin) rectangle (\\xmax,\\ymax);\n"
    result += "\\end{tikzpicture}\n"

    return result

def getLectureAffine():
    result = ""
    return result





