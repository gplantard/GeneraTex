from random import randint, choice, random
import Tools

"""
ATTENTION : Pensez à ajouter un exempel dans la fonction ``sample`` afin de pouvoir donn�es un appercu du résusltat
"""
def samples():
    result = {}
    
    result["getExpAffine()"] = getExpAffine()
    result["getExpAffine(pneg = 1) - probabilité d'avoir des coefficients négatifs"] = getExpAffine(pneg = 1)
    
    return result


def getExpAffine(pneg = 0.5):
    a = randint(1,9)
    b = randint(1,9)

    if random() < pneg:
        a = -a
    if random() < pneg:
        b = -b
    if a == 1:
        str_a = ''
    elif a == -1:
        str_a = '-'
    else:
        str_a = str(a)
    if b > 0:
        str_b = "+" + str(b)
    else:
        str_b = str(b)

    return str_a+"x"+str_b
