import RPi.GPIO as GPIO
import time

class SeguridadModel:
    def __init__(self, pin_led_ok=18, pin_led_err=23, pin_pir=4):
        self.pin_led_ok = pin_led_ok
        self.pin_led_err = pin_led_err
        self.pin_pir = pin_pir

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin_led_ok, GPIO.OUT)
        GPIO.setup(self.pin_led_err, GPIO.OUT)
        GPIO.setup(self.pin_pir, GPIO.IN)

        self.ultimo_valor = None
        self.ultimo_tiempo = time.time()

    def leer_sensor(self):
        try:
            valor = GPIO.input(self.pin_pir)
            ahora = time.time()

            # --- Bloque 1: Lectura no nula ---
            assert valor is not None, "Lectura nula del PIR"

            # --- Bloque 2: Valor válido (0 o 1) ---
            assert valor in [0, 1], f"Valor inválido del PIR: {valor}"

            # --- Bloque 3: Evitar rebotes (cambios demasiado rápidos) ---
            if self.ultimo_valor is not None and valor != self.ultimo_valor:
                assert (ahora - self.ultimo_tiempo) > 0.2, "Cambio demasiado rápido (rebote detectado)"

            # Actualizar estado
            self.ultimo_valor = valor
            self.ultimo_tiempo = ahora

            return valor

        except AssertionError as e:
            raise RuntimeError(f"Error de integridad: {e}")

    def activar_led_ok(self, estado=True):
        GPIO.output(self.pin_led_ok, GPIO.HIGH if estado else GPIO.LOW)

    def activar_led_err(self, estado=True):
        GPIO.output(self.pin_led_err, GPIO.HIGH if estado else GPIO.LOW)

    def apagar(self):
        GPIO.cleanup()
