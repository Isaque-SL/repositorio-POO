from view import View
import streamlit as st
import pandas as pd

class VisualizarAgendaUI:
    def main():
        st.header("Minha Agenda")
        horarios = View.horario_listar()
        if len(horarios) == 0:
            st.write("Nenhum horário cadastrado")
        else:
            dic = []
            for obj in horarios:
                if obj.get_id_profissional() == st.session_state["usuario_id"]:
                    cliente = View.cliente_listar_id(obj.get_id_cliente())
                    servico = View.servico_listar_id(obj.get_id_servico())
                    profissional = View.profissional_listar_id(obj.get_id_profissional())
                    if cliente != None:
                        cliente = cliente.get_nome()
                    if servico != None:
                        servico = servico.get_descricao()
                    if profissional != None:
                        profissional = profissional.get_nome()
                    dic.append({"id" : obj.get_id(), "data" : obj.get_data(), "confirmado" : obj.get_confirmado(), "cliente" : cliente, "profissional" : profissional, "serviço" : servico})
            df = pd.DataFrame(dic)
            st.dataframe(df, hide_index = True)