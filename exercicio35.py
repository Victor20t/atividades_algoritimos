#35. Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário; 
#Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário; 

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

if delta == 0:
    print("Possui apenas um raiz")
    x = -b / (2 * a)
    print(f"A raiz é: {x}")
elif delta > 0:
    print("A equação possui duas raizes reais")
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"A primeira raiz (x1) é: {x1}")
    print(f"A segunda raiz (x2) é: {x2}")
