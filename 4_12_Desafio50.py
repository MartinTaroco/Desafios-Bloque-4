#Piensa en otros atributos y métodos que podrías agregar a la clase Autor para hacerla más completa.
class Autor:
    # Constructor de la clase
    def __init__(self, nombre, nacionalidad, edad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.edad = edad

    # Método para mostrar los detalles del autor
    def mostrar_autor(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nacionalidad: {self.nacionalidad}")
        
    def saludar (self):
      print(f"Hola soy {self.nombre}, un gusto!")