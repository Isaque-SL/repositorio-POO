# QUESTÃO 2 

# numeros = list(map(int, input().split()))
# pares = []
# for i in range(len(numeros)):
#     if numeros[i] % 2 == 0:
#         pares.append(numeros[i])

# print(f" Soma dos pares: {sum(pares)}")

# QUESTÃO 3

# frase = input()

# for i in range(len(frase)):
#     if i % 2 == 0:
#         print(frase[i], end="")
# print()

# QUESTÃO 4

class agua:
    def __init__(self):
        self.ano = 2025
        self.mes = "Jan"
        self.consumo = 10
    def valor_agua(self):
        if self.consumo <= 10:
            return 38
        elif self.consumo <= 20:
            extra = (self.consumo - 10) * 5
            return 38 + extra
        else:
            extra = (self.consumo - 20) * 6
            return 38 + 50 + extra

registro = agua()

registro.usuario = input("Digite seu nome, o ano mais recente de registro, o mês e seu consumo:\n")
registro.ano = int(input())
registro.mes = input()
registro.consumo = int(input())

conta_valor = registro.valor_agua()

print(f"O valor da sua conta é: R${conta_valor}")

ver_litros = input("Gostaria de ver quantos litros de água você utilizou esse mês?\nS/N\n")

if ver_litros == "S":
    print(f"{registro.consumo * 1000} litros!")
else:
    print("Tenha um bom dia!")