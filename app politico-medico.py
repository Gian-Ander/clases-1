import politico
import  medico
import os
val=os.sys.argv[1]
tip=os.sys.argv[2]
bil=politico.Politico(tip,0.2,2,5)
mon=medico.Medico(0.1,"oro",bil,"peru",val)
print(mon.curar())