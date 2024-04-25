import streamlit as st
from PIL import Image
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

df= pd.read_csv("CursosInformatica.csv")

st.set_page_config(
    page_title="register",
    page_icon="volcano",
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


# Crear un grafo bipartito de ejemplo
G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4], bipartite=0)  # Nodos del primer conjunto
G.add_nodes_from(['A', 'B', 'C'], bipartite=1)  # Nodos del segundo conjunto
G.add_edges_from([(1, 'A'), (2, 'A'), (3, 'B'), (4, 'C')])  # Conexiones entre los conjuntos

# Dibujar el grafo
pos = {1: (1, 1), 2: (2, 1), 3: (3, 1), 4: (4, 1), 'A': (1.5, 2), 'B': (2.5, 2), 'C': (3.5, 2)}  # Posiciones de los nodos
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, edge_color='black', linewidths=1, font_size=15)

# Etiquetas de los niveles
labels = {1: "Nivel 1", 2: "Nivel 2"}
for level, label in labels.items():
    plt.text(level + 0.1, 0.5, label, rotation=90, fontsize=12, verticalalignment='center')

# Mostrar el grafo en Streamlit
st.pyplot(plt)