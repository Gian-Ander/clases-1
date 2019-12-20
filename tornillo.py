class Tornillo():
    def __init__(self,dimenciones,materiales,alicate,peso,nro_vueltas):
         self.dimenciones=dimenciones
         self.materiales=materiales
         self.alicate=alicate
         self.peso=peso
         self.nro_vueltas=nro_vueltas
    def soportar(self):
        return "el numero de vueltas del alicate es  "+self.nro_vueltas+" y el tipo de manijas es  "+self.alicate.tipo_manijas

    def setNro_vueltas(self,valor):
        self.valor=valor
    def getPeso(self):
        return self.peso