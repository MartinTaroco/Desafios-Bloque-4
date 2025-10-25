#Crea una jerarquía de clases para representar diferentes tipos de empleados en una biblioteca, utilizando herencia múltiple y composición. Por ejemplo, implementa clases como Empleado, Gerente, Tecnico, y Voluntario, donde Gerente y Tecnico hereden de Empleado, y algunos puedan tener roles adicionales mediante composición con otras clases como Administrador o Mantenimiento.

class Empleado:
  def __init__(self, nombre, edad, cedula):
    self.nombre= nombre
    self.edad = edad
    self.cedula = cedula


class Tecnico:
  def __init__(self, area, sucursal):
    self.area = area
    self.sucursal = sucursal
  
class Gerente(Empleado, Tecnico ):
  def __init__(self, nombre, edad, cedula, area, sucursal):
    Empleado.__init__(self,nombre, edad, cedula)
    Tecnico.__init__(self,area, sucursal)

  def mostrar_info(self):
    print(f"Gerente {self.nombre}, de {self.edad} años de edad, C.I: {self.cedula}, encargado del area {self.area} en la sucursal {self.sucursal}")
    
 

#Ejemplo de composición, se le pasa información de un técnico, porque el voluntario ayudará a ese técnico
class voluntario:
  def __init__(self, información):
    self.información = información #Se le pasará un objeto tecnico
    
  def mostrar_info (self):
      print(f"Este voluntario esta en el area {self.información.area} desempeñandose en la sucursal de {self.información.sucursal}")
    
  
      
martin = Gerente("MArtin", 24, 52285276, "Archivo", "Libertad")
martin.mostrar_info()

auxiliar = Tecnico("Limpieza", "Libertad")

roberto = voluntario(auxiliar)
roberto.mostrar_info()