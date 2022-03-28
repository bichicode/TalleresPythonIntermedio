"""Taller 4
Problema 1
Bianca
Crear una función que pida dos números n y m entre 1 y 10, 
lea el fichero tabla-n 
(aquí usted debe tener la tabla de multiplicar del número n). 
Mostrar en pantalla la línea m del fichero. Si
el fichero no existe debe mostrar un mensaje por pantalla informando de ello."""


def tabla(n1, nombre1):

    try:

        tablita = ""

        for i in range(13):  # --Itera para crear las lineas de la tabla
            linea = str(n1) + " X " + str(i) + " = " + str(n1*i) + " \n"
            tablita += linea

        archivo = open(nombre1, 'w', encoding='utf8')  # --Crea el archivo

        archivo.write(tablita)  # --Guarda la tabla en el archivo
        
    except Exception as e:
        print(e)

    finally:
        archivo.close()  # --Cierra el archivo


def leer(n0, m0, nombre0):
    try:
        archivos = open(nombre0, 'r')  # --abre el archivo
        
        print(archivos.readlines()[m0])  # --imprime la linea solicitada

        archivos.close()  # --Cierra el archivo

    except FileNotFoundError:  # --Si no existe el archivo retorna 2
        
        print("No existe el fichero con la tabla del ", n0)
        return 2
        
    except Exception as e:

        print(e)

        return 1

    # --Se elimino el bloque finally porque cuando no existe el archivo manda error


print("\nPrograma de las tablas de multiplicar")

n = int(input("Ingrese el primer numero entre 1 y 10: "))  # ---Numero de la tabla de multiplicar

m = int(input("Ingrese el segundo numero (linea del fichero): "))  # --Linea

nombre = 'tabla-' + str(n) + '.txt'  # --Nombre del archivo se crea dinamicamente

var = leer(n, m, nombre)  # --Va imprimir la linea m

if var == 2:  # --si el archivo no existe retorna 2

    opcioncrear = input("Desea crear el fichero S/N: ")

    if opcioncrear == "S" or opcioncrear == "s":  # --Si desea crear el archivo

        tabla(n, nombre)   # --crea el archivo con la tabla de multiplicar
        
        var = leer(n, m, nombre)   # --Va imprimir la linea m
