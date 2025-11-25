class Telefono:
    def __init__(self, Marca, Imei, SO):
        self.Marca=Marca
        self.Imei=Imei
        self.SO=SO
    def encender(self):
        pass
    def apagar(self):
        pass
    def reiniciar(self):
        pass
        
Nombrar=Telefono("Samsung", "352089654123", "Android 14")
print("Fabricante: ",end="")
print(Nombrar.Marca)
print("Serie: ",end="")
print(Nombrar.Imei)
print("Sistema: ", end="")
print(Nombrar.SO)
