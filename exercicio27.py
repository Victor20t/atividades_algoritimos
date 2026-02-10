#Faça um programa que pergunte o preço de três produtos 
# e informe qual produto você deve comprar, 
# sabendo que a decisão é sempre pelo mais barato. 

Produto1 = float(input("Digite o primeiro preço do produto: "))
Produto2 = float(input("Digite o segundo preço do produto: "))
Produto3 = float(input("Digite o terceiro preço do produto: "))

if Produto1 < Produto2 and Produto1 < Produto3:
    print(f"O produto com preço {Produto1} é o mais barato")
elif Produto2 < Produto1 and Produto2 < Produto3:
    print(f"O produto com preço {Produto2} é o mais barato")
elif Produto3 < Produto1 and Produto3 < Produto2:
    print(f"O produto com preço {Produto3} é o mais barato")
else:
    print("Os preços são iguais ou há empate")
