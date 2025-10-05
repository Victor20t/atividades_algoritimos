'''Uma grande firma deseja saber qual é o empregado mais recente e qual é o mais antigo.
 Desenvolver um programa para ler um número indeterminado de informações contendo o número do empregado
   e o número de meses de trabalho deste empregado e imprimir o mais recente e o mais antigo. Obs.:
     A última informação contém os dois números iguais a zero. 
Não existem dois empregados admitidos no mesmo mês.
'''

n_empregado = []
t_servico = []
flag = 1


while flag == 1:
    nome = input("Nome do empregado: ")
    n_empregado.append(nome)
    tempo_serv = int(input("digite quantos meses ele trabalhou: "))
    t_servico.append(tempo_serv)

    flag = int(input("digite: "))
 

antigo = max(t_servico)
recente = min(t_servico)

index_antigo = t_servico.index(antigo)
index_recente = t_servico.index(recente)
index_nome = n_empregado[index_antigo]
index_nome_r = n_empregado[index_recente]

print(f"o mais antigo se chama: {index_nome} e seu tempo é de: {antigo}")
print(f"O mais recente se chama: {index_nome_r} e seu tempo é de: {recente}")
print(f"Os funcionarios: {n_empregado}")
print(f"o mais antigo tem {antigo} meses de serviço ")
print(f"o mais recente tem {recente} meses de serviço ")