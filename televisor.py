class Televisor():
    def __init__(self,tipo_placa,tipo_pantalla,nro_parlantes,brillo):
        self.tipo_placa=tipo_placa
        self.tipo_pantalla=tipo_pantalla
        self.nro_parlantes=nro_parlantes
        self.brillo=brillo
    def proyecta(self):
        pass
    def getBrillo(self):
        return self.brillo
    def setTipo_pantalla(self,tipo_pantalla):
        self.tipo_pantalla=tipo_pantalla

