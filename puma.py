class Billetera():
    def __init__(self,tipo_costura,peso,nro_bolsillos,nro_diviciones):
        self.tipo_costura=tipo_costura
        self.peso=peso
        self.nro_bolsillos=nro_bolsillos
        self.nro_diviciones=nro_diviciones
    def guardar_billetes(self):
        pass
    def getNro_bolsillos(self):
        return self.nro_bolsillos
    def setNro_bolsillos(self,nro_bolsillos):
        self.nro_bolsillos=nro_bolsillos
