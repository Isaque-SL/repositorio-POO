import json
from models.plano import Plano

class PlanoDAO:
    __objetos = []

    @classmethod
    def inserir(cls, plano):
        cls.abrir()
        id = 0
        for aux in cls.__objetos:
            if aux.get_id() > id:
                id = aux.get_id()
        plano.set_id(id + 1)
        cls.__objetos.append(plano)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.__objetos

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.__objetos:
            if obj.get_id() == id:
                return obj
        return None

    @classmethod
    def atualizar(cls, plano_novo):
        aux = cls.listar_id(plano_novo.get_id())
        if aux != None:
            cls.__objetos.remove(aux)
            cls.__objetos.append(plano_novo)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            cls.__objetos.remove(aux)
            cls.salvar()

    @classmethod
    def abrir(cls):
        cls.__objetos = []
        try:
            with open("plano.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Plano.from_json(dic)
                    cls.__objetos.append(obj)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("planos.json", mode="w") as arquivo:
            json.dump(cls.__objetos, arquivo, default = Plano.to_json)