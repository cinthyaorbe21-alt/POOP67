class Cine:
    def __init__(self, Nombre, Direccion, Aforo):
        self.Nombre=Nombre
        self.Direccion=Direccion
        self.Aforo=Aforo
    def abrir(self):
        pass
    def iniciar_funcion(self):
        pass
    def emitir_boleto(self):
        pass
    
Encontrar=Cine("Cinemark", "Av. America 102", "950 personas")
print("Nombre: ",end="")
print(Encontrar.Nombre)
print("Dirección: ",end="")
print(Encontrar.Direccion)
print("Aforo máximo: ", end="")
print(Encontrar.Aforo)
