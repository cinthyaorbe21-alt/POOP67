#codigo 9 Clase led
import RPi.GPIO as GPIO
import time

class ledBCM:
  def __init__(self, pin):
    self.pin=pin
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.pin, GPIO.OUT)
  def parpadear(self):
    while True:
      GPIO.output(self.pin, True)
      time.sleep(1)
      GPIO.output(self.pin, False)
      time.sleep(1)
  GPIO.cleanup()
led=ledBCM(18)
led.parpadear()
