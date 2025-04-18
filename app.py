
import streamlit as st
from PIL import Image
import random
import base64
import io

st.set_page_config(page_title="Guarda-Roupa Virtual", layout="centered")

# Estilo dark premium
st.markdown("""
<style>
body {
    background-color: #111;
    color: #f5f5f5;
}
h1, h2, h3 {
    color: #fff;
}
div.stButton > button {
    background-color: #6c5ce7;
    color: white;
    border-radius: 8px;
    padding: 0.6em 1.2em;
}
div.stButton > button:hover {
    background-color: #a29bfe;
}
.file-uploader, .uploadedFile {
    background-color: #222 !important;
}
.card {
    background-color: #1e1e1e;
    border-radius: 12px;
    padding: 16px;
    margin: 10px 0;
    box-shadow: 0 4px 14px rgba(255, 255, 255, 0.1);
}
</style>
""", unsafe_allow_html=True)

st.title("✨ Guarda-Roupa Virtual com IA (Dark Edition)")

if "roupas" not in st.session_state:
    st.session_state.roupas = []

def encode_img(img):
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return base64.b64encode(byte_im).decode()

def decode_img(encoded):
    byte_data = base64.b64decode(encoded)
    return Image.open(io.BytesIO(byte_data))

uploaded_file = st.file_uploader("Fotografe ou envie uma peça de roupa", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Peça enviada", use_container_width=True)

    st.markdown("### Resultado da IA (simulado):")

    filename = uploaded_file.name.lower()
    if "jaqueta" in filename or "53ac" in filename:
        roupa = {"tipo": "Jaqueta", "cor": "Azul Claro", "estilo": "Casual"}
    elif "short" in filename or "70e8" in filename:
        roupa = {"tipo": "Shorts", "cor": "Azul Médio", "estilo": "Casual"}
    elif "regata" in filename or "332a" in filename:
        roupa = {"tipo": "Regata", "cor": "Branco", "estilo": "Básico"}
    else:
        roupa = {"tipo": "Camiseta", "cor": "Preto", "estilo": "Urbano"}

    roupa["imagem"] = encode_img(image)

    st.write(f"**Tipo:** {roupa['tipo']}")
    st.write(f"**Cor:** {roupa['cor']}")
    st.write(f"**Estilo:** {roupa['estilo']}")

    if st.button("Salvar no guarda-roupa"):
        st.session_state.roupas.append(roupa)
        st.success("Peça adicionada com sucesso!")

if st.session_state.roupas:
    st.markdown("## 🧺 Guarda-Roupa Atual")
    for item in st.session_state.roupas:
        st.image(decode_img(item["imagem"]), width=250)
        st.markdown(f"<div class='card'><b>{item['tipo']}</b> – {item['cor']} · {item['estilo']}</div>", unsafe_allow_html=True)

    if st.button("👗 Gerar Look do Dia"):
        look = random.sample(st.session_state.roupas, k=min(2, len(st.session_state.roupas)))
        st.markdown("### ✨ Look do Dia Sugerido:")
        for item in look:
            st.image(decode_img(item["imagem"]), width=180)
            st.markdown(f"👉 {item['tipo']} {item['cor']} – {item['estilo']}")
