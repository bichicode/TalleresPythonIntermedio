"""
Taller 4
Problema 3
Bianca

Crear un programa que a partir de una lista que contenga marcas de autos crear un archivo
de texto. La lista debe ser cargada cuando se ejecute el programa.

"""
try:

    print("\nPrograma de Marcas de Autos\n")

    marcas = ['Audi', 'Toyota', 'BMW', 'Ferrari']

    archivo = open('marcas.txt', 'w', encoding='utf8')  # --Creo y abro el archivo

    archivo.write(str(marcas))  # --Guardo la lista en el archivo

    archivo.close() # --Cierro el archivo

except Exception as e:
    print(e)
