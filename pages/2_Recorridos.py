import streamlit as st
import collatz as c
import func as f


col = c.Collatz()
num_evaluar = st.session_state.get("num_evaluar",10) 

#Configuración de la app
st.set_page_config(
    page_title=f"Recorridos de Collatz hasta el {num_evaluar}",   
    page_icon="🖇",
    layout="wide")


desc = "Muestra una gráfica de tipo árbol con todos los recorridos de todos los números evaluados en el rango elegido hasta converger a 1.\
      Los nodos son únicos."
f.set_sidebar(desc)

st.title("Recorridos hasta convergencia")
with st.spinner("Dibujando..."):
    col.graficar_secuencias(st.session_state["num_evaluar"])

