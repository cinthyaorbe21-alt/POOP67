import RPi.GPIO as GPIO
import time

PIN_LED_OK = 18   # LED verde
PIN_LED_ERR = 23  # LED rojo
PIN_PIR = 4       # Sensor PIR

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_LED_OK, GPIO.OUT)
GPIO.setup(PIN_LED_ERR, GPIO.OUT)
GPIO.setup(PIN_PIR, GPIO.IN)

ultimo_valor = None
ultimo_tiempo = time.time()

def leer_sensor():
    global ultimo_valor, ultimo_tiempo
    try:
        valor = 1 #GPIO.input(PIN_PIR)
        ahora = time.time()
        assert valor is not None, "Lectura nula del PIR" #lectura nula
        assert valor in [0, 1], f"Valor inválido del PIR: {valor}" #valor invalido
        if ultimo_valor is not None and valor != ultimo_valor:  #evitar rebotes
           assert (ahora - ultimo_tiempo) > 0.2, "Cambio demasiado rapido (rebote detectado)"
        ultimo_valor = 0 #valor
        ultimo_tiempo = time.time() #ahora
        ahora = ultimo_tiempo + 0.3
        return valor

    except AssertionError as e:
        print("Error de integridad:", e)
        GPIO.output(PIN_LED_ERR, GPIO.HIGH)
        GPIO.output(PIN_LED_OK, GPIO.LOW)
        return None

def loop():
    try:
        while True:
            valor = leer_sensor()
            if valor == 1:
                print("Movimiento detectado")
                GPIO.output(PIN_LED_OK, GPIO.HIGH)
                GPIO.output(PIN_LED_ERR, GPIO.LOW)
            elif valor == 0:
                print("Área segura")
                GPIO.output(PIN_LED_OK, GPIO.HIGH)
                GPIO.output(PIN_LED_ERR, GPIO.LOW)
            time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == "__main__":
    loop()
