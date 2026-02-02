from exceptions_and_model import ( Sensor, Notificador, CriticalThresholdError, SensorReadError)

class Controller:
    def __init__(self, view, token, chat_id):
        self.sensor = Sensor()
        self.view = view
        self.notificador = Notificador(token, chat_id)
        self.enviado_bienvenida = False

    def run(self):
        try:
            model = self.sensor.read()

            if not self.enviado_bienvenida:
                mensaje = (
                    f"Sistema de monitoreo iniciado.\n"
                    f"Temperatura inicial: {model.temp:.1f}°C, Humedad: {model.hum:.1f}%\n"
                    "Se enviarán alertas si la temperatura supera el umbral definido."
                )
                self.notificador.enviar_alerta(mensaje)
                self.enviado_bienvenida = True

            try:
                model.check_status()
                self.view.estado_normal(model.temp, model.hum)
            except CriticalThresholdError as e:
                self.view.estado_critico(str(e))
                self.notificador.enviar_alerta(str(e))
                return

            mensaje_temp = f"Temperatura: {model.temp:.1f}°C, Humedad: {model.hum:.1f}%"
            self.notificador.enviar_alerta(mensaje_temp)

        except SensorReadError as e:
            error_msg = f"Error sensor: {e}"
            print(error_msg)
            self.view.estado_critico(error_msg)
            self.notificador.enviar_alerta(error_msg)

        except AssertionError as e:
            error_msg = f"Error de validación: {e}"
            print(error_msg)
            self.view.estado_critico(error_msg)
            self.notificador.enviar_alerta(error_msg)


