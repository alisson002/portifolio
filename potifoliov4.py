import streamlit as st
import streamlit.components.v1 as components
import base64
from pathlib import Path
import os

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
    iframe {border:none !important; height:100vh !important; min-height:100vh !important;}
    .stApp {overflow:hidden;}
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


def load_image_as_base64(path: str) -> str:
    """Converte imagem local para base64 para embed inline no HTML."""
    if os.path.exists(path):
        with open(path, "rb") as f:
            data = base64.b64encode(f.read()).decode("utf-8")
        ext = path.rsplit(".", 1)[-1].lower()
        mime = {"jpg": "jpeg", "jpeg": "jpeg", "png": "png", "webp": "webp"}.get(ext, "jpeg")
        return f"data:image/{mime};base64,{data}"
    # Placeholder SVG caso a foto não seja encontrada
    return (
        "data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTMwIiBoZWlnaHQ9IjEzMCIgeG1sbnM9"
        "Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cmVjdCB3aWR0aD0iMTMwIiBoZWlnaHQ9"
        "IjEzMCIgZmlsbD0iIzFlMjkzYiIvPjx0ZXh0IHg9IjUwJSIgeT0iNTAlIiBkb21pbmFudC1i"
        "YXNlbGluZT0ibWlkZGxlIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjQ4IiBm"
        "b250LWZhbWlseT0ic2Fucy1zZXJpZiIgZmlsbD0iIzQ3NTU2OSI+8J+RpDwvdGV4dD48L3N2Zz4="
    )


# ── Carrega a foto e injeta como base64 ──────────────────────────────────────
photo_src = load_image_as_base64("alisson.jpeg")

# ── Lê o HTML e substitui o src da foto ──────────────────────────────────────
with open("index.html", "r", encoding="utf-8") as f:
    html_data = f.read()

# Substitui o src relativo pelo base64
html_data = html_data.replace('src="alisson.jpeg"', f'src="{photo_src}"')

# Injeta script para forçar o sidebar a usar a altura real da viewport do iframe
resize_script = """
<script>
(function() {
    function adjustSidebar() {
        var aside = document.querySelector('aside');
        if (aside) {
            aside.style.height = window.innerHeight + 'px';
        }
    }
    window.addEventListener('resize', adjustSidebar);
    adjustSidebar();
})();
</script>
"""
html_data = html_data.replace("</body>", resize_script + "</body>")

components.html(html_data, height=20000, scrolling=True)

