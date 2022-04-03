"""
Taller 5
Problema 1
Bianca

 Crear un archivo llamado resultados.xlsx
 que debe almacenar el nombre del estudiante
 y el promedio obtenido durante el periodo de clases
 (mínimo 10 estudiantes).
 El programa debe
leer la información del estudiante
y el promedio
y crear el archivo.
Una vez creado el archivo contar con una función que proceda recorrer el archivo.
Los estudiantes que tienen un promedio mayor o igual a 81 pasan al archivo de Aprobado y el resto
para al archivo de Reprobado.
"""
import os

import pandas as pd

# carpeta donde guardo los archivos
ruta = 'C:\\Users\\User\\PycharmProjects\\Intermedio\\Talleres\\Taller5'


def escribir():

    nombre = []

    promedio = []

    cont = 0  # Contador de Estudiantes registrados
    try:
        while True:

            nom = input("Estudiante: ")
            nombre.append(nom)

            cant = float(input("Promedio: "))
            promedio.append(cant)

            cont += 1

            # (mínimo 10 estudiantes)
            if cont >= 10:

                op = input("Presione X para salir ")

                if op == 'x' or op == 'X':

                    break

        zipped = list(zip(nombre, promedio))

        df = pd.DataFrame(zipped, columns=['Nombre', 'Promedio'])

        # archivo llamado resultados.xlsx que debe almacenar el nombre del estudiante y el promedio obtenido
        df.to_excel('resultados.xlsx')

        clasificar()

    except ValueError:

        print("Valor Invalido")

    return

# --------------------------------------------------------------------------------------------------------------


def clasificar():

    global ruta
    aprobados = []
    promedios = []
    reprobados = []
    promediosf = []

    try:

        dif = pd.read_excel('resultados.xlsx', header=0)

        for i in range(len(dif)):

            prom = dif.loc[i, 'Promedio']

            if prom > 80:
                aprobados.append(dif.loc[i, 'Nombre'])
                promedios.append(prom)
            else:
                reprobados.append(dif.loc[i, 'Nombre'])
                promediosf.append(prom)

        df1 = pd.DataFrame((list(zip(aprobados, promedios))), columns=['Nombre', 'Promedio'])

        # archivo llamado
        df1.to_excel('aprobado.xlsx')

        def2 = pd.DataFrame((list(zip(reprobados, promediosf))), columns=['Nombre', 'Promedio'])

        def2.to_excel('reprobado.xlsx')

        if "aprobado.xlsx" in os.listdir(ruta) and "reprobado.xlsx" in os.listdir(ruta):
            print("Archivos de aprobados y reprobados creados\nFin de Programa")

    except FileNotFoundError:
        print("Archivo no encontrado")

    except pd.errors.EmptyDataError:
        print("No data")

    return

# --------------------------------------------------------------------------------------------------------------


print("\nPrograma Del Promedio De Los Estudiantes\n")

try:

    if "resultados.xlsx" in os.listdir(ruta):

        print("El archivo resultados.xlsx ya ha sido creado ")

        opcion = int(input("1 Sobreescribir. 2 Clasificar "))

        if opcion == 2:
            clasificar()
            exit()

    escribir()

except ValueError:

    print("Valor Invalido")
