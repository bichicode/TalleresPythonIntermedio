"""
Taller 3
Problema 2
Modulo para validacion

criterios de aceptación:
• El nombre de usuario debe contener un mínimo de 6 caracteres y un máximo de 12. X
• El nombre de usuario debe ser alfanumérico. X
• Nombre de usuario con menos de 6 caracteres, retorna el valor 2. x
Enviar un mensaje que le indique al usuario lo ocurrido.
• Nombre de usuario con más de 12 caracteres, retorna el retorna el valor 3.
Enviar un mensaje que le indique al usuario lo ocurrido. x
• Nombre de usuario con caracteres distintos a los alfanuméricos, retorna el retorna el
valor 0. Enviar un mensaje que le indique al usuario lo ocurrido.
• Nombre de usuario válido, retorna el valor 1.
"""


def vali(nombre):
    try:
        if len(nombre) > 6 and len(nombre) < 13:
            return 1

        elif len(nombre) < 6:
            print("Error de cantidad de caracteres")
            return 2

        elif len(nombre) > 12:
            print("Error de cantidad de caracteres")
            return 3

    except ValueError:
        print("El nombre de usuario debe ser alfanumérico")
        return 0
