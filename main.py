#import generate2nd
#import generateTermEsSpe
#import automatisme

import pyperclip

import exMatrice
import exEquation
import exDroite

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
                sampleDocument +=  f"\\item {function} :\\\\ \n{result}\n"
            sampleDocument += "\\end{itemize}\n"
    print (sampleDocument)

    pyperclip.copy(sampleDocument)

    return sampleDocument

getSamples()
#getSamples(["exDroite"])