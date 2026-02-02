import time
import threading

class SeguridadController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        threading.Thread(target=self.loop_principal, daemon=True).start()

    def loop_principal(self):
        while True:
            try:
                valor = self.model.leer_sensor()
                if valor == 1:
                    self.view.mostrar_estado("Movimiento detectado", "green")
                    self.view.actualizar_sensor("Sensor: 1 (Movimiento)")
                    self.model.activar_led_ok(True)
                    self.model.activar_led_err(False)
                elif valor == 0:
                    self.view.mostrar_estado("Área segura", "blue")
                    self.view.actualizar_sensor("Sensor: 0 (Sin movimiento)")
                    self.model.activar_led_ok(True)
                    self.model.activar_led_err(False)
            except Exception as e:
                self.view.mostrar_estado(str(e), "red")
                self.model.activar_led_ok(False)
                self.model.activar_led_err(True)

            time.sleep(1)
