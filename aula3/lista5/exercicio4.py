def aprovado(nota1, nota2):
    media = (nota1 + nota2) / 2
    resultado = []
    if media >= 60:
        resultado = "Aprovado"
    else:
        resultado = "Reprovado"
    return resultado

nota1 = int(input())
nota2 = int(input())
media = aprovado(nota1, nota2)
print(media)
