class Agenda:
    def __init__(self):
        self.contactos=[]
        
    def agregar_contacto(self, nombre, telefono, email):
        self.contactos.append({'nombre': nombre, 'telefono': telefono, "email": email})
        
    def listar_contactos(self):
        self.listar_contactos
        
    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto [nombre]== nombre:
                return contacto
            return "contacto no encontrado"
        
    def editar_contacto (self, nombre, nuevo_nombre, nuevo_telefono, nuevo_email):
        for contacto in self.contactos:
            if contacto['nombre']==nombre:
                contacto["telefono"]= nuevo_telefono
                contacto["email"]= nuevo_email
                return "contacto actualizado"
            return "contacto no encontrado"
        
agenda=Agenda()
agenda.agregar_contacto("nahuel", "3863434058", "floresnahuel026@gmail.com")
print(agenda.listar_contactos())
print(agenda.buscar_contacto())
agenda.editar_contacto("nahuel2", "3863405869", "nabudev01@gmail.com")
print(agenda.listar_contactos())