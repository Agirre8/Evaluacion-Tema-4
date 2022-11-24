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

freq = [0.2, 0.17, 0.13, 0.21, 0.05, 0.09, 0.15]

nodos = []

#metodo para transformar simbolos  frecuencias en nodos de huffman

for x in range(len(simbolo)):
    heapq.heappush(nodos, nodo(freq[x], simbolo[x]))

#ordenar los nodos en orden ascendente, basandonos en su frecuencia
while len(nodos) > 1:
     
    left = heapq.heappop(nodos)
    right = heapq.heappop(nodos)
 
    # asignamos valor 0 y 1 a la direccion de los nodos, al izquierdo siempre se le asigna el 0 y al derecho el 1
    left.huff = 0
    right.huff = 1
 
    #combinar los dos nodos mas pequeños para crear un nodo parental como conbinacion de los 2
    newNode = nodo(left.freq+right.freq, left.symbol+right.symbol, left, right)
 
    heapq.heappush(nodos, newNode)
 
printNodo(nodos[0])
