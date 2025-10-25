#Crea una clase Musico que tenga un método instrumento y crea dos subclases Guitarrista y Baterista que sobrescriban el método instrumento. Instancia objetos de estas clases y demuestra el polimorfismo.



class Musico:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad
    
  def instrumento(self):
    print("Tocando un isntrumento")
    
    
class Guitarrista(Musico):
  def __init__(self, nombre, edad, herramienta):
    super().__init__(nombre, edad)
    self.herramienta = herramienta
  
  
  def instrumento(self):
    print(f"Tocando la {self.herramienta}")
    
class Baterista(Musico):
  def __init__(self, nombre, edad, herramienta):
    super().__init__(nombre, edad)
    self.herramienta = herramienta
  
  
  def instrumento(self):
    print(f"Tocando la {self.herramienta}")
    

martin = Musico("Martin", 24)

pedro = Guitarrista("pedro", 24, "Guitarra")
juan = Baterista("juan", 22, "Bateria")


martin.instrumento()
pedro.instrumento()
juan.instrumento()