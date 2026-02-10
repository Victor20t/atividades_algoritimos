x = float(input("valor de x: "))  
soma = 0
for i in range(50):
    expoente = 2 * i + 1
    sinal = (-1) ** i
    termo = sinal * (x ** expoente) / expoente
    soma += termo
print(soma)