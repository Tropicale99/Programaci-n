class Padre(object): #clase base se le pone object
       
    def __init__(self, nombre: str, apellido: str, edad: float ) -> None: 
        #si le cambio a flotante la edad NO se pone entero  
        self.nombre_padre = nombre
        self.apellido_padre = apellido 
        self.edad = edad
    def saludar(self):
        print(f"Hola {self.nombre_padre} {self.apellido_padre} tienes {self.edad} años")


instance_a = Padre ("Antonio","Lozoya",45.5)  #porque lo trae como entero si es flotante?
instance_a.saludar()

padre2 = Padre("Fernando","Nava",35)
padre2.saludar()

# padre3 = input()
