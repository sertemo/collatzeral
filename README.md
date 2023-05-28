## COLLATZERAL
Pequeña aplicación para evaluar un rango de número con la conjetura de Collatz y mostrar algunas gráficas.<br>
Ver la app [aquí](https://collatzeral.streamlit.app/)

## 1 - Gráficos
Muestra una gráfica de dispersión donde cada punto representa el número de iteraciones necesarias para converger de un número.

## 2 - Recorridos
Muestra una gráfica de tipo árbol con todos los recorridos de todos los números evaluados en el rango elegido hasta converger a 1.
Los nodos son únicos.

## 3 - Nodos aislados
Muestra un gráfico de tipo histograma con el número de iteraciones de cada nodo aislado en el rango de números evaluado.
Un nodo aislado es aquel que no tiene antecesor en el árbol de recorridos.

## Próximas etapas
- Añadir la parte de 'Nodos Aislados' (Hecho: 28/05/2023)
- Mejorar el rendimiento de graphviz (si se puede)
- Página nueva para ver una secuencia aislada ?
