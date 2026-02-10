#Faça um Programa que leia três números e mostre o maior deles.

numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite mais um número: "))
numero3 = float(input("Digite outro número: "))

if numero1 > numero2 and numero1 > numero3:
    print(f"Número {numero1} é o maior")
elif numero2 > numero1 and numero2 > numero3:
    print(f"Número {numero2} é o maior")
elif numero3 > numero1 and numero3 > numero2:
    print(f"Número {numero3} é o maior")
else:
    print("Os números são iguais ou há empate")
