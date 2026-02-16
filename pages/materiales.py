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
st.write("[Pulsa aquí para descargar la presentación del módulo 1](https://liveespochedu-my.sharepoint.com/:b:/g/personal/diegoe_faubla_espoch_edu_ec/IQD9YvQgJb9HQ7ehSfbu_fcPAdx0Mf7H-aEbcfB2Ttx19h4?e=vgmefN)")
st.write("[Pulsa aquí para descargar la presentación del módulo 2](https://liveespochedu-my.sharepoint.com/:b:/g/personal/diegoe_faubla_espoch_edu_ec/IQCkoa2kpnQ9SKqzUPnTd2AQAU1yapynU5KhjJqsClxleac?e=fBRQKG)")
st.write("[Pulsa aquí para descargar la presentación del módulo 3](https://liveespochedu-my.sharepoint.com/:b:/g/personal/diegoe_faubla_espoch_edu_ec/IQBJmbSXPDRHSrm6R-BULH0xAdH4yNKgeJKPCqEjdhSkHGs?e=vfI3pa)")
st.write("[Pulsa aquí para descargar la presentación del módulo 4](https://liveespochedu-my.sharepoint.com/:b:/g/personal/diegoe_faubla_espoch_edu_ec/IQBa1xaG1xnXSbk6dg5beNsSAUUlBnewIlPCBFp3Davfj2g?e=gOJHWB)")
st.write("[Pulsa aquí para descargar la presentación del módulo 5](https://liveespochedu-my.sharepoint.com/:b:/g/personal/diegoe_faubla_espoch_edu_ec/IQDxsCwZK1sHQpHk7RINLKosAZQ3EzU5hVbfaP6cX5dcjmw?e=OpqLQ7)")
st.write("[Pulsa aquí para descargar la presentación del módulo 6](https://drive.google.com/file/d/1i01K9nPEcg2bv9APAGlIwDqrIDqvTLOE/view?usp=sharing)")
st.write("[Pulsa aquí para descargar la presentación del módulo 7](https://drive.google.com/file/d/1GeF5M5mft0ufWDz3eN07tBUg3-gsBuEr/view?usp=sharing)")
st.write("[Pulsa aquí para descargar la presentación del módulo 8](https://drive.google.com/file/d/12e-2beTFhc7qoNOzbyuVnjWEP8P9yUI9/view?usp=sharing)")
st.write("[Pulsa aquí para descargar la presentación del módulo 9](https://drive.google.com/file/d/1tuQAzmd-BUsWFsdCkvTCKo_qREk0bzKX/view?usp=sharing)")
st.write("[Pulsa aquí para descargar la presentación del módulo 10](https://drive.google.com/file/d/1HVFhTDJUGd5AHSDBCysoylwgY-c4OVV6/view?usp=sharing)")
st.write("[Pulsa aquí para descargar la presentación del módulo 11](https://drive.google.com/file/d/1vHALXbU7STWPKVht9D0wU8q9UtBD4v-g/view?usp=sharing)")
st.write("[Pulsa aquí para descargar la presentación del módulo 12](https://drive.google.com/file/d/1BUkS6jhQUL74mBwSH4NUiB5_bMVUyUWJ/view?usp=sharing)")
st.write("[Pulsa aquí para descargar la presentación del módulo 13](https://drive.google.com/file/d/1mZfxD0CMoo4Wu_ooqSp889NJTkr_XYfx/view?usp=sharing)")
st.write("[Pulsa aquí para descargar la presentación del módulo 14](https://drive.google.com/file/d/1q6zFwtAc2o-p5qaJOMupYjvvJUUuhoE9/view?usp=sharing)")
st.write("[Pulsa aquí para descargar la presentación del módulo 15](https://drive.google.com/file/d/1EC1OiOyNYVQtus5g48cKDvak-CZKWxVy/view?usp=sharing)")
st.write("[Pulsa aquí para descargar la presentación del módulo 16](https://drive.google.com/file/d/1cdyHOaAWQElqwAYmFkWAh4iPtWE50igU/view?usp=sharing)")
st.write("[Pulsa aquí para descargar la presentación del módulo 17](https://www.youtube.com/@DiegoFaubla)")

st.subheader("Clases")
st.write("[Para ver las clases, pulsa en el siguiente link >] (https://www.youtube.com/@ComputerSocietyESPOCH)")

with st.container():            
    st.markdown("<br><br>", unsafe_allow_html=True) # Espacio final
    st.caption("© 2025-2026 IEEE Computer Society.")
    st.caption("Aplicación construida usando Python y Streamlit.")        
