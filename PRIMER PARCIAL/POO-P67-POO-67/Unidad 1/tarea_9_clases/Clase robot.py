class Robot:
    def __init__(self, Nombre, Tipo, Bateria):
        self.Nombre=Nombre
        self.Tipo=Tipo
        self.Bateria=Bateria
    def desplazarse(self):
        print("El robot se está desplazando")
    def ejecutar_accion(self):
        print("El robot está ejecutando")
    def verificar_sistema(self):
        print("El robot está verificando sistemas")
        
Registro=Robot("RBX-001", "Doméstico", "75.0%")
print("Nombre: ",end="")
print(Registro.Nombre)
print("Tipo: ",end="")
print(Registro.Tipo)
print("Bateria: ", end="")
print(Registro.Bateria)