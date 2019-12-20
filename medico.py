class Medico():
    def __init__(self,edad,test,politico,talla,nombre):
         self.edad=edad
         self.test=test
         self.politico=politico
         self.talla=talla
         self.nombre=nombre
    def curar(self):
        return " el doctor es de  "+self.talla+"  y el nombre del politico es"+self.politico.nombre

    def setTalla(self,talla):
        self.talla=talla
    def getEdad(self):
        return self.edad