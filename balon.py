class Balon():
    def __init__(self,dimenciones,diseno,futbolista,peso,color):
         self.dimenciones=dimenciones
         self.diseno=diseno
         self.futbolitsa=futbolista
         self.peso=peso
         self.color=color
    def divierte(self):
        return " el judagor es "+self.peso+" y la edad de futbolista es de  "+self.futbolitsa.edad

    def setPeso(self,peso):
        self.peso=peso
    def getColor(self):
        return self.color