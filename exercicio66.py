salario_main = []
filhos_main = []
contador = 0
executar = 999

while executar == 999:
    salario = int(input("DIgite seu salario: "))
    salario_main.append(salario)
    filho = int(input("digite a quantidade de filhos: "))
    filhos_main.append(filho)
    contador += 1
    executar = int(input("digite -999 para sair ou 999 para continuar "))

#MEDIA SALARIAL DA POPULAÇÃO ---> 
soma = sum(salario_main)
media = soma/contador
print(f"media de salario da populção: {media}")

#Media de quantidades de filhos -----> 
soma_filhos = sum(filhos_main)
media_filhos = soma_filhos/contador
print(f"A media de filhos da população é: {media_filhos:.2f}")

#maior salariio da populção 
maior_salario = max(salario_main)
print(f"o mairo salario foi de: {maior_salario}")

#percentual de pessoas com slaario de ate 250 

numero = 250
quantidade_250 = salario_main.count(numero)
quantidade_geral = len(salario_main)

porcentagem = quantidade_250 * quantidade_geral /100

print(f"A quanridade de pessoas que recebem 250 é de {porcentagem*100}%")
