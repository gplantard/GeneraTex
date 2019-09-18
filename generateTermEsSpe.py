import Latex
import exercices

def run():
  content = "\section*{Exercice 1}\n"
  content += exercices.getMatrixSum(5)

  content += "\section*{Exercice 2}\n"
  content += exercices.getMatrixProduct(5)

  fileName = "exercicesTermEsSpe.tex"

  print("Enregistrement du fichier")
  Latex.saveTeXFile(content, fileName)
  print("Fichier enregistré")

  print(str(content))
  """
  print("Compilation du fichier")
  Latex.compileTexFile(fileName)
  print("Fichier compilé")
  """
