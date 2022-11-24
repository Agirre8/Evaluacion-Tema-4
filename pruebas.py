#Este módulo proporciona una implementación del algoritmo de cola de
#almacenamiento dinámico, también conocido como algoritmo de cola de prioridad.

#Los montones son árboles binarios para los que cada nodo padre tiene un valor
#menor o igual que cualquiera de sus hijos. Esta libreria utiliza arrays.
import heapq

class node:
    def __init__(self, freq, symbol, left=None, right=None):
        
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
    
    def __lt__(self, nxt): #metodo less than, es para comprobar numeros menores que.
        return self.freq < nxt.freq


