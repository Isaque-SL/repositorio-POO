class Servico:
    def __init__(self, id, descricao, valor):
        self.set_id(id)
        self.set_descricao(descricao)
        self.set_valor(valor)

    def __str__(self):
        return f'{self.__id} - {self.__desc} - {self.__valor}'

    def set_id(self, id):
        self.__id = id

    def set_descricao(self, desc):
        if desc == "":
            raise ValueError("Descrição inválida.")
        self.__desc = desc

    def set_valor(self, valor):
        if float(valor) <= 0:
            raise ValueError("Valor inválido.")
        self.__valor = valor

    def get_id(self):
        return self.__id
    
    def get_descricao(self):
        return self.__desc

    def get_valor(self):
        return self.__valor

    def to_json(self):
        dic = {"id":self.__id, "desc":self.__desc, "valor":self.__valor}
        return dic
    
    @staticmethod
    def from_json(dic):
        return Servico(dic["id"], dic["desc"], dic["valor"])