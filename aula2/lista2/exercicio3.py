import math

a = int(input("Digite a base e a altura do retângulo\n"))
b = int(input())

hipotenusa = math.sqrt(((a ** 2) + (b ** 2)))
area = a * b
perimetro = (a * 2) + (b * 2)

print(f"\nÁrea = {area:.2f} - Perímetro = {perimetro:.2f} - Diagonal = {hipotenusa:.2f}")