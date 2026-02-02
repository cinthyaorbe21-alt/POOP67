class Navegador:
    def __init__(self, Nombre, Versión, Favoritos):
        self.Nombre=Nombre
        self.Versión=Versión
        self.Favoritos=Favoritos
    def abrir_pagina(self):
        pass
    def cerrar_pagina(self):
        pass
    def añadir_favoritos(self):
        pass
        
Ejecutar=Navegador("Chrome", "124.5", "github.com")
print("Nombre: ",end="")
print(Ejecutar.Nombre)
print("Versión: ",end="")
print(Ejecutar.Versión)
print("Favorito: ", end="")
print(Ejecutar.Favoritos)
