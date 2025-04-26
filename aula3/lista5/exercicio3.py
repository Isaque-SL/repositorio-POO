def iniciais(nome):
    iniciais = []
    for i in range(len(nome)):
        nome[i] = list(nome[i])
        iniciais.append(nome[i][0])
    return "".join(iniciais)

nome = input("Digite o seu nome completo:\n").split()
inicial = iniciais(nome)
print(inicial)
