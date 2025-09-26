import streamlit as st
import pandas as pd
import time
from view import View

class ManterServicoUI:

    def main():
        st.header("Cadastro de Serviços")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
       
        with tab1: 
            ManterServicoUI.listar()
        
        with tab2: 
            ManterServicoUI.inserir()
        
        with tab3: 
            ManterServicoUI.atualizar()
        
        with tab4: 
            ManterServicoUI.excluir()

    def listar():
        servicos = View.servico_listar()
        if len(servicos) == 0:
            st.write("Nenhum serviço registrado")
        else:
            list_dic = []
            for obj in servicos:
                list_dic.append(obj.to_json())
                df = pd.DataFrame(list_dic)
                st.dataframe(df)
    
    def inserir():
        desc = st.text_input("Descreva o serviço prestado")
        valor = st.text_input("Informe o valor")
        if st.button("registrar"):
            View.servico_inserir(desc, valor)
            st.success("Serviço registrado com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        servicos = View.servico_listar()
        if len(servicos) == 0:
            st.write("Nenhum serviço registrado")
        else:
            op = st.selectbox("Atualização de serviços", servicos)
            desc = st.text_input("Nova descrição", op.get_descricao())
            valor = st.text_input("Novo valor", op.get_valor())
            if st.button("Atualizar"):
                id = op.get_id()
                View.servico_atualizar(id, desc, valor)
                st.success("Serviço atualizado com sucesso")

    def excluir():
        servicos = View.servico_listar()
        if len(servicos) == 0:
            st.write("Nenhum serviço registrado")
        else:
            op = st.selectbox("Remoção de Serviços", servicos)
            if st.button("Excluir"):
                id = op.get_id()
                View.servico_excluir(id)
                st.success("Serviço removido com sucesso")