'''
Faça um programa que leia uma quantidade não determinada de números positivos.
Calcule a quantidade de números pares e ímpares,
a média de valores pares e a média geral dos números lidos. O número que encerrará a leitura será zero.
'''

numeros = [ ]
contador = 0

flag = 1 
print("para sair do loop digite 0")

while flag == 1: 
    numero = int(input("Digite um numero inteiro positivo: "))
    if numero < 0: 
        print("APenas número positivos meu bom!")
        flag = 1
    else:
        numeros.append(numero)
    contador += 1
    
    if numero < 1:
        flag = 0 

pares = 0
impares = 0
soma_de_pares = 0

for x in numeros:
    if x % 2 ==0:
        pares += 1
        soma_de_pares += x
    else:
        impares += 1
soma_numeros = sum(numeros)
media_pares = soma_de_pares/pares
media_geral = soma_numeros/(contador -1)
print(f"A media geral é {media_geral}")
print(f"a media de pares é {media_pares}")
print(f"QUantidade de numeros pares: {pares}")
print(f"Quantidade de numeros impares: {impares}")

print(numeros)