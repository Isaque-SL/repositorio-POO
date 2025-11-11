from view import View
from datetime import datetime, timedelta
import streamlit as st
import time

class AbrirAgendaUI:
    def main():
            st.header("Abrir Agenda")
                    data = st.date_input("Informe a data no formato dd/mm/aaaa", format="DD/MM/YYYY")
                            hora_inicio = st.time_input("Informe o horário inicial no formato HH:MM")
                                    hora_final = st.time_input("Informe o horário final no formato HH:MM")
                                            intervalo = st.number_input("Informe o intervalo entre os horários (min)", min_value=10, max_value = 120)
                                             
                                                     if st.button("Abrir Agenda"):
                                                                 try:
                                                                                 horario_inicio = datetime(year=data.year, month=data.month, day=data.day, hour=hora_inicio.hour, minute=hora_inicio.minute)
                                                                                                 if horario_inicio < datetime.now():
                                                                                                                     raise ValueError("Data não pode ser no passado.")
                                                                                                                                     horario_final = datetime(year=data.year, month=data.month, day=data.day, hour=hora_final.hour, minute=hora_final.minute)
                                                                                                                                                     horario = horario_inicio
                                                                                                                                                                     View.horario_inserir(data=horario, id_profissional=st.session_state["usuario_id"])
                                                                                                                                                                                     if horario_inicio > horario_final:
                                                                                                                                                                                                         horario_final += timedelta(days=1)
                                                                                                                                                                                                                         while horario < horario_final:
                                                                                                                                                                                                                                             horario += timedelta(minutes=intervalo)
                                                                                                                                                                                                                                                                 View.horario_inserir(data=horario, id_profissional=st.session_state["usuario_id"])
                                                                                                                                                                                                                                                                                 st.success("Agenda registrada com sucesso")
                                                                                                                                                                                                                                                                                                 time.sleep(2)
                                                                                                                                                                                                                                                                                                                 st.rerun()
                                                                                                                                                                                                                                                                                                                             except ValueError as erro:
                                                                                                                                                                                                                                                                                                                                             st.error(erro)