import tkinter as tk

class vista_button(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.pack()   # ← necesario
        
        self.button = tk.Button(
            self,
            text="OFF",
            width=40,
            fg="red",
            command=self.controller.toggle_button
        )
        self.button.pack(pady=40)
        
    def update_button(self, state):
        if state:
            self.button.config(text="ON", fg="green")
        else:
            self.button.config(text="OFF", fg="red")
