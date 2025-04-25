A, B, C = map(float, input().split())
delta = (B * B) - 4 * A * C
if A == 0 or B == 0 or C == 0 or delta < 0:
    print("Impossivel calcular")
else:   
    X1 = (-B + math.sqrt(delta)) / (2 * A)
    X2 = (-B - math.sqrt(delta)) / (2 * A)
    print(f"R1 = {X1:.5f}")
    print(f"R2 = {X2:.5f}")
