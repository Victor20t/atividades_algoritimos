#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores 
# e lhe contrataram para desenvolver o programa que calculará os reajustes.
#  Faça um programa que recebe o salário de um colaborador e o 
# reajuste segundo o seguinte critério, baseado no salário atual: 

#salários até R$ 280,00 (incluindo): aumento de 20% 
#salários entre R$ 280,00 e R$ 700,00: aumento de 15% 
#salários entre R$ 700,00 e R$ 1500,00: aumento de 10% 
#salários de R$ 1500,00 em diante: aumento de 5% Após o aumento ser realizado, informe na tela: 


print("--Organizações Tabajara--")
print("Aumento de salário")

salario_colaborador = float(input("Digite o valor do salario: "))

if salario_colaborador <= 280:
      percentual = 20
elif 280.00 < salario_colaborador <= 700.00:
      percentual = 15
elif 700.00 < salario_colaborador <= 1500.00:
    percentual = 10 
else:
      percentual = 5

aumento = salario_colaborador * percentual/100
novo_salario = salario_colaborador + aumento 

if salario_colaborador <= 280:
      print(f"O salario era de {salario_colaborador}")
      print("O aumento foi de 20%")
      print(f"O aumento foi de {aumento}")
      print(f"o novo salario é de {novo_salario}")
elif salario_colaborador <= 700:
      print(f"O salario era de {salario_colaborador}")
      print("O aumento foi de 15%")
      print(f"O aumento foi de {aumento}")
      print(f"o novo salario é de {novo_salario}")
elif salario_colaborador <= 1500:
      print(f"O salario era de {salario_colaborador}")
      print("O aumento foi de 10%")
      print(f"O aumento foi de {aumento}")
      print(f"o novo salario é de {novo_salario}")
else:
      print(f"O salario era de {salario_colaborador}")
      print("O aumento foi de 5%")
      print(f"O aumento foi de {aumento}")
      print(f"o novo salario é de {novo_salario}")


