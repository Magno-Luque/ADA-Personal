import streamlit as st
from PIL import Image
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

df= pd.read_csv("CursosInformatica.csv")

st.set_page_config(
    page_title="register",
    page_icon="school",
    initial_sidebar_state="expanded",
)

page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"] > .main {
        background-image: url("https://img.freepik.com/foto-gratis/fondo-acuarela-pintada-mano-forma-cielo-nubes_24972-1095.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    </style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
st.dataframe(df, width=1500)


G = nx.DiGraph()
G.add_nodes_from([1, 2, 3, 4])  
G.add_nodes_from(['A', 'B', 'C'])  
G.add_nodes_from(['D', 'E'])  
G.add_edges_from([(1, 'A'), (2, 'A'), (3, 'B'), (4, 'C')]) 
G.add_edges_from([('A', 'D'), ('C', 'E')]) 

# Dibujar el grafo
pos = {1: (1, 2), 2: (2, 2), 3: (3, 2), 4: (4, 2), 'A': (1.5, 1), 'B': (2.5, 1),
       'C': (3.5, 1), 'D':(2, 3), 'E':(3, 3)}  
nx.draw(G, pos, with_labels=True, arrows=True, node_color='skyblue', node_size=2000, edge_color='black', linewidths=1, font_size=15)

# Etiquetas de los niveles
level_labels = {"Nivel 2": ['A', 'B', 'C'], "Nivel 1": [1, 2, 3, 4], "Nivel 3":['D','E']}
level_positions = {}
for level, nodes in level_labels.items():
    y_pos = sum([pos[node][1] for node in nodes]) / len(nodes)  # Calcula la posición Y promedio de los nodos en el nivel
    level_positions[level] = (0.5, y_pos)

for level, position in level_positions.items():
    plt.text(position[0], position[1], level, rotation=90, fontsize=12, verticalalignment='center', horizontalalignment='center')

# Interacción: Mostrar información del nodo al hacer clic
clicked_node = st.sidebar.selectbox("Selecciona un nodo", [str(node) for node in G.nodes()])
if clicked_node:
    st.sidebar.markdown(f"**Información del Nodo {clicked_node}:**")
    # Muestra la información adicional solo si se hace clic en un nodo
    if clicked_node in level_labels['Nivel 1']:
        st.sidebar.write("Información específica del Nodo:")
        # Aquí puedes agregar información específica sobre el nodo de Nivel 1
    elif clicked_node in level_labels['Nivel 2']:
        st.sidebar.write("Información específica del Nodo:")
        # Aquí puedes agregar información específica sobre el nodo de Nivel 2
st.pyplot(plt)

level_labels = {"Nivel 2": ['A', 'B', 'C'], "Nivel 1": [1, 2, 3, 4], "Nivel 3":['D','E']}
level_positions = {}
for level, nodes in level_labels.items():
    y_pos = sum([pos[node][1] for node in nodes]) / len(nodes)  # Calcula la posición Y promedio de los nodos en el nivel
    level_positions[level] = (0.5, y_pos)

for level, position in level_positions.items():
    plt.text(position[0], position[1], level, rotation=90, fontsize=12, verticalalignment='center', horizontalalignment='center')


# Mostrar el grafo en Streamlit
st.pyplot(plt)