import mochila
import  libro
import os
val=os.sys.argv[1]
tip=os.sys.argv[2]
bil=mochila.Mochila(tip,0.2,2,5)
mon=libro.Libro(0.1,"oro",bil,"peru",val)
print(mon.leer())