import streamlit as st

def configurar_pantalla2(mostrar_pantalla1):
    """
    Configura los elementos y campos de la Pantalla 2.
    Genera un prompt basado en los datos ingresados en Pantalla 1 y permite su edición.
    También incluye recomendaciones de herramientas y un enlace para traducción.
    """
    # Chequeo de datos previos
    if "params" not in st.session_state or not st.session_state.params:
        st.warning("No se han proporcionado datos desde Pantalla 1. Por favor, completá los campos obligatorios.")
        if st.button("Generar un nuevo prompt"):
            mostrar_pantalla1()
        return

    params = st.session_state.params

    # Función local para generar el prompt
    def generar_prompt(params):
        """
        Genera un texto (prompt) a partir de los parámetros proporcionados.
        Estructurado en cuatro frases según lo definido.
        """
        frases = []

        # 1) Idea inicial
        if params.get("idea_inicial"):
            frases.append(f"Imaginá {params['idea_inicial']}.")

        # 2) Tipo + Estilo
        if "Otro" in params["tipo_de_imagen"]:
            tipo_imagen = params.get("tipo_de_imagen_personalizado", "un tipo no definido").lower()
        else:
            tipo_imagen = params["tipo_de_imagen"].lower()

        if "Otro" in params["estilo_artístico"]:
            estilo = params.get("estilo_artístico_personalizado", "un estilo no definido").lower()
        else:
            estilo = params["estilo_artístico"].lower()

        frases.append(f"Esta imagen es un {tipo_imagen} con un estilo {estilo}.")

        # 3) Propósito
        if params.get("proposito_categoria"):
            if "Otro" in params["proposito_categoria"]:
                proposito = params.get("proposito_personalizado", "un propósito no definido").lower()
                frases.append(f"Fue creada para {proposito}.")
            else:
                subcat = (
                    f", específicamente {params['proposito_subcategoria'].lower()}" 
                    if params.get("proposito_subcategoria") else ""
                )
                frases.append(f"Fue creada para {params['proposito_categoria'].lower()}{subcat}.")

        # 4) Características técnicas
        aspectos = []
        if params.get("iluminación"):
            aspectos.append(f"iluminación {params['iluminación'].lower()}")
        if params.get("plano"):
            aspectos.append(f"plano {params['plano'].lower()}")
        if params.get("composición"):
            aspectos.append(f"composición {params['composición'].lower()}")
        if params.get("resolución"):
            aspectos.append(f"resolución {params['resolución'].lower()}")
        if params.get("acabado"):
            aspectos.append(f"acabado {params['acabado'].lower()}")

        if aspectos:
            frases.append(f"Incluye detalles como {', '.join(aspectos)}.")

        return " ".join(frases)

    # Generar prompt
    prompt_generado = generar_prompt(params)

    # Layout de Pantalla 2
    st.title("Tu prompt está listo")

    # Área de Edición
    st.markdown("## Revisá y editá tus instrucciones")
    prompt_editado = st.text_area(
        "Podés ajustar el prompt generado:",
        value=prompt_generado,
        height=200
    )
    st.caption("Los cambios se guardan automáticamente al hacer clic fuera del cuadro.")

    # Área de Copiado
    st.markdown("---")
    st.markdown("## 📋 COPIÁ TU PROMPT")
    st.code(prompt_editado, language="")
    st.info("### ⬆️ CLICK EN EL ÍCONO DE COPIAR ⬆️\nMirá la esquina superior derecha del recuadro gris.")
    st.markdown("---")

    # Herramientas Recomendadas
    st.markdown("## Herramientas Recomendadas")
    st.markdown(
        """
        - **[DALL·E](https://openai.com/dall-e/)**: Creaciones artísticas y composiciones realistas basadas en IA de OpenAI.  
        - **[MidJourney](https://www.midjourney.com/)**: Reconocida por la alta calidad estética y detalles artísticos.  
        - **[Stable Diffusion](https://stability.ai/)**: Ideal para personalización y modificaciones detalladas de tu prompt, con gran comunidad open-source.  
        - **[Grok de Twitter](https://twitter.com/)**: Conectá tus imágenes con las tendencias actuales en redes sociales (opcional).  
        - **[Claude](https://www.anthropic.com/)**: Para mejorar prompts complejos e integrarlos con chatbots IA.  
        - **[Copilot](https://copilot.github.com/)**: Soporte creativo para generación rápida de contenido y prompts.
        """
    )

    # Traducción
    st.markdown("## ¿Necesitás el prompt en inglés?")
    st.markdown(
        """
        Muchas herramientas funcionan mejor con prompts en inglés. Si es tu caso, usá la traducción:
        1. Hacé clic en "Abrir Google Translate".
        2. El texto se cargará automáticamente.
        3. Copiá la traducción.
        """
    )
    # Codificar el prompt para URL (nativo de Python, sin librerías extra).
    text_encoded = prompt_editado.replace(" ", "%20")
    google_translate_url = f"https://translate.google.com/?sl=es&tl=en&text={text_encoded}"
    if st.button("Abrir Google Translate"):
        st.markdown(f"[Abrir Google Translate →]({google_translate_url})", unsafe_allow_html=True)

    # Instrucciones de Uso
    st.markdown("## Cómo usar tu prompt:")
    st.markdown(
        """
        1. Copiá el texto usando el ícono de arriba.
        2. Abrí la herramienta que prefieras en otra pestaña.
        3. Pegá el prompt donde dice "Describe la imagen...".
        4. ¡Generá tu imagen! (Si traducís, pegá el texto en inglés).
        """
    )

    # Botón para generar un nuevo prompt
    if st.button("Generar un nuevo prompt"):
        mostrar_pantalla1()

    st.markdown("---")
    st.markdown(
        """
        Trabajo final de un curso de IA. 
        Para cualquier feedback o consulta, escribí a [julietafantini@gmail.com](mailto:julietafantini@gmail.com).
        """
    )


if __name__ == "__main__":
    # Ejecución directa de pantalla2 (solo para pruebas)
    configurar_pantalla2(lambda: print("Pantalla 1 cargada."))
