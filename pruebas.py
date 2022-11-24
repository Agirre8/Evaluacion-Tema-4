#Este módulo proporciona una implementación del algoritmo de cola de
#almacenamiento dinámico, también conocido como algoritmo de cola de prioridad.

#Los montones son árboles binarios para los que cada nodo padre tiene un valor
#menor o igual que cualquiera de sus hijos. Esta libreria utiliza arrays.
import heapq

class nodo:
    def __init__(self, freq, simbolo, left=None, right=None):
        
        self.freq = freq
        self.symbol = simbolo
        self.left = left
        self.right = right
    
    def __lt__(self, nxt): #metodo less than, es para comprobar numeros menores que.
        return self.freq < nxt.freq

def printNodo(nodo, val=""):

    #codigo uffman para el nodo actual
    newVal = val + str(nodo.huff)

    #si el nodo no es un nodo de esquina
    if(nodo.left):
        printNodo(nodo.left, newVal)
    if(nodo.left):
        printNodo(nodo.right, newVal)

    #si el nodo es un nodo de esquina

    if(not nodo.left and not nodo.right):
        print(f"{nodo.simbolo} -->{newVal}")


simbolo = ["A", "F", "1", "3", "0", "M", "T"]

freq = []
