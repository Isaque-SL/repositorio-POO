C, N = map(int, input().split())
quant = C // N
C = C - (N * quant)
print(C)