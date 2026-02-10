'''
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
Um número primo é aquele que é divisível somente por ele mesmo e por 1.
'''

numero_inteiro = int(input("Digite aqui um número inteiro: "))
eh_primo = True

if numero_inteiro <= 1:
    print("Não é primo")
elif numero_inteiro == 2:
    print("É primo")
else:
    eh_primo = True

for i in range(2, numero_inteiro):
    if numero_inteiro % i == 0:
        eh_primo = False

    
if eh_primo == True:
    print("É primo")
else:
    print("Não é primo")