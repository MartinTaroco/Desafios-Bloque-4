#En el siguiente codigo voy a compactar del desafio 47 al 51, cumpliendo con todo lo pedido

class Libro:           #Creadir de libros
  def __init__(self, titulo, autor, isbn):
    self._titulo = titulo
    self._autor = autor
    self._isbn = isbn

  def get_titulo(self):
    return self._titulo
  
  def get_autor(self):
    return self._autor
  
  def get_isbn(self):
    return self._isbn

  def set_titulo(self, titulo_nuevo):
    self._titulo = titulo_nuevo      
    
  def set_autor(self, autor_nuevo):
    self._autor = autor_nuevo      
  
  def set_isbn(self, isbn_nuevo):
    self._isbn = isbn_nuevo      

class Autor:
  def __init__(self, nombre, nacionalidad, edad, bestseller):
    self.nombre = nombre
    self.nacionalidad = nacionalidad
    self.edad = edad
    self.bestseller = bestseller
    self.libros_escritos = []


  def descripcion(self):
    print(f"El auto se llama {self.nombre}, su nacionaldiad es {self.nacionalidad} tiene {self.edad} años y su BestSeller es {self.bestseller}")
    
  def agregar_libro(self,libro):
    self.libros_escritos.append(libro)
    
  def eliminar_libro(self,libro):
    self.libros_escritos.remove(libro)
    
  def mostrar_libros(self):
    print (self.libros_escritos)
    
    
class Biblioteca:               #Clase que guardara lista de autores y libros
  def __init__(self):
    self.lista_autores= []
    self.lista_libros = []
  
  
  def agregar_autor(self,autor):
    self.lista_autores.append((autor.nombre,autor.nacionalidad,autor.edad))  
 
  def eliminar_autor(self, autor):
     for i in self.lista_autores:
      if i[0] == autor.nombre:
        self.lista_autores.remove(i) 
  def mostrar_autores(self):
    print(self.lista_autores)
    
martin = Autor("Martin Rodriguez", "Uruguayo", 53, "El mejor libro de martin")
libro1 = Libro("libro de martin", "Martin Rodriguez", 1234567813)
martin.agregar_libro(libro1._titulo)  #El objeto martin de la clase Autor, toma el titulo del objeto libro1 creado en la clase Libro

martin.mostrar_libros()


biblioteca = Biblioteca()

biblioteca.agregar_autor(martin)

biblioteca.mostrar_autores()

biblioteca.eliminar_autor(martin)

biblioteca.mostrar_autores()