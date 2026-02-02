# modelo/led.py

class LED:
    def __init__(self):
        self.estado = False   # False = apagado, True = encendido

    def encender(self):
        self.estado = True

    def apagar(self):
        self.estado = False

    def get_estado(self):
        return "ENCENDIDO" if self.estado else "APAGADO"
