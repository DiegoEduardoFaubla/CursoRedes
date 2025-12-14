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
imagen3 = Image.open("instructor6.png")

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


st.image(imagen1, width=400)
    
with st.container():
    st.markdown("<h1 style='text-align: center;'>Curso Completo: Introducción a las redes de computadoras</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Hola, Bienvenido! ¿Comó estás? 👋</h2>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Estas listo para convertirte en un Experto en Redes! 🥷</h2>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Tu Viaje a Través de las Redes de Computadoras Comienza Aquí 🌐</h2>", unsafe_allow_html=True)

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown("<h5>¿Listo para dominar la columna vertebral del Internet? Este curso te llevará desde los cimientos teóricos (Modelos OSI y TCP/IP) hasta la configuración práctica de dispositivos.</h5>", unsafe_allow_html=True)
        st.subheader("¿Por Qué es Importante este Curso?")
        st.success("Dominarás el Modelo de Capas: Entenderás cómo se interconectan la Capa Física y la Capa de Aplicación.")
        st.success("Serás un Mago del Direccionamiento: Sabrás cómo funciona ARP, IPv4, IPv6 y harás Cálculos Matemáticos de redes como un profesional.")
        st.success("Estarás Listo para Configurar: Aplicarás tus conocimientos con un Lab de configuración en dispositivos reales o simulados.")
    with right_column:
        st.image(imagen2)

with st.container():
        st.write("---")
        st.subheader("¿Qué Lograrás al finalizar? (Objetivos de Aprendizaje)")
        st.info("Dominar los Fundamentos de Redes")
        st.info("Ser un Experto en Direccionamiento Lógico")
        st.info("Comprender la Conectividad de dispositivos")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Contenidos")
        st.header("🗺️ Estructura del Curso")
        with st.expander("Módulos 1-6"):
            st.write("Módulo 1: Las redes en nuestros tiempos")
            st.write("Módulo 2: Configuración básica de dispositivos")
            st.write("Módulo 3: Protocolos y Modelos")
            st.write("Módulo 4: Capa 1 del Modelo OSI - Capa Física")
            st.write("Módulo 5: Matemáticas de Redes (Sistema binario, hexadecimal)")
            st.write("Módulo 6: Capa 2 del Modelo OSI - Capa Enlace de Datos")
        with st.expander("Módulos 7-12"):
            st.write("Módulo 7: Tecnología Ethernet")
            st.write("Módulo 8: Capa 3 del Modelo OSI - Capa de Red")
            st.write("Módulo 9: ARP")
            st.write("Módulo 10: Configuración de dispositivos router")
            st.write("Módulo 11: IPv4")
            st.write("Módulo 12: IPv6")
        with st.expander("Módulos 13-17"):
            st.write("Módulo 13: Protocolo de mensajes de control del Internet (ICMP)")
            st.write("Módulo 14: Capa 4 del Modelo OSI - Capa de Transporte")
            st.write("Módulo 15: Capa 7 del Modelo OSI - Capa de Aplicación")
            st.write("Módulo 16: Fundamento de seguridad en una red")
            st.write("Módulo 17: Laboratorio final de configuración de dispositivos")
    with right_column:
            st_lottie(lottie_coding1, height=400, key="coding")
    
with st.container():
    st.write("---")
    st.title("Instructor")
        
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Diego Faubla")
        st.subheader("Estudiante de Ingeniería en Electrónica, Telecomunicaciones y Redes en la ESPOCH")
        st.info("Tesorero de la Rama IEEE Computer Society ESPOCH")
        st.success("Creador Digital de temas relacionados a las Telecomunicaciones.")
        st.subheader("Sobre mí")
        st.write("""Soy un estudiante apasionado por las redes de datos y la seguridad informática, con ya algunos años de experiencia aprendiendo y practicando en estos campos.
                A lo largo de mi formación he trabajado con tecnologías de routing, switching, virtualización de redes, automatización y seguridad, desarrollando un enfoque práctico y actualizado sobre cómo funcionan las infraestructuras modernas.
                Mi interés principal es seguir perfeccionándome en el ámbito de las redes empresariales y la ciberseguridad, combinando la teoría con la práctica mediante laboratorios y proyectos reales.
                Creo firmemente que el aprendizaje continuo es la clave en un mundo tecnológico que avanza a gran velocidad, y mi objetivo es compartir conocimientos y experiencias que motiven a otros a crecer en este mismo camino.""")
        st.write("""Si te interesa aprender sobre redes, seguridad o tecnologías emergentes, te invito a conocer mi canal donde subo material educativo, donde combino teoría y práctica para ofrecer una experiencia de aprendizaje clara, aplicada y actualizada. """)        
        st.write("[Youtube >] (https://www.youtube.com/@DiegoFaubla)")
    with right_column:
            st.image(imagen3,width=500)

with st.container():            
    st.markdown("<br><br>", unsafe_allow_html=True) # Espacio final
    st.caption("© 2025-2026 IEEE Computer Society.")
    st.caption("Aplicación construida usando Python y Streamlit.")
