import streamlit as st

st.set_page_config(page_title="Introducción a las redes IEEE CS ESPOCH",page_icon="💻",layout="wide")

# Definición de las páginas (archivos en tu carpeta 'pages/')
pages = [
    st.Page("pages/home.py", title="Home", icon="🏠"),
    st.Page("pages/materiales.py", title="Materiales", icon="📚"),
    st.Page("pages/repaso.py", title="Repaso", icon="✍️"),
    st.Page("pages/descargas.py", title="Descargas", icon="⬇️"),
    st.Page("pages/contacto.py", title="Contacto", icon="📧"),
]

# Crea el menú de navegación en la parte superior y ejecútalo
# Nota: La posición "top" es la clave aquí.
pg = st.navigation(pages, position="top") 
pg.run()

