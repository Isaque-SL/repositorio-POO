valores = []
for i in range(100):
    valor = int(input())  
    valores.append(valor)
print(max(valores))
print(valores.index(max(valores)) + 1)
