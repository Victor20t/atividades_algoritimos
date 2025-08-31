valor_hora = float(input("Digite aqui o valor da sua hora trabalhada: "))
hora_por_mes = int(input("Digite quantas horas você trabalha por mês: "))

salario_bruto = valor_hora * hora_por_mes 

if salario_bruto <= 900.00:
    percentual = 0
    percentual_str = "Isento"
elif salario_bruto <= 1500:
    percentual = 0.05
    percentual_str = "5%"
elif salario_bruto <= 2500:
    percentual = 0.10
    percentual_str = "10%"
else:
    percentual = 0.20
    percentual_str = "20%"

inss = salario_bruto * 0.10
fgts= salario_bruto * 0.11
ir = salario_bruto * percentual

total_descontos = inss + ir 
salario_liquido = salario_bruto-total_descontos

print(f"i. Salário Bruto: R$ {salario_bruto:.2f}")
print(f"ii. (-) IR ({percentual_str}) : R$ {ir:.2f}")
print(f"iii. (-) INSS (10%) : R$ {inss:.2f}")
print(f"iv. FGTS (11%) : R$ {fgts:.2f}")
print(f"v. Total de descontos : R$ {total_descontos:.2f}")
print(f"vi. Salário Líquido : R$ {salario_liquido:.2f}")