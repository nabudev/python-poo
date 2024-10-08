class Calculadora:
    def __init__(self, a, b):
        self.a= a
        self.b= b
        
    def suma (self):
        return self.a+self.b
    
    def resta(self):
        return self.a-self.b
    
    def multiplicar (self):
        return self.a*self.b
    
    def division (self):
        return self.a/self.b if self.b!=0 else "No se puede dividir por 0"
    
    
calc= Calculadora(10,5)
print(calc.suma())
print(calc.resta())
print(calc.multiplicar())
print(calc.division())