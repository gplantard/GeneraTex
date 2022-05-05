#import generate2nd
#import generateTermEsSpe
import automatisme

import pyperclip

import exMatrice
import exEquation
import exDroite
import exFraction
import exExpLog
import exFonction

#generate2nd.run()
#generateTermEsSpe.run()

modulesList = globals()

def getSamples(modulesNames = None):
    global modulesList
    sampleDocument = ""
    for mod in modulesList.keys():
        if mod.startswith("ex") and (modulesNames == None or (modulesNames != None and mod in modulesNames)):
            sampleDocument += "\\section {Module " + mod + "}\n"
            sampleDocument += "\\begin{itemize}\n"
            for function, result in modulesList[mod].samples().items():
                if isinstance(result, tuple) :
                    result, addMathEnv = result
                else :
                    addMathEnv = True
                #if mod in ["exDroite", "exEquation"]:
                if addMathEnv :
                    sampleDocument +=  f"\\item {function} :\\\\ \n$${result}$$\n"
                else:
                    sampleDocument +=  f"\\item {function} :\\\\ \n{result}\n"
            sampleDocument += "\\end{itemize}\n"
    return sampleDocument

#getSamples()
#getSamples(["exFraction"])

document_content = getSamples(["exFonction"]) #["exExpLog"]
#document_content = automatisme.run()
pyperclip.copy(document_content)
print(document_content)
