import streamlit as st
import streamlit.components.v1 as components
import base64
from pathlib import Path

# ============================================================
# CONFIGURACAO DA PAGINA
# ============================================================

st.set_page_config(
    page_title="Portfólio | Alisson Moreira",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Hide Streamlit default UI — the HTML page IS the entire app
st.markdown("""
<style>
    MainMenu {visibility:hidden;}
    header {visibility:hidden;}
    footer {visibility:hidden;}
    .stApp > div:first-child {padding:0;}
    .block-container {padding:0 !important; max-width:100% !important;}
    iframe {border:none !important;}
</style>
""", unsafe_allow_html=True)
# ============================================================
# ESTADO DA SESSAO
# ============================================================

if "tema" not in st.session_state:
    st.session_state.tema = "escuro"
if "pagina" not in st.session_state:
    st.session_state.pagina = "portfolio"

ESCURO = st.session_state.tema == "escuro"


# Caminho para o seu arquivo HTML
path_to_html = "sobre.html"

# Ler o arquivo HTML
with open(path_to_html, 'r', encoding='utf-8') as f:
    html_data = f.read()

# Exibir o HTML no app
components.html(html_data, height=900, scrolling=True)

