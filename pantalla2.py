import streamlit as st

def configurar_pantalla2(mostrar_pantalla1):
    """
    Pantalla exhaustiva para generar, editar y copiar el prompt.
    Incluye traducción a inglés con un solo botón (sin duplicaciones).
    """
    if "params" not in st.session_state or not st.session_state.params.get("idea_inicial"):
        st.warning("No se han proporcionado datos válidos desde la Pantalla 1.")
        if st.button("Volver a Pantalla 1"):
            mostrar_pantalla1()
        return

    params = st.session_state.params

    # Función local para generar el prompt de manera "exhaustiva"
    def generar_prompt(params):
        """
        Crea un texto final combinando la idea inicial, tipo de imagen, propósito, 
        estilo y características técnicas.
        """
        frases = []

        # (1) Idea Inicial
        idea = params["idea_inicial"].strip()
        if idea:
            frases.append(f"Imaginá {idea}.")

        # (2) Tipo de Imagen + Estilo Artístico
        if "Otro" in params["tipo_imagen"]:
            tipo = params.get("tipo_imagen_personalizado", "").strip()
        else:
            tipo = params["tipo_imagen"]

        if "Otro" in params["estilo_artistico"]:
            estilo = params.get("estilo_artistico_personalizado", "").strip()
        else:
            estilo = params["estilo_artistico"]

        if tipo and estilo:
            frases.append(f"Se trata de un {tipo.lower()} con un estilo {estilo.lower()}.")
        elif tipo:
            frases.append(f"Se trata de un {tipo.lower()}.")

        # (3) Propósito
        proposito_cat = params.get("proposito_categoria")
        subcat = params.get("proposito_subcategoria", "")
        if "Otro" in proposito_cat:
            proposito_personalizado = params.get("proposito_personalizado", "").strip()
            if proposito_personalizado:
                frases.append(f"Fue creada para {proposito_personalizado.lower()}.")
        else:
            if subcat:
                frases.append(f"Fue creada para {proposito_cat.lower()}, específicamente {subcat.lower()}.")
            else:
                # Por si no hay subcategoría
                frases.append(f"Fue creada para {proposito_cat.lower()}.")

        # (4) Características Técnicas
        iluminacion = params.get("iluminacion", "").lower()
        plano = params.get("plano", "").lower()
        composicion = params.get("composicion", "").lower()
        resolucion = params.get("resolucion", "").lower()
        acabado = params.get("acabado", "").lower()

        detalles = []
        if iluminacion:   detalles.append(f"iluminación {iluminacion}")
        if plano:         detalles.append(f"plano {plano}")
        if composicion:   detalles.append(f"composición {composicion}")
        if resolucion:    detalles.append(f"resolución {resolucion}")
        if acabado:       detalles.append(f"acabado {acabado}")

        if detalles:
            frases.append("Incluye detalles como " + ", ".join(detalles) + ".")

        # Unir todo en un solo texto
        prompt_final = " ".join(frases)
        return prompt_final.strip()

    # Generar prompt
    prompt_inicial = generar_prompt(params)

    # Sección principal de Pantalla 2
    st.title("Tu prompt está listo")
    st.markdown("Podés revisarlo y ajustarlo antes de copiarlo:")

    # Área de edición
    prompt_editado = st.text_area("Editá tu prompt", value=prompt_inicial, height=200)

    # Copiar prompt
    st.markdown("## Copiá tu prompt")
    st.code(prompt_editado, language="")
    st.info("Hacé click en el ícono (arriba a la derecha) para copiar el texto.")

    # Traducción a inglés (un solo botón)
    st.markdown("## ¿Necesitás traducirlo al inglés?")
    text_encoded = prompt_editado.replace(" ", "%20")
    translate_url = f"https://translate.google.com/?sl=es&tl=en&text={text_encoded}"
    if st.button("Abrir Google Translate"):
        st.markdown(f"[Abrir Google Translate →]({translate_url})", unsafe_allow_html=True)

    # Botón para volver a Pantalla 1
    if st.button("Generar un nuevo prompt"):
        mostrar_pantalla1()

    # Footer
    st.markdown("---")
    st.markdown(
        """
        Trabajo final de un curso de IA. 
        Para cualquier feedback o consulta, escribí a [julietafantini@gmail.com](mailto:julietafantini@gmail.com).
        """
    )
