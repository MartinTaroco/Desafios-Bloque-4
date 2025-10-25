#Considera cómo podrías implementar una biblioteca que almacene múltiples autores y libros. ¿Qué estructuras de datos usarías?
class Autor:
    # Constructor de la clase
    def __init__(self, nombre="", nacionalidad=""):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.libros = []
        
        
    # Método para mostrar los detalles del autor
    def mostrar_autor(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nacionalidad: {self.nacionalidad}")
        print(f"Sus libros son {self.libros}")

    def agregar_libros(self, libro):    
        self.libros.append(libro.titulo)
        print("Se agrego con exito!")
        
        
    def elimino_libros(self, libro):    
        self.libros.remove(libro.titulo)
        print("Se elimino con exito!")    

class Libro:
  def __init__(self, titulo, genero, ISBN):
     self.titulo = titulo
     self.genero = genero
     self.ISBN = ISBN
     
class Biblioteca:
  def __init__(self):
     self.biblioteca = []
     
  def mostrar_biblioteca(self):
    print(f"La Biblioteca tiene estos libros: {self.biblioteca}")
    
  def agregar_libros(self,autor, libro):
    self.biblioteca.append((autor.nombre, libro. titulo))      #Agrega a la lista una tupla, (autor, libro)
     
  def eliminar_libros(self,autor, libro):
    self.biblioteca.remove((autor.nombre, libro.titulo))     


fulano = Autor("Fulano", "Cubano")

La_Odisea = Libro("La odisea", "Mitologico", 123456)

fulano.agregar_libros(La_Odisea)        #Acá se relacionan, a un metodo de la clase autor le paso un objeto de la

fulano.mostrar_autor()

biblioteca = Biblioteca()   #Creamos la biblioteca

biblioteca.agregar_libros(fulano, La_Odisea)     #Le paso el objeto autor y el objeto libro
biblioteca.mostrar_biblioteca()