#Faça um programa para calcular a área de N quadriláteros. Fórmula: Área = Lado * Lado.

number_quadraods = int(input("Quantos quadrados você quer calcular?"))
                       
for i in range(1,number_quadraods + 1):
    print(f"{i}º quadrilátero")
    lado = float(input("Digite o lado do quadrado: "))
    area = lado * lado 
    print(f"A area é: {area}")
print("todos os calculos foram feitos")