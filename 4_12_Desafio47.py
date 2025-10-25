#Amplía la clase Autor para incluir una lista de libros escritos por el autor. Implementa métodos para agregar y eliminar libros de esta lista.

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
        self.libros.append(libro)
        print("Se agrego con exito!")
        
        
    def elimino_libros(self, libro):    
        self.libros.remove(libro)
        print("Se elimino con exito!")    
        
fulano = Autor("fulano", "cubano")

fulano.mostrar_autor()
fulano.agregar_libros("La odisea")
fulano.mostrar_autor()