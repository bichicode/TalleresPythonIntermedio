"""
Taller 5
Problema 1
Bianca

Crear un archivo llamado cotizaciones.xlsx
que almacene las cotizaciones de la compañía
con las siguientes columnas:
Nombre (nombre del cliente),
cantidad,
monto.
a. Tener una función que permita leer el archivo creado.
b. Tener una función que permita leer una columna del archivo creado.

"""

import pandas as pd
from openpyxl import load_workbook
from openpyxl.utils import column_index_from_string


# función que permita leer el archivo creado
def leer_archivo():
    dif = pd.read_excel('cotizaciones.xlsx', header=None)
    print(dif)
    return


# Función que permita leer una columna del archivo creado.
def leer_columna():

    filesheet = 'cotizaciones.xlsx'

    wb = load_workbook(filesheet)

    column = input("Ingrese (B Nombre), (C Cantidad), (D Monto) ")

    sheet = wb.active

    ncol = column_index_from_string(column)

    for cell, in sheet.iter_rows(min_col=ncol, max_col=ncol, values_only=True):

        print(cell)

    return


data = {}
nombre = []
cantidad = []
monto = []

while True:

    nom = input("Nombre del Cliente: ")
    nombre.append(nom)

    cant = int(input("cantidad: "))
    cantidad.append(cant)

    mon = input("Monto: ")
    monto.append(mon)

    op = input("Presione X para salir")

    if op == 'x' or op == 'X':
        break

zipped = list(zip(nombre, cantidad, monto))

df = pd.DataFrame(zipped, columns=['nombre', 'cantidad', 'monto'])

# print(df)

# Crear un archivo llamado cotizaciones.xlsx que almacene las cotizaciones de la compañía
df.to_excel('cotizaciones.xlsx')

leer_archivo()

leer_columna()





