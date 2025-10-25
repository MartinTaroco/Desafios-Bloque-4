#Crea una función que tome un objeto Autor y devuelva una lista de todos los títulos de libros escritos por el autor. Asegúrate de que la lista de libros sea accesible solo a través de métodos de la clase Autor.

class Autor:
    def __init__(self, nombre, nacionalidad):
        self.__nombre = nombre
        self.__nacionalidad = nacionalidad
        self.__lista = []

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nacionalidad(self):
        return self.__nacionalidad

    def set_nacionalidad(self, nacionalidad):
        self.__nacionalidad = nacionalidad
    
    def get_lista(self):
      return self.__lista
    
    def set_lista(self, libro):
      self.__lista.append(libro)
      

def obtener_libros(autor):
  print(autor.get_lista())

      
fulano = Autor("Martin", "Uruguayo")

fulano.set_lista("librillo")
fulano.set_lista("librillo 2")
print(fulano.get_lista())

obtener_libros(fulano)
