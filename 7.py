class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1= lado1
        self.lado2= lado2
        self.lado3= lado3
    
    def tipo_triangulo(self):
        if self.lado1==self.lado2==self.lado3:
            return "Equilatero"
        elif self.lado1==self.lado2 or self.lado2==self.lado3 or self.lado1==self.lado3:
            return "Isosceles"
        else:
            return "Escaleno"
        
triangulo= Triangulo(4,6,8)
print(triangulo.tipo_triangulo())