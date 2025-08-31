#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em MBps), 
#calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
tamanho_arquivo = float(input("Digite o tamanho do arquivo para download (em MB): "))
velocidade_link = float(input("Digite a velocidade do link de Internet (em MBps): "))
tempo_download_segundos = tamanho_arquivo / velocidade_link
tempo_download_minutos = tempo_download_segundos / 60
print(f"O tempo aproximado de download do arquivo é: {tempo_download_minutos:.2f} minutos")