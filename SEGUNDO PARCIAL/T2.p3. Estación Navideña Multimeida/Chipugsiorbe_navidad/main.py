from modelo import NavidadModel
from vista import NavidadView
from controlador import NavidadController

if __name__ == "__main__":
    m = NavidadModel()
    v = NavidadView()
    c = NavidadController(m, v)
    v.mainloop()
