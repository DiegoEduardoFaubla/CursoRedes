import streamlit as st

def aplicar_estilos():
    st.markdown("""
        <style>
        div.block-container {
            margin-top: 15px;
        }
        </style>
    """, unsafe_allow_html=True)