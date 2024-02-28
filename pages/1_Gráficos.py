import streamlit as st
import collatz as c
import func as f


col = c.Collatz()
num_evaluar = st.session_state.get("num_evaluar",10)

#Configuración de la app
st.set_page_config(
    page_title=f"Gráficos de Collatz hasta el {num_evaluar}",   
    page_icon="📈",
    layout="wide")

desc = "Muestra una gráfica de dispersión donde cada punto representa el número de iteraciones necesarias para converger hasta 1 de cada número."
f.set_sidebar(desc)

st.title("""Gráfico Iteraciones para converger :red[vs] Número inicial""")

#col1,col2,col3,col4 = st.columns(4)
#with col1:
#    color = st.color_picker(
#        "Elige un color para el marcador",
#        value=st.session_state.get("color","#FF0000"),
#        key="color"
#    )

#with col2:
#    marker = st.selectbox(
#        "Elige un tipo de marcador",
#        ("x","o",".","v","1","2","s","p","*"),
#        index=1,
#    )

#with col3:
#    color_contorno = st.color_picker(
#    "Elige un color para el contorno del marcador",
#    value=st.session_state.get("color_contorno","#0A0202"),
#    key="color_contorno"
#)

#with col4:
#    lw = st.slider(
#        "Escoge un grosor de linea",
#        min_value=0.1,
#        max_value=5.0,
#        step=0.1)

with st.spinner("Dibujando..."):
    col.plotear_iteraciones(st.session_state["num_evaluar"])



