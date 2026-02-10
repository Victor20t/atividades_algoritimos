#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
#  Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!"
#  ou "Valor Inválido!", conforme o caso. 

print("Em qual turno você estuda? ")
print("Digite M para Matutino, V para Vespertino ou N para Noturno.")

turnoAluno = input("Digite aqui: ").upper()

if turnoAluno == "M":
    print("Bom dia!")
elif turnoAluno == "V":
    print("Boa tarde!")
elif turnoAluno == "N":
    print("Boa noite!")
else:
    print("Valor Inválido!")
