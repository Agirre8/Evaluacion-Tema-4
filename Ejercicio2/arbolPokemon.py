class nodo:
    def __init__(self, dato):
        self.dato=dato
        self.izquierda=None
        self.derecha=None
class Arbol:
    # Funciones privadas
    def __init__(self, dato):
        self.raiz = Nodo(dato)
