time_1 = 0
time_2 = 0

flag = 1 
pontos = 0

while flag == 1:
    time_1, time_2 = input("Digite o placar do jogo (time1 time2): ").split()
    list_time1 = [int(time_1)]
    list_time2 = [int(time_2)]

    flag = int(input("Deseja registrar outro jogo? (1-sim/0-nao): "))

    if time_1 > time_2:
        print("Vitoria do time 1")
        pontos += 3
    elif time_2 > time_1:
        print("Vitoria do time 2")
        pontos += 3
    else:
        print("Empate")
        pontos += 1

print("Total de pontos:", pontos)