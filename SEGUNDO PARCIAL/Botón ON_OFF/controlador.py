from modelo import modelo_button
from vista import vista_button

class controlador_button:
    def __init__(self, root):
        self.model = modelo_button()
        self.view = vista_button(root, self)
        self.view.update_button(self.model.state)
        
    def toggle_button(self):
        self.model.toggle_state()
        self.view.update_button(self.model.state)
