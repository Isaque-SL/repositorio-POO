class conta:
    def __init__(self):
        self.__titular = ""
        self.__numero = ""
        self.__saldo = 0.0
    
    def set_titular(self, t):
        if t == "":
            raise ValueError()
        self.__titular = t
    def get_titular(self):
        return self.__titular
    
    def set_numero(self, n):
        if type(n) != int:
            raise ValueError()
        self.__numero = n
    def get_numero(self):
        return self.__numero
    
    def depositar(self, v):
        if v < 1:
            raise ValueError()
        self.__saldo += v
    def sacar(self, v):
        if v > self.__saldo or v < 1:
            raise ValueError()
    def get_saldo(self):
        return self.__saldo

class UI:
    @staticmethod
    def main():
        x = conta()
        titular = x.set_titular(input("Titular da conta: "))
        numero = x.set_numero(input("Número da conta: "))
        
        oper = bool(input("Qual operação? (Depósito = 0; Saque = 1)\n"))

        if oper == True:
            x.depositar(int(input()))
        else:
            x.scar(int(input()))