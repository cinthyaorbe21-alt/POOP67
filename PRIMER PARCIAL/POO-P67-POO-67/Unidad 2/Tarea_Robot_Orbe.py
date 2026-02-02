# Clase Robot
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


# Clase RobotVolador que hereda de Robot
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
r = RobotVolador("Atlas")
print(r.saludar())
r.mover(10)      # Avanza 10 → x=10, batería=90
r.volar(5)       # Sube 5 → z=5, batería=80
print(r.status())
r.volar(-3)      # Baja 3 → z=2, batería=74
print(r.status())
