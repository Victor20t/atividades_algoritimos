SalarioHora = float(input("Digite quanto você recebe por hora: "))
HorasPorMes = float(input("Digite quantas horas você trabalha por mês: "))

TotalSalario = SalarioHora * HorasPorMes

IR = TotalSalario * 11 / 100
DescontoINSS = TotalSalario * 8 / 100
Sindicato = TotalSalario * 5 / 100

SalarioLiquido = TotalSalario - (IR + DescontoINSS + Sindicato)

print(f"Salário Bruto: R${TotalSalario:.2f}")
print(f"IR (11%): R${IR:.2f}")
print(f"INSS (8%): R${DescontoINSS:.2f}")
print(f"Sindicato (5%): R${Sindicato:.2f}")
print(f"Salário Líquido: R${SalarioLiquido:.2f}")


