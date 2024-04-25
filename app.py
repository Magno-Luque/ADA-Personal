import streamlit as st
from PIL import Image
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(
    page_title="Sismos en el Perú",
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


# Añadimos un panel de control
tab1, tab2, tab3 = st.tabs([":blue[**INICIO**]", ":blue[_**ANÁLISIS A NIVEL NACIONAL**_]", ":blue[_**ANÁLISIS A NIVEL DEPARTAMENTAL**_]"])

with tab1:
    font_style_cooper_black = 'font-family: "Cooper Black", sans-serif;';
    color = '#ba55d3'  
    st.markdown(f'<h1 style="color:{color}; font-family: Cooper Black, sans-serif;">..</h1>', unsafe_allow_html=True)

with tab2:
    st.text("hello")
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # Crear el gráfico
    plt.plot(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Gráfico de ejemplo')

    # Mostrar el gráfico en Streamlit
    st.pyplot()