# 37. Faça um Programa para leitura de três notas parciais de um aluno.
#  O programa deve calcular a média alcançada por aluno e apresentar: 
#A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada; 
#A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada; 
#A mensagem "Aprovado com Distinção", se a média for igual a 10. 

nota1 = float(input("Digite uma nota: "))
nota2 = float(input("Digite uma nota: "))
nota3 = float(input("Digite uma nota: "))
nota4 = float(input("Digite uma nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f"Média alcançada: {media:.2f}")

if media == 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
