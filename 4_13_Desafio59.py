#Diseña una clase LibroDigital que herede de Libro y añada atributos como formato (e.g., PDF, EPUB) y tamaño_archivo. Además, implementa una subclase EBook que sobrescriba un método para mostrar información específica, como enlaces de descarga.

class Libro:
  def __init__(self, titulo, genero, ISBN):
     self.titulo = titulo
     self.genero = genero
     self.ISBN = ISBN
     
  

class LibroDigital(Libro):
  def __init__(self, titulo, genero, ISBN, formato):
    super().__init__(titulo, genero, ISBN)
    self.formato = formato
   
  def mostrar_info(self):
    print(self.titulo)
    print(self.genero)
    print(self.ISBN)
    print(self.formato)
    
     
  

class Ebook(LibroDigital):
    def __init__(self, titulo, genero, ISBN, formato):
      super().__init__(titulo, genero, ISBN, formato)
      self.formato = formato
         
    def mostrar_info(self):
      print(self.formato)
      return super().mostrar_info()
      
      
      
Pipi = Ebook("pipi", "Drama", 121231, "PDF")


Pipi.mostrar_info()