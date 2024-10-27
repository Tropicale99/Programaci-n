from padre import Padre

class Hijo(Padre):
    def __init__(self, nombre: str, apellido: str, edad: int) -> None:
        self.nombre_hijo = nombre
        self.apellido_hijo = apellido
        self.edad = edad
    def saludar(self):
        print(f"Hola {self.nombre_hijo} {self.apellido_hijo} tienes {self.edad} años")

instance_c = Hijo ("Alejandra","Lozoya",25)  
instance_c.saludar()