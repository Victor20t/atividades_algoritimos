#Faça um programa para somar os números pares positivos < 1000 e ao final escrever o resultado.

np = 1000
soma = 0

for i in range(2,np,2):
    soma += i
print(soma)