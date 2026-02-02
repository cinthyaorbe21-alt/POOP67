import tkinter as tk

root=tk.Tk()

label1=tk.Label(root, text="Widget 1")
label2=tk.Label(root, text="Widget 2")
label3=tk.Label(root, text="Widget 3")

label1.grid(row=0, column=0)
label2.grid(row=1, column=1)
label3.grid(row=2, column=2, rowspan=2, columnspan=2, padx10, pady=10, ipadx=5, ipady=5 ) 

root.mainloop()
