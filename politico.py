class Politico():
    def __init__(self,nombre,pais,partido_politico,edad):
        self.nombre=nombre
        self.pais=pais
        self.partido_politica=partido_politico
        self.edad=edad
    def representar(self):
        pass
    def getPais(self):
        return self.pais
    def setNombre(self,nombre):
        self.nombre=nombre

