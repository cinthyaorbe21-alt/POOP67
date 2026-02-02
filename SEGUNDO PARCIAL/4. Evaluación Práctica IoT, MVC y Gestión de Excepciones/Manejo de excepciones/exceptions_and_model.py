class SensorReadError(Exception):
    pass

class CriticalThresholdError(Exception):
    pass

import adafruit_dht
import board
import requests


class TemperatureModel:
    def __init__(self, temp, hum):
        assert 0 <= hum <= 100, "Humedad fuera de rango"
        self.temp = temp
        self.hum = hum

    def check_status(self):
        if self.temp > 29:
            raise CriticalThresholdError(
                f"¡ALERTA! Temperatura crítica: {self.temp:.1f}°C"
            )


class Sensor:
    def __init__(self):
        self.dht = adafruit_dht.DHT11(board.D4)

    def read(self):
        try:
            temp = self.dht.temperature
            hum = self.dht.humidity

            if temp is None or hum is None:
                raise SensorReadError("Lectura inválida del DHT22")

            return TemperatureModel(temp, hum)

        except RuntimeError as e:
            raise SensorReadError(str(e))


class Notificador:
    def __init__(self, token, chat_id):
        if not token:
            raise ValueError("Token de Telegram nulo")
        self.token = token
        self.chat_id = chat_id

    def enviar_alerta(self, mensaje):
        url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        data = {
            "chat_id": self.chat_id,
            "text": mensaje
        }
        response = requests.post(url, data=data)

