'''
42. Um posto está vendendo combustíveis com a seguinte tabela de descontos: 

Álcool: até 20 litros, desconto de 3% por litro acima de 20 litros, desconto de 5% por litro 

Gasolina: até 20 litros, desconto de 4% por litro acima de 20 litros, desconto de 6% por litro.

Escreva um programa que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma:
A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se
que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90. 
'''

'''
42. Um posto está vendendo combustíveis com a seguinte tabela de descontos: 

Álcool: até 20 litros, desconto de 3% por litro 
        acima de 20 litros, desconto de 5% por litro 

Gasolina: até 20 litros, desconto de 4% por litro 
          acima de 20 litros, desconto de 6% por litro.

Escreva um programa que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma:
A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se
que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90. 
'''

Combustivel = input("A - ÁLCOOL, G - GASOLINA. Faça sua escolha: ").upper()
if Combustivel != "A" and Combustivel != "G":
    print("Valor inválido") 
    exit()

litros = float(input("Digite a quantidade de litros que você deseja: "))

alcool = 1.90
gasolina = 2.50 

if Combustivel == "A":
    valorPag = litros * alcool
    nomeComb = "Álcool"
    if litros <= 20:
        desconto = 0.03
        desconto100 = "3%"
    else:
        desconto = 0.05
        desconto100 = "5%"
elif Combustivel == "G":
    valorPag = litros * gasolina
    nomeComb = "Gasolina"
    if litros <= 20:
        desconto = 0.04
        desconto100 = "4%"
    else:
        desconto = 0.06
        desconto100 = "6%"

valorDesconto = valorPag * desconto
valorFinal = valorPag - valorDesconto

print("\n--- RESUMO DA COMPRA ---")
print(f"Combustível: {nomeComb}")
print(f"Litros: {litros}")
print(f"Valor bruto: R$ {valorPag:.2f}")
print(f"Desconto ({desconto100}): R$ {valorDesconto:.2f}")
print(f"Valor final a pagar: R$ {valorFinal:.2f}")

