"""
Taller 1
Problema 1
Bianca
Cree un programa que solicite la edad del usuario y
si la edad es igual o mayor a 18
el programa debe un mensaje "Es adulto"
de lo contrario
"Es menor de edad".
Implemente el uso de excepciones para que el usuario no pueda ingresar un valor invalido en la edad.

"""

print("\nPrograma de edades")

try:
    edad = int(input("Favor ingresar la edad: "))

    if edad > 17:
        print("Es adulto")

    else:
        print("Es menor de edad")

except ValueError:

    print("Valor Invalido")

