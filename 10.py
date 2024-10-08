class Banco:
    def __init__(self, saldo_inicial=0):
        self.saldo= saldo_inicial
        
    def deposito(self, cantidad):
        self.saldo+= cantidad
        return f'Deposito realizado. Saldo actual {self.saldo}'
    
    def extraccion (self, cantidad):
        if cantidad > self.saldo:
            return "fondos insuficientes"
        else:
            self.saldo-=cantidad
            return f'Extraccion realizada. Saldo: {self.saldo}'
        
    def mostrar_saldo(self):
        return f'Saldo: {self.saldo}'
    

cuenta=Banco(500)
print(cuenta.deposito(100))
print(cuenta.extraccion(200))
print(cuenta.mostrar_saldo())