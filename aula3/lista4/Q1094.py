N = int(input())
total_experimentos = 0
total_coelhos = 0
total_ratos = 0
total_sapos = 0

for i in range(N):
    cobaia = list(input().split())
    cobaia[0] = int(cobaia[0])
    total_experimentos += cobaia[0]
    if cobaia[1] == "C":
        total_coelhos += cobaia[0]
    elif cobaia[1] == "R":
        total_ratos += cobaia[0]
    else:
        total_sapos += cobaia[0]
    cobaia = []

print(f"Total: {total_experimentos} cobaias\nTotal de coelhos: {total_coelhos}\nTotal de ratos: {total_ratos}\nTotal de sapos: {total_sapos}\n")
print(f"Percentual de coelhos: {((total_coelhos / total_experimentos) * 100):.2f} %\nPercentual de ratos: {((total_ratos / total_experimentos) * 100):.2f} %\nPercentual de sapos: {((total_sapos / total_experimentos) * 100):.2f} %")
