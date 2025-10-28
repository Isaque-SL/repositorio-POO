from view import View
from datetime import datetime
from datetime import timedelta
import streamlit as st

class AbrirAgendaUI:
    def main():
        st.header("Abrir Agenda")
        data = st.text_input("Informe a data no formato dd/mm/aaaa")
        hora_inicio = st.text_input("Informe o horário inicial no formato HH:MM")
        hora_final = st.text_input("Informe o horário final no formato HH:MM")
        intervalo = st.text_input("Informe o intervalo entre os horários (min)")

        if st.button("Abrir Agenda"):
            horario_inicio_str = f"{data} {hora_inicio}"
            horario_final_str = f"{data} {hora_final}"
            horario_final = datetime.strptime(horario_final_str, "%d/%m/%Y %H:%M")
            horario = datetime.strptime(horario_inicio_str, "%d/%m/%Y %H:%M")
            View.horario_inserir(data=horario, id_profissional=st.session_state["usuario_id"])
            if horario > horario_final:
                horario_final += timedelta(days=1)
            while horario < horario_final:
                horario += timedelta(minutes=int(intervalo))
                View.horario_inserir(data=horario, id_profissional=st.session_state["usuario_id"])
            st.success("Agenda registrada com sucesso")