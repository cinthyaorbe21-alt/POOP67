import RPi.GPIO as GPIO
import adafruit_dht
import board
import pygame
import threading

class NavidadModel:
    def __init__(self, pin_led=18, pin_boton=23, dht_pin=board.D4):
        self.pin_led = pin_led
        self.pin_boton = pin_boton
        self.sensor = adafruit_dht.DHT11(dht_pin)

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin_led, GPIO.OUT)
        GPIO.setup(self.pin_boton, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        pygame.mixer.init()
        self._audio_lock = threading.Lock()

    def leer_clima(self):
        try:
            return self.sensor.temperature, self.sensor.humidity
        except Exception:
            return None, None

    def set_led(self, estado: bool):
        GPIO.output(self.pin_led, GPIO.HIGH if estado else GPIO.LOW)

    def reproducir_audio(self, path="jingle_bells.mp3"):
        def _play():
            with self._audio_lock:
                pygame.mixer.music.load(path)
                pygame.mixer.music.play()
        threading.Thread(target=_play, daemon=True).start()

    def apagado(self):
        pygame.mixer.music.stop()
        GPIO.cleanup()
