"""Taller 2
Problema3
Bianca

Se desea un programa que almacene los nombres de los estudiantes de un salón de
clases. El usuario debe indicar la cantidad de estudiantes. Adicionalmente el programa
debe solicitar la nota de 5 parciales. El programa debe calcular el promedio eliminando
la nota más baja. Al finalizar el programa debe escribir el nombre de los estudiantes su
promedio y la literal correspondiente.
Promedio Literal
Mayor a 90 A
Mayor a 80 B
Mayor a 70 C
Mayor a 60 D
Menor o igual a 60 F"""

from statistics import mean
import numpy as np


def calificacion(n):
    
    lista=[] # --Lista donde acumularemos los estudiantes

    totales=[] # --Lista donde acumularemos calificaciones

    for i in range(n):
        
        estudiante = input("Estudiante: ")

        lista.append(estudiante) # --Agregando a la lista los estudiantes

        for j in range(3):
        
            notas = float(input("Ingrese la nota: ")) 

            totales.append(notas) # --Agregando a la lista la venta del mes

         
    aestudiante = np.array(lista) # --Creando arreglos
    anotas = np.array(totales)
    anotas = anotas.reshape(n,3) # --Asignando las notas a c/estudiante
    
    for i in range(n):
        
        promedio = round(mean(anotas[i]),2)

        if promedio > 90:
            literal = "A"
        
        elif promedio > 80 and promedio < 91:
            literal = "B"
        
        elif promedio > 70 and promedio < 81:
            literal = "C"

        elif promedio > 60 and promedio < 71:
            literal = "D"

        else:
            literal = "F"
        
        print("\nEstudiante", aestudiante[i], "Promedio", promedio, "Literal", literal )# --Imprimiendo el resultado

    return


print("\n Problema 3 Estudiantes\n")

tamano = int(input("Cantidad de Estudiantes: ")) 

calificacion(tamano) # --Llama a funcion que rellenara el array