from agendamento.templates.cliente.manterclienteUI import ManterClienteUI
from templates.manterservicoUI import ManterServicoUI
from templates.manterhorarioUI import ManterHorarioUI
from agendamento.templates.profissional.manterprofissionalUI import ManterProfissionalUI
from templates.abrircontaUI import AbrirContaUI
from templates.loginUI import LoginUI
from agendamento.templates.cliente.perfilclienteUI import PerfilClienteUI
from agendamento.templates.profissional.perfilprofissionalUI import PerfilProfissionalUI
from agendamento.templates.cliente.agendarservicoUI import AgendarServicoUI
from view import View
import streamlit as st

class IndexUI:
    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        if op == "Entrar no Sistema":
            LoginUI.main()
        if op == "Abrir Conta":
            AbrirContaUI.main()

    def menu_profissional():
        op = st.sidebar.selectbox("Menu", ["Meus Dados"])
        if op == "Meus Dados":
            PerfilProfissionalUI.main()

    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "Agendar Serviço"])
        if op == "Meus Dados":
            PerfilClienteUI.main()
        if op == "Agendar Serviço":
            AgendarServicoUI.main()
    
    def menu_admin():            
        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", "Cadastro de Serviços", "Cadastro de Horários", "Cadastro de Profissionais"])
        if op == "Cadastro de Clientes":
            ManterClienteUI.main()
        if op == "Cadastro de Serviços":
            ManterServicoUI.main()
        if op == "Cadastro de Horários":
            ManterHorarioUI.main()
        if op == "Cadastro de Profissionais":
            ManterProfissionalUI.main()
    
    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["usuario_id"]
            del st.session_state["usuario_nome"]
            st.rerun()

    def sidebar():
        if "usuario_id" not in st.session_state:
            IndexUI.menu_visitante()
        else:
            cliente = False
            admin = st.session_state["usuario_nome"] == "admin"
            for obj in View.cliente_listar():
                if obj.get_nome() == st.session_state["usuario_nome"]:
                    cliente = True
            st.sidebar.write("Bem-vindo(a), " + st.session_state["usuario_nome"])
            if admin:
                IndexUI.menu_admin()
            elif cliente:
                IndexUI.menu_cliente()
            else:
                IndexUI.menu_profissional()
            IndexUI.sair_do_sistema()
    def main():
        # View.cliente_criar_admin()
        IndexUI.sidebar()

IndexUI.main()