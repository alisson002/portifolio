import streamlit as st
from pathlib import Path

# ============================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================
st.set_page_config(
    page_title="Portfólio | Alisson Moreira",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# TEMA
# ============================================================
if "tema" not in st.session_state:
    st.session_state.tema = "escuro"


def alternar_tema():
    st.session_state.tema = "claro" if st.session_state.tema == "escuro" else "escuro"


ESCURO = st.session_state.tema == "escuro"

if ESCURO:
    BG = "#06101b"
    BG_CARD = "#0f1d32"
    BORDER = "#1e293b"
    TEXT = "#e2e8f0"
    TEXT_SUB = "#94a3b8"
    ACCENT = "#0077D4"
    GREEN = "#059669"
    TAG_BG = "#1e293b"
    TAG_TEXT = "#94a3b8"
    PREVIEW_REPO = "#131c30"
    PREVIEW_DASH = "#0b1f1a"
else:
    BG = "#F8FAFC"
    BG_CARD = "#ffffff"
    BORDER = "#e2e8f0"
    TEXT = "#06101b"
    TEXT_SUB = "#757491"
    ACCENT = "#0077D4"
    GREEN = "#059669"
    TAG_BG = "#e2e8f0"
    TAG_TEXT = "#475569"
    PREVIEW_REPO = "#e8f0fe"
    PREVIEW_DASH = "#ecfdf5"

# ============================================================
# CSS (apenas visual, não estrutural)
# ============================================================
st.markdown(f"""
<style>
    
    

    .stApp {{
        background: {BG};
    }}
    .block-container {{
        padding: 2rem 3rem 3rem !important;
        max-width: 100% !important;
    }}

    /* ── Sidebar: fundo e largura ── */
    section[data-testid="stSidebar"] {{
        background: #06101b !important;
        min-width: 280px !important;
        max-width: 280px !important;
    }}
    section[data-testid="stSidebar"] [data-testid="stSidebarContent"] {{
        padding-top: 2rem !important;
    }}

    /* Sidebar textos */
    section[data-testid="stSidebar"] .stMarkdown p,
    section[data-testid="stSidebar"] .stMarkdown span,
    section[data-testid="stSidebar"] .stCaption p {{
        color: #94a3b8 !important;
    }}
    section[data-testid="stSidebar"] hr {{
        border-color: #1e293b !important;
        margin: 0.75rem 0 !important;
    }}

    /* Sidebar: nome (header = h2) */
    section[data-testid="stSidebar"] .stMarkdown h2 {{
        color: {ACCENT} !important;
        font-size: 1.35rem !important;
        font-weight: 800 !important;
        text-align: center !important;
        font-family: 'Manrope', sans-serif !important;
        margin-bottom: 0 !important;
        padding-bottom: 0 !important;
    }}

    /* Sidebar: cargo (caption) centralizado */
    section[data-testid="stSidebar"] .stCaption {{
        text-align: center !important;
    }}
    section[data-testid="stSidebar"] .stCaption p {{
        font-size: 0.7rem !important;
        font-weight: 600 !important;
        letter-spacing: 2px !important;
        text-transform: uppercase !important;
        text-align: center !important;
    }}

    /* Sidebar: foto circular */
    section[data-testid="stSidebar"] .stImage img {{
        border-radius: 50% !important;
        border: 4px solid {ACCENT} !important;
        box-shadow: 0 4px 20px rgba(0,119,212,0.3) !important;
        width: 130px !important;
        height: 130px !important;
        object-fit: cover !important;
        display: block !important;
        margin: 0 auto !important;
    }}

    /* Sidebar: botões de navegação */
    section[data-testid="stSidebar"] .stButton button {{
        background: transparent !important;
        color: #94a3b8 !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.65rem 1rem !important;
        width: 100% !important;
        justify-content: flex-start !important;
        font-size: 0.9rem !important;
        transition: all 0.2s !important;
    }}
    section[data-testid="stSidebar"] .stButton button:hover {{
        background: rgba(0,119,212,0.1) !important;
        color: #e2e8f0 !important;
    }}
    section[data-testid="stSidebar"] .stButton button[kind="primary"] {{
        background: rgba(0,119,212,0.15) !important;
        color: #7cc4ff !important;
        font-weight: 600 !important;
    }}

    /* Sidebar: link_buttons (GitHub, LinkedIn, Email) */
    section[data-testid="stSidebar"] .stLinkButton a {{
        background: #0d2847 !important;
        border: 1px solid #1a3a5c !important;
        color: #94a3b8 !important;
        border-radius: 8px !important;
        padding: 0.6rem 1rem !important;
        width: 100% !important;
        justify-content: flex-start !important;
        font-size: 0.85rem !important;
        transition: all 0.25s !important;
    }}
    section[data-testid="stSidebar"] .stLinkButton a:hover {{
        background: {ACCENT} !important;
        color: #ffffff !important;
        border-color: {ACCENT} !important;
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(0,119,212,0.3);
    }}

    /* Sidebar: esconde o botão de fechar/colapsar padrão */
    section[data-testid="stSidebar"] button[data-testid="stBaseButton-headerNoPadding"] {{
        display: none !important;
    }}

    /* Main text colors */
    .stMarkdown p, .stMarkdown span, .stMarkdown li {{
        color: {TEXT_SUB};
    }}
    .stMarkdown h3 {{
        color: {TEXT} !important;
    }}

    /* Card containers */
    div[data-testid="stContainer"] {{
        background: {BG_CARD};
        border: 1px solid {BORDER};
        border-radius: 12px;
        padding: 0 !important;
        transition: all 0.3s;
    }}
    div[data-testid="stContainer"]:hover {{
        transform: translateY(-4px);
        box-shadow: 0 8px 30px {"rgba(0,119,212,0.1)" if ESCURO else "rgba(0,0,0,0.08)"};
    }}

    /* Tags */
    .tag-pill {{
        background: {TAG_BG};
        color: {TAG_TEXT};
        padding: 4px 12px;
        border-radius: 4px;
        font-size: 0.6rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        display: inline-block;
    }}

    /* Footer */
    .portfolio-footer {{
        text-align: center;
        padding: 2rem 0;
        border-top: 1px solid {BORDER};
        color: {TEXT_SUB};
        font-size: 0.75rem;
        letter-spacing: 1px;
        margin-top: 2rem;
    }}
</style>
""", unsafe_allow_html=True)


# ============================================================
# SIDEBAR
# ============================================================
with st.sidebar:
    # Foto
    photo_path = Path("alisson.jpeg")
    if photo_path.exists():
        st.image(str(photo_path))

    # Nome e cargo
    st.header("Alisson Moreira")
    st.caption("Analista de Dados")

    st.divider()

    # Navegação
    st.button("📊  Portfólio", key="nav_portfolio", type="primary", use_container_width=True)
    st.button("👤  Sobre Mim", key="nav_sobre", use_container_width=True)

    st.divider()

    # Links como botões
    st.link_button("💻  GitHub", "https://github.com/alisson002", use_container_width=True)
    st.link_button("🔗  LinkedIn", "https://linkedin.com/in/seu-perfil", use_container_width=True)
    st.link_button("📧  am.analistadedados@gmail.com", "mailto:am.analistadedados@gmail.com", use_container_width=True)


# ============================================================
# HELPER – renderizar projeto
# ============================================================
def render_project(
    title: str,
    tags: list[str],
    repo_name: str,
    repo_desc: str,
    repo_url: str,
    dash_name: str,
    dash_desc: str,
    dash_url: str,
):
    # Header: título + tags
    tags_html = " ".join(f'<span class="tag-pill">{t}</span>' for t in tags)
    header_col, tags_col = st.columns([3, 2])
    with header_col:
        st.subheader(title)
    with tags_col:
        st.markdown(
            f"<div style='text-align:right;padding-top:0.5rem;'>{tags_html}</div>",
            unsafe_allow_html=True,
        )

    st.divider()

    # Cards
    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.markdown(
                f"<div style='background:{PREVIEW_REPO};height:180px;display:flex;"
                f"align-items:center;justify-content:center;font-size:3rem;"
                f"border-radius:8px;margin-bottom:1rem;'>💻</div>",
                unsafe_allow_html=True,
            )
            st.markdown(f"<small style='color:{ACCENT};font-weight:700;"
                        f"letter-spacing:2px;font-size:0.65rem;'>📂 REPOSITORIO GIT</small>",
                        unsafe_allow_html=True)
            st.markdown(f"**{repo_name}**")
            st.caption(repo_desc)
            st.link_button("Ver codigo-fonte →", repo_url)

    with col2:
        with st.container(border=True):
            st.markdown(
                f"<div style='background:{PREVIEW_DASH};height:180px;display:flex;"
                f"align-items:center;justify-content:center;font-size:3rem;"
                f"border-radius:8px;margin-bottom:1rem;'>📊</div>",
                unsafe_allow_html=True,
            )
            st.markdown(f"<small style='color:{GREEN};font-weight:700;"
                        f"letter-spacing:2px;font-size:0.65rem;'>📈 DASHBOARD AO VIVO</small>",
                        unsafe_allow_html=True)
            st.markdown(f"**{dash_name}**")
            st.caption(dash_desc)
            st.link_button("Abrir dashboard ↗", dash_url)

    st.write("")


# ============================================================
# BOTÃO DE TEMA
# ============================================================
_, tema_col = st.columns([10, 1])
with tema_col:
    icon = "☀️" if ESCURO else "🌙"
    st.button(icon, on_click=alternar_tema, key="tema_btn")

# ============================================================
# CONTEÚDO PRINCIPAL
# ============================================================

render_project(
    title="Analise de Vendas - Forecasting",
    tags=["Python", "Pandas"],
    repo_name="Tratamento de Dados",
    repo_desc="Pipeline completo de limpeza, transformacao e feature engineering para previsao de vendas com decomposicao sazonal.",
    repo_url="https://github.com/seu-usuario/projeto-vendas",
    dash_name="Dashboard Interativa",
    dash_desc="Painel executivo com drill-down por regiao, periodo e categoria de produto com intervalos de confianca.",
    dash_url="https://seu-app.streamlit.app",
)

render_project(
    title="Analise de Sentimentos - NLP",
    tags=["NLP", "Transformers", "Scikit-learn"],
    repo_name="Modelo e Scraping",
    repo_desc="Modelo BERT fine-tuned para classificacao multiclasse de avaliacoes de clientes em 4 categorias de produto.",
    repo_url="https://github.com/seu-usuario/projeto-sentimentos",
    dash_name="Painel de Insights",
    dash_desc="Visualizacao de tendencias emocionais e nuvem de palavras para orientar estrategias de marketing.",
    dash_url="https://seu-app-sentimentos.streamlit.app",
)

render_project(
    title="Analise de teste",
    tags=["NLP", "Transformers", "Scikit-learn"],
    repo_name="teste",
    repo_desc="sdfjhsdkfjhksjdfhjshdfsdf dsfdsfsd f sdfsdfsdfsdfsd.",
    repo_url="https://github.com/seu-usuario/projeto-sentimentos",
    dash_name="Painel de Insights",
    dash_desc="Visualizacao de tendencias emocionais e nuvem de palavras para orientar estrategias de marketing.",
    dash_url="https://seu-app-sentimentos.streamlit.app",
)

# ============================================================
# FOOTER
# ============================================================
st.divider()
st.caption("© 2026 Alisson Moreira · Portfólio de Analista de Dados")
