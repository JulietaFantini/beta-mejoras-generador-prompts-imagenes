import os
import streamlit as st
from pantalla1 import configurar_pantalla1
from pantalla2 import configurar_pantalla2

def main():
    """
    Punto de entrada principal de la aplicación Streamlit.
    Maneja la navegación entre Pantalla 1 y Pantalla 2.
    """
    # Configuración para evitar el estilo predeterminado de Streamlit
    os.environ["STREAMLIT_THEME"] = "false"

    # Inicializar variables en session_state si no existen
    if "pantalla_actual" not in st.session_state:
        st.session_state.pantalla_actual = "pantalla1"

    # Funciones para cambiar de pantalla
    def mostrar_pantalla1():
        st.session_state.pantalla_actual = "pantalla1"

    def mostrar_pantalla2():
        st.session_state.pantalla_actual = "pantalla2"

    # Configuración de estilo general desde config.toml o inyección CSS
    st.set_page_config(
        page_title="Generador de Prompts con IA",
        page_icon=":art:",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Inyectar estilos personalizados para títulos, textos y diseño general
    st.markdown(
        """
        <style>
        h1, h2, h3 { font-family: "Sans-serif"; color: #1A202C; }
        .st-markdown p { font-family: "Monospace"; font-size: 16px; color: #1A202C; }
        .stButton>button { background-color: #6B46C1; color: white; border-radius: 8px; font-size: 16px; }
        .st-expander { background-color: #EEEAF5; border-radius: 8px; }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Navegación entre pantallas
    if st.session_state.pantalla_actual == "pantalla1":
        configurar_pantalla1(mostrar_pantalla2=mostrar_pantalla2)
    elif st.session_state.pantalla_actual == "pantalla2":
        configurar_pantalla2(mostrar_pantalla1)

if __name__ == "__main__":
    main()
