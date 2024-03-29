from random import randint, choice, random
import Tools

"""
ATTENTION : Pensez à ajouter un exempel dans la fonction ``sample`` afin de pouvoir donn�es un appercu du résusltat
"""
def samples():
    result = {}
    #result["getLogSimplification() - Général"] = """Fourni un exercice de type simplification d'expression logarithmique. 
    #La fonction ne peut pas demander le log d'un nombre premier. il est possible de d'avoir nue log d'un décimal."""
    result["getLogSimplification() (basé sur des entiers entre 2 et 10)"] = getLogSimplification()
    result["getLogSimplification([2,3,5])"] = getLogSimplification([2,3,5])
    result["getLogSimplification([2,3,5], p = 1) (proba de décalage de virgule entre 1 et 3 ou -1 et -3)"] = getLogSimplification([2,3,5], p = 1)
    result["getLogSimplification([2,5], p = 1) (suppression des virgules en cas d'entier)"] = getLogSimplification([2,5], p = 1,iteration = 4)
    result["getLogSimplification([3], p = 0, iteration = 3) (nombre de multiplication d'entier)"] = getLogSimplification([3], p = 0, iteration = 3)
    result["getLogSimplification([2,3,5], p = 0, iteration = 4) (nombre de multiplication d'entier)"] = getLogSimplification([2,3,5], p = 0, iteration = 4)
    result["getLogSimplification([2,3,5], p = 0, maxIteration = 5) (nombre max de multiplication d'entier si iteration non défini, defaut : 3 ou 5 si liste donnée)"] = getLogSimplification([2,3,5], p = 0, maxIteration = 5)
    result["getLogEquation()"] = getLogEquation()
    result["getLogEquation(onlyInt=True)"] = getLogEquation(onlyInt=False)
    result["getLogEquation(nbTerm=2) (defaut)"] = getLogEquation(nbTerm=2)
    result["getLogEquation(nbTerm=3)"] = getLogEquation(nbTerm=3)
    result["getLogEquation(nbTerm=4)"] = getLogEquation(nbTerm=4)
    result["getLogEquation(onlyInt=True, nbTerm=4)"] = getLogEquation(nbTerm=4)
    #result["getLogSimplificationConsigne()"] = getLogSimplificationConsigne()
    #result["getLogSimplificationConsigne([2,3,5])"] = getLogSimplificationConsigne([2,3,5])
    return result


def getLogSimplificationConsigne(logs = [2,3,5,7]):
    if (logs != None):
        consigne ="Exprimez les valeurs suivantes en fonction de "
        for i in range(len(logs)):
            n = logs[i]
            consigne += f"$\\log({n})$"
            if i < len(logs)-2:
                consigne += ", "
            elif i == len(logs)-2:
                consigne += " et "
            else:
                consigne += "."
        return consigne


def getLogSimplification(logs=None, p=0.5, iteration = None, maxIteration = 3):
    def get_number(list, p, iteration, maxIteration):
        a = 1
        if iteration == None:
            iteration = randint(1,maxIteration)
            if list != None or iteration == 1:
                iteration += 2
        for i in range(iteration):
            if list == None:
                a *= randint(2,10)
            else:
                a *= choice(list)
        if random() < p:
            a *= 10**(randint(1,3)*(-1)**(randint(1,2)))
        if a in [1,2,3,5,7,11,13,17,19,23]:
            a = get_number(list,p, iteration, maxIteration)
        # suppression des virgules inutile dans le cas de nombre entier
        if int(a)==a:
            return int(a)
        return a

    return f"\\log({get_number(logs, p, iteration, maxIteration)})"

def getLogEquation(onlyInt = False, nbTerm = 2):

    
    if nbTerm > 4:
        nbTerm = 4
    if nbTerm < 2:
        nbTerm = 2

    content = ""
    var ={"a":1,"b":1,"c":1,"d":1}
    if onlyInt:
        var["a"] = randint(1, 100)
        var["b"] = randint(1, 100)
        var["c"] = randint(1, 100)
        var["d"] = randint(1, 100)
    else :
        for v in var.keys():
            val = round(random(), 4)*10**(randint(0,3))
            if val == int(val):
                val = int(val)
            var[v] = val

    a = var["a"]
    b = var["b"]
    c = var["c"]
    d = var["d"]
    
    if nbTerm == 2:
        content = f"{a}^x = {b}"
    elif nbTerm == 3:
        content = f"{c} \\times {a}^x = {b}"
    else:
        content = str(c) + " \\times " + str(a) + "^x = "+ str(d) + " ^ {" + str(b) + "}"
    return content