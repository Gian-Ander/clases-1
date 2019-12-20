class Mototaxi():
    def __init__(self,nro_asientos,nro_cambios,carro,nro_espejos,valor):
         self. nro_asientos=nro_asientos
         self.nro_cambios=nro_cambios
         self.carro=carro
         self.nro_espejos=nro_espejos
         self.valor=valor
    def comprar(self):
        return " EL CARRO ES DE VALOR  "+self.valor+" Y EL TIPO DE CARBURADOR DEL AUTO "+self.carro.tipo_carburador

    def setValor(self,valor):
        self.valor=valor
    def getNro_espejos(self):
        return self.nro_espejos