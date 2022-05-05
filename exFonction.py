from random import randint, choice, random
from time import strftime
import Tools
from Trinome import Trinome

"""
ATTENTION : Pensez à ajouter un exempel dans la fonction ``sample`` afin de pouvoir donn�es un appercu du résusltat
"""
def samples():
    result = {}
    
    result["getExprAffine()"] = getExprAffine()
    result["getExprAffine(pneg = 0) - probabilité d'avoir des coefficients négatifs"] = getExprAffine(pneg = 0)
    result["getExprAffine(pneg = 1)"] = getExprAffine(pneg = 1)
    result["getDivAffine() (forme (ax+b)/(cx+d))"] = getDivAffine()
    result["getExerciceDerivePoly() - Exercice d'étude de variation d'un polynome (degré 3)"] = getExerciceDerivePoly(), False    
    result["getExerciceDerivePoly(nbRacine = 1) - Racine Unique"] = getExerciceDerivePoly(nbRacine = 1), False
    result["getExerciceDerivePoly(nbRacine = 2) - Racines forcement différentes"] = getExerciceDerivePoly(nbRacine = 2), False
    result["getExerciceDerivePoly(functionName = 'g')"] = getExerciceDerivePoly(functionName = 'g'), False 
    result["getExerciceDerivePoly(onlyInt = True)"] = getExerciceDerivePoly(onlyInt = True), False 
    
    return result


def getExprAffine(pneg = 0.5):
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

def getDivAffine():
    str_num = getExprAffine()
    str_den = getExprAffine()
    if str_num == str_den:
        return getDivAffine() # on recommence si la fraction vaut 1
    return "\\dfrac{"+str_num+"}{"+str_den+"}"

def getExerciceDerivePoly(nbRacine = None, functionName = 'f', onlyInt = False):
    # TODO : permettre de changer le nom de la fonction
    # ne donne ques des polynome de degré trois pour le moment
    ok = False
    while (ok == False):
        x1 =  randint(1,9) * choice([-1,1])
        x2 =  randint(1,9) * choice([-1,1])
        while nbRacine == 2 and x1 == x2:
            x2 =  randint(1,9) * choice([-1,1])
        a =  randint(1,4) * choice([-1,1])

        if nbRacine == 1:
            f = Trinome.fromFactor(a,x1,x1)
        else:
            f = Trinome.fromFactor(a,x1,x2)
        if onlyInt == False or (onlyInt and f.a % 3 == 0 and f.b % 2 == 0):
            ok = True

    f_facto = f.toString(Trinome.Forme.FACTORISEE)
    f_dev = f.toString(Trinome.Forme.DEVELOPPEE)

    
    if f.a % 3 == 0:
        if f.a == 3:
            A = ""
        elif f.a == -3:
            A = "-"
        else:
            A = str(f.a//3)
    else:
        A = "\\dfrac{"+str(f.a)+"}{3}"

    if f.b % 2 == 0:
        if f.b == 2:
            B = "+"
        elif f.b == -2:
            B = "-"
        else:
            B = Tools.getSignedString(f.b//2)
    else:
        B = "\\dfrac{"+str(abs(f.b))+"}{2}"
        if f.b > 0:
            B = " + " + B
        elif f.b < 0:
            B = " - " + B

    
    if f.c == 1:
        C = ""
    elif f.c == -1:
        C = "-"
    else:
        C = Tools.getSignedString(f.c)

    d = randint(1,20) * choice([-1,1])
    D = Tools.getSignedString(d)
        
    F = f"{A}x^3 {B}x^2 {C}x {D}"
    

    content = f"Soit ${functionName}(x) = {F}$."
    questions = """ 
    \\begin{enumerate}
        \\item Dériver $"""+functionName+"""(x)$ et démontrer que le résultat est $"""+f_dev+"""$.
        \\item Démontrer que $"""+functionName+"""'(x) = """+f_facto+"""$.
        \\item Résoudre $"""+functionName+"""'(x)=0$
        \\item En déduire le tableau de signe de $"""+functionName+"""'$.
        \\item En déduire le tableau de variation de $"""+functionName+"""$
    \\end{enumerate}
    """
    return content + questions