import os
import streamlit as st
from pantalla1 import configurar_pantalla1, configurar_sidebar
from pantalla2 import configurar_pantalla2

def main():
    """
    Punto de entrada principal de la aplicación Streamlit.
    Maneja la navegación entre Pantalla 1 y Pantalla 2.
    """

    # Desactiva el tema predeterminado de Streamlit si querés forzarlo, 
    # aunque con config.toml ya se aplica el tema personalizado.
    # os.environ["STREAMLIT_THEME"] = "false"

    # Configuración de la página (usa la info de config.toml para colores y fuentes)
    st.set_page_config(
        page_title="Generador de Prompts con IA",
        page_icon=":art:",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Inicializar variables en session_state si no existen
    if "pantalla_actual" not in st.session_state:
        st.session_state.pantalla_actual = "pantalla1"

    # Funciones para cambiar de pantalla
    def mostrar_pantalla1():
        st.session_state.pantalla_actual = "pantalla1"

    def mostrar_pantalla2():
        st.session_state.pantalla_actual = "pantalla2"

    # Inyectar estilos adicionales mínimos (botones, expanders, etc.)
    st.markdown(
        """
        <style>
        /* Ajuste de botones al color principal (primaryColor del config) */
        .stButton>button {
            background-color: #7B4DAE;
            color: #FFFFFF;
            border-radius: 8px;
            font-size: 16px;
            border: none;
        }
        .stButton>button:hover {
            background-color: #693DA6; /* un poco más oscuro en hover */
        }

        /* Expanders con un fondo gris muy suave */
        .st-expander {
            background-color: #F8F6FC !important;
            border-radius: 8px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Mostrar la barra lateral educativa SIEMPRE
    configurar_sidebar()

    # Navegación entre pantallas
    if st.session_state.pantalla_actual == "pantalla1":
        configurar_pantalla1(mostrar_pantalla2=mostrar_pantalla2)
    elif st.session_state.pantalla_actual == "pantalla2":
        configurar_pantalla2(mostrar_pantalla1)


if __name__ == "__main__":
    main()
