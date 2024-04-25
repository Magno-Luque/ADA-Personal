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


G = nx.DiGraph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, edge_color='black', linewidths=1, font_size=15, arrows=True)

st.pyplot(plt)