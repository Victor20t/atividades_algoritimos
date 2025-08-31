#Escrever um algoritmo que leia o nome de um vendedor,
# o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro).
#  Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas,
#  informar o seu nome, o salário fixo e salário no final do mês.
nome_vendedor = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salário fixo do vendedor: R$ "))
total_vendas = float(input("Digite o total de vendas efetuadas no mês (em R$): "))
comissao = total_vendas * 0.15
salario_final = salario_fixo + comissao

print("----- Resumo do Vendedor -----")
print(f"Nome do Vendedor: {nome_vendedor}")
print(f"Salário Fixo: R$ {salario_fixo:.2f}")
print(f"Salário Final no Mês: R$ {salario_final:.2f}")
