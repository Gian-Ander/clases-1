import BILLETRA
import  MONEDA
import os
val=os.sys.argv[1]
tip=os.sys.argv[2]
bil=BILLETRA.Billetera(tip,0.2,2,5)
mon=MONEDA.Moneda(0.1,"oro",bil,"peru",val)
print(mon.comprar())