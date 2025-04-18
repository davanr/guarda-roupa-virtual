
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Guarda-Roupa Virtual", layout="centered")

st.title("👗 Guarda-Roupa Virtual com IA")

st.markdown("Faça upload de uma peça de roupa para classificar automaticamente com IA (simulado).")

uploaded_file = st.file_uploader("Escolha uma imagem", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Peça enviada", use_column_width=True)

    st.markdown("### Resultado da IA (simulado):")

    filename = uploaded_file.name.lower()

    if "jaqueta" in filename or "53ac" in filename:
        st.write("**Tipo:** Jaqueta")
        st.write("**Cor:** Azul Claro")
        st.write("**Estilo:** Casual")
        st.write("**Tecido:** Jeans")

    elif "short" in filename or "70e8" in filename:
        st.write("**Tipo:** Shorts")
        st.write("**Cor:** Azul Médio")
        st.write("**Estilo:** Casual")
        st.write("**Tecido:** Jeans")

    elif "regata" in filename or "332a" in filename:
        st.write("**Tipo:** Regata")
        st.write("**Cor:** Branco")
        st.write("**Estilo:** Básico")
        st.write("**Tecido:** Algodão")

    else:
        st.write("**Tipo:** Não identificado")
        st.write("**Cor:** —")
        st.write("**Estilo:** —")
        st.write("**Tecido:** —")

    st.success("Peça classificada! Você pode salvar no seu guarda-roupa.")
