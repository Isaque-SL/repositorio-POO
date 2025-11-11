from models.plano import Plano
from models.planoDAO import PlanoDAO
from models.servicoDAO import ServicoDAO
from models.planoDAO import planoDAO
from view import View
import pandas as pd
import streamlit as st
import time

class ManterPlanoUI:

    def main():
        st.header("Cadastro de Planos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
       
        with tab1: 
            ManterPlanoUI.listar()
        
        with tab2: 
            ManterPlanoUI.inserir()
        
        with tab3: 
            ManterPlanoUI.atualizar()
        
        with tab4: 
            ManterPlanoUI.excluir()
        
    def listar():
        planos = View.planos_listar()
        if len(planos) == 0:
            st.write("Nenhum plano cadastrado")
        else:
            list_dic = []
            for obj in planos:
                list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index=True)
    
    def inserir():
        servicos = View.servico_listar()
        tema = st.text_input("Informe o tema")
        valor = st.text_input("Informe o valor")
        servicos_lista = st.multiselect("Insira os serviços ofertados", servicos)
        if st.button("Inserir"):
            try:
                View.plano_inserir(tema, valor, servicos_lista)
                st.success("Plano criado com sucesso")
                time.sleep(2)
                st.rerun()            
            except ValueError as erro:
                st.error(erro)
    
    def atualizar():
        planos = View.planos_listar()
        servicos = View.servico_listar()
        if len(planos) == 0:
            st.write("Nenhum plano cadastrado")
        else:
            op = st.selectbox("Atualização de planos", planos)
            tema = st.text_input("Novo tema", op.get_tema())
            valor = st.text_input("Novo valor", op.get_preco())
            servicos_lista = st.multiselect("Novos serviços", servicos)
            if st.button("Atualizar"):
                try:
                    id = op.get_id()
                    View.plano_atualizar(id, tema, valor, servicos_lista)
                    st.success("Plano atualizado com sucesso")
                    time.sleep(2)
                    st.rerun()
                except ValueError as erro:
                    st.error(erro)
    
    def excluir():
        planos = View.plano_listar()
        if len(planos) == 0:
            st.write("Nenhum plano cadastrado")
        else:
            op = st.selectbox("Exclusão de Planos", planos)
            if st.button("Excluir"):
                try:
                    id = op.get_id()
                    View.plano_excluir(id)
                    st.success("Plano excluído com sucesso")
                    time.sleep(2)
                    st.rerun()
                except ValueError as erro:
                    st.error(erro)