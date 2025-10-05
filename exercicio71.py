login = input("Digite seu login: ")
senha = int(input("Digite sua senha: "))

lista_login = ["kezia", "victor", "admin"]
lista_senha = [1234, 5678, 0000]

if login in lista_login:
    index = lista_login.index(login)
    if senha == lista_senha[index]:
        print("Acesso permitido")
    else:
        print("Senha incorreta")
else:
    print("Login incorreto")