#Añade un método biografia a la clase Autor y sobrescríbelo en la clase Escritor. Instancia un objeto de la clase Escritor y muestra cómo se puede acceder al método biografia de ambas clases.

class Autor:
  def __init__(self, nombre, apellido):
    self.nombre = nombre
    self.apellido = apellido
    
  def biografia(self):
    print(f"Autor {self.nombre} {self.apellido}")


class Escritor:
  def __init__(self, nombre, apellido):
    self.nombre = nombre
    self.apellido = apellido
    
  def biografia(self):
    print(f"Escritor {self.nombre} {self.apellido}")
    

martin = Escritor("martin", "taroco")
martin.biografia()

Autor.biografia(martin)