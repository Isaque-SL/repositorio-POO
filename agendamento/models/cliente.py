class Cliente:
    def __init__(self, id, nome, email, fone, senha, id_plano = 0):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_telefone(fone)
        self.set_senha(senha)
        self.set_id_plano(id_plano)

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"
    
    def set_id(self, id):
        self.__id = id
        
    def set_nome(self, nome):
        if nome == "":
            raise ValueError("Nome é obrigatório.")
        self.__nome = nome
    
    def set_email(self, email):
        if email == "":
            raise ValueError("E-mail é obrigatório.")
        self.__email = email

    def set_telefone(self, fone):
        self.__fone = fone

    def set_senha(self, senha):
        if senha == "":
            raise ValueError("Senha é obrigatória.")
        self.__senha = senha

    def set_id_plano(self, id_plano):
        self.__id_plano = id_plano

    def get_id(self):
        return self.__id
    
    def get_nome(self):
        return self.__nome
    
    def get_email(self):
        return self.__email
    
    def get_telefone(self):
        return self.__fone
    
    def get_senha(self):
        return self.__senha
    
    def get_id_plano(self):
        return self.__id_plano
    
    def to_json(self):
        dic = {"id":self.__id, "nome":self.__nome, "email":self.__email, "fone":self.__fone, "senha":self.__senha, "id_plano":self.__id_plano}
        return dic

    @staticmethod
    def from_json(dic):
        return Cliente(dic["id"], dic["nome"], dic["email"], dic["fone"], dic["senha"], dic["id_plano"])