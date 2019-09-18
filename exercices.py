from random import *
lettres = "abcdefghxyz"

def getNumberOrLetter(min, max, p, nbLetter=4):
  if (random()<p): # on choisit une lettre plustôt qu'un nombre
  
    temp_letters = lettres[:nbLetter]
    return temp_letters[randint(0,len(temp_letters)-1)]
  else:
    return str(randint(min,max))

def getPolynomeDerivation():
    result = ""
    n = random.randint(2,6)
    while (n>=0):
        a = randint(2,9)
        result+=str(a)+" \\times x^{"+str(n)+"}"
        n-= randint(1,3)
    return r"$f(x)=%result hspace{1cm} f'(x)=.........\\\\".replace("%result",result)

def getMatrix(m=0,n=0, p=0):
    result = "\\begin{pmatrix}"
    if m==0:
        m= randint(1,4)
    if n==0:
        n= randint(1,4)
    valeurs =""
    for i in range(m):
        for j in range (n):
            valeurs+= getNumberOrLetter(-5,5,p)
            if (j!=n-1):
                valeurs += "&"
        if (i!=m-1):
            valeurs+=" \\\\ \n"
    result += valeurs+"\n"
    result += "\\end{pmatrix}"
    return result

def getMatrixSum(nbEx=1):
    result="Calculer les sommes suivantes:\\\\\n"
    for i in range (nbEx):
        m= randint(1,4)
        n= randint(1,4)
        matA = getMatrix(m,n)
        matB = getMatrix(m,n)
        result+="$$ " + matA + "+" + matB + " = $$\n"
    return result

def getMatrixProduct(nbEx=1):
    result="Calculer les produits suivants:\\\\\n"
    for i in range (nbEx):
        m= randint(1,4)
        n= randint(1,4)
        p= randint(1,4)
        matA = getMatrix(m,p, .1)
        matB = getMatrix(p,n, .5)
        result+="$$ " + matA + "\\times" + matB + " = $$\n"
    return result

def getAbsoluteEq(nbEx = 1, onlyInteger = True):
  ops=["+","-"]
  result="""
  Résoudre les équations suivantes:
  \\begin{itemize}\n
  \\begin{multicols}{2}\n"""
  for i in range(nbEx):
    if (onlyInteger):
      v = randint(1,9)
      r = randint(1,9)
    else:
      v = round(random()*10,1)
      r = round(random()*10,1)
    op = ops[randint(0,len(ops)-1)]
    p=0.2
    if (random()<p):#forme |a=x|=b
      result+="\item $|"+str(v)+op+"x| = "+str(r)+"\hspace{1cm} x = ......... $ ou $x = .........$\n"
    else:#forme |a=x|=b
      result+="\item $|x"+op+str(v)+"| = "+str(r)+"\hspace{1cm} x = ......... $ ou $x = .........$\n"
  result+="\end{multicols}\n\\end{itemize}" 
  return result

def getAbsoluteIneq(nbEx = 1, onlyInteger = True):
  ops=["+","-"]
  ineqs=["<",">","<=",">="]
  result="""
  Résoudre les inéquations suivantes:
  \\begin{itemize}\n
  \\begin{multicols}{2}\n"""
  for i in range(nbEx):
    if (onlyInteger):
      v = randint(1,9)
      r = randint(1,9)
    else:
      v = round(random()*10,1)
      r = round(random()*10,1)
    op = ops[randint(0,len(ops)-1)]
    ineq = ineqs[randint(0,len(ineqs)-1)]
    p=0.2
    if (random()<p):#forme |a=x|=b
      result+="\item $|"+str(v)+op+"x|"
    else:#forme |a=x|=b
      result+="\item $|x"+op+str(v)+"|"
    result+=  ineq+str(r)+"\hspace{1cm} x \in ..................$\n"
  result+="\end{multicols}\n\\end{itemize}" 
  return result