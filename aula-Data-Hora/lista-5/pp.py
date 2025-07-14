from datetime import datetime
from datetime import timedelta

class Paciente:
    def __init__(self, nome, cpf, tele, nasc):
        self.set_nome(nome)
        self.set_cpf(cpf)
        self.set_telefone(tele)
        self.set_nascimento(nasc)
        self.__nome = self.get_nome()
        self.__cpf = self.get_cpf()
        self.__tele = self.get_telefone()
        self.__nasc = self.get_nascimento()

    def set_nome(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    def set_cpf(self, cpf):
        if type(cpf) == str:
            raise ValueError("Formato não suportado.")
        self.__cpf = cpf

    def get_cpf(self):
        return self.__cpf

    def set_telefone(self, tele):
        if type(tele) == str:
            raise ValueError("Formato não suportado.")
        self.__tele = tele

    def get_telefone(self):
        return self.__tele

    def set_nascimento(self, nasc):
        if type(nasc) != datetime:
            raise ValueError("Formato não suportado.")
        self.__nasc = nasc

    def get_nascimento(self):
        return self.__nasc
    
    def idade(self):
        hoje = timedelta(days = 1, hours = 12)
        idade = self.get_nascimento
        pass
    
    def ToString(self):
        return f"idade = {timedelta(days = self.get_nascimento}"

class UI:
    @staticmethod
    def main():
        nome = "sssss"
        cpf = 34
        tele = 333
        nasc = datetime(2000, 1, 1)

        a = Paciente(nome, cpf, tele, nasc)
        print(a.ToString())

UI.main()