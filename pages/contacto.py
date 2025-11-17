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

#Seccion 5 Contacto: Redes Sociales
st.image(imagen1,width=400)

st.header(f"Para mas información visita nuestras redes sociales 📱")

st.write("[Instagram >] (https://www.instagram.com/computersocietyespoch/)")
st.write("[Youtube >] (https://www.youtube.com/@ComputerSocietyESPOCH)")
st.write("[Facebook >] (https://www.facebook.com/profile.php?id=61583790411433)")
st.write("[TikTok >] (https://www.tiktok.com/@cs_espoch?is_from_webapp=1&sender_device=pc)")

with st.container():            
    st.markdown("<br><br>", unsafe_allow_html=True) # Espacio final
    st.caption("© 2025-2026 IEEE Computer Society.")
    st.caption("Aplicación construida usando Python y Streamlit.")
