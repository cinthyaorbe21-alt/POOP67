import tkinter as tk

def mostrar_posicion(fila, columna):
    print(f"Has hecho clic en la posicion: fila {fila}, columna {columna}")

root=tk.Tk()
root.title("Chess Table")
root.geometry("600x600")

for fila in range (8):
    for columna in range(8):
        color="white" if (fila + columna) % 2 == 0 else "black"

        
        boton=tk.Button(
            root,
            bg=color,
            width=6,
            height=3,
            command=lambda f=fila, c=columna: mostrar_posicion(f, c)
            )
        boton.grid(row=fila, column=columna, sticky="nsew")

for i in range(8):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)


root.loop()
