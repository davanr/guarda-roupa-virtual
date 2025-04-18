
import streamlit as st
from PIL import Image
import random

st.set_page_config(page_title="Guarda-Roupa Virtual", layout="centered")

st.markdown("""
<style>
    .title {
        font-size: 40px;
        font-weight: 600;
        color: #2c3e50;
        text-align: center;
        font-family: 'Segoe UI', sans-serif;
    }
    .subtitle {
        font-size: 20px;
        color: #7f8c8d;
        text-align: center;
        margin-bottom: 30px;
    }
    .card {
        border-radius: 16px;
        padding: 20px;
        background-color: #f8f9fa;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">👗 Guarda-Roupa Virtual</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Organize suas roupas com inteligência e estilo</div>', unsafe_allow_html=True)

if "roupas" not in st.session_state:
    st.session_state.roupas = []

uploaded_file = st.file_uploader("Fotografe ou envie uma peça de roupa", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Peça enviada", use_column_width=True)

    st.markdown("### Resultado da IA (simulado):")

    filename = uploaded_file.name.lower()
    if "jaqueta" in filename or "53ac" in filename:
        roupa = {"tipo": "Jaqueta", "cor": "Azul Claro", "estilo": "Casual", "imagem": uploaded_file}
    elif "short" in filename or "70e8" in filename:
        roupa = {"tipo": "Shorts", "cor": "Azul Médio", "estilo": "Casual", "imagem": uploaded_file}
    elif "regata" in filename or "332a" in filename:
        roupa = {"tipo": "Regata", "cor": "Branco", "estilo": "Básico", "imagem": uploaded_file}
    else:
        roupa = {"tipo": "Camiseta", "cor": "Preto", "estilo": "Urbano", "imagem": uploaded_file}

    st.write(f"**Tipo:** {roupa['tipo']}")
    st.write(f"**Cor:** {roupa['cor']}")
    st.write(f"**Estilo:** {roupa['estilo']}")

    if st.button("Salvar no guarda-roupa"):
        st.session_state.roupas.append(roupa)
        st.success("Peça adicionada com sucesso!")

if st.session_state.roupas:
    st.markdown("## 🧺 Guarda-Roupa Atual")
    for item in st.session_state.roupas:
        st.image(item["imagem"], width=200)
        st.markdown(f"<div class='card'><b>{item['tipo']}</b> – {item['cor']} · {item['estilo']}</div>", unsafe_allow_html=True)

    if st.button("👗 Gerar Look do Dia"):
        look = random.sample(st.session_state.roupas, k=min(2, len(st.session_state.roupas)))
        st.markdown("### ✨ Look do Dia Sugerido:")
        for item in look:
            st.image(item["imagem"], width=150)
            st.markdown(f"👉 {item['tipo']} {item['cor']} – {item['estilo']}")
