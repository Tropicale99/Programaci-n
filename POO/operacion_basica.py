

class OperacionesBasicas(object):
    #constructor
    def __init__(self, number_one: float, number_two:float) -> None: 
        self.number_one = number_one
        self.number_two = number_two
        
#que y como es el cuerpo
#una interface se llega por la hernencia

    def sumar(self)-> int:
        result = self.number_one + self.number_two
        return result
        
    def restar(self)-> str:
        result = self.number_one - self.number_two
        return result

    def dividir(self)-> float:
        result = self.number_one / self.number_two
        return result
    
    def multiplicar (self)-> float:
        result = self.number_one * self.number_two
        return result

