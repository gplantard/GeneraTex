import Latex
import exercices

content= """
\section{Exercice}\n
"""
"""
content+= exercices.getMatrixSum(nbEx=5)
"""
content+= exercices.getMatrixProduct(nbEx=7)


fileName="exerciceMatrice.tex"

print("Enregistrement du fichier")
Latex.saveTeXFile(content, fileName)
print("Fichier enregistré")

print (str(content))

"""
print("Compilation du fichier")
Latex.compileTexFile(fileName)
print("Fichier compilé")
"""