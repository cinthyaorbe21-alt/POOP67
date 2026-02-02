import tkinter as tk

root=tk.Tk()
root.geometry("300x200")

def funcion_menu():
    print(f"se selecciono la opcion del menu")

menu_bar=tk.Menu(root)

menu_opciones=tk.Menu(menu_bar, tearoff=0)
menu_opciones.add_command(label="Opcion 1", command=funcion_menu)
menu_opciones.add_command(label="Opcion 2", command=funcion_menu)
menu_opciones.add_separator()
menu_opciones.add_command(label="Salir", command=root.quit)

menu_bar.add_cascade(label="Archivo", menu=menu_opciones)

root.config(menu=menu_bar)
root.mainloop()
