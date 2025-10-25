#Implementa la clase Autor con métodos getter y setter utilizando decoradores @property para manejar los atributos privados nombre y nacionalidad.

class Autor:
    def __init__(self, nombre, nacionalidad):
        self.__nombre = nombre
        self.__nacionalidad = nacionalidad
        self.__lista = []

    @property
    def nombre(self):
      return self.__nombre
    
    @property
    def nacionalidad(self):
      return self.__nacionalidad
    
    
    @nombre.setter
    def nombre(self, nombre):
      self.__nombre = nombre    
    
    @nacionalidad.setter
    def nacionalidad(self, nacionalidad):
      self.__nacionalidad = nacionalidad 
    
fulano = Autor("Martin", "Uruguayo")

print(fulano.nombre)
fulano.nombre = "Pedro"
print(fulano.nombre)