import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Sismos en el Perú",
    page_icon="volcano",
    initial_sidebar_state="expanded",
)

page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"] > .main {
        background-image: url("https://raw.githubusercontent.com/gcdavidq/Project_PA/main/im1.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    </style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
image1 = Image.open('Imagen_Mapa_Peru.jpeg')

# Añadimos un panel de control
tab1, tab2, tab3 = st.tabs([":blue[**INICIO**]", ":blue[_**ANÁLISIS A NIVEL NACIONAL**_]", ":blue[_**ANÁLISIS A NIVEL DEPARTAMENTAL**_]"])

with tab1:
    font_style_cooper_black = 'font-family: "Cooper Black", sans-serif;';
    color = '#ba55d3'  
    st.markdown(f'<h1 style="color:{color}; font-family: Cooper Black, sans-serif;">ANÁLISIS SÍSMICO REGISTRADOS EN EL PERÚ (1960_2022)</h1>', unsafe_allow_html=True)

    st.image(image1)

with tab2:
    print("hello")