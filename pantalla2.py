import streamlit as st

def configurar_pantalla2(mostrar_pantalla1):
    """
    Configura los elementos y campos de la Pantalla 2.
    Genera un prompt basado en los datos ingresados en Pantalla 1 y permite su edición.
    También incluye recomendaciones de herramientas y un enlace para traducción.
    """
    if "params" not in st.session_state or not st.session_state.params:
        st.warning("No se han proporcionado datos desde Pantalla 1. Por favor, completá los campos obligatorios.")
        if st.button("Volver a Pantalla 1"):
            mostrar_pantalla1()
        return

    params = st.session_state.params

    # Generación del prompt
    def generar_prompt(params):
        prompt = ""

        if params.get("idea_inicial"):
            prompt += f"Imagina {params['idea_inicial']}. "

        if params.get("tipo_de_imagen"):
            if params["tipo_de_imagen"] == "Otro":
                prompt += f"Tipo de imagen: {params.get('tipo_de_imagen_personalizado', '').lower()}. "
            else:
                prompt += f"Tipo de imagen: {params['tipo_de_imagen'].lower()}. "

        if params.get("estilo_artístico"):
            if params["estilo_artístico"] == "Otro":
                prompt += f"Estilo artístico: {params.get('estilo_artístico_personalizado', '').lower()}. "
            else:
                prompt += f"Estilo artístico: {params['estilo_artístico'].lower()}. "

        if params.get("proposito_categoria"):
            prompt += f"Propósito: {params['proposito_categoria'].lower()}"
            if params.get("subpropósito"):
                prompt += f", específicamente {params['subpropósito'].lower()}. "
            else:
                prompt += ". "

        if params.get("iluminación"):
            prompt += f"Iluminación: {params['iluminación'].lower()}. "

        if params.get("plano_fotográfico"):
            prompt += f"Plano fotográfico: {params['plano_fotográfico'].lower()}. "

        if params.get("composición"):
            prompt += f"Composición: {params['composición'].lower()}. "

        if params.get("paleta_de_colores"):
            prompt += f"Paleta de colores: {params['paleta_de_colores'].lower()}. "

        if params.get("textura"):
            prompt += f"Textura: {params['textura'].lower()}. "

        if params.get("resolucion"):
            prompt += f"Resolución y formato: {params['resolucion'].lower()}. "

        return prompt.strip()

    prompt_generado = generar_prompt(params)

    # Pantalla principal
    st.title("Tu Prompt Generado")
    st.markdown(
        "Este es el prompt generado basado en los datos ingresados. Podés ajustarlo según sea necesario y copiarlo para usarlo con herramientas de IA."
    )

    # Edición del prompt
    st.subheader("Editar Prompt")
    prompt_editado = st.text_area(
        "Podés editar el prompt generado:",
        value=prompt_generado,
        height=200
    )

    # Copiar prompt
    st.subheader("Copiar Prompt")
    st.markdown(
        "Hacé clic en el botón para copiar el prompt al portapapeles.")
    if st.button("Copiar al portapapeles"):
        st.code(prompt_editado)
        st.success("Prompt copiado exitosamente.")

    # Traducción
    st.subheader("¿Querés traducir tu prompt?")
    st.markdown(
        "Algunas herramientas funcionan mejor con prompts en inglés. Podés usar Google Translate para traducir tu texto."
    )
    google_translate_url = f"https://translate.google.com/?sl=es&tl=en&text={prompt_editado.replace(' ', '%20')}"
    st.markdown(f"[Traducir con Google Translate →]({google_translate_url})")

    # Recomendaciones de herramientas
    st.subheader("Herramientas Recomendadas")
    st.markdown(
        "Basándonos en el propósito y estilo artístico seleccionados, recomendamos las siguientes herramientas:")
    st.markdown(
        "- **[DALL·E](https://openai.com/dall-e/)**: Ideal para generar composiciones artísticas y creativas.\n"
        "- **[MidJourney](https://www.midjourney.com/)**: Especializada en imágenes de alta calidad y estética única.\n"
        "- **[Stable Diffusion](https://stability.ai/)**: Excelente para prompts personalizados y ajustes detallados."
    )

    # Botón para volver a Pantalla 1
    if st.button("Volver a Pantalla 1"):
        mostrar_pantalla1()

if __name__ == "__main__":
    configurar_pantalla2(lambda: print("Pantalla 1 cargada."))
