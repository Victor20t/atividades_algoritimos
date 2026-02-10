#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo. 

try:
    numero = float(input("Insira um número: "))

    if numero > 0:
        print("Número positivo")
    elif numero < 0:
        print("Número negativo")
    else:
        print("O número é zero")

except ValueError:
    print("Não é um número válido")
