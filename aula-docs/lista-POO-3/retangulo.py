import math

class retangulo:
    def __init__(self):
        self.__base = 0.0
        self.__altura = 0.0
    
    def set_base(self, base):
        if base < 1:
            raise ValueError()
        self.__base = base
    
    def get_base(self):
        return self.__base
    
    def set_altura(self, altura):
        if altura < 1:
            raise ValueError()
        self.__altura = altura
    
    def get_altura(self):
        return self.__altura
    
    def calc_area(self):
        return self.__base * self.__altura
    
    def calc_diagonal(self):
        return math.sqrt((self.__base ** 2) + (self.__altura ** 2))
    
    def __str__(self):
        return f"Base = {self.__base}\nAltura = {self.__altura}"
    
# class UI:
#     @staticmethod
#     def main():

    

