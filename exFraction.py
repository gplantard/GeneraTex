from Tools import randomValue
from random import random, choice
from Calcul import Calcul

def samples():
    result = {}
    result["getAddition()"] = getAddition()
    result["getAddition(min = 15, max = 40) (default : 1 et 9)"] = getAddition(min = 15, max = 40)
    result["getAddition(pSub = 1) (proba soustration, default : 0.5)"] = getAddition(pSub = 1)
    result["getAddition(pNeg = 1) (proba valeurs négatives, default : 0.5)"] = getAddition(pNeg = 1)

    result["getMultiplication()"] = getMultiplication()
    result["getMultiplication(min = 15, max = 40) (default : 1 et 9)"] = getMultiplication(min = 15, max = 40)
    result["getMultiplication(pDiv = 1) (proba soustration, default : 0.5)"] = getMultiplication(pDiv = 1)
    result["getMultiplication(pDiv = 1, fraction = True) (proba soustration, default : 0.5)"] = getMultiplication(pDiv = 1, fraction = True)
    result["getMultiplication(pNeg = 1) (proba valeurs négatives, default : 0.5)"] = getMultiplication(pNeg = 1)

    result["getExpression()"] = getExpression()
    result["getExpression(template = \"f+f-f*f\")"] = getExpression(template = "f+f-f*f")
    result["getExpression(\"f+f*f\")"] = getExpression("f+f*f")
    result["getExpression(\"f+e*f\")"] = getExpression("f+e*f")
    result["getExpression(\"f*(e+f)\")"] = getExpression("f*(e+f)")
    result["getExpression(\"f+(e+f)\")"] = getExpression("f+(e+f)")

    result["getExpression(\"(f+e)$^2$/(n+e+f)\\textasciicircum (p+n)\")"] = getExpression("(f+e)²/(n+e+f)^(p+n)")

    return result

def getAddition(min=1, max=9, pSub = 0.5, pNeg = .5):
    a = randomValue(min, max)
    b = randomValue(min, max)
    c = randomValue(min, max)
    d = randomValue(min, max)
    while d == 1 and b == 1: # ajout de deux entiers : inutile
        d = randomValue(min, max)

    if random() < pNeg : a = -a
    if random() < pNeg : b = -b
    if random() < pNeg : c = -c
    if random() < pNeg : d = -d

    if b == 1:
        frac1 = str(a)
    else:
        frac1 = "\\dfrac{"+str(a)+"}{"+str(b)+"}"

    if d == 1:
        frac2 = str(c)
    else:
        frac2 = "\\dfrac{"+str(c)+"}{"+str(d)+"}"

    op = "+" if random() > pSub else "-"

    return frac1 + op + frac2

def getMultiplication(min=1, max=9, pDiv = 0.5, pNeg = .5, fraction = False):
    """
    Retourne un calcul de multiplication de fraction
    - min : valeur minimum
    """
    a = randomValue(min, max, pNeg = pNeg)
    b = randomValue(min, max, pNeg = pNeg)
    c = randomValue(min, max, pNeg = pNeg)
    d = randomValue(min, max, pNeg = pNeg)
    while d == 1 and b == 1: # ajout de deux entiers : inutile
        d = randomValue(min, max, pNeg = pNeg)


    if b == 1:
        frac1 = str(a)
    else:
        frac1 = "\\dfrac{"+str(a)+"}{"+str(b)+"}"

    if d == 1:
        frac2 = str(c)
    else:
        frac2 = "\\dfrac{"+str(c)+"}{"+str(d)+"}"

    op = "\\times" if random() > pDiv else "\\div"
    if fraction and op == "\\div":
        return "\\dfrac{"+frac1 + "}{" + frac2+"}"
    else :
        return frac1 + op + frac2

def convertTemplate(template, min = 1, max = 9, pNeg=.5):
    result = ""
    for c in template:
        if c == "f":
            a = randomValue(min, max, pNeg = pNeg)
            b = randomValue(min, max, pNeg = pNeg)
            result += "("+str(a)+"/"+str(b)+")"
        elif c == "e":
            a = randomValue(min, max, pNeg = pNeg)
            result += f"{a}"
        elif c == "p":
            a = randomValue(min, max, pNeg = 0)
            result += f"{a}"
        elif c == "n":
            a = randomValue(min, max, pNeg = 1)
            result += f"{a}"
        else:
            result += c
    calcul = Calcul.fromExpression(result)
    return calcul.toLatex()


def getExpression(template = "", pNeg = .5):
    if template == "":
        templates = []
        templates.append("f+f*f")
        templates.append("f-f*f")
        templates.append("f+e*f")
        templates.append("f(f+f)")

        template = choice(templates)

    return convertTemplate(template, pNeg)


