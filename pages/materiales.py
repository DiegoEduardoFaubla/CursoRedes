import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

# Función para la animación
def load_lottieurl(url):
  r = requests.get(url)
  if r.status_code !=200:
    return None
  return r.json()

#Animaciones
lottie_coding1 = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_0yfsb3a1.json")
#lottie_coding2 = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_ggwq3ysg.json")

#Imagenes a usar
imagen1 = Image.open("CS.jpeg")
imagen2 = Image.open("inicio.jpg")
imagen3 = Image.open("instructor4.png")


st.markdown("""
    <style>
    /* Afecta el contenedor principal de Streamlit */
    section[data-testid="stSidebar"] {
        top: 0;
    }
    div.block-container {
        padding-top: 0rem;   /* 🔹 reduce espacio superior */
        margin-top: 15px;   /* 🔹 sube todo el contenido */
    }
    </style>
""", unsafe_allow_html=True)

#Seccion 2 Materiales: clases, laminas
st.image(imagen1,width=400)

st.header(f"Aquí podrás obtener los materiales que te brindarán conocimiento 📚")

st.subheader("Láminas")
st.write("[Pulsa aquí para descargar la presentación del módulo 1](https://liveespochedu-my.sharepoint.com/:f:/g/personal/diegoe_faubla_espoch_edu_ec/IgB5pLmUyH2YQZOfNBoY-s52AQS-yIOp9KnkJWJb-pUeUis?e=Ob8pHv)")
st.write("[Pulsa aquí para descargar la presentación del módulo 2](https://liveespochedu-my.sharepoint.com/:f:/g/personal/diegoe_faubla_espoch_edu_ec/IgDdyE3ybxEHQY_lhbsyOSTbASfn-IS-X4KfEe9Vcy7qCG8?e=0ptvec)")
st.write("[Pulsa aquí para descargar la presentación del módulo 3](https://liveespochedu-my.sharepoint.com/:f:/g/personal/diegoe_faubla_espoch_edu_ec/IgA8CetNaSQdRbANhrA2_1aHAVSS1Ujcshf7TS5PZRxK6S0?e=fJrziA)")
st.write("[Pulsa aquí para descargar la presentación del módulo 4](https://www.youtube.com/@DiegoFaubla)")
st.write("[Pulsa aquí para descargar la presentación del módulo 5](https://www.youtube.com/@DiegoFaubla)")
st.write("[Pulsa aquí para descargar la presentación del módulo 6](https://www.youtube.com/@DiegoFaubla)")
st.write("[Pulsa aquí para descargar la presentación del módulo 7](https://www.youtube.com/@DiegoFaubla)")
st.write("[Pulsa aquí para descargar la presentación del módulo 8](https://www.youtube.com/@DiegoFaubla)")
st.write("[Pulsa aquí para descargar la presentación del módulo 9](https://www.youtube.com/@DiegoFaubla)")
st.write("[Pulsa aquí para descargar la presentación del módulo 10](https://www.youtube.com/@DiegoFaubla)")
st.write("[Pulsa aquí para descargar la presentación del módulo 11](https://www.youtube.com/@DiegoFaubla)")
st.write("[Pulsa aquí para descargar la presentación del módulo 12](https://www.youtube.com/@DiegoFaubla)")
st.write("[Pulsa aquí para descargar la presentación del módulo 13](https://www.youtube.com/@DiegoFaubla)")
st.write("[Pulsa aquí para descargar la presentación del módulo 14](https://www.youtube.com/@DiegoFaubla)")
st.write("[Pulsa aquí para descargar la presentación del módulo 15](https://www.youtube.com/@DiegoFaubla)")
st.write("[Pulsa aquí para descargar la presentación del módulo 16](https://www.youtube.com/@DiegoFaubla)")
st.write("[Pulsa aquí para descargar la presentación del módulo 17](https://www.youtube.com/@DiegoFaubla)")

st.subheader("Clases")
st.write("[Para ver las clases, pulsa en el siguiente link >] (https://www.youtube.com/@ComputerSocietyESPOCH)")

with st.container():            
    st.markdown("<br><br>", unsafe_allow_html=True) # Espacio final
    st.caption("© 2025-2026 IEEE Computer Society.")
    st.caption("Aplicación construida usando Python y Streamlit.")        
