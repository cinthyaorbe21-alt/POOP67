#codigo 8 Funcion led con boton en puerto BOARD
import RPi.GPIO as GPIO
import time

def but_board(foco, but):
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(foco, GPIO.OUT)
  GPIO.setup(but, GPIO.IN)

  while True:
    if GPIO.input(but):
      GPIO.output(foco, False)
    else:
      GPIO.output(foco, True)
but_board(12, 22)
