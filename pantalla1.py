import streamlit as st

def configurar_sidebar():
    """
    Configura la barra lateral educativa con reglas, guía paso a paso y documentación completa.
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
            - Revisa siempre la coherencia entre el estilo y el propósito.

            #### Ejemplo Antes/Después
            - **Antes**: "Un paisaje."
            - **Después**: "Un paisaje montañoso al atardecer, con nubes de colores cálidos y un río reflejando la luz del sol."
            """)

        with st.expander("Documentación detallada"):
            st.markdown("""
            ### Referencia Técnica
            - **Términos clave**: Explicación detallada de conceptos.
            - **FAQs**: Preguntas frecuentes respondidas.
            - **Créditos y fuentes**: Detalles del desarrollo del proyecto.
            """)


def configurar_pantalla1(mostrar_pantalla2=None):
    """
    Configura la pantalla inicial de la aplicación para capturar parámetros clave.
    """
    if "params" not in st.session_state:
        st.session_state.params = {}

    params = st.session_state.params

    st.title("Creador de Imágenes con IA")
    st.markdown(
        """
        ¡Hola! Vamos a transformar tu idea en una imagen única. 
        Este asistente te guiará paso a paso para crear una descripción que las IAs entenderán perfectamente.

        Comencemos con lo esencial...
        """
    )

    # 1. IDEA INICIAL
    st.header("1. Idea Inicial")
    st.markdown("¿Qué imagen tenés en mente? Describe los elementos principales y el ambiente deseado.")
    params["idea_inicial"] = st.text_input(
        "Describí tu idea inicial:",
        placeholder="Ejemplo: Una ciudad futurista flotando entre nubes al atardecer."
    )
    with st.expander("Ver ejemplos de ideas iniciales"):
        st.markdown(
            """
            ✅ "Ciudad futurista flotando entre nubes púrpuras al amanecer."
            ❌ "Una ciudad" (muy general).
            """
        )
    st.info("🎯 Tip: Describí el elemento principal y el ambiente para guiar mejor a la IA.")

    # 2. TIPO DE IMAGEN
    st.header("2. Tipo de Imagen")
    st.markdown("¿Cómo querés que se vea tu imagen? Seleccioná una opción.")
    params["tipo_de_imagen"] = st.selectbox(
        "Seleccioná el tipo de imagen:",
        [
            "Fotografía (Para un look realista)",
            "Ilustración (Para estilo artístico)",
            "Render 3D (Para visualización técnica)",
            "Arte Digital (Combina realismo y creatividad)",
            "Pintura Digital (Efecto pictórico)",
            "Otro (Describe tu idea)"
        ]
    )

    if "Otro" in params["tipo_de_imagen"]:
        params["tipo_de_imagen_personalizado"] = st.text_input(
            "Describí tu tipo de imagen personalizado:",
            placeholder="Ejemplo: Collage surrealista."
        )

    # 3. PROPÓSITO
    st.header("3. Propósito")
    st.markdown("¿Para qué vas a usar la imagen? Seleccioná una categoría y, si corresponde, una subcategoría.")
    
    # Agregamos "Otro" para ser coherentes
    proposito_opciones = ["Marketing y Publicidad", "Arte y Diseño", "Contenido Digital", "Educativo", "Otro (Describe)"]
    
    params["proposito_categoria"] = st.selectbox(
        "Categoría:",
        proposito_opciones
    )

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
            placeholder="Ejemplo: Uso personal, inspiración, etc."
        )

    # 4. ESTILO ARTÍSTICO
    st.header("4. Estilo Artístico")
    st.markdown("¿Qué estilo visual preferís? Esto definirá la estética general de tu imagen.")
    params["estilo_artístico"] = st.selectbox(
        "Seleccioná el estilo artístico:",
        [
            "Realista (Fiel a la realidad)",
            "Minimalista (Simple y esencial)",
            "Digital (Moderno y tecnológico)",
            "Surrealista (Fantástico)",
            "Pop Art (Colorido y popular)",
            "Cyberpunk (Futurista)",
            "Otro (Describe el estilo)"
        ]
    )
    if "Otro" in params["estilo_artístico"]:
        params["estilo_artístico_personalizado"] = st.text_input(
            "Describí tu estilo artístico personalizado:",
            placeholder="Ejemplo: Realismo fotográfico con elementos surrealistas."
        )

    # 5. CARACTERÍSTICAS TÉCNICAS
    st.header("5. Características Técnicas")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Iluminación")
        st.markdown("Tipo de luz:")
        params["iluminación"] = st.selectbox(
            "Opciones:",
            [
                "Natural (Luz día)",
                "Artificial (Estudio)",
                "Dramática (Contraste)",
                "Ambiental (Suave)",
                "Nocturna"
            ]
        )

    with col2:
        st.subheader("Plano")
        st.markdown("Distancia y perspectiva:")
        params["plano"] = st.selectbox(
            "Opciones:",
            [
                "General (Todo el contexto)",
                "Medio (Equilibrado)",
                "Primer Plano (Detalles)",
                "Detalle (Máximo acercamiento)"
            ]
        )

    with col3:
        st.subheader("Composición")
        st.markdown("Organización visual:")
        params["composición"] = st.selectbox(
            "Opciones:",
            [
                "Centrada",
                "Regla de Tercios",
                "Simétrica",
                "Dinámica"
            ]
        )

    st.subheader("Resolución")
    params["resolución"] = st.selectbox(
        "Opciones:",
        [
            "Redes Sociales (1080x1080)",
            "Web (1920x1080)",
            "Móvil (9:16)",
            "Alta Calidad (2K/4K)"
        ]
    )

    st.subheader("Acabado")
    params["acabado"] = st.selectbox(
        "Opciones:",
        [
            "Natural",
            "Suave",
            "Texturizado",
            "Brillante"
        ]
    )

    # VALIDAR Y CONTINUAR
    if st.button("Validar y continuar"):
        # Simple validación: revisar si algo está vacío.
        # Omitimos "proposito_subcategoria" si es "Otro"
        errores = []
        for campo, valor in params.items():
            # Si es un string y está en blanco, lo consideramos error
            if isinstance(valor, str) and not valor.strip():
                errores.append(campo)

        if errores:
            st.error("Por favor, completá todos los campos obligatorios o retirá los que no apliquen.")
        else:
            st.success("¡Todo listo! Avanzando a la siguiente etapa.")
            if mostrar_pantalla2:
                mostrar_pantalla2()
