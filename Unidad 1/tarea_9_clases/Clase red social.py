class Red_Social:
    def __init__(self, Nombre, Version, Contenido):
        self.Nombre=Nombre
        self.Version=Version
        self.Contenido=Contenido
    def enviar_snap(self):
        pass
    def usar_filtros(self):
        pass
    def ver_historial(self):
        pass
        
App=Red_Social("Snapchat", "12.63.0.48", "Fotos y videos efimeros")
print("Nombre: ",end="")
print(App.Nombre)
print("Versión: ",end="")
print(App.Version)
print("Tipo de contenido: ", end="")
print(App.Contenido)
