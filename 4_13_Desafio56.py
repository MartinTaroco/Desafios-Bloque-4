#Desarrolla una función que reciba una lista de objetos Autor y devuelva el autor que ha escrito el mayor número de libros. Utiliza el encapsulamiento para acceder a la información necesaria de cada objeto Autor.
 
class Autor:
    def __init__(self, nombre, nacionalidad, cantidad_obras):
        self.__nombre = nombre
        self.__nacionalidad = nacionalidad
        self.__cantidad_obras = cantidad_obras
        self.__lista = []

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nacionalidad(self):
        return self.__nacionalidad

    def set_nacionalidad(self, nacionalidad):
        self.__nacionalidad = nacionalidad
    
    def get_cantidad_obras(self):
        return self.__cantidad_obras

    def set_cantidad_obras(self, obras):
        self.__cantidad_obras = obras
    
    
    
    def get_lista(self):
      return self.__lista
    
    def set_lista(self, libro):
      self.__lista.append(libro)
      

def obtener_libros(autor):
  print(autor.get_lista())

      
fulano = Autor("Martin", "Uruguayo", 22)
mengano = Autor("Martin", "Uruguayo", 23)
Ciclano = Autor("pipi", "Cucu", 3)
Lista_autores = [fulano, mengano]

def mas_obras(lista):
  max = 0
  autor = ""
  for i in lista:
    cantidad = i.get_cantidad_obras()
    if cantidad > max:
      max = cantidad
      autor = i.get_nombre()
          
  print(f"El autor con mas obras es: {autor} y tiene una cntidad de {max} obras")

mas_obras(Lista_autores)