numero = int(input("Digite um número: ")) 

if numero <= 0:
    print("Número inválido. Por favor, digite um número positivo.")

flag = 1 
n = 1
while flag == 1:
    produto =  n * (n +1) * (n + 2)

    if produto == numero:
        print(f"O número {numero} é um número triangular, pois {n} * {n+1} * {n+2} = {numero}")
        flag = 0
    elif produto > numero:
            print(f"O número {numero} não é um número triangular.")
            flag = 0
    else: 
        n += 1
        flag = 1