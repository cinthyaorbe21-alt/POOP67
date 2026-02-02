import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.geometry("300x200")

label=tk.Label(root, text="Selecciona tu opcion")
label.pack()

opciones=["Opcion 1", "Opcion 2", "Opcion 3"]

combo= ttk.Combobox(root, values=opciones)
combo.pack()

def seleccionado(event):
    label.config(text=f"Seleccionaste {combo.get()}")

combo.bind("<<ComboboxSelected>>", seleccionado)

root.mainloop()
