class Adyacente(object):
    def __init__(self, distancia, info):
        self.distancia = distancia
        self.visitado = False
        self.info = info
        self.sig = None
        

