# Clase base Robot
class Robot:
    def __init__(self, nombre):
        self.nombre = nombre
        self.bateria = 100
        self.x = 0

    def saludar(self):
        return f"Hola, soy {self.nombre}"

    def mover(self, distancia):
        self.x += distancia
        self.bateria -= abs(distancia)

    def status(self):
        return f"batería={self.bateria}, x={self.x}"


class RobotVolador(Robot):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.z = 0

    def volar(self, altura):
        self.z += altura
        self.bateria -= abs(altura) * 2

    def status(self):
        return f"batería={self.bateria}, x={self.x}, z={self.z}"


# ------------------ SIMULACIÓN ------------------
r = RobotVolador("Bender")
print(r.saludar())
r.mover(15)      
r.volar(10)      
print(r.status())
r.volar(-5)      
print(r.status())
