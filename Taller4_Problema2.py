"""Taller 4
Problema 2
Bianca

Crear un archivo con frases introducidas por el usuario. 
El usuario debe introducir n frases 
y las mismas deben adicionarse al archivo. 
Una vez creado el archivo 
debe tener una función que permita leer el contenido del archivo.
"""


def frases(n):

    try:

        parrafo = ""

        for i in range(n):
            linea = input("ingrese su frase: ") + " \n"
            parrafo += linea

        # ---Abre el archivo modo escritura
        archivo = open('C:\\Users\\User\\PycharmProjects\\Intermedio\\Talleres\\Taller4\\archivofrases.txt', 'w',
                       encoding='utf8')

        # --Guarda las frases en el archivo
        archivo.write(parrafo)

    except Exception as e:
        print(e)

    finally:
        archivo.close()


def leer():

    try:
        # --Abre el archivo modo lectura
        archivo = open('C:\\Users\\User\\PycharmProjects\\Intermedio\\Talleres\\Taller4\\archivofrases.txt', 'r')

        print("\nContenido del Archivo:\n")

        # --Imprime linea por linea el contenido del archivo
        for i in archivo:

            print(i)

    except Exception as e:

        print(e)

    finally:
        
        archivo.close()


print("\nPrograma de Frases")

cantidaddefrases = int(input("Ingrese cantidad de frases: "))  # --Cuantas frases ingresara

frases(cantidaddefrases)

leer()
