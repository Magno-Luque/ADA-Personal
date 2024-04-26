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


asigCodAcro = {}
asigAcroCod = {}
nombresNivel = {}
cursosNivel = {}
posic = {}
nombresCiclo = []
listas = [('C0613', 'C0614'),('C0659', 'C0657'),('C0657', 'C0741'),('C0622', 'C0742'),
          ('C0201', 'C0208'),('C0614', 'C0513'),('C0667', 'C8274'),('C0741', 'C0743'),
          ('C0667', 'C0750'),('C0742', 'C0745'),('C0657', 'C0503'),('C8275', 'C8277'),
          ('C8191', 'C0679'),('C8277', 'C8278'),('C8276', 'C8279'),('C0503', 'C8281'),
          ('C0679', 'C1330'),('C8277', 'C8282'),('C8279', 'C8283'),('C8279', 'C8284'),
          ('C8425', 'C8426'),('C0359', 'C8285'),('C8279', 'C8286'),('C0359', 'C8287'),
          ('C1330', 'C1343'),('C1335', 'C1342'),('C8426', 'C8427'),('C8287', 'C8288'),
          ('C8285', 'C8289'),('C1343', 'C8290'),('C8427', 'C8428'),('C8287', 'C8291'),
          ('C8290', 'C8272'),('C8269', 'C8271'),('C8284', 'C8292')]
listAristas = []


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
  nombresCiclo.append(i)
  if contador % 2==0:
      c += 0.5
  for k in j:
    posic[k] = (c, 20 - contador*2)
    c +=1

for tupla in listas:
    updated_i = (asigCodAcro[tupla[0]], asigCodAcro[tupla[1]]) 
    listAristas.append(updated_i)

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
G.add_edges_from(listAristas)

coloresPorNivel = {
    "PRIMER CICLO": "red","SEGUNDO CICLO": "blue",
    "TERCER CICLO": "green","CUARTO CICLO": "magenta",
    "QUINTO CICLO": "red","SEXTO CICLO": "blue",
    "SÉTIMO CICLO": "green","OCTAVO CICLO": "magenta",
    "NOVENO CICLO": "red","DECIMO CICLO": "blue",
}
colors_by_edge = {
    ('F', 'CR1'): "black",
    ('CR1', 'CDI'): "black",
    ('CDI', 'AMGA'): "black",
    ('AMGA', 'QG'): "black",
    ('QG', 'III'): "black",
    # Agrega más colores para otras aristas según sea necesario
}

aristasColors = []

for nivel, arista in colors_by_edge.items():
    aristasColors.append(coloresPorNivel[nivel])

plt.figure(figsize=(17, 27))
nx.draw(G, posic, with_labels=True, node_color='skyblue', node_size=8000, edge_color=aristasColors,width=5, linewidths=1, font_size=20)

posicionNivel = {}
for nivel, nodos in cursosNivel.items():
    y_pos = sum([posic[node][1] for node in nodos]) / len(nodos) 
    posicionNivel[nivel] = (0.5, y_pos)

for nivel, posicion in posicionNivel.items():
    plt.text(posicion[0], posicion[1], nivel, rotation=90, fontsize=20, verticalalignment='center', horizontalalignment='center')

st.pyplot(plt)


nivelPresionado = st.sidebar.selectbox("Selecciona un ciclo", nombresCiclo)
if nivelPresionado:
    st.sidebar.markdown(f"**Información del Nodo {nivelPresionado}:**")
    if nivelPresionado in level_labels['Nivel 1']:
        st.sidebar.write("Información específica del Nodo:")
    elif nivelPresionado in level_labels['Nivel 2']:
        st.sidebar.write("Información específica del Nodo:")
st.pyplot(plt)