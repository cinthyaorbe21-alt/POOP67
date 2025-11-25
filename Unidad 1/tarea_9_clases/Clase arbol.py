class Arbol:
    def __init__(self, Tipo, Edad, Ubicacion):
        self.Tipo=Tipo
        self.Edad=Edad
        self.Ubicacion=Ubicacion
    def fotosintesis(self):
        pass
    def extender_ramas(self):
        pass
    def generar_semillas(self):
        pass
        
Plantar=Arbol("Roble", "15 años", "Parque Central")
print("Tipo: ",end="")
print(Plantar.Tipo)
print("Edad: ",end="")
print(Plantar.Edad)
print("Ubicación: ", end="")
print(Plantar.Ubicacion)
