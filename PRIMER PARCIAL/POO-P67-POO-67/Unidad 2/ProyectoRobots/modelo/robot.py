class Robot:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estado = False  # apagado por defecto

    def encender(self):
        self.estado = True
        return f"{self.nombre} encendido."

    def apagar(self):
        self.estado = False
        return f"{self.nombre} apagado."

    def mover(self, direccion):
        if self.estado:
            return f"{self.nombre} se mueve hacia {direccion}."
        else:
            return f"{self.nombre} está apagado. No puede moverse."


class RobotExplorador(Robot):
    def __init__(self, nombre="RobotExplorador"):
        super().__init__(nombre)


class RobotIndustrial(Robot):
    def __init__(self, nombre="RobotIndustrial"):
        super().__init__(nombre)

