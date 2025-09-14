contador = 0
contador_regular = 0
contador_bom = 0 
some = 0

for i in range(15):
    idade = int(input("Digite sua idade: "))
    quest = int(input("Qual sua nota em relação ao filme: ótimo -> 3, bom -> 2, regular -> 1.: "))
    
    if quest == 3:
        some += idade
        contador += 1
    if quest == 1:
        contador_regular += 1
    if quest == 2:
        contador_bom += 1

total = contador_regular + contador + contador_bom
porcentagem = (contador_bom / total) * 100

if contador > 0:
    media = some / contador
    print(f"Média de idade de quem respondeu ótimo: {media:.1f}")
else:
    print("Ninguém respondeu ótimo")

print(f"Quantidade de pessoas que responderam REGULAR: {contador_regular}")
print(f"Porcentagem de pessoas que responderam BOM: {porcentagem:.1f}%")