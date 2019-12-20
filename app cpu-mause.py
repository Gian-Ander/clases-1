import cpu
import  mause
import os
val=os.sys.argv[1]
tip=os.sys.argv[2]
bil=cpu.Cpu(tip,0.2,2,5)
mon=mause.Mause(0.1,"oro",bil,"peru",val)
print(mon.indicar())