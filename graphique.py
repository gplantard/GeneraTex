class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return str((self.x, self.y))

class Droite:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def fromAffine(a, b):
        self.a = a
        self.b = -1
        self.c = b

    def __repr__(self):
        return f"{self.a}x+{self.b}y+{self.c}=0"

    def __eq__(self, d2):
        if d2.a == 0:
            coefa = 0
        else:
            coefa = self.a / d2.a
        if d2.b == 0:
            coefb = 0
        else:
            coefb = self.b / d2.b

        if d2.c == 0:
            coefc = 0
        else:
            coefc = self.c / d2.c

        # TODO : gérer les coef multi à 0
        return coefa == coefB and coefa == coefc


class Repere:
    def __init__(self, xmin = -5, xmax = 5,  xStep = 1, ymin = -3, ymax = 5, yStep = 1, xUnitVect=(1,0), yUnitVect = (0,1)):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.xStep = xStep
        self.yStep = yStep
        self.xUnitVect = xUnitVect
        self.yUnitVect = yUnitVect
        self.cartesien = False

    def render(self):
        result=""
        if self.cartesien:

            result += "\\begin{axis}[\n"
            result += "axis lines=middle,\n"
            result += "grid=both,\n"
            result += "xtick={"+str(self.xmin)+","+str(self.xmin+self.xStep)+",...,"+str(self.xmax)+"},\n"
            result += "ytick={"+str(self.ymin)+","+str(self.ymin+self.yStep)+",...,"+str(self.ymax)+"},\n"
            result += "x={("+str(self.xUnitVect[0])+"cm, "+str(self.xUnitVect[1])+"cm)},\n"
            result += "y={("+str(self.yUnitVect[0])+"cm, "+str(self.yUnitVect[1])+"cm)},\n"
            result += "xmin="+str(self.xmin)+",xmax="+str(self.xmax)+",\n"
            result += "ymin="+str(self.ymin)+",ymax="+str(self.ymax)+"\n"
            result += "]\n"
            result += "\\end{axis}\n"
        else:
            result = "% Dimensions du repere\n"
            result += "\\def\\xmin{"+str(self.xmin)+"} \\def\\xmax{"+str(self.xmax)+"} \\def\\ymin{"+str(self.ymin)+"} \\def\\ymax{"+str(self.ymax)+"}\n"

            result += "% Styles des axes et de la grille\n"
            result += "\\tikzstyle{axe}=[->,>=stealth']\n"
            result += "\\tikzstyle{grille}= [xstep="+str(self.xStep)+",ystep="+str(self.yStep)+",very thin, gray]\n"

            result += "% Grille\n"
            result += "\\draw [grille] (\\xmin,\\ymin) grid (\\xmax,\\ymax);\n"

            result += "% Annotations axes et unites\n"
            result += "\\draw [axe] (\\xmin,0)--(\\xmax,0) node[above left]  {$x$};\n"
            result += "\\draw [axe] (0,\\ymin)--(0,\\ymax) node[below right] {$y$};\n"
            result += "\\draw [axe,thick] (0,0)--(1,0) node[below left]  {$\\vec{i}$};\n"
            result += "\\draw [axe,thick] (0,0)--(0,1) node[below left] {$\\vec{j}$};\n"

            result += "% Clip pour que les figures ne sortent pas du cadre\n"
            result += "\\clip (\\xmin,\\ymin) rectangle (\\xmax,\\ymax);\n"

        return result


class Graphique:

    def __init__(self):
        self.repere = Repere()
        self.points = {}
        self.droites = {}


    def render(self):
        result = "\\begin{tikzpicture}[x="+str(self.repere.xUnitVect[0])+"cm,y="+str(self.repere.yUnitVect[1])+"cm]"
        result += self.repere.render()
        result += "\\end{tikzpicture}"
        return result
