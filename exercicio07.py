#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.

salario_por_hora = float(input("Quanto você ganha por hora? "))
horas_trabalhadas_no_mes = float(input("Quantas horas você trabalhou no mês? "))

salario_total = salario_por_hora * horas_trabalhadas_no_mes

print(f"O seu salário total neste mês é: R$ {salario_total:.2f}")