class Cliente:
    def __init__(self, id, nome, email, fone):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_telefone(fone)

    def set_id(self, id):
        self.__id = id
        
    def set_nome(self, nome):
        self.__nome = nome
    
    def set_email(self, email):
        self.__email = email

    def set_telefone(self, fone):
        self.__fone = fone

    def get_id(self):
        return self.__id
    
    def get_nome(self):
        return self.__nome
    
    def get_email(self):
        return self.__email
    
    def get_telefone(self):
        return self.__fone
    
    def to_json(self):
        dic = {"id":self.__id, "nome":self.__nome, "email":self.__email, "fone":self.__fone}
        return dic

    @staticmethod
    def from_json(dic):
        return Cliente(dic["id"], dic["nome"], dic["email"], dic["fone"])