andares = [int(input()), int(input()), int(input())]
tempo = []

tempo.append((andares[1] * 2) + (andares[2] * 4))
tempo.append((andares[0] * 2) + (andares[2] * 2))
tempo.append((andares[0] * 4) + (andares[1] * 2))

tempo.sort()
print(tempo[0])
