#Escreva um programa que leia três números inteiros e positivos (A, B, C) e calcule a seguinte expressão: 
# D = (R + S) / 2, onde R = (A + B)² e S = (B + C)²
A = int(input("Digite o valor de A (inteiro e positivo): "))
B = int(input("Digite o valor de B (inteiro e positivo): "))
C = int(input("Digite o valor de C (inteiro e positivo): "))
R = (A + B) ** 2
S = (B + C) ** 2
D = (R + S) / 2
print(f"O valor de D é: {D}")