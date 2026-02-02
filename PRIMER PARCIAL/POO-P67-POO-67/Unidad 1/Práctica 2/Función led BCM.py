#codigo 5 funcion de led con puerto BCM
import RPi.GPIO as GPIO
import time

def lbc(pin, modo):
  GPIO.setwarnings(False)
  GPIO.setmode(modo)
  GPIO.setup(pin, GPIO.OUT)

  while True:
    GPIO.output(pin, True)
    times.sleep(1)
    GPIO.output(pin, False)
    time.sleep(1)
lbc(18, GPIO.BCM)
