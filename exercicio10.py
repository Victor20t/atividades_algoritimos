#Elaborar um algoritmo que efetue a apresentação do valor da conversão em real (R$) de um valor lido em dólar (US$).
#  O algoritmo deverá solicitar o valor da cotação do dólar e também a quantidade de dólares disponíveis com o usuário.

import requests
import json

url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"

try:
    resposta = requests.get(url)
    resposta.raise_for_status()  # Levanta um erro para códigos de status HTTP ruins (4xx ou 5xx)

    dados = resposta.json()
    cotacao = float(dados['USDBRL']['bid'])
    
    print(f"A cotação do dólar hoje é: R$ {cotacao:.2f}")
except requests.exceptions.RequestException as e:
    print(f"Erro ao conectar com a API: {e}")
except (KeyError, ValueError) as e:
    print(f"Erro ao processar os dados da API: {e}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")

quantidade_dolares = float(input("Digite a quantidade de dólares que você possui: "))
valor_em_reais = cotacao * quantidade_dolares
print(f"O valor em reais (R$) é: {valor_em_reais:.2f} R$")