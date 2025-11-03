import streamlit as st
from view import View

class AlterarSenhaUI:
    def main():
        st.header("Meus Dados")
        op = View.cliente_listar_id(st.session_state["usuario_id"])
        nome = st.text_input("Informe o novo nome", op.get_nome())
        email = st.text_input("e-mail", op.get_email(), disabled=True, help="Não é possível alterar o e-mail de acesso.")
        fone = st.text_input("Informe o novo telefone", op.get_telefone())
        senha = st.text_input("Informe a nova senha", op.get_senha(),type="password")
        if st.button("Atualizar"):
            id = op.get_id()
            email = op.get_email()
            View.cliente_atualizar(id, nome, email, fone, senha)
            st.success("Administrador atualizado com sucesso")