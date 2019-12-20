class Escritorio():
    def __init__(self,nro_cajones,materiales,peso,forma):
        self.nro_cajones=nro_cajones
        self.peso=peso
        self.materiales=materiales
        self.forma=forma
    def sostener(self):
        pass
    def getForma(self):
        return self.forma
    def setMateriales(self,materiales):
        self.materiales=materiales

