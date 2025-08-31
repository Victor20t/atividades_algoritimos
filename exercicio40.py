'''
40. Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
 O resultado da operação deve ser acompanhado de uma frase que diga se o número é: 
par ou ímpar; 
positivo ou negativo; 
inteiro ou decimal. '''

print("**** Programa de Operações ****")

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

operacao = int(input("Escolha a operação: 1 - Soma, 2 - Subtracao, 3 - Multiplicacao, 4 - Divisao: "))

if operacao == 1:
    resultado = numero1 + numero2
    nome_op = "Soma"
elif operacao == 2:
    resultado = numero1 - numero2
    nome_op = "Subtracao"
elif operacao == 3:
    resultado = numero1 * numero2
    nome_op = "Multiplicacao"
elif operacao == 4:
    if numero2 == 0:
        print("Erro: Divisao por zero nao e permitida.")
        exit()
    resultado = numero1 / numero2
    nome_op = "Divisao"
else:
    print("Operacao invalida.")
    exit()

resultado_int = int(resultado)
if resultado_int % 2 == 0:
    paridade = "Par"
else:
    paridade = "Impar"

if resultado > 0:
    sinal = "Positivo"
elif resultado < 0:
    sinal = "Negativo"
else:
    sinal = "Zero"

if resultado == resultado_int:
    tipo = "Inteiro"
else:
    tipo = "Decimal"

print(f"{nome_op}: {resultado}")
print(f"Caracteristicas: {paridade}, {sinal}, {tipo}")
