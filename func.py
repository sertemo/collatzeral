import streamlit as st

def set_sidebar(desc):
    """ Función para setear la sidebar en todas las páginas """
    with st.sidebar:
        st.markdown(
        f"""
        ## Info
        {desc}
        """)
        st.divider()

        choice = st.number_input(
            "Escoge un límite máximo sobre el que evaluar la conjetura de Collatz (2-100.000)",
            min_value=2,
            max_value=100_000,
            key="num_evaluar",
            value=st.session_state.get("num_evaluar",10)
        )
