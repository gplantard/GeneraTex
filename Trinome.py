from sys import stderr
from math import sqrt

from Tools import wellTyped

class Trinome:
    class Forme:
        DEVELOPPEE = 1
        FACTORISEE = 2
        CANONIQUE = 3

    def __init__(self, a, b, c):

        self.a = wellTyped(a)
        self.b = wellTyped(b)
        self.c = wellTyped(c)
    
    @staticmethod
    def fromFactor(a, x1, x2):
        b = a * (x1 + x2)
        c = a * x1 * x2
        return Trinome(a,b,c)

    def _getDelta(self):
        return wellTyped(self.b**2-4*self.a*self.c)

    def _getX1(self):
        if self.delta < 0 :
            return None
        return wellTyped((-self.b - sqrt(self.delta))/(2*self.a))
    
    def _getX2(self):
        if self.delta < 0 :
            return None
        return wellTyped((-self.b + sqrt(self.delta))/(2*self.a))

    delta = property(_getDelta)
    x1 = property(_getX1)
    x2 = property(_getX2)

    def __repr__(self) -> str:
        return self.toString()

    def toString(self, mode = Forme.DEVELOPPEE):
        # TODO : Utiliser Calcul.fromExpression() puis str
        if mode == Trinome.Forme.FACTORISEE:
            result = ""
            if self.a != 0:
                if self.a == 1:
                    str_a = ""
                elif self.a == -1:
                    str_a = "-"
                else:
                    str_a= str(self.a)
                result += str_a
            if self.x1 == 0 and self.x2 == 0:
                result += "x^2"
            elif self.x1 == 0 or self.x2 == 0:
                result += "x"
            if  self.x1 != 0:
                result += "(x "
                if self.x1 > 0:
                    result += "+"
                result += str(self.x1) + ")"
            if self.x1 == self.x2:
                result += "^{2}"
            elif  self.x2 != 0:
                result += "(x "
                if self.x2 > 0:
                    result += "+"
                result += str(self.x2) + ")"
                        
        else : # default : if mode == Trinome.Forme.DEVELOPPE:
            result = ""
            if self.a != 0:
                if self.a == 1:
                    str_a = ""
                elif self.a == -1:
                    str_a = "-"
                else:
                    str_a= str(self.a)
                result += str_a + " x^{2}"
            if self.b != 0:
                if self.b > 0:
                    result += " + "
                if self.b == 1 :
                    str_b = ""
                elif self.b == -1:
                    str_b = "-"
                else:
                    str_b= str(self.b)
                result += str_b + " x"
            if self.c != 0:
                if self.c > 0:
                    result += " + "
                result += str(self.c)
        return result
        