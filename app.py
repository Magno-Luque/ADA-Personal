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


def mostrar_informacion_nodo(nodo):
    # Define la información para cada nodo
    informacion_nodos = {
        'A': 'Información sobre el nodo A',
        'B': 'Información sobre el nodo B',
        'C': 'Información sobre el nodo C',
        'D': 'Información sobre el nodo D'
    }
    return informacion_nodos.get(nodo, 'Información no disponible')

def main():
    grafo = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D'],
        'D': ['B', 'C']
    }

    # Crear una visualización del grafo
    G = nx.Graph(grafo)
    pos = nx.spring_layout(G)

    # Mostrar el grafo en Streamlit
    st.title('Visualización de un Grafo')
    st.write(nx.info(G))

    # Dibujar el grafo
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=12, font_weight='bold')
    plt.title('Grafo')
    st.pyplot()

    # Interacción con los nodos
    nodo_seleccionado = st.selectbox('Seleccione un nodo:', list(grafo.keys()))

    if st.button('Mostrar información'):
        info = mostrar_informacion_nodo(nodo_seleccionado)
        st.write(f'Información sobre el nodo {nodo_seleccionado}:')
        st.write(info)

if __name__ == '__main__':
    main()