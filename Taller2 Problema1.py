"""
Taller2
Problema1
Bianca

Crea un array o arreglo unidimensional donde le indiques el tamaño por teclado y crear
una función que rellene el array o arreglo con los múltiplos de un número pedido
por teclado."""

from operator import mod
import numpy as np


def relleno(n):
    
    lista=[] # --Lista donde acumularemos los multiplos

    contador = 0 # -- El contador inicia en 0 porque cero es multiplo de todos los numeros 

    numeromultiplo = int(input("Numero: ")) # --Numero pedido por teclado para obtener sus multiplos

    while True:
        
        if contador % numeromultiplo == 0:

            lista.append(contador) # --Agregando a la lista los multiplos

        if len(lista) >= n: # --Cuando el contador iguala al tama;o indicado por teclado rompe el ciclo

            break

        contador += 1
         

    arreglo = np.array(lista) # --Creando el arreglo unidimensional

    print("Los multiplos de ",n, "son ", arreglo) # --Imprimiendo el resultado

    print(type(arreglo))

    return


print("\n Problema 1 Crear array\n")

tamano = int(input("Ingrese el tamano: ")) # -- Tama;o que tiene el arreglo

relleno(tamano) # --Llama a funcion que rellenara el array