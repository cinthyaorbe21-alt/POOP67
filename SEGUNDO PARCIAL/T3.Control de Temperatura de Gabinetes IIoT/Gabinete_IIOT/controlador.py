from modelo import SensorModel, FalloHardwareError, SobrecalentamientoError
import vista
import time

def ejecutar():
    sensor = SensorModel()

    try:
        vista.configurar_gpio()
        vista.led_normal()

        while True:  # Bucle infinito hasta Ctrl+C
            try:
                humedad, temperatura = sensor.get_data()
                print(f"Temp: {temperatura}°C | Humedad: {humedad}%")
                vista.led_normal()
                time.sleep(2)

            except FalloHardwareError as e:
                print(f"[ERROR HARDWARE] {e} | GPIO: {e.gpio_pin}")
                vista.led_apagar()
                vista.led_rojo_intermitente(ciclos=5, tiempo=0.5)

            except SobrecalentamientoError as e:
                print(f"[ALERTA] {e} | GPIO: {e.gpio_pin} | Temp: {e.temp_actual}°C")
                vista.led_apagar()
                vista.led_rojo_intermitente(ciclos=10, tiempo=0.3)

    except KeyboardInterrupt:
        print("\nLectura interrumpida.")

    finally:
        vista.limpiar_gpio()
        print("Sistema seguro: GPIO liberado.")
