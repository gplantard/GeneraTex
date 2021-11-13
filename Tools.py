import random
lettres = "abcdefghxyz"

def getNumberOrLetter(min, max, p, possibleLetters=None):
  if (random.random()<p): # on choisit une lettre plustôt qu'un nombre
    if possibleLetters == None:
        possibleLetters = lettres
    return random.choice(possibleLetters)
  else:
    return str(randomValue(min,max))

def randomValue(min, max, nbDigit=0):
    result = round(random.uniform(min, max),nbDigit)
    if nbDigit == 0:
        return int(result)
    return result


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
