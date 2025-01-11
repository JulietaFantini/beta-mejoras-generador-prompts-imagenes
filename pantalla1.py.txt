import streamlit as st

def configurar_pantalla1(mostrar_pantalla2):
    """
    Configura los elementos y campos de la Pantalla 1.
    Permite al usuario definir parámetros clave y opcionales para generar prompts.
    """
    if "params" not in st.session_state:
        st.session_state.params = {}

    params = st.session_state.params

    st.title("Creador de imágenes con IA")
    st.markdown(
        "Definí los detalles clave para transformar tu idea en una imagen creada con IA. "
        "Completá los campos obligatorios para comenzar y ajustá los detalles opcionales para un prompt más preciso."
    )

    # Idea inicial
    st.header("1. Idea Inicial")
    st.markdown(
        "Describe la imagen que tenés en mente. Podés incluir elementos principales como ubicación, hora del día o el ambiente que querés transmitir."
    )
    with st.expander("¿Necesitás inspiración? Ver ejemplos"):
        st.info("Ejemplo: 'Ciudad futurista al amanecer con rascacielos de cristal.'")
        st.info("Ejemplo: 'Un bosque mágico iluminado por luciérnagas.'")
    params["idea_inicial"] = st.text_input(
        "Ingresá tu idea aquí:",
        placeholder="Escribí tu idea inicial."
    )

    # Tipo de imagen
    st.header("2. Tipo de Imagen")
    st.markdown(
        "Seleccioná el tipo de imagen que querés crear. Cada tipo tiene un enfoque único, desde realismo hasta conceptual."
    )
    params["tipo_de_imagen"] = st.selectbox(
        "Elige el tipo de imagen:",
        ["Fotografía", "Ilustración", "Render 3D", "Arte Conceptual", "Collage Surrealista", "Otro"]
    )
    if params["tipo_de_imagen"] == "Otro":
        params["tipo_de_imagen_personalizado"] = st.text_input(
            "Describe el tipo de imagen (ej.: 'Collage surrealista')."
        )

    # Estilo artístico
    st.header("3. Estilo Artístico")
    st.markdown(
        "Elegí un estilo artístico que defina el tono de tu imagen. Si tenés un estilo específico en mente, personalizalo."
    )
    with st.expander("¿Querés ejemplos de estilos?"):
        st.info("Arte Digital: Ideal para conceptos modernos y futuristas.")
        st.info("Impresionismo: Perfecto para paisajes con toques artísticos suaves.")
        st.info("Surrealismo: Para imágenes oníricas y poco convencionales.")
    params["estilo_artístico"] = st.selectbox(
        "Seleccioná un estilo artístico:",
        ["Arte Digital", "Impresionismo", "Minimalismo", "Surrealismo", "Fotorrealismo", "Otro"]
    )
    if params["estilo_artístico"] == "Otro":
        params["estilo_artístico_personalizado"] = st.text_input(
            "Describí tu estilo artístico personalizado (ej.: 'realismo fotográfico con elementos surrealistas')."
        )

    # Propósito de la imagen
    st.header("4. Propósito de la Imagen")
    st.markdown(
        "Seleccioná el propósito principal de tu imagen. Esto ayudará a optimizar el resultado final según el uso previsto."
    )
    params["proposito_categoria"] = st.selectbox(
        "Propósito general:",
        ["Publicidad", "Arte y Decoración", "Entretenimiento Digital", "Educativo", "Proyectos Técnicos"]
    )
    if params["proposito_categoria"]:
        subpropósitos = {
            "Publicidad": ["Campañas Publicitarias", "Branding", "Anuncios Digitales"],
            "Arte y Decoración": ["Arte Conceptual", "Diseño Ambiental", "Decoración Personalizada"],
            "Entretenimiento Digital": ["Videojuegos", "Storyboarding", "Diseño Cinematográfico"],
            "Educativo": ["Material Didáctico", "Diagramas Técnicos", "Proyectos STEM"],
            "Proyectos Técnicos": ["Modelos CAD", "Prototipos Técnicos", "Diagramas de Ingeniería"]
        }
        params["subpropósito"] = st.selectbox(
            "Subpropósito:",
            subpropósitos.get(params["proposito_categoria"], [])
        )

    # Detalles opcionales
    st.header("Detalles Opcionales")
    st.markdown(
        "Estos ajustes permiten personalizar aún más tu imagen. Son completamente opcionales, pero pueden influir en el resultado final."
    )

    # Iluminación
    st.subheader("Iluminación")
    st.markdown("Definí el tipo de iluminación que querés para tu imagen. Ejemplo: luz natural para escenas realistas.")
    params["iluminación"] = st.selectbox(
        "Opciones de iluminación:",
        ["Luz Natural", "Luz Artificial", "Dramática", "Ambiental", "Contraluz"]
    )

    # Plano fotográfico
    st.subheader("Plano Fotográfico")
    st.markdown("Seleccioná el encuadre para tu imagen, desde primeros planos hasta vistas generales.")
    params["plano_fotográfico"] = st.selectbox(
        "Opciones de plano:",
        ["Primer Plano", "Plano General", "Plano Medio", "Plano Cenital"]
    )

    # Composición
    st.subheader("Composición")
    st.markdown("Elegí una composición que organice visualmente los elementos en tu imagen.")
    params["composición"] = st.selectbox(
        "Opciones de composición:",
        ["Simétrica", "Regla de los Tercios", "Perspectiva Central"]
    )

    # Paleta de colores
    st.subheader("Paleta de Colores")
    st.markdown("Seleccioná un esquema de colores que defina el tono y la atmósfera de tu imagen.")
    params["paleta_de_colores"] = st.selectbox(
        "Opciones de paleta de colores:",
        ["Monocromático", "Cálidos", "Fríos", "Pastel"]
    )

    # Textura
    st.subheader("Textura")
    st.markdown("Definí la textura visual predominante, como suave, rugosa o metálica.")
    params["textura"] = st.selectbox(
        "Opciones de textura:",
        ["Suave", "Rugosa", "Metálica", "Vidriosa"]
    )

    # Resolución y formato
    st.subheader("Resolución y Formato")
    st.markdown("Definí la resolución y proporción de tu imagen según su uso final.")
    params["resolucion"] = st.selectbox(
        "Opciones de resolución:",
        ["300x300 px", "800x800 px", "1920x1080 px", "16:9", "1:1"]
    )

    # Validar y continuar
    if st.button("Generar Prompt"):
        errores = []
        if not params.get("idea_inicial"):
            errores.append("Por favor, completá la idea inicial.")
        if not params.get("tipo_de_imagen"):
            errores.append("Seleccioná un tipo de imagen.")
        if not params.get("estilo_artístico"):
            errores.append("Seleccioná un estilo artístico.")
        if not params.get("proposito_categoria"):
            errores.append("Seleccioná el propósito de la imagen.")

        if errores:
            for error in errores:
                st.error(error)
        else:
            mostrar_pantalla2()

if __name__ == "__main__":
    configurar_pantalla1(lambda: print("Pantalla 2 cargada."))
