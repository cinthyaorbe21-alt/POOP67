#codigo 7 Funcion led con boton en puerto BCM
import RPi.GPIO as GPIO
import time

def but_bcm(foco, but):
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(foco, GPIO.OUT)
  GPIO.setup(but, GPIO.IN)

  while True:
    if GPIO.input(but):
      GPIO.output(foco, False)
    else:
      GPIO.output(foco, True)
but_bcm(18, 25)
