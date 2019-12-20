class Mochila():
    def __init__(self,materiales,nro_bolsillos,nro_cierres,tipo_costura):
        self.materiales=materiales
        self.nro_bolsillos=nro_bolsillos
        self.nro_cierres=nro_cierres
        self.tipo_costura=tipo_costura
    def guardar_(self):
        pass
    def getMateriales(self):
        return self.nro_bolsillos
    def setNro_bolsillos(self,nro_bolsillos):
        self.nro_bolsillos=nro_bolsillos
