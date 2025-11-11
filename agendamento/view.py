from models.cliente import Cliente
from models.clienteDAO import ClienteDAO
from models.servico import Servico
from models.servicoDAO import ServicoDAO
from models.horario import Horario
from models.horarioDAO import HorarioDAO
from models.profissional import Profissional
from models.profissionalDAO import ProfissionalDAO
from models.plano import Plano
from models.planoDAO import PlanoDAO
from datetime import datetime

class View:
    def cliente_listar():
       r = ClienteDAO.listar()
       r.sort(key = lambda obj : obj.get_nome())
       return r
    
    def cliente_listar_id(id):
        return ClienteDAO.listar_id(id)
    
    def cliente_inserir(nome, email, fone, senha, id_plano = 0):
        if "admin" == email:
            raise ValueError("E-mail inacessível.")
        for obj in View.cliente_listar():
            if obj.get_email() == email:
                raise ValueError("Este e-mail já foi cadastrado.")
        for obj in View.profissional_listar():
            if obj.get_email() == email:
                raise ValueError("Este e-mail já foi cadastrado.")
        cliente = Cliente(0, nome, email, fone, senha, id_plano)
        ClienteDAO.inserir(cliente)

    def cliente_atualizar(id, nome, email, fone, senha, id_plano = 0):
        if "admin" == email:
            raise ValueError("E-mail inacessível.")
        for obj in View.cliente_listar():
            if obj.get_email() == email and obj.get_id() != id:
                raise ValueError("Este e-mail já foi cadastrado.")
        for obj in View.profissional_listar():
            if obj.get_email() == email and obj.get_id() != id:
                raise ValueError("Este e-mail já foi cadastrado.")

        cliente = Cliente(id, nome, email, fone, senha, id_plano)
        ClienteDAO.atualizar(cliente)
        
    def cliente_excluir(id):
        for obj in View.horario_listar():
            if obj.get_id_cliente() == id:
                raise ValueError("Cliente tem horário marcado : Não é possível excluir.")
        cliente = Cliente(id, "Nulo", "Nulo", "", "0")
        ClienteDAO.excluir(cliente)

    def cliente_criar_admin():
        for c in View.cliente_listar():
            if c.get_email() == "admin":
                return View.cliente_inserir("admin", "admin", "admin", "1234")
    
    def cliente_autenticar(email, senha):
        for c in View.cliente_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id": c.get_id(), "nome": c.get_nome()}
        return None

    def servico_listar():
        r = ServicoDAO.listar()
        r.sort(key = lambda obj : obj.get_descricao())
        return r
    
    def servico_listar_id(id):
        return ServicoDAO.listar_id(id)
    
    def servico_inserir(desc, valor):
        for obj in View.servico_listar():
            if obj.get_descricao() == desc:
                raise ValueError("Serviço já cadastrado")
        servico = Servico(0, desc, valor)
        ServicoDAO.inserir(servico)

    def servico_atualizar(id, desc, valor):
        for obj in View.servico_listar():
            if obj.get_id() != id and obj.get_descricao() == desc:
                raise ValueError("Descrição já cadastrada em outro serviço")
        servico = Servico(id, desc, valor)
        ServicoDAO.atualizar(servico)
        
    def servico_excluir(id):
        for obj in View.horario_listar():
            if obj.get_id_servico() == id:
                raise ValueError("Serviço já agendado: não é possível excluir.")
        servico = Servico(id, "None", "0")
        ServicoDAO.excluir(servico)

    def horario_inserir(data, confirmado = False, id_cliente = None, id_profissional = None, id_servico = None):
        for obj in View.horario_listar():
            if (obj.get_data() == data) and (obj.get_id_profissional() == id_profissional):
                raise ValueError("Horário já cadastrado.")
        c = Horario(0, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_profissional(id_profissional)
        c.set_id_servico(id_servico)
        HorarioDAO.inserir(c)

    def horario_listar():
        r = HorarioDAO.listar()
        r.sort(key = lambda obj : obj.get_data())
        return r
    
    def horario_listar_id(id):
        return HorarioDAO.listar_id(id)

    def horario_atualizar(id, data, confirmado, id_cliente, id_profissional, id_servico):
        for obj in View.horario_listar():
            if (obj.get_id() != id) and (obj.get_id_profissional() == id_profissional) and obj.get_data() == data:
                raise ValueError("Horário já cadastrado.")
        c = Horario(id, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_profissional(id_profissional)
        c.set_id_servico(id_servico)
        HorarioDAO.atualizar(c)

    def horario_excluir(id):
        obj = View.horario_listar_id(id)
        if obj.get_id_cliente() != None:
            raise ValueError("Horário agendado : Não pode excluir.")
        c = Horario(id, None)
        HorarioDAO.excluir(c)

    def horario_agendar_horario(id_profissional):
        r = []
        agora = datetime.now()
        for h in View.horario_listar():
            if h.get_data() >= agora and h.get_confirmado() == False and h.get_id_cliente() == None and h.get_id_profissional() == id_profissional:
                r.append(h)
        r.sort(key = lambda h : h.get_data())
        return r

    def profissional_listar():
       r = ProfissionalDAO.listar()
       r.sort(key = lambda obj : obj.get_nome())
       return r
    
    def profissional_listar_id(id):
        return ProfissionalDAO.listar_id(id)
    
    def profissional_inserir(nome, especialidade, conselho, email, senha):
        if "admin" == email:
            raise ValueError("E-mail inacessível.")
        for obj in View.profissional_listar():
            if obj.get_email() == email:
                raise ValueError("Este e-mail já foi cadastrado.")
        for obj in View.cliente_listar():
            if obj.get_email() == email:
                raise ValueError("Este e-mail já foi cadastrado.")
        profissional = Profissional(0, nome, especialidade, conselho, email, senha)
        ProfissionalDAO.inserir(profissional)

    def profissional_atualizar(id, nome, especialidade, conselho, email, senha):
        if "admin" == email:
            raise ValueError("E-mail inacessível.")
        for obj in View.profissional_listar():
            if obj.get_email() == email and obj.get_id() != id:
                raise ValueError("Este e-mail já foi cadastrado.")
        for obj in View.cliente_listar():
            if obj.get_email() == email and obj.get_id() != id:
                raise ValueError("Este e-mail já foi cadastrado.")
        profissional = Profissional(id, nome, especialidade, conselho, email, senha)
        ProfissionalDAO.atualizar(profissional)
        
    def profissional_excluir(id):
        for obj in View.horario_listar():
            if obj.get_id_profissional() == id:
                raise ValueError("Profissional tem horário marcado : Não é possível excluir.")
        profissional = Profissional(id, "Nulo", "", "", "Nulo", "0")
        ProfissionalDAO.excluir(profissional)
    
    def profissional_autenticar(email, senha):
        for p in View.profissional_listar():
            if p.get_email() == email and p.get_senha() == senha:
                return {"id": p.get_id(), "nome": p.get_nome()}
        return None

    def profissional_criar_admin():
        for p in View.profissional_listar():
            if p.get_email() == "admin":
                return View.profissional_inserir("admin", "admin", "admin", "email", "1234")

    def planos_listar():
       r = PlanoDAO.listar()
       r.sort(key = lambda obj : obj.get_tema())
       return r
    
    def plano_listar_id(id):
        return PlanoDAO.listar_id(id)
    
    def plano_inserir(tema, preco, servicos):
        for obj in View.plano_listar():
            if obj.tema() == tema:
                raise ValueError("Tema não pode ser igual")
        plano = Plano(0, tema, preco, servicos)
        PlanoDAO.inserir(plano)
    
    def plano_atualizar(id, tema, preco, servicos):
        for obj in View.planos_listar():
            if obj.get_tema() == tema:
                raise ValueError("Tema não pode ser igual")
        plano = Plano(id, tema, preco, servicos)
        PlanoDAO.inserir(plano)
    
    def plano_excluir(id):
        for obj in View.cliente_listar():
            if obj.get_id_plano() == id:
                raise ValueError("Esse plano já possui clientes")
        plano = Plano(id, "Nulo", "Nulo", "Nulo")
        PlanoDAO.excluir(plano)