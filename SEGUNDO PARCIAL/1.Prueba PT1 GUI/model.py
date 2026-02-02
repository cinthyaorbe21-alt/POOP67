class RegalosModel:
    def __init__(self):
        self.regalos = []

    def agregar_regalo(self, regalo): #define la funcion agregar regalo
        self.regalos.append(regalo)

    def obtener_regalos(self): # define la funcion obtener regalo
        return self.regalos

