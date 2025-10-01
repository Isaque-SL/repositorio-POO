from models.cliente import Cliente
from models.clienteDAO import ClienteDAO
from models.servico import Servico
from models.servicoDAO import ServicoDAO
from models.horario import Horario
from models.horarioDAO import HorarioDAO

class View:
    def cliente_listar():
       return ClienteDAO.listar()
    
    def cliente_listar_id(id):
        return ClienteDAO.listar_id(id)
    
    def cliente_inserir(nome, email, fone):
       cliente = Cliente(0, nome, email, fone)
       ClienteDAO.inserir(cliente)

    def cliente_atualizar(id, nome, email, fone):
        cliente = Cliente(id, nome, email, fone)
        ClienteDAO.atualizar(cliente)
        
    def cliente_excluir(id):
        cliente = Cliente(id, "", "", "")
        ClienteDAO.excluir(cliente)

    def servico_listar():
       return ServicoDAO.listar()
    
    def servico_listar_id(id):
        return ServicoDAO.listar_id(id)
    
    def servico_inserir(desc, valor):
       servico = Servico(0, desc, valor)
       ServicoDAO.inserir(servico)

    def servico_atualizar(id, desc, valor):
        servico = Servico(id, desc, valor)
        ServicoDAO.atualizar(servico)
        
    def servico_excluir(id):
        servico = Servico(id, "", "")
        ServicoDAO.excluir(servico)

    def horario_inserir(data, confirmado, id_cliente, id_servico):
        c = Horario(0, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        HorarioDAO.inserir(c)

    def horario_listar():
        return HorarioDAO.listar()
    
    def horario_atualizar(id, data, confirmado, id_cliente, id_servico):
        c = Horario(id, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        HorarioDAO.atualizar(c)

    def horario_excluir(id):
        c = Horario(id, None)
        HorarioDAO.excluir(c)