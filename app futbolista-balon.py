import futbolista
import  balon
import os
val=os.sys.argv[1]
tip=os.sys.argv[2]
bil=futbolista.Futbolista(tip,0.2,2,5)
mon=balon.Balon(0.1,"oro",bil,"peru",val)
print(mon.divierte())