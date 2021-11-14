from Tools import getValideName, LatexFontSize

# TODO : Placement de point sur les repères non orthogomaux (cartesien)
# TODO : Choisir graduation complete, graduation des 1, vecteur unitaire ou point I et J
# TODO : Envisager le paramétrage de l'affichage (couleur, taille...) pour chaque élément
# TODO : Equation de droites (prevoir paramétrique) \draw[scale=0.5, domain=-3:3, smooth, variable=\x, blue] plot ({\x}, {\x*\x});

class Point:
    possibleName = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

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
        return Droite(a,-1, b)

    def getCoefDirecteur(self):
        if self.b == 0:
            return None
        else:
            return -self.a/self.b

    def getImage(self, x):
        if self.b == None: # droite parallèle à l'axe des ordonnées
            return None
        else:
            return (-self.a * x - self.c)/self.b

    def getAntecedent(self, y):
        if self.a == None: # droite parallèle à l'axe des abscisses
            return None
        else:
            return (-self.b * y - self.c)/self.a

    def clip(self, xmin, xmax, ymin , ymax):
        if self.a == 0: #droite parallèle aux abscisses
            k = -self.c/self.b
            if k < ymin + 1:
                v = "above"
            else:
                v = "below"
            return ((xmin, k), (xmax, k), f"{v} left")
        elif self.b == 0: # Droite parallèle aux ordonnées
            k = -self.c/self.a
            if k > xmax - 1:
                h = "right"
            else:
                h = "left"
            return ((xmin, k),(xmax, k),  f"below {h}")
        else:
            v = "below"
            h = "left"
            p1 = (self.getAntecedent(ymin), ymin)
            p2 = (self.getAntecedent(ymax), ymax)
            p3 = (xmin, self.getImage(xmin))
            p4 = (xmax, self.getImage(xmax))

            if self.getCoefDirecteur() > 0:
                if p1[0] < p3[0]:
                    pgauche = p3
                else:
                    pgauche = p1

                if p2[0] > p4[0]:
                    pdroite = p4
                    v = "above"
                    h = "left"
                else:
                    pdroite = p2
                    v = "below"
                    h = "right"
            else:
                if p2[0] < p3[0]:
                    pgauche = p3
                else:
                    pgauche = p2

                if p1[0] > p4[0]:
                    pdroite = p4
                    v = "below"
                    h = "left"
                else:
                    pdroite = p1
                    v = "above"
                    h = "right"

            return (pgauche, pdroite, f"{v} {h}")

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
    def __init__(self, xmin = -5.5, xmax = 5.5,  ymin = -3.5, ymax = 5.5, xStep = 1, yStep = 1, xUnitVect=(.5,0), yUnitVect = (0,.5)):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.xStep = xStep
        self.yStep = yStep
        self.xUnitVect = xUnitVect
        self.yUnitVect = yUnitVect
        self.cartesien = False

    def render(self, forceClip = False):
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

        if forceClip:
            result += "% Clip pour que les figures ne sortent pas du cadre\n"
            result += "\\clip (\\xmin,\\ymin) rectangle (\\xmax,\\ymax);\n"

        return result


class Graphique:

    def __init__(self):
        self.repere = Repere()
        self.points = {}
        self.droites = {}

    def addPoint(self, x, y, nom=""):
        if nom == "":
            nom = getValideName("A", self.points.keys(), Point.possibleName)
        self.points[nom] = Point(x,y)

    def addDroite(self, a, b, c, nom = ""):
        if nom == "":
            nom = getValideName("d", self.droites.keys())
        self.droites[nom]= Droite(a,b,c)

    def addAffine(self, a, b, nom=""):
        if nom == "":
            nom = getValideName("d", self.droites.keys())
        self.droites[nom] = Droite.fromAffine(a,b)



    def renderPoints(self, size = 4, withLabel = True, labelSize = LatexFontSize.normalsize):
        result = ""
        if withLabel:
            for name, p in self.points.items():
                result +="\\draw plot[only marks,mark=x,mark size="+str(size)+"pt] coordinates "
                result += "{"+str((p.x, p.y))+"}"
                result += " node["+self.getNodePosition(p.x, p.y)+"]{\\"+labelSize+"{$"+name+"$}}"
                result += ";\n"
        else:
            pointListStr = "{"
            for name, p in self.points.items():
                pointListStr += str((p.x, p.y))
            pointListStr += "}"

            result += "\\draw plot[only marks,mark=x,mark size="+str(size)+"pt] coordinates"
            result += pointListStr
            result += ";\n"
        return result

    def renderDroites(self, width = 1, withLabel = True, labelSize = LatexFontSize.normalsize):
        #\draw (0,0) -- (1,1);
        result = ""
        for nom, d in self.droites.items():
            xmin = self.repere.xmin
            xmax = self.repere.xmax
            ymin = self.repere.ymin
            ymax = self.repere.ymax
            pgauche, pdroite, position = d.clip(xmin, xmax, ymin, ymax)

            result += "\\draw [line width="+str(width)+"pt, cap=round] "+str(pgauche)+" -- "+str(pdroite)

            if withLabel:
                result += " node["+position+"]{\\"+labelSize+"{$("+nom+")$}}"
            result += ";\n"
        return result


    def render(self, labelSize = LatexFontSize.normalsize):
        if self.repere.cartesien:
            result = "\\begin{tikzpicture}\n"
        else:
            result = "\\begin{tikzpicture}[x="+str(self.repere.xUnitVect[0])+"cm,y="+str(self.repere.yUnitVect[1])+"cm]"
        # Code du repère
        result += self.repere.render()
        # Code des points
        result += "\n%Codage des points\n"
        result += self.renderPoints(labelSize = labelSize)

        #Code des droites
        result += "\n%Codage des droites\n"
        result += self.renderDroites(labelSize = labelSize)

        result += "\\end{tikzpicture}\n"
        return result

    def getNodePosition(self, x, y):
        h = ""
        v = ""
        if x > self.repere.xmax - self.repere.xUnitVect[0]-self.repere.xStep:
            h="left"
        else:
            h ="right"
        if y > self.repere.ymax - self.repere.yUnitVect[1]-self.repere.yStep:
            v = "below"
        else:
            v ="above"

        return f"{v} {h}"

