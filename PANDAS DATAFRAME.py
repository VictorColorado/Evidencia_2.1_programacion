import pandas as pd
import random

separador=("*"*20)+"/n"

diccionario_notas={"Crecensio":[87,100,None],"Domitila":[80,None,57],\
                   "Rutilio":[80,70,57],"Panfilo":[20,100,100],"Ludoviko":[100,100,100]}

notas_diccionario=pd.DataFrame(diccionario_notas)
print(notas_diccionario)
print(separador)

diccionario_notas_aletorias={\
    "Crecensio":[random.randrange(60,101)for x in range(3)],\
    "Domitila":[80,100,57],"Rutilio":[80,70,57],"Panfilo":[20,100,100],\
    "Ludoviko":[100,100,100]}
notas_diccionario=pd.DataFrame(diccionario_notas_aletorias)
print(notas_diccionario)
print(separador)

notas_diccionario.index=["Programacion","Base de datos","Contabilidad"]
print(notas_diccionario)
print(separador)