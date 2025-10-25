#Modifica la clase Autor para que pueda tener una lista de libros escritos por el autor. Proporciona un método para agregar libros a esta lista.

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
      
      

fulano = Autor("Martin", "Uruguayo")

fulano.set_lista("librillo")
print(fulano.get_lista())
