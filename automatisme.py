#import Latex
import exEquation
import exDroite
import exFraction
from Exercice import *
from random import random, randint, choice, shuffle
#from Tools import randomValue

def run():
    content = ""

    # Exercice sur les equations
    content += "\\begin{minipage}{.4\\linewidth}\n"
    ex = Exercice("Résoudre les équations suivantes :")
    ex += exEquation.getAffine()
    ex += exEquation.getDoubleAffine()
    ex += exEquation.getProduitAffine(simple = True)
    ex += exEquation.getProduitAffine()
    ex += exEquation.getSquareAffine()

    content += str(ex)
    content += "\\end{minipage}\n"

    # Exercice sur les inéquations
    content += "\\begin{minipage}{.4\\linewidth}\n"
    ex = Exercice("Résoudre les inéquations suivantes :")
    ex += exEquation.getAffine(equation = False)
    ex += exEquation.getAffine(equation = False)
    ex += exEquation.getAffine(equation = False)
    ex += exEquation.getDoubleAffine(equation = False)
    ex += exEquation.getDoubleAffine(equation = False)
    content += str(ex)
    content += "\\end{minipage}\n"

    # Exercice sur les droites (lecture graphique)
    ex = Exercice("Donner l'équation des droites suivantes :")

    content += str(ex)
    content += exDroite.getLectureAffine(4)

    # Exercice sur les droites (tracé)
    xmin=-5.5
    xmax = 5.5
    ymin=-3.5
    ymax=5.5

    ex = Exercice("Tracer les droites demandées dans le repère suivant :")
    repere = exDroite.getRepere(xmin, xmax, ymin, ymax, xunit=1, yunit=1)

    a_list = ["0","1","2","3","4","5"]
    for i in range (0,6):
        for j in range (1,6):
            if ((i%j != 0) and (j%i != 0)):
                a_list.append("\dfrac{"+str(i)+"}{"+str(j)+"}")
    b_list = [i for i in range (int(ymin+1), int(ymax-1))]

    nb_droite = 4
    a_choice = []
    b_choice = []
    while len(a_choice)<nb_droite:
        a = choice(a_list)
        if (random()>.5):
            a = "-"+a
        if a not in a_choice:
            a_choice.append(a)

    while len(b_choice)<nb_droite:
        b = choice(b_list)

        if b not in b_choice:
            b_choice.append(b)

    for i in range(nb_droite):
        equation = "$y="
        if (a_choice[i] != 0):
            equation += str(a_choice[i])+"x"
        if (b_choice[i] != 0):
            if b_choice[i] > 0:
                equation += "+"
            equation += str(b_choice[i])
        ex+= equation+"$"

    content += ex.renderTitle()
    content += ex.renderConsigne()+"\\\\\n"
    content += "\\begin{minipage}{.45\\linewidth}\n"
    content += repere
    content += "\\end{minipage}\\hfill\n"
    content += "\\begin{minipage}{.4\\linewidth}\n"
    content += ex.renderQuestions()
    content += "\\end{minipage}\n"


    content += "\\begin{minipage}{.45\\linewidth}\n"
    # Exercice sur les fractions
    ex = Exercice("Donner le résultat sous forme simplifié :")
    #ex += exFraction.getAddition(pSub=0)
    #ex += exFraction.getAddition(pSub=1)
    #ex += exFraction.getMultiplication(pDiv=0)
    #ex += exFraction.getMultiplication(pDiv=1)
    ex += "$"+exFraction.getExpression("f-e*f")+"$"
    ex += "$"+exFraction.getExpression("f+f*f-f")+"$"
    ex += "$"+exFraction.getExpression("f(f+f)")+"$"
    ex += "$"+exFraction.getExpression("(f+f)/(f-f)")+"$"
    content += str(ex)
    content += "\\end{minipage}\n"

    content += "\\begin{minipage}{.45\\linewidth}\n"
    # Exercice sur les puissances
    ex = Exercice("Donner le résultat sous forme $a^n$ :")
    ex += "$A="+exFraction.getExpression("2^e/(2^e*2^e)")+"$"
    ex += "$B="+exFraction.getExpression("(4^e*(4^e)^e)/(4^e*4^e)")+"$"
    ex += "$C="+exFraction.getExpression("(7^e*(7^e)^e)/((7^e)^e*7^e)")+"$"
    content += str(ex)
    content += "\\end{minipage}\n"

    # Exercice sur développer et réduire
    ex = Exercice("Développer et réduire les expression suivantes :")
    ex += "$A="+exFraction.getExpression("e * x*(x-e) + (x+e)²")+"$"
    ex += "$B="+exFraction.getExpression("(e*x+e) * (x-e) - (x+e)²")+"$"
    ex += "$C="+exFraction.getExpression("e * x* (x-e)² -(e*x+e) *(x+e)²")+"$"
    content += str(ex)

    # Tableau de signe (afine double affine)
    ex = Exercice("Etablir le tableau de signe des fonction suivante :")
    for i in range(2):
        # fonction affine
        a = randint(1,10)
        b = randint(1,10)
        letter = "x"

        op1 = choice(["+","-"])
        neg1 = choice(["-", ""])

        if a == 1:
            a = ""
        ex += "$f(x) = {}{}{} {} {}$".format(neg1,a, letter, op1, b)

    for i in range(2):
        a = randint(1,10)
        b = randint(1,10)
        c = randint(1,10)
        d = randint(1,10)

        letter = "x"

        op1 = choice(["+","-"])
        neg1 = choice(["-", ""])
        op2 = choice(["+","-"])
        neg2 = choice(["-", ""])

        if a == 1:
            a = ""
        if c == 1 :
            c = ""
        ex += f"$f(x)=({neg1}{a}{letter} {op1} {b}) ({neg2}{c}{letter} {op2} {d})$"
    content += str(ex)

    # pourcentage (question aléatoire)
    ex = Exercice()
    a =randint(2,9)
    b =randint(2,9)
    total = choice([20, 25])
    ex += f"Un sac contient {a} jetons rouges, {b} jetons bleus et {total-a-b} jetons verts. \
    Déterminer, en pourcentage, la proportion de jetons {choice(['rouges', 'bleus', 'verts'])} dans le sac."

    question = f"Une veste coûte {randint(1,200)*10}\\euro. On obtient une remise de {choice([20, 25, 50, 75, 10])}\\% sur son prix."
    question += choice(["Quel est le montant de la remise ?", "Quelle est le nouveau prix ?"])
    ex += question

    ex+= f"Donner le coefficient multiplicateur correspondant à une {choice(['hausse', 'baisse'])} de {randint(5,95)}\\%."

    ex+= f"Dire si le coefficient multiplicateur {randint(10, 190)/100} correspond à une hausse ou à une baisse et indiquer le pourcentage d'évolution associé."

    op1 = "augmenté"
    op2 = "diminué"
    if random()>.5:
        op1, op2 = op2, op1

    p = randint(1,9)*10
    questions = ["Le prix a augmenté.", "Le prix a baissé.", "Le prix est revenu au prix initial.", "On ne peut pas savoir."]
    question = f"Le prix d'un objet a {op1} de {p}\\% puis a {op2} de {p}\\%.\\\\\nComment est le prix maintenant ?"
    question += "\\begin{enumerate}[label=\\alph*)]"
    shuffle(questions)
    for q in questions:
        question += f"\\item {q}"
    question += "\\end{enumerate}"
    ex+= question

    content += str(ex)

    #fileName = "automatisme.tex"
    #print("Enregistrement du fichier")
    #Latex.saveTeXFile(content, fileName)
    #print("Fichier enregistré")

    #print(str(content))
    return content
    """
    print("Compilation du fichier")
    Latex.compileTexFile(fileName)
    print("Fichier compilé")
    """
