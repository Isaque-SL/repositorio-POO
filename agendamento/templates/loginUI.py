import streamlit as st
from view import View

class LoginUI:
    def main():
        st.header("Entrar no Sistema")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")
        profissional = st.checkbox("Profissional")
        if profissional:
            st.text("Você está acessando sua conta na qualidade de Profissional.\nCaso queira acessar como cliente, desmarque esta opção.")
        if st.button("Entrar"):
            if profissional:
                p = View.profissional_autenticar(email, senha)
                if p == None:
                    st.write("E-mail ou senha inválidos")
                else:
                    st.session_state["usuario_id"] = p["id"]
                    st.session_state["usuario_nome"] = p["nome"]
                    st.rerun()
            else:
                c = View.cliente_autenticar(email, senha)
                if c == None:
                    st.write("E-mail ou senha inválidos")
                else:
                    st.session_state["usuario_id"] = c["id"]
                    st.session_state["usuario_nome"] = c["nome"]
                    st.rerun()