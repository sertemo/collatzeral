import streamlit as st

import graphviz
import matplotlib.pyplot as plt

class Collatz:
  def _generador(self,num, yield_str:bool=False):
    ''' Función auxiliar que genera
    números de la secuencia de Collatz partiendo
    de 'num'.
    Tiene la posibilidad de devolver en tipo `str` que es 
    necesario para generar el gráfico en graphviz '''
    yield str(num) if yield_str else num
    while num >1:
      if num % 2 == 0:
        num = int(num / 2)
        yield str(num) if yield_str else num
      else:
        num = int(3 * num + 1)
        yield str(num) if yield_str else num

  def _evaluar_rango(self,limite_max,yield_str=False):
    """ Función auxiliar para crear el generador de secuencias """
    self._seqs = (self._generador(i,yield_str) for i in range(2,limite_max+1))
  
  def printear_iteraciones_rango(self,limite_max,yield_str=False):
    self._evaluar_rango(limite_max,yield_str)
    for gen in self._seqs:
      print(list(gen))

  def plotear_iteraciones(self,limite_max,color,marker,color_contorno,lw,yield_str=False):
    self._evaluar_rango(limite_max,yield_str)

    x = range(2,limite_max+1)
    y = (len(list(gn)) for gn in self._seqs)

    fig, ax = plt.subplots()
    #plt.figure(figsize=(16,5),layout="constrained")
    plt.xlabel("Número de inicio")
    plt.ylabel("Número de iteraciones para converger a 1")
    plt.title("Evaluación conjetura de Collatz")

    ax.scatter(x,list(y),c=color,marker=marker,alpha=0.5,linewidths=lw,edgecolors=color_contorno)
    st.pyplot(fig)
  
  def graficar_secuencias(self,limite_max):
    ''' Función para graficar las secuencias cuando evaluamos Collatz en un rango. '''
    graph = graphviz.Digraph(format="png",strict=True)

    #Evaluamos el rango devolviendo strings
    self._evaluar_rango(limite_max,True)

    #Creamos los edges
    for seq in self._seqs:
      seq_list = list(seq)
      for idx,numero in enumerate(seq_list[:-1]):
        graph.edge(numero,seq_list[idx+1])
    
    st.graphviz_chart(graph)

 