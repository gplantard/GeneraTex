from Trinome import Trinome
import derive_st2s

import pyperclip

f = Trinome.fromFactor(-3,-2,2)


print (f.toString())
print (f.toString(Trinome.Forme.FACTORISEE))
print(f.getPrimitive())
