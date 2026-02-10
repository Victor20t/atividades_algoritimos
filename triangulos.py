lista = []

i = 0
while i < 3:
    valor = float(input(f"Digite o {i+1}º número positivo: "))
    if valor <= 0:
        print("Valor inválido. Digite novamente.")
        continue
    lista.append(valor)
    i += 1

def bubbleSort(lista):
    n = len(lista)
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                swapped = True
        if not swapped:
            break

if __name__ == "__main__":
    bubbleSort(lista)

    print("Sorted array:")
    for i in range(len(lista)):
        print(lista[i], end=" ")

def trianguloSorN(lista):

    if lista[0] + lista[1] > lista[2]:
        return True
    else:        
        return False
    
def tipo_triangulo(lista):

    if lista[0] == lista[2]:
        return "Equilátero"
    elif lista[0] == lista[1] or lista[1] == lista[2]:
        return "Isósceles"
    else:
        return "Escaleno"

if trianguloSorN(lista):
    print("Os números formam um triângulo.")
    print(f"É um triângulo do tipo: {tipo_triangulo(lista)}")
else:
    print("Os números não formam um triângulo.")


"."