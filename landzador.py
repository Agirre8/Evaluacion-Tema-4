import sys
# from Ejercicios.Ej1 import Ejercicio1 as ej1
# from Ejercicios.Ej2 import Ejercicio2 as ej2
# from Ejercicios.Ej3 import Ejercicio3 as ej3



sys.path.insert(0,"/Users/smite/Documents/GitHub/Evaluacion-Tema-4/Ejercicios/Ej3")
sys.path.insert(0,"/Users/smite/Documents/GitHub/Evaluacion-Tema-4/Ejercicios/Ej1")
sys.path.insert(0,"/Users/smite/Documents/GitHub/Evaluacion-Tema-4/Ejercicios/Ej2")

from Ejercicio1 import Ej1 as Ej1
from Ejercicio2 import *
from Ejercicio3 import Ej3 as Ej3


def ejecutar():
    n = input("Inserte el numero de el ejercicio que quieras ejecutar:")

    if n == 1:
        mensaje = input("inserte un mensaje que contenga los caracteres A, 0, 1, 3, F, M, T")

        Ej1.codificarMensaje(mensaje)
        print(f"El mensaje codificado es {mensajeCodificado}")
        Ej1.descodificarMensaje(MensajeCodificado)
        print(f"El mensaje decodificado es {mensaje}")


    elif n==2:
        print(".")
    elif n==3:
                                
        maravillas=[{'Nombre': 'Gran Muralla China', 'Pais': 'China', 'Tipo': 'ARQUITECTURA'}, {'Nombre': 'Coliseo de Roma' , 'Pais': 'Italia' , 'Tipo': 'ARQUITECTURA'}, 
                    {'Nombre': 'Ciudad de Petra', 'Pais': 'Jordania ' , 'Tipo': 'ARQUITECTURA'}, {'Nombre': 'Bahía de Ha Long', 'Pais': 'Vietnam' , 'Tipo': 'NATURAL'}, 
                    {'Nombre': 'Isla Jeju', 'Pais': 'Corea Sur' , 'Tipo': 'NATURAL'}, {'Nombre': 'Machu Picchu', 'Pais': 'Peru' , 'Tipo': 'ARQUITECTURA'}, 
                    {'Nombre': 'Taj Mahal', 'Pais': 'India', 'Tipo':'ARQUITECTURA'}]

        dist = [['Gran Muralla China', 'Coliseo de Roma', 7565], ['Coliseo de Roma','Machu Picchu', 10478], ['Gran Muralla China', 'Ciudad de Petra', 6217], 
                ['Gran Muralla China', 'Machu Picchu', 17038], ['Gran Muralla China', 'Taj Mahal', 7510], ['Ciudad de Petra','Taj Mahal', 4396], 
                ['Coliseo de Roma','Ciudad de Petra', 3673], ['Bahía de Ha Long', 'Isla Jeju', 2362 ],['Machu Picchu', 'Taj Mahal', 16941], 
                ['Coliseo de Roma','Taj Mahal', 6571], ['Ciudad de Petra', 'Machu Picchu',  12547], ]

        m1 = Ej3.nodoVertice(maravillas[0])
        m2 = Ej3.nodoVertice(maravillas[1])
        m3 = Ej3.nodoVertice(maravillas[2])
        m4 = Ej3.nodoVertice(maravillas[3])
        m5 = Ej3.nodoVertice(maravillas[4])
        m6 = Ej3.nodoVertice(maravillas[5])
        m7= Ej3.nodoVertice(maravillas[6])

        grafo = Ej3.Grafo()
        grafo.insertar(m1)
        grafo.insertar(m2)
        grafo.insertar(m3)
        grafo.insertar(m4)
        grafo.insertar(m5)
        grafo.insertar(m6)
        grafo.insertar(m7)


        grafo.mostrar()
        Ej3.visitado(grafo)
        maravillas = [m1, m2, m3, m4, m5, m6, m7]
        vertice = grafo.inicio
        n = 0

        Ej3.colocar_adyacencia(vertice, maravillas, dist, n) 
        

    else:
        print("El numero de ejercicio que has insertado es incorrecto!!!!")