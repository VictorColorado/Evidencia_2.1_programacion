import numpy as np
import pandas as pd

separador=("*"*20)+"/n"

notas = pd.Series([87,100,85,60,79])
print(type(notas))
print(notas)
print(separador)

iguales = pd.Series(100,range(6))
print(type(iguales))
print(iguales)
print(separador)

print("notas:")
print(f"{notas}")
print(f"cantidad={notas.count()}")
print(f"media={notas.mean()}")
print(f"minimo={notas.min()}")
print(f"maximo={notas.max()}")
print(f"desviacion standard={notas.std()}")
print("sumarizacion descriptiva:")
print(notas.describe())
print(separador)

print("Series con indice personalizados:")
notas_asignadas=pd.Series([87,100,86,60,78],index=["Cresencio","Domitila","Rutilio","Panfilo","Ludoviko"])

print(notas_asignadas)
print(separador)

print("serie generada a partir de un dicionario")
notas_asignadas_dict=pd.Series({"Cresencio":87,"Domitila":100,"Rutilio":85,"Panfilo":60,"Ludoviko":78})

print(notas_asignadas_dict)
print (separador)

print(f"Laclificacion de rutilio es {notas_asignadas_dict['Rutilio']}")
print(f"La calificaion de rutilio es {notas_asignadas_dict.Rutilio}")