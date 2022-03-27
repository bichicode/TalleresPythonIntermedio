"""
Taller 3

Problema 3

Bianca

Se desea un programa que lea los empleados de un departamento
y sus horas trabajadas en la semana
y el salario por hora.
Tener un módulo que calcule el salario a pagar.

"""


import calculo

print("\nprograma de planilla")

try:

    planilla = ""

    cant = int(input("Cantidad de empleados: "))

    for i in range(cant):

        empleado = input("Nombre: ")

        horas = int(input("Horas: "))

        sal = float(input("Salario: "))

        bruto, neto = calculo.salario(horas, sal)

        planilla += empleado + " Salario bruto: " + str(bruto) + " Salario neto: " + str(neto) + "\n"

    print(planilla)

except ValueError:
    print("Valor Invalido")
