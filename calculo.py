"""
Taller 3
Problema 3
Bianca
Tener un módulo que calcule el salario a pagar.
Si en la semana el trabajador excede las 40 horas el excedente debe calcularse el salario por hora con
un recargo del 1.50%.
Indicar el monto del salario bruto,
el impuesto de seguro social 9.75%,
el impuesto de seguro educativo 1.25
y el salario neto (salario bruto menos los impuestos).
"""


def salario(horas, rata):

    pexcedente = 0

    if horas > 40:

        excedente = horas - 40

        pexcedente = excedente * (rata*1.50)

        horas = 40

    bruto = horas * rata + pexcedente

    ss = bruto * 0.0975

    se = bruto * 0.0125

    neto = round(bruto - ss - se, 2)

    return round(bruto, 2), neto

