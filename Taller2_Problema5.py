"""Taller 2
Problema 5
Bianca

 Se desea un programa maneje dos arreglos de números enteros de igual tamaño. 
 El usuario debe indicar la operación aritmética que desea realizar. 
 Presentar el resultado de la operación aritmética realizada."""


import numpy as np

a = np.array([100, 1, 10, 11, 20, 21, 30, 31, 40])

b = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18])


opcion =input("Ingrese la operacion a realizar ( + - / *  %) ")

if opcion == "+":

    print(a + b)

elif opcion == "-":

    print(a - b)

elif opcion == "/":

    print(a / b)

elif opcion == "*":

    print(a * b)

elif opcion == "%":

    print(a % b)

else:
    print("Error de tipo de dato recibido")