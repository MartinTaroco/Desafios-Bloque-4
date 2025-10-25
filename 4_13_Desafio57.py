#Implementa una clase Poeta que herede de Autor y tenga un atributo para el tipo de poesía que escribe.

class Autor:
    def __init__(self, nombre):
        self.nombre = nombre
        
        

class Poeta(Autor):
  def __init__(self, nombre, genero):
     super().__init__(nombre)
     self.genero = genero
     
  def mostras_poeta(self):
    print(self.nombre)
    print(self.genero)
    
    
fulano = Poeta("Martin", "Drama")


fulano.mostras_poeta()