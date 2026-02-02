#codigo 10 Clase boton
import RPi.GPIO as GPIO
import time

class butBoard:
  def __init__(self, pin, boton):
    self.pin=pin
    self.boton=boton
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(self.pin, GPIO.OUT)
    GPIO.setup(self.boton, GPIO.IN)
  def encender(self):
    while True:
      if GPIO.input(self.boton):
        GPIO.output(self.pin, False)
      else:
        GPIO.output(self.pin, True)
    GPIO.cleanup()
board=butBoard(12, 22)
board.encender()
