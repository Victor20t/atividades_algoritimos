#Faça um Programa que peça dois números e imprima o maior deles. 

try:
    numero1 = float(input("Digite um número: "))
    numero2 = float(input("Digite mais um número: "))

    if numero1 > numero2:
        print(f"Número {numero1} é maior que {numero2}")
    elif numero2 > numero1:
        print(f"Número {numero2} é maior que {numero1}")
    else:
        print("Os números são iguais")

except ValueError:
    print("Não é um número válido")

