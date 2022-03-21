"""Taller 1
Problema 2
Bianca
Crear un diccionario que manejo información para cinco colores.
Buscar la descripción en el diccionario
según la clave que indique el usuario.
Crear una excepción para evitar que el programa falle
cuando el usuario ingrese una clave que no existe en el diccionario.
"""

print("\nManejo de Errores Diccionario")

diccionario = {"rojo": "El color de la manzana", "azul": "El mar", "amarillo": "El sol",
               "Verde": "Las hojas de los arboles"}
try:
    llave = input("Ingrese la clave: ")

    print(diccionario[llave])

except KeyError:
    print("Error, la clave no es valida ")
