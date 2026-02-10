#A Loja Mamão com Açúcar está vendendo seus produtos em 5 (cinco) prestações sem juros. 
# Faça um algoritmo que receba um valor de uma compra e mostre o valor das prestações.

valor_compra = float(input("Digite o valor da compra: R$ ")) 
valor_prestacao = valor_compra / 5
print(f"O valor de cada prestação é: R$ {valor_prestacao:.2f}")

