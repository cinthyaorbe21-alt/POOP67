class SensorError(Exception):
    def __init__(self, mensaje, id_sensor, codigo_error):
        super().__init__(mensaje)
        self.id_sensor=id_sensor
        self.codigo_error=codigo_error

class SensorOffline(SensorError):
    pass

class Umbral(SensorError):
    pass

class SensorModel:
    def __init__(self, id_sensor):
        self.id_sensor = id_sensor

    def obtener_lectura(self):
        import random
        # Simulamos 3 estados: Normal, Desconectado (None), Crítico (alto)
        valor = random.choice([22.0, 25.4, None,
                               None,None,None,None,
                               None, 95.0,100,99.1,
                               23,45,50,76,56,1])
        """ valor = random.uniform(0,100)
        valor=round(valor,2)"""
        
        if valor is None:
            raise SensorOffline("HARDWARE_ERROR: Sensor no responde.", self.id_sensor, 404)
        if valor > 90:
            raise Umbral("UMBRAL_EXCEDIDO: Temperatura crítica.", self.id_sensor, 500)
            
        return valor