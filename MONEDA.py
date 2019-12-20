class Moneda():
    def __init__(self,dimenciones,materiales,billetera,pais,valor):
         self.dimenciones=dimenciones
         self.materiales=materiales
         self.billetera=billetera
         self.pais=pais
         self.valor=valor
    def comprar(self):
        return " la moneda de valor "+self.valor+" esta guardada en una billetra cuyo material es "+self.billetera.tipo_costura

    def setValor(self,valor):
        self.valor=valor
    def getMateriales(self):
        return self.materiales