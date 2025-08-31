# 32. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
# e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#
# Média de Aproveitamento   Conceito
# Entre 9.0 e 10.0          A
# Entre 7.5 e 9.0           B
# Entre 6.0 e 7.5           C
# Entre 4.0 e 6.0           D
# Entre 4.0 e zero          E
#
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem
# “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite um número: "))
numero3 = float(input("Digite um número: "))
numero4 = float(input("Digite um número: "))

media = (numero1 + numero2 + numero3 + numero4) / 4

if 9.0 <= media <= 10.0:
    print("O conceito da sua nota é A")
    print("APROVADO")
elif 7.5 <= media < 9.0:
    print("O conceito da sua nota é B")
    print("APROVADO")
elif 6.0 <= media < 7.5:
    print("O conceito da sua nota é C")
    print("APROVADO")
elif 4.0 <= media < 6.0:
    print("O conceito da sua nota é D")
    print("REPROVADO")
else:
    print("O conceito da sua nota é E")
    print("REPROVADO")

print(f"As notas do semestre: {numero1}, {numero2}, {numero3}, {numero4}")
print(f"A sua média foi: {media:.2f}")
