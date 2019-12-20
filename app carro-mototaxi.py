import carro
import  mototaxi
import os
val=os.sys.argv[1]
tip=os.sys.argv[2]
bil=carro.Carro(tip,0.2,2,5)
mon=mototaxi.Mototaxi(0.1,"oro",bil,"peru",val)
print(mon.comprar())