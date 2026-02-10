#Faça um programa que receba dois números inteiros e
#gere os números inteiros que estão no intervalo compreendido por eles.

numero1 = int(input("Digite um numero inteiro"))
numero2 = int(input("Digite um numero inteiro"))

if numero1 < numero2:
    for i in range(numero1 + 1, numero2):
        print(i)
elif numero1 > numero2:
    for i in range(numero2 + 1, numero1):
        print(i)