class Libro():
    def __init__(self,portada,peso,mochila,edicion,materia):
         self.portada=portada
         self.peso=peso
         self.mochila=mochila
         self.edicion=edicion
         self.materia=materia
    def leer(self):
        return " la mochila tiene un peso de  "+self.peso+" y en ellla se llevan los libros de "+self.mochila.materiales

    def setPeso(self,peso):
        self.peso=peso
    def getEdicion(self):
        return self.edicion