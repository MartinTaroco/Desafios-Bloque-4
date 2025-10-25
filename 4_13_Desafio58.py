#Crea una clase Bibliotecario que herede de Usuario y tenga atributos específicos como sección y años_experiencia.

class Usuario:
  def __init__(self, nombre, apellido):
    self.nombre = nombre
    self.apellido = apellido
    
    

class Bibliotecario(Usuario):
  def __init__(self, nombre, apellido, seccion, años_experiencia):
    super().__init__(nombre, apellido)
    self.seccion = seccion
    self.años_experiencia = años_experiencia
    
    
    
    
    
    
