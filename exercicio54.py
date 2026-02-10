y = 1003
soma_total = 0

for i in range(1,51):
    y -= 3
    termo = y/i
    soma_total += termo
    print(f"Termo {i}: {y}/{i} = {termo:.2f}")

print(f"Soma total: {soma_total}")