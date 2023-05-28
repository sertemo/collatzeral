import streamlit as st
import collatz as c
import func as f

col = c.Collatz()
num_evaluar = st.session_state.get("num_evaluar",10)

#Configuración de la app
st.set_page_config(
    page_title=f"Nodos aislados de Collatz hasta el {num_evaluar}",   
    page_icon="🌀",
    layout="wide")

#st.session_state

desc = "Muestra un gráfico de tipo histograma con el número de iteraciones de cada nodo aislado en el rango de números evaluado.\
    Un nodo aislado es aquel que no tiene antecesor en el árbol de recorridos."
f.set_sidebar(desc)


st.title("Nodos aislados vs número de iteraciones")
with st.spinner("Calculando..."):
    nodos_aislados = col.mostrar_nodos_aislados(num_evaluar)
    st.bar_chart(data=nodos_aislados,x="Nodos aislados",y="iteraciones")

