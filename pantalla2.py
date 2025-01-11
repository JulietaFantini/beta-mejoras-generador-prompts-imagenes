import streamlit as st

def configurar_sidebar():
    """
    Configura la barra lateral con reglas, documentación y tips.
    """
    with st.sidebar:
        st.title("Guía de Prompts")

        with st.expander("Cómo crear prompts efectivos"):
            st.markdown("""
            ### Reglas Básicas
            1. Sé específico en cada descripción.
            2. Define el estilo visual claramente.
            3. Especifica el propósito.
            4. Incluye detalles técnicos relevantes.
            5. Evita términos genéricos como "bonito" o "interesante".

            #### Ejemplo Práctico
            ✅ "Fotografía profesional de un café acogedor al atardecer, con luz cálida entrando por ventanales."
            ❌ "Una foto de un café."
            """)

        with st.expander("Aprende a generar prompts"):
            st.markdown("""
            ### Proceso Básico
            1. Define tu idea principal.
            2. Elige el tipo de imagen.
            3. Especifica el propósito.
            4. Ajusta detalles técnicos como iluminación y composición.

            #### Tips Prácticos
            - Comienza con lo general y ve afinando los detalles.
            - Revisa la coherencia entre el estilo y el propósito.

            #### Ejemplo Antes/Después
            - **Antes**: "Un paisaje."
            - **Después**: "Un paisaje montañoso al atardecer, con nubes de colores cálidos y un río reflejando la luz del sol."
            """)

        with st.expander("Documentación detallada"):
            st.markdown("""
            ### Referencia Técnica
            - **Términos clave**: Explicación detallada de conceptos.
            - **FAQs**: Preguntas frecuentes.
            - **Créditos y fuentes**: Detalles del desarrollo del proyecto.
            """)


def configurar_pantalla1(mostrar_pantalla2=None):
    """
    Pantalla exhaustiva con Idea Inicial, Tipo de Imagen, Propósito, 
    Estilo Artístico y Características Técnicas.
    """
    if "params" not in st.session_state:
        st.session_state.params = {}

    params = st.session_state.params

    st.title("Creador de Imágenes con IA")
    st.markdown(
        """
        ¡Hola! Vamos a transformar tu idea en una imagen única. 
        Este asistente te guiará paso a paso para crear una descripción 
        que las IAs entenderán perfectamente.

        Comencemos con lo esencial...
        """
    )

    # 1) IDEA INICIAL
    st.header("1. Idea Inicial")
    params["idea_inicial"] = st.text_input(
        "Describí tu idea inicial:",
        placeholder="Ejemplo: Una ciudad futurista flotando entre nubes al atardecer."
    )
    st.info("Describí el elemento principal y el ambiente que imaginás.")

    # 2) TIPO DE IMAGEN
    st.header("2. Tipo de Imagen")
    tipo_imagen_opciones = [
        "Fotografía (look realista)",
        "Ilustración (estilo artístico)",
        "Render 3D (visualización técnica)",
        "Arte Digital (mezcla realismo y creatividad)",
        "Pintura Digital (efecto pictórico)",
        "Otro (describir)"
    ]
    params["tipo_imagen"] = st.selectbox("Seleccioná el tipo de imagen:", tipo_imagen_opciones)

    if "Otro" in params["tipo_imagen"]:
        params["tipo_imagen_personalizado"] = st.text_input(
            "Describí tu tipo de imagen personalizado:",
            placeholder="Ejemplo: Collage surrealista"
        )

    # 3) PROPÓSITO
    st.header("3. Propósito")
    proposito_opciones = [
        "Marketing y Publicidad",
        "Arte y Diseño",
        "Contenido Digital",
        "Educativo",
        "Otro (Describe)"
    ]
    params["proposito_categoria"] = st.selectbox("Categoría:", proposito_opciones)

    if params["proposito_categoria"] == "Marketing y Publicidad":
        params["proposito_subcategoria"] = st.selectbox(
            "Subcategorías:",
            ["Redes Sociales", "Productos", "Campañas"]
        )
    elif params["proposito_categoria"] == "Arte y Diseño":
        params["proposito_subcategoria"] = st.selectbox(
            "Subcategorías:",
            ["Decoración", "Portfolio"]
        )
    elif params["proposito_categoria"] == "Contenido Digital":
        params["proposito_subcategoria"] = st.selectbox(
            "Subcategorías:",
            ["Web/Blog", "Presentaciones"]
        )
    elif params["proposito_categoria"] == "Educativo":
        params["proposito_subcategoria"] = st.selectbox(
            "Subcategorías:",
            ["Material Didáctico", "Infografías"]
        )
    elif "Otro" in params["proposito_categoria"]:
        params["proposito_personalizado"] = st.text_input(
            "Describí el propósito:",
            placeholder="Ej: Uso personal, inspiración, etc."
        )

    # 4) ESTILO ARTÍSTICO
    st.header("4. Estilo Artístico")
    estilo_opciones = [
        "Realista (Fiel a la realidad)",
        "Minimalista (Simple y esencial)",
        "Digital (Moderno y tecnológico)",
        "Surrealista (Fantástico)",
        "Pop Art (Colorido y popular)",
        "Cyberpunk (Futurista)",
        "Otro (Describe el estilo)"
    ]
    params["estilo_artistico"] = st.selectbox("Elegí el estilo:", estilo_opciones)

    if "Otro" in params["estilo_artistico"]:
        params["estilo_artistico_personalizado"] = st.text_input(
            "Describí tu estilo artístico personalizado:",
            placeholder="Ejemplo: Realismo fotográfico con toques surrealistas."
        )

    # 5) CARACTERÍSTICAS TÉCNICAS
    st.header("5. Características Técnicas")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Iluminación")
        iluminacion_opciones = ["Natural", "Artificial", "Dramática", "Ambiental", "Nocturna"]
        params["iluminacion"] = st.selectbox("Seleccioná el tipo de luz:", iluminacion_opciones)

    with col2:
        st.subheader("Plano")
        plano_opciones = ["General (Todo el contexto)", "Medio (Equilibrado)", "Primer Plano (Detalles)", "Detalle (Máximo acercamiento)"]
        params["plano"] = st.selectbox("Distancia y perspectiva:", plano_opciones)

    with col3:
        st.subheader("Composición")
        composicion_opciones = ["Centrada", "Regla de Tercios", "Simétrica", "Dinámica"]
        params["composicion"] = st.selectbox("Organización visual:", composicion_opciones)

    st.subheader("Resolución")
    resolucion_opciones = ["Redes Sociales (1080x1080)", "Web (1920x1080)", "Móvil (9:16)", "Alta Calidad (2K/4K)"]
    params["resolucion"] = st.selectbox("Tamaño según uso:", resolucion_opciones)

    st.subheader("Acabado")
    acabado_opciones = ["Natural", "Suave", "Texturizado", "Brillante"]
    params["acabado"] = st.selectbox("Efecto final:", acabado_opciones)

    # Botón para Validar y Continuar
    if st.button("Validar y Continuar"):
        # Simple check: la idea_inicial no esté vacía
        if not params["idea_inicial"].strip():
            st.error("Por favor, completá al menos tu idea inicial.")
        else:
            st.success("¡Todo listo! Avanzando a la siguiente etapa...")
            if mostrar_pantalla2:
                mostrar_pantalla2()
