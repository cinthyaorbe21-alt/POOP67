# controlador/controlador.py

from modelo.led import LED
from vista.vista import mostrar_estado_led

class ControladorLED:
    def __init__(self):
        self.led = LED()

    def procesar_comando(self, comando):
        comando = comando.upper()

        if comando == "LED ON":
            self.led.encender()
        elif comando == "LED OFF":
            self.led.apagar()
        else:
            return "Comando no reconocido"

        estado = self.led.get_estado()
        return mostrar_estado_led(estado)

