#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário. 

lado_do_quadrado = float(input("Insira o lado do quadrado: "))

area = lado_do_quadrado ** 2
dobro_da_area = area * 2

print(f"A área do quadrado é: {area:.2f}")
print(f"O dobro da área é: {dobro_da_area:.2f}")

