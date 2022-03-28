"""
Taller 4
Problema4
Bianca

Crear un programa que a partir de una lista creada por el usuario
que tenga el nombre de cinco frutas
pase a crear un archivo de texto.
Tener funciones que permitan realizar las acciones
de leer una línea del archivo,
leer todas las líneas del archivo,
mover el puntero en el archivo
"""


def crear_archivo():
    try:

        parrafo = []

        for i in range(5):
            linea = input("Fruta: ")
            parrafo.append(linea)
        print(parrafo)

        # ---Abre el archivo modo escritura
        archivo = open('frutas.txt', 'w', encoding='utf8')

        # --Guarda las frases en el archivo
        for f in parrafo:
            archivo.write(str(f))
            archivo.write("\n")

    except Exception as e:
        print(e)

    finally:
        archivo.close()


def leeru(l):
    try:
        # --Abre el archivo modo lectura
        archivo = open('frutas.txt', 'r')

        print("\nLinea del Archivo:\n")
        print(archivo.readlines()[l-1])


    except Exception as e:

        print(e)

    finally:

        archivo.close()


def leert():
    try:
        # --Abre el archivo modo lectura
        archivo = open('frutas.txt', 'r')
        # --Imprime el contenido del archivo
        print("Contenido del Archivo:\n")

        print(archivo.read())

    except Exception as e:

        print(e)

    finally:

        archivo.close()


def mpuntero():
    try:

        posicion = int(input("A donde desea desplazar el puntero:\n1 Inicio 2 Actual 3 final "))
        # --Abre el archivo modo lectura
        archivo = open('frutas.txt', 'r')

        archivo.seek(posicion-1)
        line = archivo.readline()
        print("La lectura de datos con seek es ", line)

    except Exception as e:

        print(e)

    finally:

        archivo.close()


print("\nPrograma de Frutas")

crear_archivo()

linea = int(input("Cual linea desea leer? "))

leeru(linea)

leert()

mpuntero()
