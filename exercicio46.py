'''
Escreva um programa que calcula a média de 30 alunos
e informa a situação (reprovado, aprovado ou recuperação).
'''

for i in range(30):

    print(f"Dados do aluno {i + 1}:")

    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    media = (nota1 + nota2 + nota3) / 3

    if media >= 7.0:
        print("Situação: Aprovado")
    elif media >= 5.0:
        print("Situação: Recuperação")
    else:
        print("Situação: Reprovado")

    print("-" * 30) 