# 14. Escrever um algoritmo para determinar o consumo médio de um automóvel sendo fornecida a distância total 
# percorrida pelo automóvel e o total de combustível gasto.
distancia_percorrida = float(input("Digite a distância total percorrida (em km): "))
combustivel_gasto = float(input("Digite o total de combustível gasto (em litros): "))
consumo_medio = distancia_percorrida / combustivel_gasto
print(f"O consumo médio do automóvel é: {consumo_medio:.2f} km/l")
