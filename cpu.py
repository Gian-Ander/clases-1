class Cpu:
    def __init__(self,tipo_entrada,peso,forma,tipo_placa):
        self.tipo_entrada=tipo_entrada
        self.peso=peso
        self.forma=forma
        self.tipo_placa=tipo_placa
    def indicar(self):
        pass
    def getPeso(self):
        return self.peso
    def setTipo_entrada(self,tipo_entrada):
        self.tipo_entrada=tipo_entrada



