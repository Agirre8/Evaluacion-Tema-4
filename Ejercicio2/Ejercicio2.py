import csv
import pandas as pd

df = pd.read_csv("Pokemon.csv")#como estan en el mismo directorio no hace falta especificar el path

def leer_filas():
    print(df.head(3))#para ver las primeras 10 filas
    print(df.tail(3))#para ver las ultimas 10 filas

#leer columnas del 0 al 5
def leer_columas():    
    print(df["Name"][0:5])

#funcion iloc para seleccionar filas especificas
def seleccionar_fila():    
    print(df.iloc[1:4]["Name"])


#seleccionar un elemento especifico de una columa y una fila exacta
def localizar_especifico():    
    print(df.iloc[2,1])

#para ir iterando por todo el csv
def iterar_csv():    
    for index, row in df.iterrows():
        print(index, row["Name"]) #podemos elegir que columna iterar

#funcion para encontrar un dato especifico dentro de una columna por ejemplo
def localizar_tipo():    
    print(df.loc[df["Type 1"] == "Fire"]) #solo elegimos los del tipo fuego


#funcion describe, te da informacion del csv
def describe():
    df.describe()

#funcion para ordenar valores del csv
def ordenar():
    df.sort_values(["Name", "HP"], ascending=[1,0])#el nombre sera descendiente y la vida ascendente
    df.sort_values("Name", ascending=False)#de menos a mayor

#operar con columnas, y crear otra con el total
def operar():
    df["total"] = df["HP"]+df["Attack"]+df["Defense"]+df["Sp. Atk"]+df["Sp. Def"]+df["Speed"]
    print(df)

#eliminar columna, la de total por ejemplo
def eliminar():
    df = df.drop(colums="total")

