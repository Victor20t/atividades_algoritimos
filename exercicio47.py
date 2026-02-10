'''
Escreva um programa que leia 10 números e informe o maior e o menor número.
'''
numero = int(input("DIgite um número"))
maior_numero = numero
menor_numero = numero

for i in range(2, 10):
    novo_numero = int(input(f"Digite um número {i}"))

    if novo_numero > maior_numero:
        maior_numero = novo_numero

    if novo_numero < menor_numero:
        menor_numero = novo_numero

    print(f"O maior número digitado foi: {maior_numero}")
    print(f"O menor número digitado foi: {menor_numero}")