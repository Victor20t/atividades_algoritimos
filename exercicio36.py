#Faça um Programa que peça um número correspondente a um determinado ano e em
#  seguida informe se este ano é ou não bissexto. 

numeroDoAno = int(input("Digite o Ano da sua escolha: "))

if numeroDoAno % 400 == 0:
    print("O ano é bissexto.")
elif numeroDoAno % 100 == 0:
    print("O ano não é bissexto.")
elif numeroDoAno % 4 == 0:
    print("O ano é bissexto.")
else:
    print("O ano não é bissexto.")