'''
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa
que leia um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperatura informada,
bem como a média das temperaturas. 
'''

temperaturas = 0 
soma = 0 
maior = -float('inf')
menor = float('-inf')
contador = 0
continuar = True

while continuar:
    temp = float(input("Digite a temperatura (ou -999 para sair): "))
    if temp == -999:
        continuar = False
    else:
        soma += temp
        contador += 1
        if temp > maior:
            maior = temp
        if temp < menor or menor == float('-inf'):
            menor = temp
        
        media = soma / contador
    
    print(f"Maior temperatura: {maior}")
    print(f"Menor temperatura: {menor}")