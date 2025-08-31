#Faça um algoritmo que receba um valor que foi depositado e exiba o valor com rendimento após um mês. 
# Considere fixo o juro da poupança em 0,70% a. m.
valor_rendimento = float(input("Digite o valor depositado: R$ "))
rendimento = valor_rendimento * 0.007
valor_final = valor_rendimento + rendimento
print(f"O valor com rendimento após um mês é: R$ {valor_final:.2f}")

