class IOT:
    def __init__(self, Codigo, TipoDispositivo, ZonaInstalada):
        self.Codigo=Codigo
        self.TipoDispositivo=TipoDispositivo
        self.ZonaInstalada=ZonaInstalada
    def encender(self):
        print("El dispositivo está encendido")
    def apagar(self):
        print("El dispositivo está apagado")
    def enviar_datos(self):
        print("El dispositivo esta enviando datos")
        
Rastreo=IOT("TMP2025", "Sensor de Temperatura", "Almacén Principal")
print("Codigo: ",end="")
print(Rastreo.Codigo)
print("Tipo de dispositivo: ",end="")
print(Rastreo.TipoDispositivo)
print("Zona instalada: ", end="")
print(Rastreo.ZonaInstalada)
