n = int(input("Quantos termos? "))
s = 0

for i in range(n):
    numerador = i + 1
    denominador = 2 * i + 1
    termo = numerador / denominador
    s += termo
    print(f"Termo {i+1}: {numerador}/{denominador} = {termo:.3f}")

print(f"\nSoma total: {s:.6f}")