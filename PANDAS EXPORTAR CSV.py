import pandas as pd
import random
separador= ("*" * 20) + "\n"

diccionario_notas_aletorias={\
    "Crescencio":[random.randrange(60,101) for x in range(3)], \
    "Domitila":[80,100,57], "Rutilio":[80,70,57], "Pánfilo":[20,100,100], \
    "Ludoviko":[100,100,100]}
notas=pd.DataFrame(diccionario_notas_aletorias)
notas.index=["Programacion","Base de datos","Contabilidad"]

notas.to_csv(r'notas.csv',index=True,header=True)
print("EXITO!")
                        
                    