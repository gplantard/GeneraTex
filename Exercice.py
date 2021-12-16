class Question:
    def __init__(self, consigne = "", content = ""):
        self.consigne = consigne
        self.content = content

    def __str__(self):
        content = ""
        if self.consigne != "":
            content += self.consigne + "\\\\\n"
        content += self.content
        return content

class Exercice:

    global_compteur = 1

    def __init__(self, consigne = "", number = None):
        if number == None:
            self.number = Exercice.global_compteur
            Exercice.global_compteur += 1
        else:
            self.number = number
            if self.number >= Exercice.global_compteur :
                Exercice.global_compteur = self.number +1
        self.consigne = consigne
        self.questions = []

    def add(self, content, question = ""):
        q = Question(question, content)
        self.questions.append(q)

    def __iadd__(self, content):
        self.add(content)
        return self

    def __str__(self):
        content = self.renderTitle()
        content += self.renderConsigne()
        content += self.renderQuestions()

        return content

    def renderTitle(self):
        return "\section*{Exercice " + str(self.number) +"}\n"

    def renderConsigne(self):
        return self.consigne + "\n"

    def renderQuestions(self):
        content = "\n\\begin{enumerate}[label=\\alph*)]\n"
        for q in self.questions:
            content += "\\item "+str(q)+"\n"
        content += "\\end{enumerate}\n"
        return content