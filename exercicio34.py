# 34. Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
#  O programa deverá pedir os valores de a, b e c e fazer as consistências,
#  informando ao usuário nas seguintes situações: 
#Se o usuário informar o valor de A igual a zero,
#  a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado; 
#Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuáro e encerre o programa; 

import math

a = float(input("Digite o valor de A: "))

if a != 0:
    b = float(input("Digite o valor de B: "))
    c = float(input("Digite o valor de C: "))
else:
    print("Não é equação do segundo grau")
    exit()

delta = b**2 - (4 * a * c)

if delta < 0:
    print("Não existem raízes reais")
else:
    raiz = math.sqrt(delta)
    print("Cálculo das raízes")
    x1 = (-b + raiz) / (2 * a)
    x2 = (-b - raiz) / (2 * a)
    print(f"Valor de x1 = {x1} e valor de x2 = {x2}")
3