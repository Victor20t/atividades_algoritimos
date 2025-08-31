atleta_idade = int(input("DIgite a idade do Atleta: "))

if atleta_idade < 5:
    print("Idade não se enquadra em nenhuma categoria.")
elif 5 <= atleta_idade <= 7:
    print("Infantil A")
elif 8 <= atleta_idade <= 10:
    print("Infantil B")
elif 11 <= atleta_idade <= 13:
    print("Juvenil A")
elif 14 <= atleta_idade <= 17:
    print("Juvenil B")
else:
    print("Adulto")