import streamlit as st
from Retangulo import Retangulo as rt

class RetanguloUI:
    def main():
        st.header("Cálculos com Retângulo")
        st.write("Informe a base:")
        base = st.number_input()
        altura = st.number_input()
        if st.button("Calcular"):
            