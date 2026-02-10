'''
45. Tendo como dados de entrada a altura e o sexo de uma pessoa, 
construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: 
para homens: (72.7*h) – 58 
para mulheres: (62.1*h) - 44.7 
(h = altura)
'''

sexo = input("Digite H para homem ou M para mulher: ").upper()
altura = float(input("Digite sua altura (em metros): "))

if sexo == "H": 
    peso_ideal = (72.7 * altura) - 58
    print(f"Seu peso ideal é: {peso_ideal:.2f} kg")
elif sexo == "M":
    peso_ideal = (62.1 * altura) - 44.7
    print(f"Seu peso ideal é: {peso_ideal:.2f} kg")
else:
    print("Informações inválidas")
