import os
import streamlit as st
from pantalla1 import configurar_pantalla1, configurar_sidebar
from pantalla2 import configurar_pantalla2

def main():
    """
    Punto de entrada principal de la aplicación.
    Maneja la navegación entre Pantalla 1 y Pantalla 2.
    """

    # Opcional: forzar a false el tema default, podría anular config.toml. Normalmente, se deja comentado.
    # os.environ["STREAMLIT_THEME"] = "false"

    st.set_page_config(
        page_title="Generador de Prompts con IA",
        page_icon=":art:",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Inyectar CSS adicional:
    #  1) Botones color violeta
    #  2) Expanders con fondo suave
    #  3) Inputs en sans-serif
    #  4) Evitar scroll al final
    st.markdown(
        """
        <style>
        /* 1) Botones con color #6B46C1 */
        .stButton>button {
            background-color: #6B46C1 !important;
            color: #FFFFFF !important;
            border-radius: 8px;
            font-size: 16px;
            border: none;
        }
        .stButton>button:hover {
            background-color: #5A3AA9 !important; /* un poco más oscuro en hover */
        }

        /* 2) Expanders con fondo violeta claro */
        .st-expander {
            background-color: #F8F6FC !important; 
            border-radius: 8px;
        }

        /* 3) Inputs y labels en sans-serif */
        .stTextInput label, .stTextArea label, 
        .stSelectbox label, .stRadio label, .stCheckbox label {
            font-family: sans-serif !important;
        }
        .stTextInput input, .stTextArea textarea, 
        .stSelectbox [role="combobox"], 
        .stRadio div[data-testid="stMarkdownContainer"],
        .stCheckbox div[data-testid="stMarkdownContainer"] {
            font-family: sans-serif !important;
        }

        /* 4) Forzar scroll top */
        html, body {
            scroll-behavior: auto !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Barra lateral educativa (definida en pantalla1.py)
    configurar_sidebar()

    # Manejo de navegación
    if "pantalla_actual" not in st.session_state:
        st.session_state.pantalla_actual = "pantalla1"

    def mostrar_pantalla1():
        st.session_state.pantalla_actual = "pantalla1"
        st.experimental_rerun()  # recargamos y quedamos arriba

    def mostrar_pantalla2():
        st.session_state.pantalla_actual = "pantalla2"
        st.experimental_rerun()

    # Lógica de cuál pantalla mostrar
    if st.session_state.pantalla_actual == "pantalla1":
        configurar_pantalla1(mostrar_pantalla2=mostrar_pantalla2)
    elif st.session_state.pantalla_actual == "pantalla2":
        configurar_pantalla2(mostrar_pantalla1=mostrar_pantalla1)


if __name__ == "__main__":
    main()
