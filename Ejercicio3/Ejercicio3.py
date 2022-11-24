class Adyacente(object):
    def __init__(self, distancia, info):
        self.distancia = distancia
        self.visitado = False
        self.info = info
        self.sig = None
        

class nodoVertice(object):
    def __init__(self, info):
        self.info = info
        self.sig = None
        self.adyacentes = None   
        self.visitado = False

    
    def insertar_adyacente(self, info, distancia):
        nodo = Adyacente(info, distancia)
        if self.adyacentes is None:
            self.adyacentes = nodo
        else:
            aux_adyacente = self.adyacentes
            self.sig = aux_adyacente 
            self.adyacentes = nodo

class Grafo(object):
    def __init__(self):
        self.inicio = None
        self.tamaño = 0
        
    def insertar(grafo, dato):

        if grafo.inicio is None:
            grafo.inicio = dato
        else:
            aux_grafo = grafo.inicio
            grafo.inicio = dato
            grafo.inicio.sig = aux_grafo
            grafo.tamaño +=1
    
    def mostrar(self):
        vertice = self.inicio
        while vertice is not None:
            if not vertice.visitado:
                vertice.visitado= True
                print(vertice.info)
                vertice = vertice.sig 

def visitado(grafo):
    vertice = grafo.inicio
    while vertice is not None:
        vertice.visitado = False
        vertice = vertice.sig