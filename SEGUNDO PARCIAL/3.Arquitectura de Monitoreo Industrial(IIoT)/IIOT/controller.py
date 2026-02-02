import time
from model import SensorModel, SensorOffline,Umbral
from view import SensorView
class SensorController:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def ejecutar_monitoreo(self):
        try:
            # Intenta obtener la lógica del modelo
            lectura = self.modelo.obtener_lectura()
            # Si tiene éxito, se lo pasa a la vista
            self.vista.mostrar_datos(lectura)
        
        except (SensorOffline, Umbral) as e:
            # Captura las excepciones personalizadas y usa la vista para el reporte
            self.vista.mostrar_error(e)
            self.protocolo_seguridad()

    def protocolo_seguridad(self):
        print("[SISTEMA] Activando ventiladores y registrando log de falla...")

if __name__ == "__main__":
    # Inicializamos los componentes
    mi_modelo = SensorModel(id_sensor="IIOT-PY-001")
    mi_vista = SensorView()
    mi_controlador = SensorController(mi_modelo, mi_vista)

    # Simulamos 5 ciclos de lectura
    print("Iniciando Simulación en Spyder...")
    for i in range(5):
        print(f"Ciclo {i+1}:")
        time.sleep(1)
        mi_controlador.ejecutar_monitoreo()