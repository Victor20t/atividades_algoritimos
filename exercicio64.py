valor_de_divida = int(input("Digite o valor da divida: "))
quantidade_de_parcelas = 0 
valor_do_juros = 0 
valor_da_parcela = 0

print( ''' 

'Quantidade de Parcelas  % 'de Juros sobre o valor inicial da dívida
        1      			     0
	3   		             10
	6       		         15
	 ''')

quantidade_de_parcelas = int(input("Quantas parcelas: "))

if quantidade_de_parcelas == 3:
    valor_do_juros = 10
elif quantidade_de_parcelas == 6:
        valor_do_juros = 15
else:
    valor_da_parcela = 0 

juros = valor_de_divida * valor_do_juros/100
print("#" * 30)
print(f"Valor da divida: {valor_de_divida}")
print(f"Valo do juros: {juros}")
print(f"Quantidade de parcelas {quantidade_de_parcelas}")
print(f"Valor total: {valor_de_divida+juros}")


'''
valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela. '''
