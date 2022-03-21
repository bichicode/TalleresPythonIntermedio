"""Taller 1
Problema 3
Bianca
Crear una lista con cinco valores numéricos enteros.
El programa debe solicitar al usuario
la posición que ocupa en la lista el numero a consultar.
Cree una excepción que valide
que la posición ingresada por el usuario no se salga fuera del rango
de los índices de los valores que forman la lista"""

print("\nPrograma de Errores Valores Numericos")

lista = [0, 10, 20, 30, 40]

try:
    posicion = int(input("Ingrese la posicion del numero a consultar: "))

    print(lista[posicion])

except ValueError:
    print("Valor Invalido")

except IndexError:
    print("Ese indice esta fuera del rango")
