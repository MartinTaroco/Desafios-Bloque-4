#Implementa una clase EscritorAcademico que herede de Escritor y Academico, e incluya un método adicional para publicar artículos académicos. Asegúrate de utilizar correctamente la función super() para inicializar las clases base.


class Escritor:
  def __init__(self, nombre):
    self.nombre = nombre
    
class Academico:
  def __init__(self, universidad):
    self.universidad = universidad
    

class EscritorAcademica(Escritor, Academico):
    def __init__(self, nombre, universidad, prestigio):
     Escritor.__init__(self, nombre)
     Academico.__init__(self, universidad)
     self.prestigio = prestigio
    
    
    def mostrar_info(self):
      print(self.nombre)
      print(self.universidad)
      print(self.prestigio)
      
      
Mario = EscritorAcademica("Mario", "Harvard", "Malo")

Mario.mostrar_info()