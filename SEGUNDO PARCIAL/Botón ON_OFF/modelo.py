import datetime

class modelo_button:
    def __init__(self, filename="estado.txt"):
        self.filename = filename
        self.state = False
        self.load_state()
        
    def toggle_state(self):
        self.state = not self.state   # ← corregido
        self.save_state()
        
    def save_state(self):
        estado = "ON" if self.state else "OFF"
        fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.filename, "a") as f:
            f.write(f"{estado}: {fecha_hora}\n")
    
    def load_state(self):
        try:
            with open(self.filename, "r") as f:
                lineas = f.readlines()
                if lineas:
                    ultimo = lineas[-1].strip()
                    self.state = ultimo.startswith("ON")
                else:
                    self.save_state()
        except FileNotFoundError:
            self.save_state()   # ← faltaban paréntesis

        