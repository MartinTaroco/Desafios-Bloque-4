#Crea una clase Libro que tenga atributos privados para el título, autor y ISBN. Proporciona métodos getter y setter para cada atributo.

class Libro:
  def __init__(self, titulo, genero, ISBN):
     self.__titulo = titulo
     self.__genero = genero
     self.__ISBN = ISBN
     
  def get_nombre(self):
      return self.__titulo
    
  def set_nombre(self, titulo):
    self.__titulo = titulo
   
  def get_genero(self):
      return self.__genero
        
  def set_genero(self, genero):
    self.__genero = genero
    
    
  def get_ISBN(self):
      return self.__ISBN
    
  def set_ISBN(self, ISBN):
    self.__ISBN = ISBN

Odisea = Libro("La odisea", "mitologico", 1213313)

print(Odisea.get_nombre())