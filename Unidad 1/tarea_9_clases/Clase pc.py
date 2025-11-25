class PC:
    def __init__(self, Fabricante, Serie, Sistema):
        self.Fabricante=Fabricante
        self.Serie=Serie
        self.Sistema=Sistema
    def iniciar_sesion(self):
        pass
    def instalar_software(self):
        pass
    def actualizar_drivers(self):
        pass
        
Iniciar=PC("Dell", "Inspiron X15", "Windows 11")
print("Fabricante: ",end="")
print(Iniciar.Fabricante)
print("Serie: ",end="")
print(Iniciar.Serie)
print("Sistema: ", end="")
print(Iniciar.Sistema)
