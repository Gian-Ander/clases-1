import persona
import  perro
import os
val=os.sys.argv[1]
tip=os.sys.argv[2]
bil=persona.Persona(tip,0.2,2,5)
mon=perro.Perro(0.1,"oro",bil,"peru",val)
print(mon.comprar())