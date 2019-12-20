class Cuaderno():
    def __init__(self,nro_hojas,diseno,escritorio,tamano,peso):
         self.nro_hojas=nro_hojas
         self.diseno=diseno
         self.escritorio=escritorio
         self.tamano=tamano
         self.peso=peso
    def rayar(self):
        return " el diseño del cuaderno es "+self.diseno+" y se encuentra en el escritorio el cual tiene  "+self.escritorio.nro_cajones

    def setDiseno(self,diseno):
        self.diseno=diseno
    def getMateriales(self):
        return self.materiales