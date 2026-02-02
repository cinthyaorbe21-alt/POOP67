class IA:
    def __init__(self, Modelo, Version, Categoria):
        self.Modelo=Modelo
        self.Version=Version
        self.Categoria=Categoria
    def generar_respuesta(self):
        pass
    def analizar_datos(self):
        pass
    def reconocer_imagen(self):
        pass
        
Asistente=IA("Gemini Pro", "2.0", "Asistencia Multimodal")
print("Modelo: ",end="")
print(Asistente.Modelo)
print("Versión: ",end="")
print(Asistente.Version)
print("Categoria ", end="")
print(Asistente.Categoria)
