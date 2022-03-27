"""

Taller 3
Problema 1

Bianca

Se desea un programa que calcule el monto a pagar de las compras.
El usuario debe indicar cuando termina con las compras.
El usuario debe leer el precio del producto comprado y la cantidad.
Si el subtotal es mayor o igual a 800.00 aplicar un descuento del 2%.
Tener en un módulo las constantes del impuesto y del porcentaje de descuento.

"""

import impuestoyporcentaje as constantes




print("\nPrograma de Compras")

subtotales = 0

while True:

    try:

        producto = float(input("Precio: "))

        cantidad = int(input("Cantidad: "))

        subtotales = subtotales + (producto * cantidad)

        op = input("Ingrese X para salir ")

        if (op == "x") or (op == "X"):
            break

    except ValueError:
        print("Error de datos")

if subtotales >= 800.00:
    subtotales = subtotales * constantes.descuento

total = subtotales * constantes.impuestos

print("\nSubTotal: %.2f" % subtotales, "\nTotal: %.2f" % total)
