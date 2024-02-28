import streamlit as st

#Configuración de la app
st.set_page_config(
    page_title="Evaluaciones de la Conjetura de Collatz -STM-",   
    page_icon="🔄",)

#st.session_state

st.title("Conjetura de Collatz")
st.divider()
st.header("Enunciado")
st.write(""" 
Sea la siguiente operación, aplicable a cualquier número entero positivo:
- Si el número es par, se divide entre 2.
- Si el número es impar, se multiplica por 3 y se suma 1.

Formalmente, esto equivale a una función:  """)
st.latex(r""" f:\N \rarr \N""")
st.latex(r"""f(n) = \begin{cases}
    {n \over 2} &\text{si}~n~\text{par} \\
    3n+1 &\text{si}~n~\text{impar}
\end{cases} """)
st.markdown(""" 
Ahora se forma una sucesión mediante la aplicación de esta operación repetidamente, comenzando por cualquier
entero positivo, y tomando el resultado de cada paso como la entrada del siguiente.
La conjetura dice que siempre alcanzaremos el 1 independientemente del número con el que comencemos. 
Ver en la [wiki](https://es.wikipedia.org/wiki/Conjetura_de_Collatz) explicación completa. """)
