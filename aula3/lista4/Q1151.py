N = int(input())
anteriores = [0]
fibo = 0
sequencia = []
for i in range(N):
    sequencia.append(str(fibo))
    if i == 0:
        fibo += 1
    else:
        anteriores.append(fibo)
        fibo = sum(anteriores)
        anteriores.pop(0)
print(" ".join(sequencia))
