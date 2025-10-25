#En este desafío, vamos a extender la clase Libro para crear una subclase LibroEspecializado. Un LibroEspecializado, además de tener un título y un autor, también tiene un campo de estudio y un nivel de especialización (básico, intermedio, avanzado).


class Libro:
  def __init__(self, titulo, autor):
    self.titulo = titulo
    self.autor = autor
    
    
class LibroEspecializado(Libro):
  def __init__(self, titulo, autor, campo_de_estudio, nivel_de_especialziacion):
    super().__init__(titulo, autor)
    self.campo_de_estudio = campo_de_estudio
    self.nivel_de_especializacion = nivel_de_especialziacion
    

