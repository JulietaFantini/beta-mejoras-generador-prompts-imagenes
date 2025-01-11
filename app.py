import os
import streamlit as st
from pantalla1 import configurar_pantalla1, configurar_sidebar
from pantalla2 import configurar_pantalla2

def main():
    """
    Punto de entrada principal de la aplicación Streamlit.
    Maneja la navegación entre Pantalla 1 y Pantalla 2.
    """

    # Podés descomentar si querés desactivar totalmente el tema predeterminado de Streamlit.
    # os.environ["STREAMLIT_THEME"] = "false"

    # Configuración de la página (usa la info de config.toml para colores y fuentes)
    st.set_page_config(
        page_title="Generador de Prompts con IA",
        page_icon=":art:",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Inyectar estilos adicionales:
    # 1) Botones y expanders,
    # 2) Forzar sans-serif en inputs (manteniendo monospace en el resto).
    st.markdown(
        """
        <style>
        /* ==== 1) Botones con el color primario (#6B46C1) ==== */
        .stButton>button {
            background-color: #6B46C1;
            color: #FFFFFF;
            border-radius: 8px;
            font-size: 16px;
            border: none;
        }
        .stButton>button:hover {
            background-color: #5A3AA9; /* un poco más oscuro en hover */
        }

        /* ==== 2) Expanders con un fondo gris-lavanda ==== */
        .st-expander {
            background-color: #F8F6FC !important; /* tono muy suave */
            border-radius: 8px;
        }

        /* ==== 3) Forzar sans-serif en inputs y labels ==== */
        /* Etiquetas de los campos de entrada */
        .stTextInput label, .stTextArea label, .stSelectbox label, .stRadio label, .stCheckbox label {
            font-family: sans-serif !important;
        }
        /* Texto dentro de los inputs, textareas, selects, etc. */
        .stTextInput input, .stTextArea textarea, 
        .stSelectbox [role="combobox"], 
        .stRadio div[data-testid="stMarkdownContainer"], 
        .stCheckbox div[data-testid="stMarkdownContainer"] {
            font-family: sans-serif !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Mostrar la barra lateral educativa SIEMPRE
    configurar_sidebar()

    # Inicializar variable de navegación si no existe
    if "pantalla_actual" not in st.session_state:
        st.session_state.pantalla_actual = "pantalla1"

    # Funciones para cambiar de pantalla
    def mostrar_pantalla1():
        st.session_state.pantalla_actual = "pantalla1"

    def mostrar_pantalla2():
        st.session_state.pantalla_actual = "pantalla2"

    # Lógica de navegación
    if st.session_state.pantalla_actual == "pantalla1":
        configurar_pantalla1(mostrar_pantalla2=mostrar_pantalla2)
    elif st.session_state.pantalla_actual == "pantalla2":
        configurar_pantalla2(mostrar_pantalla1)


if __name__ == "__main__":
    main()
