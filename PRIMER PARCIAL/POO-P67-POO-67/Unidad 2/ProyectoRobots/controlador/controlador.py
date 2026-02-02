import datetime

class Controlador:
    def __init__(self, robot, vista):
        self.robot = robot
        self.vista = vista

    def registrar_accion(self, accion):
        fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("log.txt", "a") as archivo:
            archivo.write(f"[{fecha_hora}] {self.robot.nombre}: Acción -> {accion}\n")

    def encender_robot(self):
        mensaje = self.robot.encender()
        self.vista.mostrar_mensaje(mensaje)
        self.registrar_accion("encender")

    def apagar_robot(self):
        mensaje = self.robot.apagar()
        self.vista.mostrar_mensaje(mensaje)
        self.registrar_accion("apagar")

    def mover_robot(self, direccion):
        mensaje = self.robot.mover(direccion)
        self.vista.mostrar_mensaje(mensaje)
        self.registrar_accion(f"mover {direccion}")
