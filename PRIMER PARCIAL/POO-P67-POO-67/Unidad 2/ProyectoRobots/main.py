from modelo.robot import RobotExplorador, RobotIndustrial
from vista.vista import Vista
from controlador.controlador import Controlador

def main():
    vista = Vista()

    # Robot Explorador
    explorador = RobotExplorador()
    controlador_explorador = Controlador(explorador, vista)

    controlador_explorador.encender_robot()
    controlador_explorador.mover_robot("adelante")
    controlador_explorador.mover_robot("izquierda")
    controlador_explorador.mover_robot("derecha")
    controlador_explorador.apagar_robot()

    print("-" * 45)

    # Robot Industrial
    industrial = RobotIndustrial()
    controlador_industrial = Controlador(industrial, vista)

    controlador_industrial.encender_robot()
    controlador_industrial.mover_robot("derecha")
    controlador_industrial.apagar_robot()

if __name__ == "__main__":
    main()
