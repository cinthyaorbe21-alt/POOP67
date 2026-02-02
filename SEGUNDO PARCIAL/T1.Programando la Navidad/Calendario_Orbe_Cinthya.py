import tkinter as tk
from tkinter import messagebox
import random

# Lista de regalos virtuales
FRASES = ["✨ Que la magia de la Navidad ilumine tu corazón ✨", 
          "❤️ Te deseo una Navidad llena de abrazos sinceros ❤️", 
          "🎀 Un abrazo navideño para ti 🎀",
          "🎅 Que tus sueños brillen más fuerte esta Navidad 🎅",
          "❄️ Que esta Navidad te traiga paz y dulzura ❄️",
          "🎁 Sonríe, es Navidad!!! 🎁",
          "🌟 Que esta Navidad te regale momentos inolvidables 🌟"]

# Colores rojo y dorado navideño
COLORES_NAVIDAD = ["#b30000", "#d4af37"]  # rojo navideño y dorado

# Iconos navideños para cada recuadro
ICONOS = ["🎄", "🎁", "⭐", "❄️", "🔔", "🧦", "🎅"]

class CalendarioApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Mi Calendario de Adviento")

        # Canvas de fondo
        self.canvas = tk.Canvas(self.master, width=600, height=550, bg="#e8f8f5")
        self.canvas.pack()

        # Texto decorativo
        self.canvas.create_text(
            300, 20,
            text="🎄 Calendario de Adviento 🎁",
            font=("Comic Sans MS", 22, "bold"),
            fill="#b30000"
        )

        # Frame sobre el Canvas
        self.frame = tk.Frame(self.master, bg="#e8f8f5")
        self.canvas.create_window(300, 300, window=self.frame)

        # Crear botones
        self.crear_botones()

    def crear_botones(self):
        for i in range(4):          # Filas
            for j in range(6):      # Columnas
                dia = (i * 6) + j + 1

                # Alternar colores rojo y dorado
                color_fondo = COLORES_NAVIDAD[(i + j) % 2]

                # Elegir icono navideño según el día
                icono = ICONOS[(dia - 1) % len(ICONOS)]

                # Botón con icono + número
                boton = tk.Button(
                    self.frame,
                    text=f"{icono}\n{dia}",   # icono arriba, número abajo
                    bg=color_fondo,
                    fg="white",
                    font=("Comic Sans MS", 16, "bold"),
                    width=6,
                    height=3
                )

                boton.config(command=lambda d=dia: self.abrir_regalo(d))

                # Márgenes externos entre botones
                boton.grid(row=i, column=j, padx=5, pady=5)

    def abrir_regalo(self, dia):
        mensaje = random.choice(FRASES)
        messagebox.showinfo(f"Día {dia}", mensaje)

if __name__ == '__main__':
    root = tk.Tk()
    app = CalendarioApp(root)
    root.mainloop()
