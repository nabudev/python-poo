class Alumno:
    def __init__(self, nombre, nota):
        self.nombre= nombre
        self.nota= nota
        
        
    def mostrar_resultado(self):
        if self.nota>=6:
            return f'{self.nombre} ha aprobado con {self.nota}'
        else:
            return f'{self.nombre} desaprobo con {self.nota}'
        
alumno= Alumno("nacho", 1)
print(alumno.mostrar_resultado())