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

# ============================================================
# ESTADO DA SESSAO
# ============================================================

if "tema" not in st.session_state:
    st.session_state.tema = "escuro"
if "pagina" not in st.session_state:
    st.session_state.pagina = "portfolio"

ESCURO = st.session_state.tema == "escuro"


# ============================================================
# PALETA DE CORES POR TEMA
# ============================================================

if ESCURO:
    C = {
        "app_bg":           "#06101b",
        "sidebar_bg":       "#06101b",
        "sidebar_border":   "#1e293b",
        "sidebar_text":     "#94a3b8",
        "sidebar_text_h":   "#e2e8f0",
        "titulo":           "#f1f5f9",
        "texto":            "#cbd5e1",
        "desc":             "#94a3b8",
        "card_bg":          "#0f1d32",
        "card_border":      "#1e293b",
        "card_shadow":      "rgba(0,119,212,0.1)",
        "card_nome":        "#f1f5f9",
        "tag_bg":           "#1e293b",
        "tag_cor":          "#94a3b8",
        "header_border":    "#1e293b",
        "ph_repo":          "#0d1b2e",
        "ph_dash":          "#0b1e1a",
        "dash_border":      "rgba(0,119,212,0.25)",
        "rodape_border":    "#1e293b",
        "rodape_cor":       "#64748b",
        "about_card_bg":    "#0f1d32",
        "about_card_border":"#1e293b",
        "skill_bg":         "#06101b",
        "skill_border":     "#1e293b",
        "skill_cor":        "#94a3b8",
        "contact_bg":       "#06101b",
        "contact_border":   "#1e293b",
        "contact_valor":    "#e2e8f0",
    }
else:
    C = {
        "app_bg":           "#F8FAFC",
        "sidebar_bg":       "#06101b",
        "sidebar_border":   "#1e293b",
        "sidebar_text":     "#94a3b8",
        "sidebar_text_h":   "#e2e8f0",
        "titulo":           "#06101b",
        "texto":            "#475569",
        "desc":             "#757491",
        "card_bg":          "#ffffff",
        "card_border":      "#e2e8f0",
        "card_shadow":      "rgba(0,0,0,0.08)",
        "card_nome":        "#06101b",
        "tag_bg":           "#e2e8f0",
        "tag_cor":          "#475569",
        "header_border":    "#e2e8f0",
        "ph_repo":          "#e8f0fe",
        "ph_dash":          "#ecfdf5",
        "dash_border":      "rgba(0,119,212,0.15)",
        "rodape_border":    "#e2e8f0",
        "rodape_cor":       "#757491",
        "about_card_bg":    "#ffffff",
        "about_card_border":"#e2e8f0",
        "skill_bg":         "#F8FAFC",
        "skill_border":     "#e2e8f0",
        "skill_cor":        "#475569",
        "contact_bg":       "#F8FAFC",
        "contact_border":   "#e2e8f0",
        "contact_valor":    "#06101b",
    }

AZUL = "#0077D4"


# ============================================================
# CSS GLOBAL
# ============================================================

css = f"""
<style>
    /* --- Esconder UI padrao do Streamlit --- */
    #MainMenu, header, footer {{visibility: hidden;}}
    .stDeployButton {{display: none;}}

    /* --- Fundo geral --- */
    .stApp {{ background-color: {C["app_bg"]}; }}

    /* --- Sidebar --- */
    section[data-testid="stSidebar"] {{
        background-color: {C["sidebar_bg"]};
        padding-top: 0.5rem;
    }}
    section[data-testid="stSidebar"] * {{
        color: {C["sidebar_text"]} !important;
    }}
    section[data-testid="stSidebar"] hr {{
        border-color: {C["sidebar_border"]};
    }}

    /* --- Foto perfil --- */
    .foto-perfil {{
        display: block;
        margin: 0 auto 1rem auto;
        width: 130px; height: 130px;
        border-radius: 50%;
        object-fit: cover;
        border: 4px solid {AZUL};
        box-shadow: 0 4px 20px rgba(0,119,212,0.3);
    }}

    /* --- Nome sidebar --- */
    .sb-nome {{
        text-align: center;
        font-size: 1.35rem;
        font-weight: 800;
        color: {AZUL} !important;
        margin-bottom: 0.15rem;
        font-family: 'Segoe UI', sans-serif;
    }}
    .sb-cargo {{
        text-align: center;
        font-size: 0.7rem;
        font-weight: 600;
        color: {C["sidebar_text"]} !important;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 1rem;
    }}

    /* --- Botoes de navegacao na sidebar --- */
    section[data-testid="stSidebar"] .nav-btns button {{
        background: rgba(255,255,255,0.03) !important;
        border: 1px solid {C["sidebar_border"]} !important;
        border-radius: 10px !important;
        color: {C["sidebar_text"]} !important;
        font-weight: 500 !important;
        font-size: 0.85rem !important;
        padding: 0.6rem 0.5rem !important;
        transition: all 0.25s !important;
        cursor: pointer !important;
    }}
    section[data-testid="stSidebar"] .nav-btns button:hover {{
        background: rgba(0,119,212,0.12) !important;
        border-color: {AZUL} !important;
        color: #7cc4ff !important;
        transform: translateY(-1px);
    }}
    section[data-testid="stSidebar"] .nav-btns button:focus {{
        box-shadow: 0 0 0 2px rgba(0,119,212,0.3) !important;
    }}
    /* Botao ativo */
    section[data-testid="stSidebar"] .nav-btns .active-btn button {{
        background: rgba(0,119,212,0.18) !important;
        border-color: {AZUL} !important;
        color: #7cc4ff !important;
        font-weight: 600 !important;
    }}
    /* Reduzir espaco interno dos botoes nav */
    section[data-testid="stSidebar"] .nav-btns .stHorizontalBlock {{
        gap: 0.5rem !important;
    }}
    section[data-testid="stSidebar"] .nav-btns,
    section[data-testid="stSidebar"] .nav-btns > div {{
        margin-top: -0.5rem !important;
        margin-bottom: -0.5rem !important;
    }}

    /* --- Bottom links sidebar --- */
    .sb-bottom {{
        border-top: 1px solid {C["sidebar_border"]};
        padding-top: 0.75rem;
        margin-top: 0.5rem;
    }}
    .sb-bottom a, .sb-bottom .sb-email-btn {{
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 0.45rem 1rem;
        border-radius: 8px;
        color: {C["sidebar_text"]} !important;
        text-decoration: none;
        font-size: 0.8rem;
        transition: all 0.2s;
        cursor: pointer;
        border: none;
        background: none;
        font-family: inherit;
        width: 100%;
        position: relative;
    }}
    .sb-bottom a:hover, .sb-bottom .sb-email-btn:hover {{
        color: {AZUL} !important;
        background: rgba(0,119,212,0.08);
    }}

    /* --- Projeto header --- */
    .pj-header {{
        display: flex;
        justify-content: space-between;
        align-items: flex-end;
        border-bottom: 2px solid {C["header_border"]};
        padding-bottom: 0.75rem;
        margin-bottom: 1.25rem;
        margin-top: 1.5rem;
    }}
    .pj-titulo {{
        font-size: 1.5rem;
        font-weight: 700;
        color: {C["titulo"]};
        font-family: 'Segoe UI', sans-serif;
    }}
    .pj-tags {{ display: flex; gap: 0.5rem; }}
    .tag {{
        background: {C["tag_bg"]};
        color: {C["tag_cor"]};
        padding: 4px 12px;
        border-radius: 4px;
        font-size: 0.6rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
    }}

    /* --- Colunas de igual altura --- */
    div[data-testid="stHorizontalBlock"] {{
        align-items: stretch !important;
    }}
    div[data-testid="stColumn"] > div,
    div[data-testid="stColumn"] > div > div,
    div[data-testid="stColumn"] > div > div > div,
    div[data-testid="stColumn"] > div > div > div > div,
    div[data-testid="stColumn"] > div > div > div > div > div {{
        height: 100% !important;
    }}

    /* --- Card wrapper --- */
    .card-w {{
        display: block;
        height: 100%;
        text-decoration: none !important;
        color: inherit !important;
    }}
    .card-w *, .card-w:hover {{ text-decoration: none !important; }}

    /* --- Cards --- */
    .card {{
        background: {C["card_bg"]};
        border-radius: 12px;
        overflow: hidden;
        border: 1px solid {C["card_border"]};
        transition: all 0.3s;
        height: 100%;
        display: flex;
        flex-direction: column;
    }}
    .card:hover {{
        box-shadow: 0 8px 30px {C["card_shadow"]};
        transform: translateY(-4px);
    }}
    .card.dash {{ border-color: {C["dash_border"]}; }}

    .card-ph {{
        width: 100%; height: 200px;
        display: flex; align-items: center; justify-content: center;
        font-size: 3rem;
    }}
    .card-body {{
        padding: 1.25rem 1.5rem;
        flex: 1;
        display: flex;
        flex-direction: column;
    }}
    .card-label {{
        font-size: 0.65rem;
        font-weight: 700;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 0.4rem;
    }}
    .card-label.repo {{ color: {AZUL}; }}
    .card-label.dsh {{ color: #059669; }}
    .card-nome {{
        font-size: 1.15rem;
        font-weight: 700;
        color: {C["card_nome"]};
        margin-bottom: 0.5rem;
    }}
    .card-desc {{
        font-size: 0.85rem;
        color: {C["desc"]};
        line-height: 1.6;
        flex: 1;
    }}
    .card-link {{
        display: inline-flex;
        align-items: center;
        gap: 6px;
        color: {AZUL};
        font-size: 0.85rem;
        font-weight: 600;
        margin-top: 1rem;
    }}

    /* --- Rodape --- */
    .rodape {{
        text-align: center;
        padding: 2rem 0;
        margin-top: 3rem;
        border-top: 1px solid {C["rodape_border"]};
        color: {C["rodape_cor"]};
        font-size: 0.75rem;
        letter-spacing: 1px;
    }}

    /* --- Sobre mim --- */
    .about-card {{
        background: {C["about_card_bg"]};
        border: 1px solid {C["about_card_border"]};
        border-radius: 16px;
        padding: 2rem 2.25rem;
        margin-bottom: 1.5rem;
    }}
    .about-card h3 {{
        font-size: 1.1rem;
        font-weight: 700;
        color: {C["titulo"]};
        margin-bottom: 0.75rem;
    }}
    .about-text {{
        font-size: 0.95rem;
        line-height: 1.8;
        color: {C["texto"]};
        text-align: justify;
        hyphens: auto;
    }}
    .about-text strong {{ color: {C["titulo"]}; }}

    .about-label {{
        color: {AZUL};
        font-size: 0.7rem;
        font-weight: 700;
        letter-spacing: 3px;
        text-transform: uppercase;
        margin-bottom: 0.5rem;
    }}
    .about-title {{
        font-size: 2.2rem;
        font-weight: 800;
        color: {C["titulo"]};
        margin-bottom: 2rem;
        font-family: 'Segoe UI', sans-serif;
    }}

    .skills-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(110px, 1fr));
        gap: 0.6rem;
        margin-top: 0.75rem;
    }}
    .skill {{
        background: {C["skill_bg"]};
        border: 1px solid {C["skill_border"]};
        border-radius: 8px;
        padding: 0.65rem 0.75rem;
        text-align: center;
        font-size: 0.78rem;
        font-weight: 600;
        color: {C["skill_cor"]};
        transition: all 0.2s;
    }}
    .skill:hover {{
        border-color: {AZUL};
        color: {AZUL};
        transform: translateY(-2px);
    }}

    .ct-list {{ display: flex; flex-direction: column; gap: 0.6rem; margin-top: 0.75rem; }}
    .ct-item {{
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 0.75rem 1rem;
        border-radius: 10px;
        background: {C["contact_bg"]};
        border: 1px solid {C["contact_border"]};
        transition: all 0.2s;
        text-decoration: none !important;
        color: inherit;
        position: relative;
    }}
    .ct-item:hover {{
        border-color: {AZUL};
        transform: translateX(4px);
    }}
    .ct-icon {{
        width: 36px; height: 36px;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        font-size: 1.1rem;
    }}
    .ct-icon.em {{ background: rgba(0,119,212,0.1); }}
    .ct-icon.gh {{ background: rgba(71,85,105,0.1); }}
    .ct-icon.li {{ background: rgba(10,102,194,0.1); }}
    .ct-icon.lo {{ background: rgba(239,68,68,0.08); }}
    .ct-info {{ display: flex; flex-direction: column; }}
    .ct-lbl {{
        font-size: 0.6rem; font-weight: 600;
        text-transform: uppercase; letter-spacing: 1px;
        color: #757491; margin-bottom: 1px;
    }}
    .ct-val {{
        font-size: 0.88rem; font-weight: 500;
        color: {C["contact_valor"]};
    }}
</style>
"""

st.markdown(css, unsafe_allow_html=True)


# ============================================================
# DADOS DOS PROJETOS
# ============================================================

PROJETOS = [
    {
        "titulo": "Análise de Vendas - Forecasting",
        "tags": ["Python", "Pandas"],
        "repo_nome": "Tratamento de Dados",
        "repo_desc": "Pipeline completo de limpeza, transformação e feature engineering para previsão de vendas com decomposição sazonal.",
        "repo_url": "https://github.com/seu-usuario/projeto-vendas",
        "repo_img": None,
        "dash_nome": "Dashboard Interativa",
        "dash_desc": "Painel executivo com drill-down por região, período e categoria de produto com intervalos de confiança.",
        "dash_url": "https://seu-app.streamlit.app",
        "dash_img": None,
    },
    {
        "titulo": "Análise de Sentimentos - NLP",
        "tags": ["NLP", "Transformers", "Scikit-learn"],
        "repo_nome": "Modelo e Scraping",
        "repo_desc": "Modelo BERT fine-tuned para classificação multiclasse de avaliações de clientes em 4 categorias de produto.",
        "repo_url": "https://github.com/seu-usuario/projeto-sentimentos",
        "repo_img": None,
        "dash_nome": "Painel de Insights",
        "dash_desc": "Visualização de tendências emocionais e nuvem de palavras para orientar estratégias de marketing.",
        "dash_url": "https://seu-app-sentimentos.streamlit.app",
        "dash_img": None,
    },
    {
        "titulo": "Análise de teste",
        "tags": ["NLP", "Transformers", "Scikit-learn"],
        "repo_nome": "teste",
        "repo_desc": "sdfjhsdkfjhksjdfhjshdfsdf dsfdsfsd f sdfsdfsdfsdfsd .",
        "repo_url": "https://github.com/seu-usuario/projeto-sentimentos",
        "repo_img": None,
        "dash_nome": "Painel de Insights",
        "dash_desc": "Visualização de tendências emocionais e nuvem de palavras para orientar estratégias de marketing.",
        "dash_url": "https://seu-app-sentimentos.streamlit.app",
        "dash_img": None,
    },
]


# ============================================================
# FUNCOES AUXILIARES
# ============================================================

def img_b64(caminho: str) -> str:
    dados = Path(caminho).read_bytes()
    return base64.b64encode(dados).decode()


def foto_perfil_html() -> str:
    caminho = Path(__file__).parent / "alisson.jpeg"
    if caminho.exists():
        b64 = img_b64(str(caminho))
        return f'<img class="foto-perfil" src="data:image/jpeg;base64,{b64}" alt="Foto de perfil">'
    return '<div style="width:130px;height:130px;border-radius:50%;background:#475569;margin:0 auto 1rem auto;"></div>'


def card_repo(p: dict) -> str:
    img = ""
    if p["repo_img"]:
        src = p["repo_img"] if p["repo_img"].startswith("http") else f"data:image/png;base64,{img_b64(p['repo_img'])}"
        img = f'<img style="width:100%;height:200px;object-fit:cover;display:block;" src="{src}">'
    else:
        img = f'<div class="card-ph" style="background:{C["ph_repo"]};">💻</div>'
    return f"""
    <a href="{p["repo_url"]}" target="_blank" class="card-w">
        <div class="card">
            {img}
            <div class="card-body">
                <div class="card-label repo">📂 Repositório Git</div>
                <div class="card-nome">{p["repo_nome"]}</div>
                <div class="card-desc">{p["repo_desc"]}</div>
                <span class="card-link">Ver código-fonte →</span>
            </div>
        </div>
    </a>"""


def card_dash(p: dict) -> str:
    img = ""
    if p["dash_img"]:
        src = p["dash_img"] if p["dash_img"].startswith("http") else f"data:image/png;base64,{img_b64(p['dash_img'])}"
        img = f'<img style="width:100%;height:200px;object-fit:cover;display:block;" src="{src}">'
    else:
        img = f'<div class="card-ph" style="background:{C["ph_dash"]};">📊</div>'
    return f"""
    <a href="{p["dash_url"]}" target="_blank" class="card-w">
        <div class="card dash">
            {img}
            <div class="card-body">
                <div class="card-label dsh">📈 Dashboard ao Vivo</div>
                <div class="card-nome">{p["dash_nome"]}</div>
                <div class="card-desc">{p["dash_desc"]}</div>
                <span class="card-link">Abrir dashboard ↗</span>
            </div>
        </div>
    </a>"""


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:
    # Foto + nome
    st.markdown(foto_perfil_html(), unsafe_allow_html=True)
    st.markdown('<div class="sb-nome">Alisson Moreira</div>', unsafe_allow_html=True)
    st.markdown('<div class="sb-cargo">Analista de Dados</div>', unsafe_allow_html=True)

    st.divider()

    # # Navegacao
    # pagina_atual = st.session_state.pagina
    # nav_html = f"""
    # <div class="sb-nav">
    #     <a href="#" class="{'active' if pagina_atual == 'portfolio' else ''}"
    #        onclick="return false;" id="nav-portfolio">
    #         📊 Portfólio
    #     </a>
    #     <a href="#" class="{'active' if pagina_atual == 'sobre' else ''}"
    #        onclick="return false;" id="nav-sobre">
    #         👤 Sobre Mim
    #     </a>
    # </div>
    # """
    # st.markdown(nav_html, unsafe_allow_html=True)

    # Botoes de navegacao estilizados
    port_active = "active-btn" if st.session_state.pagina == "portfolio" else ""
    sobre_active = "active-btn" if st.session_state.pagina == "sobre" else ""
    st.markdown(f'<div class="nav-btns"><div class="{port_active}">', unsafe_allow_html=True)
    if st.button("📊 Portfólio", key="btn_port", use_container_width=True):
        st.session_state.pagina = "portfolio"
        st.rerun()
    st.markdown(f'</div><div class="{sobre_active}">', unsafe_allow_html=True)
    if st.button("👤 Sobre Mim", key="btn_sobre", use_container_width=True):
        st.session_state.pagina = "sobre"
        st.rerun()
    st.markdown('</div></div>', unsafe_allow_html=True)

    st.divider()

    # Tema
    tema_label = "☀️ Tema Claro" if ESCURO else "🌙 Tema Escuro"
    if st.button(tema_label, key="btn_tema", use_container_width=True):
        st.session_state.tema = "claro" if ESCURO else "escuro"
        st.rerun()

    st.divider()

    # Links inferiores
    st.markdown(
        """
        <div class="sb-bottom">
            <a href="https://github.com/alisson002" target="_blank">🧑🏾‍💻 GitHub</a>
            <a href="https://linkedin.com/in/seu-perfil" target="_blank">🔗 LinkedIn</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Email com copiar
    components.html(
        f"""
        <style>
            * {{ margin:0; padding:0; box-sizing:border-box; font-family:'Segoe UI',sans-serif; }}
            body {{ background:transparent; }}
            .email-btn {{
                display:flex; align-items:center; gap:10px;
                padding:0.45rem 1rem; border-radius:8px;
                color:#94a3b8; font-size:0.8rem;
                cursor:pointer; border:none; background:none;
                width:100%; position:relative; transition:all 0.2s;
                font-family:inherit;
            }}
            .email-btn:hover {{ color:#0077D4; background:rgba(0,119,212,0.08); }}
            .badge {{
                position:absolute; top:-8px; right:6px;
                background:#059669; color:#fff; font-size:0.58rem;
                font-weight:700; padding:2px 8px; border-radius:20px;
                opacity:0; transform:translateY(4px);
                transition:all 0.3s; pointer-events:none;
            }}
            .badge.show {{ opacity:1; transform:translateY(0); }}
        </style>
        <button class="email-btn" id="copy-btn" type="button">
            ✉️ am.analistadedados@gmail.com
            <span class="badge" id="badge">Copiado!</span>
        </button>
        <script>
            document.getElementById('copy-btn').addEventListener('click', function() {{
                var ta = document.createElement('textarea');
                ta.value = 'am.analistadedados@gmail.com';
                ta.style.position = 'fixed';
                ta.style.left = '-9999px';
                document.body.appendChild(ta);
                ta.focus();
                ta.select();
                document.execCommand('copy');
                document.body.removeChild(ta);
                var b = document.getElementById('badge');
                b.classList.add('show');
                setTimeout(function() {{ b.classList.remove('show'); }}, 2000);
            }});
        </script>
        """,
        height=40,
    )


# ============================================================
# PAGINA: PORTFOLIO
# ============================================================

if st.session_state.pagina == "portfolio":
    for projeto in PROJETOS:
        tags_html = "".join(f'<span class="tag">{t}</span>' for t in projeto["tags"])
        st.markdown(
            f"""
            <div class="pj-header">
                <div class="pj-titulo">{projeto["titulo"]}</div>
                <div class="pj-tags">{tags_html}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        col_r, col_d = st.columns(2, gap="medium")
        with col_r:
            st.markdown(card_repo(projeto), unsafe_allow_html=True)
        with col_d:
            st.markdown(card_dash(projeto), unsafe_allow_html=True)

    st.markdown(
        '<div class="rodape">© 2026 Alisson Moreira · Portfólio de Analista de Dados</div>',
        unsafe_allow_html=True,
    )


# ============================================================
# PAGINA: SOBRE MIM
# ============================================================

elif st.session_state.pagina == "sobre":
    # Cabecalho
    st.markdown(
        f'<div class="about-label">Sobre Mim</div>'
        f'<div class="about-title">Alisson Moreira</div>',
        unsafe_allow_html=True,
    )

    # Card: Quem sou eu
    st.markdown(
        f"""
        <div class="about-card">
            <h3 style="color:{C['titulo']};">👤 Quem sou eu</h3>
            <p class="about-text">
                Analista de dados com experiência em
                <strong style="color:{C['titulo']};">tratamento</strong>,
                <strong style="color:{C['titulo']};">modelagem</strong> e
                <strong style="color:{C['titulo']};">visualização de dados</strong>.
                Transformo bases brutas em insights acionáveis através de pipelines
                em <strong style="color:{C['titulo']};">Python</strong>,
                <strong style="color:{C['titulo']};">Pandas</strong> e
                <strong style="color:{C['titulo']};">SQL</strong>,
                além de dashboards interativas.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Card: Ferramentas
    skills = ["Python", "Pandas", "SQL", "Streamlit", "Looker", "Power BI", "Git", "Excel"]
    skills_html = "".join(f'<div class="skill">{s}</div>' for s in skills)
    st.markdown(
        f"""
        <div class="about-card">
            <h3 style="color:{C['titulo']};">🛠️ Ferramentas e Tecnologias</h3>
            <div class="skills-grid">{skills_html}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Card: Contato - Email
    st.markdown(
        f"""
        <div class="about-card">
            <h3 style="color:{C['titulo']};">📬 Contato</h3>
            <div class="ct-list">
                <div class="ct-item" style="cursor:default;">
                    <div class="ct-icon em">✉️</div>
                    <div class="ct-info">
                        <span class="ct-lbl">E-mail</span>
                        <span class="ct-val">am.analistadedados@gmail.com</span>
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Card: Contato - GitHub
    st.markdown(
        f"""
        <div class="about-card" style="margin-top:-1rem;">
            <div class="ct-list">
                <a class="ct-item" href="https://github.com/alisson002" target="_blank"
                   style="text-decoration:none;color:inherit;">
                    <div class="ct-icon gh">🧑🏾‍💻</div>
                    <div class="ct-info">
                        <span class="ct-lbl">GitHub</span>
                        <span class="ct-val">alisson002</span>
                    </div>
                </a>
                <a class="ct-item" href="https://linkedin.com/in/seu-perfil" target="_blank"
                   style="text-decoration:none;color:inherit;">
                    <div class="ct-icon li">🔗</div>
                    <div class="ct-info">
                        <span class="ct-lbl">LinkedIn</span>
                        <span class="ct-val">Alisson Moreira</span>
                    </div>
                </a>
                <div class="ct-item" style="cursor:default;">
                    <div class="ct-icon lo">📍</div>
                    <div class="ct-info">
                        <span class="ct-lbl">Localização</span>
                        <span class="ct-val">Natal - RN</span>
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="rodape">© 2026 Alisson Moreira · Portfólio de Analista de Dados</div>',
        unsafe_allow_html=True,
    )
