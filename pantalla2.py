import streamlit as st

def configurar_pantalla2(mostrar_pantalla1):
    """
    Configura los elementos y campos de la Pantalla 2.
    Genera un prompt basado en los datos ingresados en Pantalla 1 y permite su edición.
    También incluye recomendaciones de herramientas y un enlace para traducción.
    """
    if "params" not in st.session_state or not st.session_state.params:
        st.warning("No se han proporcionado datos desde Pantalla 1. Por favor, completá los campos obligatorios.")
        # Botón para generar un nuevo prompt
if st.button("Generar un nuevo prompt"):
    mostrar_pantalla1()

# Mensaje final
st.markdown("---")
st.markdown(
    """
    Trabajo final de un curso de IA. Para cualquier feedback o consulta, escribí a [julietafantini@gmail.com](mailto:julietafantini@gmail.com).
    """
)
            mostrar_pantalla1()
        return

    params = st.session_state.params

    # Generación del prompt
    def generar_prompt(params):
        """
        Genera un texto (prompt) a partir de los parámetros proporcionados.
        Estructurado en cuatro frases según lo definido.
        """
        frases = []

        # Primera Frase
        if params.get("idea_inicial"):
            frases.append(f"Imagina {params['idea_inicial']}.")

        # Segunda Frase
        tipo_imagen = params.get("tipo_de_imagen_personalizado", params["tipo_de_imagen"]) if "Otro" in params["tipo_de_imagen"] else params["tipo_de_imagen"]
        estilo = params.get("estilo_artístico_personalizado", params["estilo_artístico"]) if "Otro" in params["estilo_artístico"] else params["estilo_artístico"]
        frases.append(f"Esta imagen es un {tipo_imagen.lower()} con un estilo {estilo.lower()}.")

        # Tercera Frase
        if params.get("proposito_categoria"):
            if params.get("proposito_categoria") == "Otro":
                proposito = params.get("proposito_personalizado", "un propósito no definido").lower()
                frases.append(f"Fue creada para {proposito}.")
            else:
                subcat = f", específicamente {params['proposito_subcategoria'].lower()}" if params.get("proposito_subcategoria") else ""
                frases.append(f"Fue creada para {params['proposito_categoria'].lower()}{subcat}.")

        # Cuarta Frase
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

    prompt_generado = generar_prompt(params)

    # Pantalla principal
    st.title("Tu prompt está listo")

    # Área de Edición
    st.markdown("## Revisá y editá tu prompt")
    prompt_editado = st.text_area(
        "Podés ajustar el prompt generado:",
        value=prompt_generado,
        height=200
    )
    st.caption("Los cambios se guardan automáticamente al hacer clic fuera del cuadro.")

    # Área de Copiado
    st.markdown("---")
    st.markdown("## 📋 COPIÁ TU PROMPT")
    st.info("### ⬆️ CLICK EN EL ÍCONO DE COPIAR ⬆️\nMirá la esquina superior derecha del recuadro gris 👉")
    st.code(prompt_editado, language="")
    st.success("✅ Cuando copies el texto, verás una confirmación aquí")
    st.markdown("---")

    # Herramientas Recomendadas
    st.markdown("## Herramientas Recomendadas")
    st.markdown(
        """
        - **[DALL·E](https://openai.com/dall-e/)**: Herramienta de OpenAI para dibujar imágenes con inteligencia artificial.
          Permite creaciones artísticas y composiciones realistas, basada en modelos GPT.
        - **[MidJourney](https://www.midjourney.com/)**: Reconocida por su calidad artística y estética muy cuidada en las imágenes generadas.
        - **[Stable Diffusion](https://stability.ai/)**: Ideal para personalización y modificaciones detalladas de tu prompt.
        - **[Grok de Twitter](https://twitter.com/)**: Conectá tus imágenes con las tendencias más actuales en redes sociales.
        - **[Claude](https://www.anthropic.com/)**: Ideal para analizar y mejorar prompts complejos, integrándose con chatbots IA.
        - **[Copilot](https://copilot.github.com/)**: Soporte creativo para generación rápida y versátil de contenido y prompts.
        """
    )

    # Traducción
    st.markdown("## ¿Necesitás el prompt en inglés?")
    st.markdown(
        """
        Muchas herramientas funcionan mejor con prompts en inglés. Si es tu caso, usá la traducción.

        1. Hacé clic en "Abrir Google Translate".
        2. El texto se cargará automáticamente.
        3. Copiá la traducción.
        """
    )
    google_translate_url = f"https://translate.google.com/?sl=es&tl=en&text={prompt_editado.replace(' ', '%20')}"
    if st.button("Abrir Google Translate"):
        st.markdown(f"[Abrir Google Translate →]({google_translate_url})", unsafe_allow_html=True)

    # Instrucciones de Uso
    st.markdown("## Cómo usar tu prompt:")
    st.markdown(
        """
        1. Copiá el texto usando el ícono de arriba.
        2. Abrí la herramienta que prefieras en otra pestaña.
        3. Pegá el prompt donde dice "Describe la imagen...".
        4. ¡Generá tu imagen! Si utilizás el traductor, asegurate de pegar el texto traducido.
        """
    )

    
    st.markdown(
        """
        Trabajo final de un curso de IA. Para cualquier feedback o consulta, escribí a [julietafantini@gmail.com](mailto:julietafantini@gmail.com).
        """
    )

    # Botón para generar un nuevo prompt
    if st.button("Generar un nuevo prompt"):
        mostrar_pantalla1()

if __name__ == "__main__":
    configurar_pantalla2(lambda: print("Pantalla 1 cargada."))
