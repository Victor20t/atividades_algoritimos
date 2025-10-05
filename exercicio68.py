codigos = [100,101,102,103,104,105]
lanches = ["Cachorro quente", "bauru simples", "bauru com ovo", 'Hambúrguer', "cheeseburguer", "refrigerante"]
precos = [1.20, 1.30,1.50,1.20,1.30,1.0]

print("lanches\tcodigo\tpreco")
print( "-" * 30)
for lanche, codigo, preco in zip(lanches, codigos, precos):
    print(f"{lanche}\t{codigo}\t{preco}")
    print("-" * 30)
total_compra = 0.0
flag = 1

while flag == 1:
    input_codigo = int(input("Digtie o codigo do seu lanche: "))
    quantidade = int(input("Digite a quantidade: "))
    soma = quantidade * precos[codigos.index(input_codigo)]
    total_compra += soma

    if input_codigo in codigos:
        index = codigos.index(input_codigo)
        print(f"Voce pediu {quantidade} {lanches[index]} que custa R$ {precos[index]:.2f}, ao total deu R$ {quantidade * precos[index]:.2f}")
        print(f"Total parcial: R$ {total_compra:.2f}")
    else:
        print("Codigo invalido")

    flag = int(input("Deseja pedir mais alguma coisa? (1-sim/0-nao): "))

