class Control():
    def __init__(self,nro_pilas,nro_botones,televisor,tipo_placa,peso):
         self.nro_pilas=nro_pilas
         self.nro_botones=nro_botones
         self.televisor=televisor
         self.tipo_placa=tipo_placa
         self.peso=peso
    def comprar(self):
        return " el peso del televisor es  "+self.peso+" y el tipo de placa es  "+self.televisor.tipo_placa

    def setpeso(self,peso):
        self.peso=peso
    def getNro_pilas(self):
        return self.nro_pilas