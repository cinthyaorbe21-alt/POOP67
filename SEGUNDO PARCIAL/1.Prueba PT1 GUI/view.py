import tkinter as tk
from tkinter import ttk

class RegalosView(tk.Tk): #Se define una clase llamada RegalosView que hereda de tk.Tk.
    def __init__(self):
        super().__init__()
        self.title("Lista de Regalos MVC") #define el titulo de la ventana
        self.geometry("400x300") #tamaño de la ventana

        self.label = tk.Label(self, text=" Lista de Regalos MVC ")
        self.label.pack(pady=5) #cuadro de texto no editable 

        self.entry = tk.Entry(self)
        self.entry.pack(pady=5)# crea una caja de texto

        self.combo = ttk.Combobox(self, values=["Amigos", "Hermanos", "Padres", "Mascotas"])
        self.combo.current(0) # pone por defecto la primera opcion
        self.combo.pack(pady=5)

        self.boton = tk.Button(self, text="Agregar a la Bolsa", bg="red", fg="white")
        self.boton.pack(pady=10) # crea un boton con el texto: agregar bolsa 

        self.lista = tk.Listbox(self, width=40)
        self.lista.pack(pady=10)
