import adafruit_dht
import board

# --- PASO 1: Crear excepciones personalizadas ---
class FalloHardwareError(Exception):
    """Se lanza cuando el sensor devuelve None o falla físicamente."""
    def __init__(self, message, gpio_pin):
        super().__init__(message)
        self.gpio_pin = gpio_pin

class SobrecalentamientoError(Exception):
    """Se lanza cuando la temperatura excede los 30°C."""
    def __init__(self, message, gpio_pin, temp_actual):
        super().__init__(message)
        self.gpio_pin = gpio_pin
        self.temp_actual = temp_actual

class SensorModel:
    def __init__(self, pin=board.D4):
        self.pin_number = 4 # Para el reporte de error
        try:
            self.dht_device = adafruit_dht.DHT11(pin)
        except Exception as e:
            print(f"Error al inicializar sensor: {e}")

    def get_data(self):
        try:
            humidity = self.dht_device.humidity
            temperature = self.dht_device.temperature
        except Exception:
            humidity = None
            temperature = None

        # --- PASO 3: Lanzar excepciones con 'raise' ---
        if humidity is None or temperature is None:
            raise FalloHardwareError("Sensor no responde o desconectado", self.pin_number)

        if temperature > 30:
            raise SobrecalentamientoError("¡CRÍTICO! Temperatura > 30°C", self.pin_number, temperature)

        return humidity, temperature
