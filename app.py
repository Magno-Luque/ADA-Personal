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
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, edge_color='black', linewidths=1, font_size=15)

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

###########################

asigCodAcro = {}
asigAcroCod = {}
nombresNivel = {}
cursosNivel = {}
posic = {}

for index, row in df.iterrows():
    asigCodAcro[row['Código']] = row['Acrónimo']

for index, row in df.iterrows():
    asigAcroCod[row['Acrónimo']] = row['Código']

nivel = ["PRIMER","SEGUNDO","TERCER","CUARTO","QUINTO","SEXTO","SÉTIMO","OCTAVO","NOVENO","DÉCIMO"]

for num, nombre in enumerate(nivel):
  nombresNivel[nivel[num]] = num+1

for nombre, ciclo in nombresNivel.items():
    dicTem = [] 
    for index, row in df.iterrows():
        if ciclo == row['Ciclo']:
            dicTem.append(row['Acrónimo'])
    cursosNivel[nombre + ' CICLO'] = dicTem 

for contador, (i, j) in enumerate(cursosNivel.items()):
  c = 1
  if contador % 2==0:
      c += 0.5
  for k in j:
    posic[k] = (c, 20 - contador*2)
    c +=1

G = nx.DiGraph()
G.add_nodes_from(['F', 'CR1', 'CDI', 'AMGA', 'QG', 'III'])
G.add_nodes_from(['CR2', 'CII', 'FI1', 'BI', 'PII', 'FP'])
G.add_nodes_from(['CVI', 'FI2', 'QO/QCS', 'CS', 'POO', 'EsD'])
G.add_nodes_from(['EcD', 'PA', 'FI3', 'EP', 'OAC', 'AED'])
G.add_nodes_from(['FD', 'I1', 'ADA', 'SO', 'CDR', 'IML'])
G.add_nodes_from(['PI1', 'BD', 'ILP', 'CSI', 'SI', 'AE1'])
G.add_nodes_from(['DP1', 'I2', 'HCD', 'CPD', 'IS', 'AE2'])
G.add_nodes_from(['PI2', 'DP2', 'I3', 'DSW', 'V', 'AE3'])
G.add_nodes_from(['DNI', 'E', 'T1', 'I4', 'DSM', 'AE4'])
G.add_nodes_from(['NRI', 'T2', 'TASI', 'DI', 'AE5', 'AE6'])

plt.figure(figsize=(17, 27))
nx.draw(G, posic, with_labels=True, node_color='skyblue', node_size=8000, edge_color='black', linewidths=1, font_size=20)

posicionNivel = {}
for nivel, nodos in cursosNivel.items():
    y_pos = sum([posic[node][1] for node in nodos]) / len(nodos) 
    posicionNivel[nivel] = (0.5, y_pos)

for nivel, posicion in posicionNivel.items():
    plt.text(posicion[0], posicion[1], nivel, rotation=90, fontsize=28, verticalalignment='center', horizontalalignment='center')

st.pyplot(plt)