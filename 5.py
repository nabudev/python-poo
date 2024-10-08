class Persona:
    def __init__(self, nombre, edad):
        self.nombre= nombre
        self.edad=edad
    
    def mayor_edad(self, otra_persona):
        return max(self.edad, otra_persona)
    
    
persona1= Persona("nahuel", 22)
persona2= Persona("ali", 26)
print(persona1.mayor_edad(persona2))