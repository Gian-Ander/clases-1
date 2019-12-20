import escritoiro
import  cuaderno
import os
val=os.sys.argv[1]
tip=os.sys.argv[2]
bil=escritoiro.Escritorio(tip,0.2,2,5)
mon=cuaderno.Cuaderno(0.1,"oro",bil,"peru",val)
print(mon.rayar())