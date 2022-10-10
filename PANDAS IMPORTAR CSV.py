import pandas as pd
separador= ("*" * 20) + "\n"

notas = pd.read_csv("notas.csv", index_col=0)

print(notas)
print(separador)
