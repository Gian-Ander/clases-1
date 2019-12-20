import televisor
import  control
import os
val=os.sys.argv[1]
tip=os.sys.argv[2]
bil=televisor.Televisor(tip,0.2,2,5)
mon=control.Control(0.1,"oro",bil,"peru",val)
print(mon.comprar())