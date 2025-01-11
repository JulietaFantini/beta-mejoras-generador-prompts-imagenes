import streamlit as st

# --------------------------
# Función principal
# --------------------------
def main():
    # Configuración de la página
    st.set_page_config(
        page_title="Generador de Prompts",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Estado para alternar entre pantallas
    if "mostrar_pantalla2" not in st.session_state:
        st.session_state.mostrar_pantalla2 = False
    
    # Barra lateral
    configurar_sidebar()
    
    # Lógica de navegación
    if st.session_state.mostrar_pantalla2:
        configurar_pantalla2()
    else:
        configurar_pantalla1()


# --------------------------
# Barra lateral educativa
# --------------------------
def configurar_sidebar():
    with st.sidebar:
        st.title("Guía de Prompts")
        
        # 1. Reglas Básicas
        with st.expander("Cómo crear prompts efectivos"):
            st.markdown("""
                ### Reglas Fundamentales
                1. Sé específico en cada descripción  
                2. Define el estilo visual claramente  
                3. Especifica el propósito  
                4. Incluye detalles técnicos relevantes  
                5. Mantén la coherencia  

                ### Ejemplos Prácticos
                ✅ **Bien**: "Fotografía profesional de un café acogedor al atardecer, 
                   con luz cálida entrando por ventanales"  
                ❌ **Mal**: "Foto de un café"
            """)
        
        # 2. Guía Paso a Paso
        with st.expander("Aprende a generar prompts"):
            st.markdown("""
                ### Proceso Básico
                1. Define tu idea principal  
                2. Elige el tipo de imagen  
                3. Especifica el propósito  
                4. Ajusta detalles técnicos  

                ### Tips Prácticos
                - Comienza con lo general  
                - Añade detalles específicos  
                - Revisa la coherencia  
            """)
        
        # 3. Manual Completo (placeholder)
        with st.expander("Documentación detallada"):
            st.markdown("""
                ### Referencia Técnica
                [Aquí iría el contenido del manual completo]

                ### FAQs
                [Preguntas frecuentes, si las hubiera]
            """)


# --------------------------
# Pantalla 1: Creación
# --------------------------
def configurar_pantalla1():
    st.title("Creador de imágenes con IA")
    st.markdown("Transformá tu idea en una imagen única mediante prompts personalizados.")

    # Sección 1: Idea Principal
    st.header("1. Idea Inicial")
    st.markdown("Contanos brevemente qué imagen tenés en mente. Te ayudaremos a estructurar el prompt.")

    idea = st.text_input(
        "Descripción base de tu imagen",
        placeholder="Ej.: Una ciudad futurista flotando entre nubes de color púrpura"
    )

    # (Opcional) Botón para dar feedback inmediato (puede comentarse si no se usa)
    if st.button("Validar Idea"):
        if not idea.strip():
            st.warning("¡Ojo! Parece que no ingresaste ninguna idea principal.")
        else:
            st.success("¡Excelente! Tu idea inicial está lista para usar.")
    
    with st.expander("Ver ejemplos de ideas"):
        st.info(
            "**Buenos ejemplos**\n"
            "- Ciudad futurista flotante al atardecer\n"
            "- Retrato minimalista en blanco y negro\n\n"
            "**Mal ejemplo**\n"
            "- Foto de un café"
        )

    # Sección 2: Parámetros Principales
    st.header("2. Parámetros Principales")
    st.markdown("Definí el tipo de imagen y su propósito para afinar el estilo y la intención de tu prompt.")

    col1, col2 = st.columns(2)

    with col1:
        tipo_imagen = st.selectbox(
            "¿Qué tipo de imagen buscás?",
            ["Fotografía", "Ilustración", "Render 3D", 
             "Arte Digital", "Pintura Digital"]
        )

    with col2:
        proposito = st.selectbox(
            "¿Para qué se va a usar esta imagen?",
            ["Marketing y Publicidad", "Arte y Diseño",
             "Contenido Digital", "Educativo"]
        )

    # Sección 3: Detalles Técnicos
    st.header("3. Aspectos Técnicos")
    st.markdown("Elegí cómo querés que sea la iluminación, la composición y la resolución.")

    col1, col2, col3 = st.columns(3)

    with col1:
        iluminacion = st.selectbox(
            "Iluminación",
            ["Natural", "Artificial", "Dramática",
             "Ambiental", "Nocturna"]
        )

    with col2:
        composicion = st.selectbox(
            "Composición",
            ["Centrada", "Regla de Tercios",
             "Simétrica", "Dinámica"]
        )

    with col3:
        resolucion = st.selectbox(
            "Resolución",
            ["Redes Sociales", "Web", "Móvil",
             "Alta Calidad"]
        )

    # Botón para avanzar a Pantalla 2, con validación mínima
    if st.button("Generar Prompt"):
        if not idea.strip():
            st.warning("Antes de generar el prompt, ingresá una idea principal.")
        else:
            # Guardamos los valores en session_state por si se quieren usar en la generación final
            st.session_state.idea = idea
            st.session_state.tipo_imagen = tipo_imagen
            st.session_state.proposito = proposito
            st.session_state.iluminacion = iluminacion
            st.session_state.composicion = composicion
            st.session_state.resolucion = resolucion

            st.session_state.mostrar_pantalla2 = True
            st.experimental_rerun()


# --------------------------
# Pantalla 2: Edición
# --------------------------
def configurar_pantalla2():
    st.title("Tu prompt está listo")
    st.markdown("Revisá el texto generado y ajustalo según necesites. Luego, copialo y ¡listo!")

    # Área de Edición
    st.header("Revisa y edita tu prompt")
    
    # Generamos el prompt a partir de lo que guardamos en session_state
    prompt_generado = generar_prompt()

    texto_editable = st.text_area(
        "Editar Prompt",
        value=prompt_generado,
        height=200
    )
    st.caption("Podés agregar detalles adicionales o corregir la redacción para que sea más precisa.")

    # Área de Copiado
    st.markdown("---")
    st.header("Copiá tu prompt final")
    st.info("Cuando estés conforme con tu prompt, hacé click en el ícono de copiado (arriba a la derecha).")

    st.code(texto_editable, language="")

    # Traducción
    st.header("¿Necesitás traducirlo al inglés?")
    google_translate_url = f"https://translate.google.com/?sl=es&tl=en&text={texto_editable}"
    st.markdown(f"[Traducir a inglés]({google_translate_url})")

    # Herramientas Sugeridas
    st.header("Herramientas Sugeridas")
    with st.expander("Ver opciones recomendadas"):
        st.markdown("""
        - **DALL-E (OpenAI)**: Ideal para composiciones artísticas o experimentales.  
        - **MidJourney**: Excelente para obtener estilos visuales muy detallados y 'pintorescos'.  
        - **Stable Diffusion**: Una opción open-source con gran versatilidad y comunidad activa.
        """)

    if st.button("Volver a Pantalla 1"):
        st.session_state.mostrar_pantalla2 = False
        st.experimental_rerun()


# --------------------------
# Función de generación de prompt
# (Podés adaptarla a tu gusto)
# --------------------------
def generar_prompt():
    """Esta función arma el prompt con la info guardada en session_state.
       Ajustala según tu gusto y formato en español argentino, etc.
    """
    # Recuperamos valores de session_state
    idea = st.session_state.get("idea", "")
    tipo_imagen = st.session_state.get("tipo_imagen", "")
    proposito = st.session_state.get("proposito", "")
    iluminacion = st.session_state.get("iluminacion", "")
    composicion = st.session_state.get("composicion", "")
    resolucion = st.session_state.get("resolucion", "")

    # Acá se puede armar la oración/estructura final
    # Ejemplo simple:
    prompt = (
        f"{idea}. "
        f"Tipo de imagen: {tipo_imagen}. "
        f"Propósito: {proposito}. "
        f"Iluminación: {iluminacion}. "
        f"Composición: {composicion}. "
        f"Resolución para: {resolucion}."
    )

    return prompt


# --------------------------
# Punto de entrada
# --------------------------
if __name__ == "__main__":
    main()
