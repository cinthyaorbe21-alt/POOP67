import tkinter as tk

root=tk.Tk()

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

label1=tk.Label(root, text="Etiqueta 1")
label1.grid(row=0, column=0)

label2=tk.Label(root, text="Etiqueta 2")
label2.grid(row=0, column=1)

button1=tk.Button(root, text="Botón 1")
button1.grid(row=1, column=0)

button2=tk.Button(root, text="Botón 2")
button2.grid(row=1, column=1)

root.mainloop()
