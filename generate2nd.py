import Latex
import exercices

def run():
  content = "\section*{Exercice 1}\n"
  content += exercices.getAbsoluteEq(10)

  content += "\section*{Exercice 2}\n"
  content += exercices.getAbsoluteEq(10, False)

  content += "\section*{Exercice 3}\n"
  content += exercices.getAbsoluteIneq(10)

  content += "\section*{Exercice 4}\n"
  content += exercices.getAbsoluteIneq(10, False)

  fileName = "exercices2nd.tex"

  print("Enregistrement du fichier")
  Latex.saveTeXFile(content, fileName)
  print("Fichier enregistré")

  print(str(content))
  """
  print("Compilation du fichier")
  Latex.compileTexFile(fileName)
  print("Fichier compilé")
  """
