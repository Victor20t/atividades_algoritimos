#Faça um programa para calcular um valor A elevado a um expoente B. Os valores A e B deverão ser lidos. 
# Não usar A** B  e sim uma estrutura de repetição.

a = int(input("Digite o valor de A: "))
b = int(input("Digite o expoente B: "))
reserva = 1

for i in range(b):
    reserva *= a

print(f"{a}^{b} = {reserva}")