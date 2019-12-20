class Mause():
    def __init__(self,nro_entradas,nro_placas,cpu,enfriador,peso):
         self.nro_entradas=nro_entradas
         self.nro_placas=nro_placas
         self.cpu=cpu
         self.enfriador=enfriador
         self.peso=peso
    def indicar(self):
        return " el cpu tiene de peso  "+self.peso+" y el numero de entradas es  "+self.cpu.tipo_entrada

    def setPeso(self,valor):
        self.peso=peso
    def getNro_placas(self):
        return self.nro_placas