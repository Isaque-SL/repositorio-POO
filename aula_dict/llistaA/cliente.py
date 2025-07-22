class Cliente:
    def __init__(self, id, nome, email, fone):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_telefone(fone)
        self.__id = 0
        self.__nome = ""
        self.__email = ""
        self.__tele = 0
    
    def set_id(self, id):
        if type(id) != int:
            raise ValueError("Formato não permitido.\n")
        self.__id = id
    def get_id(self):
        return self.__id
    
    def set_nome(self, nome):
        self.__nome = nome
    def get_nome(self):
        return self.__nome
    
    def set_telefone(self, tele):
        pass