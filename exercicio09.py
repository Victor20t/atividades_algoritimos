#Faça um Programa que peça a temperatura em graus Celsius,
#  transforme e mostre em graus Farenheit.

graus_celsius = float(input("Digite a temperatura em graus Celsius: "))
graus_fahrenheit = (graus_celsius * 9 / 5) + 32
print(f"A temperatura em Fahrenheit é: {graus_fahrenheit:.2f} °F")
