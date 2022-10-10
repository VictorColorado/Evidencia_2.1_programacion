import pandas as pd
import random
separador = ("*" * 20) + "\n"

diccionario_notas_aleatorias = { \
    "Crescencio":[random.randrange(60,101) for x in range(3)], \
    "Domitila":[80,100,57], "Rutilio":[80,70,57], "Panfilo":[20,100,100], \
    "Ludoviko":[100,100,100]}
notas = pd.DataFrame(diccionario_notas_aleatorias)
notas.index = ["Programacion", "Base de datos", "Contabilidad"]

print("Todas las asignaturas,todos los estudiantes")
subConjunto = notas.loc["Programacion":"Contabilidad"]
print(subConjunto)
x = input("Presiona una tecla")

print(separador)

print("Ultimas dos asignaturas,todos los estudiantes")
subConjunto = notas.loc["Base de datos":"Contabilidad"]
print(subConjunto)
print(separador)

print("solamente calificaiones aprobatorias")
aprobados=notas[notas>=70]
print(aprobados)
print(separador)

print("solamente calificaciones aprobatorias entre 70 y 80")
aprobados=notas[(notas>=70)&(notas>=80)]
print(aprobados)
print(separador)

print("solamente calidicaciones no aprobatorias que sean pares")
reprobados_pares=notas[(notas>=70)&(notas%2==0)]
print(reprobados_pares)
print(separador)

print("La calificación de 'Panfilo' en 'Programación'")
nota_PanfiloProgramacion = notas.at["Programacion","Panfilo"]
print(nota_PanfiloProgramacion)
print(separador)

print("modificaremos la nota de panfilo en programacion")
nota_PanfiloProgramacion=notas.at["Programacion","Panfilo"]
print(nota_PanfiloProgramacion)
print(separador)


