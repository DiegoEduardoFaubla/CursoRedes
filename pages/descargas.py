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

#Seccion 4 Descargas: escenarios
st.image(imagen1,width=400)

st.header(f"Estas en descargas 💽")
st.subheader(f"Hallarás los laboratorios que te ayudarán a poner en práctica lo aprendido.")

st.write("[Pulsa aquí para descargar los laboratorios del módulo 1](https://drive.google.com/drive/folders/1XIiD33slwSL1Qlrm9flFepgLTVDNi5PK?usp=sharing)")
st.write("[Pulsa aquí para descargar los laboratorios del módulo 2](https://drive.google.com/drive/folders/1H__Xm_vdBnfNJkkhS-anwN3kGEGhJSRC?usp=sharing)")
st.write("[Pulsa aquí para descargar los laboratorios del módulo 3](https://drive.google.com/drive/folders/1Eskm5GPo1kI8cQt5ScNvy0hVkXw_glYL?usp=sharing)")
st.write("[Pulsa aquí para descargar los laboratorios del módulo 4](https://www.youtube.com/@DiegoFaubla)")
st.write("[Pulsa aquí para descargar los laboratorios del módulo 5](https://www.youtube.com/@DiegoFaubla)")
st.write("[Pulsa aquí para descargar los laboratorios del módulo 6](https://drive.google.com/drive/folders/17GNwjblh0gVEg0MLFZ_IcLZSz1kvpg13?usp=sharing)")
st.write("[Pulsa aquí para descargar los laboratorios del módulo 7](https://drive.google.com/drive/folders/1-kNYchM1MaDbLM45YbSKLGHGuhNNsUKK?usp=sharing)")
st.write("[Pulsa aquí para descargar los laboratorios del módulo 8](https://drive.google.com/drive/folders/1icHLFbNcFUZf2rKJ1p1m0kdny2b9nUKo?usp=sharing)")
st.write("[Pulsa aquí para descargar los laboratorios del módulo 9](https://drive.google.com/drive/folders/1VVEjfl-K9IcGHkmRatwnvGaumbdVIAbA?usp=sharing)")
st.write("[Pulsa aquí para descargar los laboratorios del módulo 10](https://drive.google.com/drive/folders/1ZL5DeyxIWAkcXwCblHVAVRk383jVBsIk?usp=sharing)")
st.write("[Pulsa aquí para descargar los laboratorios del módulo 11](https://drive.google.com/drive/folders/1iwB7OmGlVkpqj98a7Q1CLuB6DufSwz7V?usp=sharing)")
st.write("[Pulsa aquí para descargar los laboratorios del módulo 12](https://drive.google.com/drive/folders/12QsYjQex1laU9HOWcLuy1_OF97L9QwAn?usp=sharing)")
st.write("[Pulsa aquí para descargar los laboratorios del módulo 13](https://drive.google.com/drive/folders/1YCzI7tAJgAPNU65-XlZkMiNgUdtI6DV1?usp=sharing)")
st.write("[Pulsa aquí para descargar los laboratorios del módulo 14](https://drive.google.com/drive/folders/1R0BKt1uTbLDEYu8Ak12jWoVQygCjP9tA?usp=sharing)")
st.write("[Pulsa aquí para descargar los laboratorios del módulo 15](https://drive.google.com/drive/folders/1mnlY1tNIFF0AjdD0ErymXneYZ3VUdEMa?usp=drive_link)")
st.write("[Pulsa aquí para descargar los laboratorios del módulo 16](https://drive.google.com/drive/folders/1Ll5NTem7XOwHa0aiCrDL66v8auXQhTZm?usp=sharing)")
st.write("[Pulsa aquí para descargar los laboratorios del módulo 17](https://www.youtube.com/@DiegoFaubla)")
    
with st.container():            
    st.markdown("<br><br>", unsafe_allow_html=True) # Espacio final
    st.caption("© 2025-2026 IEEE Computer Society.")
    st.caption("Aplicación construida usando Python y Streamlit.")            
