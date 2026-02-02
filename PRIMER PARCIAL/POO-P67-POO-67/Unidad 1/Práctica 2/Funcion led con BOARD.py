#codigo 6 funcion de led con puerto BOARD
import RPi.GPIO as GPIO
import time

def lbo(pin, modo):
  GPIO.setwarnings(False)
  GPIO.setmode(modo)
  GPIO.setup(pin, GPIO.OUT)

  while True:
    GPIO.output(pin, True)
    times.sleep(1)
    GPIO.output(pin, False)
    time,sleep(1)
lbo(12, GPIO.BOARD)
