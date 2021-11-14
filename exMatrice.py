from Tools import getMatrix, randomValue
import random
"""
ATTENTION : Pensez à ajouter un exempel dans la fonction ``sample`` afin de pouvoir données un appercu du résusltat
"""
def samples():
    result = {}
    result["getSum() - dimention aléatoire"] = getSum()
    result["getSum(3,4)"] = getSum(3,4)
    result["getProduct()"] = getProduct()
    result["getProduct(2,3,4)"] = getProduct(2,3,4)
    result["getProduct(probaLetterMat1 = .1, probaLetterMat2 = .8) (proba par défaut : 0"] = getProduct(probaLetterMat1 = .1, probaLetterMat2 = .8)
    return result

def getSum(m = None, n = None):
    if m == None:
        m = random.randint(1,4)
    if n == None:
        n = random.randint(1,4)
        while (m==1 and n==1):
            n = random.randint(1,4)
    matA = getMatrix(m,n)
    matB = getMatrix(m,n)
    result = matA + "+" + matB
    return result

def getProduct(nbLineResult = None, nbColonneResult = None, dimInterne = None, probaLetterMat1 = 0, probaLetterMat2 = 0):
    if nbLineResult == None :
        nbLineResult = random.randint(1,4)
    if nbColonneResult == None :
        nbColonneResult = random.randint(2,4)
    if dimInterne == None :
        dimInterne= random.randint(2,4)

    matA = getMatrix(nbLineResult,dimInterne, probaLetterMat1) # proba de 0.1 d'avoir une lettre au lieu d'un nombre
    matB = getMatrix(dimInterne,nbColonneResult, probaLetterMat2)
    result = matA + "\\times" + matB
    return result



