import threading
import time
import RPi.GPIO as GPIO

class NavidadController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self._ultimo_boton = 0

        threading.Thread(target=self._loop_sensor, daemon=True).start()
        threading.Thread(target=self._loop_boton, daemon=True).start()

    def _loop_sensor(self):
        while True:
            t, h = self.model.leer_clima()
            self.view.after(0, self.view.actualizar_datos, t, h)
            time.sleep(1.2)

    def _loop_boton(self):
        while True:
            if GPIO.input(self.model.pin_boton) == GPIO.LOW:
                ahora = time.time()
                if (ahora - self._ultimo_boton) > 0.25:  # debounce
                    self._ultimo_boton = ahora
                    self._on_boton_presionado()
            time.sleep(0.02)

    def _on_boton_presionado(self):
        self.model.set_led(True)
        self.view.after(0, self.view.animar_led, True)
        self.model.reproducir_audio("jingle_bells.mp3")

        def _apagado():
            self.model.set_led(False)
            self.view.animar_led(False)
        self.view.after(5000, _apagado)
