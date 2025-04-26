N = int(input())
valores = []
for i in range(N):
    X, Y = map(int, input().split())
    if Y == 0:
        valores.append("divisao impossivel")
    else:
        valores.append(X / Y)
for j in range(N):
    if type(valores[j]) == int:
        print(f"{valores[j]:.1f}")
    else:
        print(valores[j])
