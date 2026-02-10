#Escreva um programa que calcula o fatorial de um dado número N.

n = 5 
resultado = 1

for i in range(1, n + 1):
    resultado *= i 

print(resultado)