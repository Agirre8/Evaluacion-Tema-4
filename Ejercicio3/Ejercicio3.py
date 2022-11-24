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

def distancia(v1, v2, lista):
    for i in range(len(lista)):
        if v1.info['Nombre'] in lista[i] and v2.info['Nombre'] in lista[i]:
            v1.insertar_adyacente(v2, distancia[i][2])

def ajustarvertice(vertice, vertice2, dist):
    if vertice2 is not None:
        if not isinstance(vertice2.info, dict):
            vertice2 = vertice2.info
        if vertice.info['Tipo'] == vertice2.info['Tipo']:
            distancia(vertice, vertice2, dist)
        ajustarvertice(vertice, vertice2.sig, dist)

def colocar_adyacencia(vertice, maravillas, dist, n):
    if vertice is not None:
        vertice2 = vertice.sig
        if not vertice.visitado:
            vertice.visitado = True
            ajustarvertice(vertice, vertice2, dist)
            if n < 6:
                n = n + 1
                colocar_adyacencia(maravillas[n], maravillas, dist, n)
                   
maravillas=[{'Nombre': 'Gran Muralla China', 'Pais': 'China', 'Tipo': 'ARQUITECTURA'}, {'Nombre': 'Coliseo de Roma' , 'Pais': 'Italia' , 'Tipo': 'ARQUITECTURA'}, 
            {'Nombre': 'Ciudad de Petra', 'Pais': 'Jordania ' , 'Tipo': 'ARQUITECTURA'}, {'Nombre': 'Bahía de Ha Long', 'Pais': 'Vietnam' , 'Tipo': 'NATURAL'}, 
            {'Nombre': 'Isla Jeju', 'Pais': 'Corea Sur' , 'Tipo': 'NATURAL'}, {'Nombre': 'Machu Picchu', 'Pais': 'Peru' , 'Tipo': 'ARQUITECTURA'}, 
            {'Nombre': 'Taj Mahal', 'Pais': 'India', 'Tipo':'ARQUITECTURA'}]

dist = [['Gran Muralla China', 'Coliseo de Roma', 7565], ['Coliseo de Roma','Machu Picchu', 10478], ['Gran Muralla China', 'Ciudad de Petra', 6217], 
        ['Gran Muralla China', 'Machu Picchu', 17038], ['Gran Muralla China', 'Taj Mahal', 7510], ['Ciudad de Petra','Taj Mahal', 4396], 
        ['Coliseo de Roma','Ciudad de Petra', 3673], ['Bahía de Ha Long', 'Isla Jeju', 2362 ],['Machu Picchu', 'Taj Mahal', 16941] 
        ['Coliseo de Roma','Taj Mahal', 6571], ['Ciudad de Petra', 'Machu Picchu',  12547], ]

m1 = nodoVertice(maravillas[0])
m2 = nodoVertice(maravillas[1])
m3 = nodoVertice(maravillas[2])
m4 = nodoVertice(maravillas[3])
m5 = nodoVertice(maravillas[4])
m6 = nodoVertice(maravillas[5])
m7= nodoVertice(maravillas[6])
