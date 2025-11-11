import streamlit as st
from view import View
from models.planoDAO import PlanoDAO
import time

class AgendarServicoUI:
    def main():
        st.header("Agendar Serviço")
        cliente = View.cliente_listar_id(st.session_state["usuario_id"])
        if cliente.get_id_plano() != 0:
            plano = st.checkbox("Gostaria de agendar pelo seu plano?")
        
        if plano:
            plano_cliente = PlanoDAO.listar_id(cliente.get_id_plano())
            servicos = View.servico_listar()
            for obj in 
        
        profs = View.profissional_listar()
        if len(profs) == 0: 
            st.write("Nenhum profissional cadastrado")
        else:
            profissional = st.selectbox("Informe o profissional", profs)
            horarios = View.horario_agendar_horario(profissional.get_id())
            if len(horarios) == 0: 
                st.write("Nenhum horário disponível")
            else:
                horario = st.selectbox("Informe o horário", horarios)
                servicos = View.servico_listar()
                servico = st.selectbox("Informe o serviço", servicos, help="A moeda de transação é Real.")
                if st.button("Agendar"):
                    View.horario_atualizar(horario.get_id(), horario.get_data(), False, st.session_state["usuario_id"], profissional.get_id(), servico.get_id())
                    st.success("Horário agendado com sucesso")
                    time.sleep(2)
                    st.rerun()