class Plano:
    def __init__(self, id, tema, preco, servicos):
        self.set_id(id)
        self.set_tema(tema)
        self.set_preco(preco)
        self.set_servicos(servicos)

    def __str__(self):
        return f"{self.__id} - {self.__tema} - {self.__preco}"

    def set_id(self, id):
        self.__id = id

    def set_tema(self, tema):
        if tema == "":
            raise ValueError("Tema do plano é obrigatório.")
        self.__tema = tema

    def set_preco(self, preco):
        if float(preco) <= 0:
            raise ValueError("Preço inválido.")
        self.__preco = float(preco)

    def set_servicos(self, servicos):
        self.__servicos = servicos

    def get_id(self):
        return self.__id

    def get_tema(self):
        return self.__tema

    def get_preco(self):
        return self.__preco

    def get_servicos(self):
        return self.__servicos

    def to_json(self):
        dic = {
            "id": self.__id,
            "tema": self.__tema,
            "preco": self.__preco,
            "servicos": self.__servicos,
        }
        return dic

    @staticmethod
    def from_json(dic):
        return Plano(dic["id"], dic["tema"], dic["preco"], dic["servicos"])
