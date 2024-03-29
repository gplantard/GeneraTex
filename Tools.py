import random
lettres = "abcdefghxyz"

class LatexFontSize:
    tiny = "tiny"
    scriptsize = "scriptsize"
    footnotesize = "footnotesize"
    small = "small"
    normalsize = "normalsize"
    large = "large"
    Large = "Large"
    LARGE = "LARGE"
    huge = "huge"
    Huge = "Huge"

def getNumberOrLetter(min, max, p, possibleLetters=None):
  if (random.random()<p): # on choisit une lettre plustôt qu'un nombre
    if possibleLetters == None:
        possibleLetters = lettres
    return random.choice(possibleLetters)
  else:
    return str(randomValue(min,max))

def randomValue(min, max, nbDigit=0, pNeg=0):
    result = round(random.uniform(min, max),nbDigit)
    if nbDigit == 0:
        result =  int(result)
    if random.random() < pNeg:
        result = -result
    return result

def getValideName(defaultName, usedNameList, PossibleName = None):
    if defaultName in usedNameList:
        # On recherche dans la liste proposé si il y a une possibilité
        if PossibleName != None:
            for n in PossibleName:
                if n not in usedNameList:
                    return n
        # On rajoute un nombre en indice
        index = 1
        while defaultName+"_"+str(index) in usedNameList:
            index += 1
        return defaultName+"_"+str(index)
    return defaultName



def getMatrix(m=None,n=None, p=0, min = -5, max = 5):
    result = "\\begin{pmatrix}"
    if m == None:
        m = random.randint(1,4)
    if n == None:
        n = random.randint(1,4)
        while (m==1 and n==1):
            n = random.randint(1,4)
    valeurs =""
    for i in range(m):
        for j in range (n):
            valeurs+= getNumberOrLetter(min,max,p)
            if (j!=n-1):
                valeurs += "&"
        if (i!=m-1):
            valeurs+=" \\\\ \n"
    result += valeurs+"\n"
    result += "\\end{pmatrix}"
    return result

def isfloat(x):
    try:
        a = float(x)
    except (TypeError, ValueError):
        return False
    else:
        return True

def isint(x):
    try:
        a = float(x)
        b = int(a)
    except (TypeError, ValueError):
        return False
    else:
        return a == b

def wellTyped(x):
    if isint(x):
        return int(x)
    if isfloat(x):
        return float(x)
    return x

def getSignedString(x):
    # TODO : Utiliser cette fonction partout où c'est nécessaire
    if x > 0 : 
        return " + "+str(x)
    else:
        return str(x)


