#Faça um Programa que peça as 4 notas bimestrais e mostre a média. 

nota1 = float(input("Insira a nota do Primeiro Bimestre: "))
nota2 = float(input("Insira a nota do Segundo Bimestre: "))
nota3 = float(input("Insira a nota do Terceiro Bimestre: "))
nota4 = float(input("Insira a nota do Quarto Bimestre: "))

soma = (nota1 + nota2 + nota3 + nota4) / 4 
print("A média bimestral é:", soma)