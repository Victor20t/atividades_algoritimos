# 33. Faça um Programa que peça os 3 lados de um triângulo.
# O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#
# Dicas:
# - Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro.
# - Triângulo Equilátero: três lados iguais.
# - Triângulo Isósceles: quaisquer dois lados iguais.
# - Triângulo Escaleno: três lados diferentes.

lado1 = float(input("Digite um lado"))
lado2 = float(input("Digite um lado"))
lado3 = float(input("Digite um lado"))

if  lado1 > 0 and lado2 > 0 and lado3 >0:
    if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
        print("Definitivamente é um triângulo")
        if lado1 == lado2 and lado2 == lado3:
            print("é quilatero")
        elif lado1 == lado2 or lado2 == lado3 or lado3 ==lado1:
            print("é iso")
        else:
            print("é escaleno")
    else:
        print("Não é um triângulo")
else:
    print("Informa Números Positivos")
