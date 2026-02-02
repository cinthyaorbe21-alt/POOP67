class SensorView:
    def mostrar_datos(self, valor):
        print(f"[INFO] Lectura actual: {valor}°C - Estado: OK")

    def mostrar_error(self, error):
        print("\n--- ALERTA DE SISTEMA ---")
        print(f"MENSAJE: {error}")
        print(f"ID DISPOSITIVO: {error.id_sensor}")
        print(f"CÓDIGO TÉCNICO: {error.codigo_error}")
        print("-------------------------\n")