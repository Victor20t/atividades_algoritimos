#    8. Faça um programa para: 
#a) Ler um valor x qualquer
#b) Calcular Y = (x+1)+(x+2)+(x+3)+(x+4)+(x+5)+…(x+100).

x = float(input("digite x"))
y = 100 
soma = 0

for i in range(1,y + 1):
    y = x + i 
    soma += y
print(soma)