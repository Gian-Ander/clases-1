import alicate
import  tornillo
import os
val=os.sys.argv[1]
tip=os.sys.argv[2]
bil=alicate.Alicate(tip,0.2,2,5)
mon=tornillo.Tornillo(0.1,"oro",bil,"peru",val)
print(mon.soportar())