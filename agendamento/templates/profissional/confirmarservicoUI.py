import streamlit as st
from view import View

class ConfirmarServicoUI:
        def main():
            st.header("Confirmar Serviço")
            horarios = View.horario_listar()
            horarios_cliente = []
            for obj in horarios:
                if (obj.get_id_cliente() == st.session_state["usuario_id"]) and (obj.get_confirmado() == False):
                    horarios_cliente.append(obj)
            if len(horarios_cliente) == 0:
                st.write("Nenhum serviço cadastrado")
            else:
                horario = st.selectbox("Informe o horário", horarios_cliente)
                cliente = st.selectbox("Cliente", View.cliente_listar_id(horario.get_id_cliente()), disabled = True)
                if st.button("Confirmar"):
                    View.horario_atualizar(horario.get_id(), horario.get_data(), True, horario.get_id_cliente(), horario.get_id_profissional(), horario.get_id_servico())
                    st.success("Serviço confirmado!")