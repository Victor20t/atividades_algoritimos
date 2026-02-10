'''
41.Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são: 
    "Telefonou para a vítima?" 
    "Esteve no local do crime?" 
    "Mora perto da vítima?" 
    "Devia para a vítima?" 
    "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente". 
'''
print("Responda sim ou não")

suspeita = 0 

Pergunta1 = input("Telefonou para a vítima? ").upper()
Pergunta2 = input("Esteve no local do crime? ").upper()
Pergunta3 = input("Mora perto da vítima? " ).upper()
Pergunta4 = input("Devia para a vítima? " ).upper()
Pergunta5 = input("Já trabalhou com a vítima? ").upper()

if Pergunta1 == "SIM":
    suspeita += 1

if Pergunta2 == "SIM":
    suspeita += 1 

if Pergunta3 == "SIM":
    suspeita += 1 

if Pergunta4 == "SIM":
    suspeita += 1 

if Pergunta5 == "SIM":
    suspeita += 1 

print(f"\nTotal de respostas SIM: {suspeita}")

if suspeita == 2:
    print("Classificação: Suspeita")
elif 3 <= suspeita <= 4: 
    print("Classificação: Cúmplice")
elif suspeita == 5:
    print("Classificação: Assassino")
else:
    print("Classificação: Inocente")
