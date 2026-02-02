import RPi.GPIO as GPIO


class View:

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        self.LED_ROJO = 17
        self.LED_VERDE = 27

        GPIO.setup(self.LED_ROJO, GPIO.OUT)
        GPIO.setup(self.LED_VERDE, GPIO.OUT)

    def estado_normal(self, temp, hum):
        GPIO.output(self.LED_ROJO, GPIO.LOW)
        GPIO.output(self.LED_VERDE, GPIO.HIGH)
        print(f"NORMAL | Temp: {temp:.1f}°C | Hum: {hum:.1f}%")

    def estado_critico(self, mensaje):
        GPIO.output(self.LED_VERDE, GPIO.LOW)
        GPIO.output(self.LED_ROJO, GPIO.HIGH)
        print(f"{mensaje}")

    def limpiar(self):
        GPIO.cleanup()
