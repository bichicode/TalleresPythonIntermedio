"""Taller 2
Problema 2
Bianca

Crear un arreglo con los vendedores de una sucursal. El usuario debe indicar la cantidad
de vendedores. En un segundo arreglo crear los montos de las ventas del mes. El
programa debe indicar el nombre del vendedor y la comisión del 3% que gana en el mes
con respecto a los montos de las ventas reportadas.
"""

import numpy as np


def comision(n):
    
    lista=[] # --Lista donde acumularemos los vendedores

    totales=[] # --Lista donde acumularemos las ventas

    for i in range(n):
        
        vendedor = input("Vendedor: ")

        lista.append(vendedor) # --Agregando a la lista los vendedores

        venta = float(input("Venta del mes: ")) 

        totales.append(venta) # --Agregando a la lista la venta del mes

         
    avendedor = np.array(lista) # --Creando arreglos
    atotales = np.array(totales)
    
    for i in range(n):
    
        print("Vendedor", avendedor[i], "Comision ", atotales[i]*0.03) # --Imprimiendo el resultado

    return


print("\n Problema 2 Vendedores\n")

tamano = int(input("Cantidad de vendedores: ")) 

comision(tamano) # --Llama a funcion que rellenara el array