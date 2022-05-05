from Tools import getNumberOrLetter, randomValue
from random import choice, random, randint
"""
ATTENTION : Pensez à ajouter un exemple dans la fonction ``sample`` afin de pouvoir donner un apperçue du résultat
"""
def samples():
    """Liste des exemples à générer pour montrer les possiblilités du module
    """
    result = {}
    result["getAbsoluteEq()"] = (getAbsoluteEq(),False)
    result["getAbsoluteEq(nbDigit = 2)"] = getAbsoluteEq(nbDigit = 2),False
    result["getAbsoluteEq(p = 1) (proba de d'échanger les termes, 0.2 par défaut)"] = getAbsoluteEq(p = 1),False

    result["getAbsoluteIneq()"] = getAbsoluteIneq(),False
    result["getAbsoluteIneq(nbDigit = 2)"] = getAbsoluteIneq(nbDigit = 2),False
    result["getAbsoluteIneq(p = 1) (proba de d'échanger les termes, 0.2 par défaut)"] = getAbsoluteIneq(p = 1),False

    result["getAffine()"] = getAffine(),False
    result["getAffine(nbDigit = 2)"] = getAffine(nbDigit = 2),False
    result["getAffine(equation = False)"] = getAffine(equation = False),False
    result["getAffine(possibleLetter = \"abcdefg\")"] = getAffine(possibleLetter = "abcdefg"),False

    result["getDoubleAffine()"] = getDoubleAffine(),False #nbDigit = 0, equation = True, possibleLetter = "x"):
    result["getDoubleAffine(nbDigit = 2)"] = getDoubleAffine(nbDigit = 2),False
    result["getDoubleAffine(equation = False)"] = getDoubleAffine(equation = False),False
    result["getDoubleAffine(possibleLetter = \"abcdefg\")"] = getDoubleAffine(possibleLetter = "abcdefg"),False

    result["getProduitAffine()"] = getProduitAffine(), False #nbDigit = 0, equation = True, possibleLetter = "x"):
    result["getProduitAffine(nbDigit = 2)"] = getProduitAffine(nbDigit = 2),False
    result["getProduitAffine(equation = False)"] = getProduitAffine(equation = False),False
    result["getProduitAffine(possibleLetter = \"abcdefg\")"] = getProduitAffine(possibleLetter = "abcdefg"),False
    result["getProduitAffine(simple = True)"] = getProduitAffine(simple = True),False

    result["getSquareAffine()"] = getSquareAffine(), False #nbDigit = 0, possibleLetter = "x"):
    result["getSquareAffine(nbDigit = 2)"] = getSquareAffine(nbDigit = 2),False
    result["getSquareAffine(possibleLetter = \"abcdefg\")"] = getSquareAffine(possibleLetter = "abcdefg"),False

    result["getSquare()"] = getSquare(), False #(nbDigit = 0, possibleLetter = "x"):
    result["getSquare(nbDigit = 2)"] = getSquare(nbDigit = 2),False
    result["getSquare(possibleLetter = \"aze\")"] = getSquare(possibleLetter = "aze"),False




    return result


def getAbsoluteEq(nbDigit = 0, p = 0.2):

    v = randomValue(1,9,nbDigit)
    r = randomValue(1,9,nbDigit)

    op = choice(["+","-"])

    if (random()<p):#forme |a=x|=b
        result = "$|"+str(v)+op+"x| = "+str(r)+"\hspace{1cm} x = ......... $ ou $x = .........$"
    else:#forme |a=x|=b
        result = "$|x"+op+str(v)+"| = "+str(r)+"\hspace{1cm} x = ......... $ ou $x = .........$"

    return result

def getAbsoluteIneq(nbDigit = 0,  p = 0.2):
    v = randomValue(1,9,nbDigit)
    r = randomValue(1,9,nbDigit)

    op = choice(["+", "-"])
    ineq = choice(["<",">","\leq","\geq"])

    result=""
    if (random()<p):#forme |a=x|=b
        result+="$|"+str(v)+op+"x|"
    else:#forme |a=x|=b
        result+="$|x"+op+str(v)+"|"
    result+=  ineq+str(r)+"\hspace{1cm} x \in ..................$"
    return result


def getAffine(nbDigit = 0, equation = True, possibleLetter = "x"):
    a = randomValue(1,20,nbDigit)
    b = randomValue(1,20,nbDigit)
    c = randomValue(1,20,nbDigit)

    letter = choice(possibleLetter)
    if equation:
        eq = "="
    else :
        eq = choice(["<", ">", "\geq", "\leq"])
    op = choice(["+","-"])
    neg = choice(["-", ""])

    if a == 1:
        a = ""
    return f"${neg}{a}{letter} {op} {b} {eq} {c}$"

def getDoubleAffine(nbDigit = 0, equation = True, possibleLetter = "x"):
    a = randomValue(1,20,nbDigit)
    b = randomValue(1,20,nbDigit)
    c = randomValue(1,20,nbDigit)
    d = randomValue(1,20,nbDigit)

    letter = choice(possibleLetter)

    op1 = choice(["+","-"])
    neg1 = choice(["-", ""])
    op2 = choice(["+","-"])
    neg2 = choice(["-", ""])

    if equation:
        eq = "="
    else :
        eq = choice(["<", ">", "\geq", "\leq"])

    if a == 1:
        a = ""
    if c == 1 :
        c = ""
    return f"${neg1}{a}{letter} {op1} {b} {eq} {neg2}{c}{letter} {op2} {d}$"

def getProduitAffine(nbDigit = 0, equation = True, possibleLetter = "x", simple = False):
    a = randomValue(1,20,nbDigit)
    b = randomValue(1,20,nbDigit)
    c = randomValue(1,20,nbDigit)
    d = randomValue(1,20,nbDigit)

    letter = choice(possibleLetter)

    op1 = choice(["+","-"])
    neg1 = choice(["-", ""])
    op2 = choice(["+","-"])
    neg2 = choice(["-", ""])

    if simple:
        a = 1
        c = 1
        neg1 = ""
        neg2 = ""

    if equation:
        eq = "="
    else :
        eq = choice(["<", ">", "\geq", "\leq"])

    if a == 1:
        a = ""
    if c == 1 :
        c = ""
    return f"$({neg1}{a}{letter} {op1} {b}) ({neg2}{c}{letter} {op2} {d}){eq} 0$"

def getSquareAffine(nbDigit = 0, possibleLetter = "x"):
    a = randomValue(1,9,nbDigit)
    b = randomValue(1,9,nbDigit)
    c = randomValue(1,9,nbDigit)

    letter = choice(possibleLetter)

    eq = "="

    op = choice(["+","-"])
    neg = choice(["-", ""])

    if a == 1:
        a = ""
    return f"$({neg}{a}{letter} {op} {b})^2{eq} {round(c**2, nbDigit * 2)}$"


def getSquare(nbDigit = 0, possibleLetter = "x"):
    a = randomValue(1,9,nbDigit)
    b = randomValue(1,9,nbDigit)

    letter = choice(possibleLetter)

    eq = "="

    if a == 1:
        a = ""
    return f"${a}{letter}^2 {eq} {round((b**2)*a, nbDigit * 2)}$"



