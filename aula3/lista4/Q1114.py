senha = 2002
tentativa = int(input())

if tentativa == senha:
    print("Acesso Permitido")
else:
    print("Senha Invalida")
    while tentativa != senha:
        tentativa = int(input())
        if tentativa == senha:
            print("Acesso Permitido")
        else:
            print("Senha Invalida")
