import tkinter as tk
from controlador import controlador_button

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Botón ON / OFF")
    app = controlador_button(root)
    root.mainloop()
