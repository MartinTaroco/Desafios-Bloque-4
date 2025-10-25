#Crea una clase Libro con atributos como título, género e ISBN. ¿Cómo podrías relacionar esta clase con la clase Autor?

#Respuesta, voy a hacer que el metodo en la clase de agregar y eliminar libro, lea los objetos creados por la clase libro y saque de ahí el titulo.

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
     

fulano = Autor("Fulano", "Cubano")
La_Odisea = Libro("La odisea", "Mitologico", 123456)

fulano.agregar_libros(La_Odisea)        #Acá se relacionan, a un metodo de la clase autor le paso un objeto de la

fulano.mostrar_autor()