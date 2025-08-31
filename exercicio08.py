#Faça um Programa que peça a temperatura em graus Farenheit, 
# transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9). 

graus_fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))

graus_celsius = 5 * (graus_fahrenheit - 32) / 9

print(f"A temperatura em Celsius é: {graus_celsius:.2f} °C")