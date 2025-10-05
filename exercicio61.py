'''
Faça um programa que peça para n pessoas a sua idade,
ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25, 26 e 60 e maior que 60;
e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
'''

n = int(input("Digite quantas pessoas vão responder: "))
soma = 0

for i in range(n):
    idade = int(input("Digite sua idade: "))  
    soma += idade                             

media = soma / n  

print(f"A soma das idades é: {soma}")
print(f"A media é igual a: {media}")

if media <= 25:
    print("A turma é de jovens")    
elif media <= 60:
    print("Turma de adultos")       
else:
    print("Turma de idosos")        