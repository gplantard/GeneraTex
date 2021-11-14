from sys import stderr
class Calcul:
    def __init__(self, left, right, op):

        self.left = left
        self.right = right
        self.op = op

    def __repr__(self):
        result = ""
        if isinstance(self.left, Calcul):
            if Calcul.comOperator(self.op, self.left.op):
                strLeft = f"({self.left})"
            else:
                strLeft = f"{self.left}"
        else:
            strLeft = str(self.left)

        if isinstance(self.right, Calcul):
            if Calcul.comOperator(self.op, self.right.op):
                strRight = f"({self.right})"
            else:
                strRight = f"{self.right}"
        else:
            strRight = str(self.right)

        return strLeft + "" + self.op + "" + strRight

    def toLatex(self):
        result = ""
        if isinstance(self.left, Calcul):
            if Calcul.comOperator(self.op, self.left.op) and self.op != "/":
                left = "\\left("+ self.left.toLatex()+"\\right)"
            else:
                left = self.left.toLatex()
        else:
            left = str(self.left)

        if isinstance(self.right, Calcul):
            if Calcul.comOperator(self.op, self.right.op) and self.op != "/":
                right = "\\left("+ self.right.toLatex()+"\\right)"
            else:
                right = self.right.toLatex()
        else:
            right = str(self.right)

        if self.op == "+":
            return left + " + " + right
        if self.op == "-":
            return left + " - " + right
        if self.op == "*":
            return left + " \\times " + right
        if self.op == "/":
            return "\\dfrac{"+left+"}{"+right+"}"
        if self.op == "**" or "^":
            return left + "^{" + right + "}"

    @staticmethod
    def comOperator(op1, op2):
        operateurs = ["+","-","*","/","**","^", "²"]
        index1 = operateurs.index(op1)
        index2 = operateurs.index(op2)
        return index1 > index2

    def toNPIArray(self):
        result = []
        if isinstance(self.left, Calcul):
            result.extend(self.left.toNPIArray())
        else:
            result.append(self.left)
        if isinstance(self.right, Calcul):
            result.extend(self.right.toNPIArray())
        else:
            result.append(self.right)
        result.append(self.op)
        return result

    def toNPI(self):
        result = ""
        array = self.toNPIArray()
        for v in array:
            result += v + " "
        return result

    @staticmethod
    def fromExpressionArray(expression):
        # Ne gère pas les parenthèses
        #operations = ["**","^","*","/", "+","-"]
        operations = ["+","-","*","/","**","^", "²"]
        for op in operations:
            if op in expression:
                pos = expression.index(op)
                if op =="²":
                    gauche = expression[:pos]
                    result = Calcul(Calcul.fromExpression(gauche), 2, "^")
                else:
                    gauche = expression[:pos]
                    droite = expression[pos+len(op):]
                    result = Calcul(Calcul.fromExpressionArray(gauche), Calcul.fromExpressionArray(droite), op)
                return result
        if type(expression) == type([]):
            return expression[0]
        return expression

    @staticmethod
    def fromExpression(expression):
        operations = ["+","-","*","/","**","^", "²"]
        parenthese = Calcul.extractParenthese(expression)
        if isinstance(expression, Calcul):
            return expression
        result = []
        temp = ""
        i = 0
        while i < len(expression):
            c = expression[i]
            if c in operations:
                result.append(temp)
                temp = ""
                if c=="²":
                    result.append("^")
                    temp = '2'
                else:
                    result.append(c)
            elif c == "(":
                j = parenthese[i]
                result.append(Calcul.fromExpression(expression[i+1: j]))
                i = j-1
            elif isinstance(c, Calcul):
                result.append(c)
            else:
                temp += c
            i+=1
        result.append(temp)
        #conversion du tableau en calcul
        return Calcul.fromExpressionArray(result)

    @staticmethod
    def fromNPIArray(NPIArrayExpression):
        pile = []
        for e in NPIArrayExpression:
            if e in ["+","-","*","/","**","^"]:
                droite = pile.pop()
                gauche = pile.pop()
                calcul = Calcul(gauche, droite, e)
                pile.append(calcul)
            elif e == "²": # TODO : verif, normalement inutile
                gauche = pile.pop()
                calcul = Calcul(gauche, 2, '^')
                pile.append(calcul)
            else:
                pile.append(e)
        return pile[0]

    @staticmethod
    def fromNPI(expression):
        return Calcul.fromNPIArray(expression.strip().split(" "))

    @staticmethod
    def extractParenthese(expression):
        pile = []
        couple_list = {}
        content = []
        for i in range(len(expression)):
            c = expression[i]
            if (c=='('):
                pile.append(i)
            elif (c==')'):
                if len(pile) > 0:
                    val = pile.pop() # val contient l'indice de la parenthèse ouvrante correspondante
                    couple_list[val] = i # on ajoute le couple d'indice à la liste des résultats
                else :
                    print ("Expression '",expression,"' invalide : Parenthèse fermante en trop", file = stderr)
                    return None
        if (len(pile)==0):
            return couple_list
        else:
            print ("Expression '",expression,"' invalide : Parenthèse ouvrante en trop", file = stderr)
            return False

    def eval(self):
        if self.op == None:
            return self.left
        if type(self.left) == Calcul:
            left = self.left.eval()
        else:
            left = eval(self.left)
        if type(self.right) == Calcul:
            right = self.right.eval()
        else :
            right = eval(self.right)

        if self.op == "+":
            return left + right
        if self.op == "-":
            return left - right
        if self.op == "*":
            return left * right
        if self.op == "/":
            return left / right
        if self.op == "**" or "^":
            return left ** right


#expression ="1*2-34+5*6-8²"
#expression ="1+(2-(3+4)*5)/((6-7)^2*8)²"
#expression ="1+2-(f+4)*e²+((6-7)^2*8)²"
expression ="(1/2)^2"
calcul = Calcul.fromExpression(expression)
print (calcul)
#calcul = Calcul(1, 2, "+")
print("Code Latex :")
print("$$"+calcul.toLatex()+"$$")


