#Reflexiona sobre cómo podrías implementar una función de búsqueda para encontrar un libro específico o autor en una biblioteca.

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

  def buscar_autor(self, autor):

      for i in self.biblioteca:
          if i[0] == autor.nombre:         #Iteramos en la biblioteca y nos fijamos si el primer elemento de cada tuple(nombre) coincide con el autor.
            print("Esta el autor")
          else:
            print("No esta ese autor")
  
  def buscar_libro(self, libro):  
      for i in self.biblioteca:
          if i[1] == libro.titulo:
            print("Esta el libro")
          else:
            print("No esta ese libro")
                    
            
            
            
fulano = Autor("Fulano", "Cubano")

La_Odisea = Libro("La odisea", "Mitologico", 123456)

fulano.agregar_libros(La_Odisea)        #Acá se relacionan, a un metodo de la clase autor le paso un objeto de la

fulano.mostrar_autor()

biblioteca = Biblioteca()   #Creamos la biblioteca

biblioteca.agregar_libros(fulano, La_Odisea)     #Le paso el objeto autor y el objeto libro
biblioteca.mostrar_biblioteca()

biblioteca.buscar_autor(fulano)
biblioteca.buscar_libro(La_Odisea)