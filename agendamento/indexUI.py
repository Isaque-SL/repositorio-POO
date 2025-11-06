from templates.admin.manterclienteUI import ManterClienteUI
from templates.admin.manterservicoUI import ManterServicoUI
from templates.admin.manterhorarioUI import ManterHorarioUI
from templates.admin.manterprofissionalUI import ManterProfissionalUI
from templates.admin.perfiladminUI import AlterarSenhaUI
from templates.abrircontaUI import AbrirContaUI
from templates.profissional.abriragendaUI import AbrirAgendaUI
from templates.profissional.visualizaragendaUI import VisualizarAgendaUI
from templates.profissional.confirmarservicoUI import ConfirmarServicoUI
from templates.loginUI import LoginUI
from templates.cliente.perfilclienteUI import PerfilClienteUI
from templates.profissional.perfilprofissionalUI import PerfilProfissionalUI
from templates.cliente.agendarservicoUI import AgendarServicoUI
from templates.cliente.meusservicosUI import MeusServicosUI
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
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "Abrir Agenda", "Minha Agenda", "Confirmar Serviço"])
        if op == "Meus Dados":
            PerfilProfissionalUI.main()
        if op == "Abrir Agenda":
            AbrirAgendaUI.main()
        if op == "Minha Agenda":
            VisualizarAgendaUI.main()
        if op == "Confirmar Serviço":
            ConfirmarServicoUI.main()

    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "Agendar Serviço", "Meus Serviços"])
        if op == "Meus Dados":
            PerfilClienteUI.main()
        if op == "Agendar Serviço":
            AgendarServicoUI.main()
        if op == "Meus Serviços":
            MeusServicosUI.main()
    
    def menu_admin():            
        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", "Cadastro de Serviços", "Cadastro de Horários", "Cadastro de Profissionais", "Meus Dados"])
        if op == "Cadastro de Clientes":
            ManterClienteUI.main()
        if op == "Cadastro de Serviços":
            ManterServicoUI.main()
        if op == "Cadastro de Horários":
            ManterHorarioUI.main()
        if op == "Cadastro de Profissionais":
            ManterProfissionalUI.main()
        if op == "Meus Dados":
            AlterarSenhaUI.main()
    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["usuario_id"]
            del st.session_state["usuario_nome"]
            del st.session_state["usuario_email"]
            st.rerun()

    def sidebar():
        if "usuario_id" not in st.session_state:
            IndexUI.menu_visitante()
        else:
            cliente = False
            admin = st.session_state["usuario_email"] == "admin"
            for obj in View.cliente_listar():
                if obj.get_email() == st.session_state["usuario_email"]:
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
        IndexUI.sidebar()

IndexUI.main()