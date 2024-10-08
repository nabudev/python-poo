class Persona:
    def __str__(self, nombre, edad):
        self.nombre= nombre
        self.edad= edad
        
    def comparar_edad(self, otra_persona):
        if self.edad>otra_persona.edad:
            return f'{self.nombre} es mayor que {otra_persona.nombre}'
        elif self.edad<otra_persona.edad:
            return f'{self.nombre} es menor que {otra_persona.nombre}'
        else:
            return f'{self.nombre} y {otra_persona.nombre} tienen la misma edad'

persona1=Persona("juan", 21)
persona2=Persona("nacho", 22)
print(persona1.comparar_edad(persona2))