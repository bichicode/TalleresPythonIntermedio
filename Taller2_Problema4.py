"""Taller 2
Problema 4
Bianca

Se desea un programa que maneje en un arreglo por trimestre 
las ventas para tres sucursales. 
El programa debe suministrar la siguiente información:
a. La sucursal con mayor venta en todo el año.
b. Según el trimestre que indica el usuario cuál es la sucursal con la mayor venta.
c. Según el trimestre que indica el usuario cuál es la sucursal con la menor venta.
"""

import numpy as np 

trimestres = 4 # --hay cuatro trimestres por anio

sucursales = 3

lista = []

totales = []

for j in range(trimestres):
    
    print ("\nTrimestre", j+1)

    for i in range(sucursales):

        print("Sucursal", i+1)
        nventas = float(input("Ingrese la venta: ")) 
        totales.append(nventas) # --Agregando a la lista del trimestre 

trimestre1 = np.array(totales[0:3]) # --Creando arreglos
trimestre2 = np.array(totales[3:6])
trimestre3 = np.array(totales[6:9])
trimestre4 = np.array(totales[9:])

sucursal1 = np.array([trimestre1[0], trimestre2[0], trimestre3[0], trimestre4[0]])
sucursal2 = np.array([trimestre1[1], trimestre2[1], trimestre3[1], trimestre4[1]])
sucursal3 = np.array([trimestre1[2], trimestre2[2], trimestre3[2], trimestre4[2]])


# ------sucursal con mayor venta en todo el a;o

A = sum(sucursal1)
B = sum(sucursal2)
C = sum(sucursal3)

if(A > B and A > C):
    print("La sucursal con mayor venta en todo el año es la sucursal 1 con ", A)

elif(B > A and B > C):
    print("La sucursal con mayor venta en todo el año es la sucursal 2 con ", B)

else:
    print("La sucursal con mayor venta en todo el año es la sucursal 3 con ", C)

# ----Según el trimestre que indica el usuario cuál es la sucursal con la mayor venta.

comparar = int(input("Ingrese el trimestre para saber la mayor venta "))

print("La mayor venta es: ")

if comparar == 1:
    print(max(trimestre1))

elif comparar == 2:
    print(max(trimestre2))

elif comparar == 3:
    print(max(trimestre3))

elif comparar == 4:
    print(max(trimestre4))

# ----Según el trimestre que indica el usuario cuál es la sucursal con la mayor venta.

comparar = int(input("Ingrese el trimestre para saber la menor venta "))

print("La menor venta es: ")

if comparar == 1:
    print(min(trimestre1))

elif comparar == 2:
    print(min(trimestre2))

elif comparar == 3:
    print(min(trimestre3))

elif comparar == 4:
    print(min(trimestre4))

