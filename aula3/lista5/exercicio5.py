def formatar_nome(nome):
    partes = nome.split()
    nome_formatado = []
    for parte in partes:
        nome_formatado.append(parte.capitalize())
    return ' '.join(nome_formatado)
nome = input("Digite seu nome: ")
print(f"Nome formatado: {formatar_nome(nome)}")
