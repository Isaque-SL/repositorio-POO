from view import View
from datetime import datetime
import streamlit as st

data = st.text_input("Informe a data no formato dd/mm/aaaa")
hora_inicio = st.text_input("Informe o horário inicial no formato HH:MM")
hora_final = st.text_input("Informe o horário final no formato HH:MM")
intervalo = st.text_input("Informe o intervalo entre os horários (min)")
datetime.now().strftime("%d/%m/%Y %H:%M")

if st.button("Abrir Agenda"):
    
    View.horario_inserir(datetime.strptime(data, "%d/%m/%Y %H:%M"))
    st.success("Horário inserido com sucesso")
