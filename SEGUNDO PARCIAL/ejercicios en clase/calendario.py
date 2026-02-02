import tkinter as tk
from tkinter import messagebox
import random

FRASES = [
    "✨Un chocolate azul✨", "✨Un deseo dorado ✨", "✨Vale por un abrazo elegante✨",
    "✨Un poema navideño✨", "✨Una estrella fugaz✨", "✨Tiempo para ti✨",
    "✨Un recuerdo brillante✨", "✨Una canción✨", "✨Un descanso merecido✨",
    "✨Un paseo bajo las luces✨", "✨Un café contigo✨", "✨Un secreto feliz✨",
    "✨Un regalo inesperado✨", "✨Un mensaje especial✨", "✨Un día sin preocupaciones✨",
    "✨Un momento de paz✨", "✨Un deseo cumplido✨", "✨Una sonrisa compartida✨",
    "✨Un abrazo virtual✨", "✨Un sueño dorado✨", "✨Una historia mágica✨",
    "✨Un día de juegos✨", "✨Una sorpresa azul✨", "✨Feliz Navidad✨"
]

class CalendarioEleganteApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Calendario de Adviento")
        self.canvas = tk.Canvas(master, width=800, height=600, bg="#1a1a40")  # Fondo azul profundo
        self.canvas.pack()
        self.crear_cuadros_estilo_navidad()

    def crear_cuadros_estilo_navidad(self):
        filas, columnas = 4, 6
        base_x, base_y = 40, 40
        espacio_x, espacio_y = 120, 120

        for i in range(filas):
            for j in range(columnas):
                dia = (i * columnas) + j + 1

                # Tamaños irregulares pero dentro de límites
                ancho = random.randint(70, 100)
                alto = random.randint(60, 90)

                x1 = base_x + j * espacio_x
                y1 = base_y + i * espacio_y
                x2 = x1 + ancho
                y2 = y1 + alto

                # Cuadro azul marino con borde dorado
                rect = self.canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill="#000033", outline="#FFD700", width=3
                )
                texto = self.canvas.create_text(
                    (x1 + x2)//2, (y1 + y2)//2,
                    text=str(dia), font=("Georgia", 14, "bold"), fill="#FFD700"
                )

                # Asociar clic
                self.canvas.tag_bind(rect, "<Button-1>", lambda e, d=dia: self.abrir_regalo(d))
                self.canvas.tag_bind(texto, "<Button-1>", lambda e, d=dia: self.abrir_regalo(d))

    def abrir_regalo(self, dia):
        mensaje = random.choice(FRASES)
        messagebox.showinfo(f"Día {dia}", mensaje)

if __name__ == '__main__':
    root = tk.Tk()
    app = CalendarioEleganteApp(root)
    root.mainloop()
