import Tools



def getPolynomeDerivation():
    result = ""
    n = random.randint(2,6)
    while (n>=0):
        a = randint(2,9)
        result+=str(a)+" \\times x^{"+str(n)+"}"
        n-= randint(1,3)
    return r"$f(x)=%result hspace{1cm} f'(x)=.........\\\\".replace("%result",result)


