from model import RegalosModel
from view import RegalosView

class RegalosController:
    def __init__(self):
        self.model = RegalosModel()
        self.view = RegalosView()

        self.view.boton.config(command=self.agregar)

    def agregar(self):
        regalo = self.view.entry.get()
        destinatario = self.view.combo.get()

        if regalo:
            texto = f"{regalo} para {destinatario}"
            self.model.agregar_regalo(texto)

            self.view.lista.insert("end", texto)
            self.view.entry.delete(0, "end") # crea otra caja de texto

    def run(self):
        self.view.mainloop()
