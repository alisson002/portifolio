import streamlit as st
import streamlit.components.v1 as components
import base64
from pathlib import Path

# ============================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================

st.set_page_config(
    page_title="Portfólio | Alisson - Analista de Dados",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# PALETA DE CORES E CSS CUSTOMIZADO
# ============================================================
# Cores: #0077D4 (azul primário), #475569 (cinza escuro),
#         #757491 (cinza lilás), #F8FAFC (fundo claro), #06101b (fundo escuro)

CORES = {
    "primaria": "#0077D4",
    "cinza_escuro": "#475569",
    "cinza_lilas": "#757491",
    "fundo_claro": "#F8FAFC",
    "fundo_escuro": "#06101b",
}

css = f"""
<style>
    /* ---------- Reset e fundo geral ---------- */
    .stApp {{
        background-color: {CORES["fundo_claro"]};
    }}

    /* ---------- Sidebar ---------- */
    section[data-testid="stSidebar"] {{
        background-color: {CORES["fundo_escuro"]};
        padding-top: 1rem;
    }}
    section[data-testid="stSidebar"] * {{
        color: #e2e8f0 !important;
    }}
    section[data-testid="stSidebar"] hr {{
        border-color: {CORES["cinza_escuro"]};
    }}

    /* ---------- Foto de perfil circular ---------- */
    .foto-perfil {{
        display: block;
        margin: 0 auto 1rem auto;
        width: 160px;
        height: 160px;
        border-radius: 50%;
        object-fit: cover;
        border: 4px solid {CORES["primaria"]};
        box-shadow: 0 4px 20px rgba(0, 119, 212, 0.3);
    }}

    /* ---------- Nome na sidebar ---------- */
    .sidebar-nome {{
        text-align: center;
        font-size: 1.5rem;
        font-weight: 700;
        color: #f1f5f9 !important;
        margin-bottom: 0.25rem;
        font-family: 'Segoe UI', sans-serif;
    }}
    .sidebar-titulo {{
        text-align: center;
        font-size: 0.8rem;
        font-weight: 600;
        color: {CORES["primaria"]} !important;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 1.5rem;
    }}

    /* ---------- Sobre mim na sidebar ---------- */
    .sidebar-sobre {{
        background: rgba(255, 255, 255, 0.04);
        border-radius: 10px;
        padding: 1rem 1.1rem;
        border: 1px solid rgba(255, 255, 255, 0.06);
        color: #94a3b8 !important;
        font-size: 0.85rem;
        line-height: 1.75;
        text-align: justify;
        hyphens: auto;
    }}
    .sidebar-sobre strong {{
        color: #e2e8f0 !important;
    }}

    /* ---------- Contato na sidebar ---------- */
    .contato-item {{
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 0.6rem 0.9rem;
        border-radius: 8px;
        background: rgba(255, 255, 255, 0.03);
        margin-bottom: 0.45rem;
        transition: all 0.2s ease;
        text-decoration: none !important;
    }}
    .contato-item:hover {{
        background: rgba(0, 119, 212, 0.12);
        transform: translateX(3px);
    }}
    .contato-icone {{
        width: 32px;
        height: 32px;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.95rem;
        flex-shrink: 0;
    }}
    .contato-icone.email {{ background: rgba(0, 119, 212, 0.15); }}
    .contato-icone.linkedin {{ background: rgba(10, 102, 194, 0.15); }}
    .contato-icone.github {{ background: rgba(255, 255, 255, 0.08); }}
    .contato-icone.local {{ background: rgba(239, 68, 68, 0.12); }}
    .contato-texto {{
        display: flex;
        flex-direction: column;
    }}
    .contato-label {{
        font-size: 0.65rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: {CORES["cinza_lilas"]} !important;
        line-height: 1;
        margin-bottom: 2px;
    }}
    .contato-valor {{
        font-size: 0.82rem;
        color: #e2e8f0 !important;
        text-decoration: none !important;
    }}

    /* ---------- Badge "Copiado!" ---------- */
    .copiado-badge {{
        position: absolute;
        top: -8px;
        right: 8px;
        background: #059669;
        color: #fff !important;
        font-size: 0.65rem;
        font-weight: 700;
        padding: 3px 10px;
        border-radius: 20px;
        opacity: 0;
        transform: translateY(5px);
        transition: all 0.3s ease;
        pointer-events: none;
        letter-spacing: 0.5px;
    }}
    .copiado-badge.visivel {{
        opacity: 1;
        transform: translateY(0);
    }}
    .contato-item.email-item {{
        position: relative;
    }}

    /* ---------- Cabeçalho hero ---------- */
    .hero-subtitulo {{
        color: {CORES["primaria"]};
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 3px;
        text-transform: uppercase;
        margin-bottom: 0.5rem;
    }}
    .hero-titulo {{
        font-size: 2.8rem;
        font-weight: 800;
        color: {CORES["fundo_escuro"]};
        line-height: 1.2;
        margin-bottom: 1rem;
        font-family: 'Segoe UI', sans-serif;
    }}
    .hero-titulo span {{
        color: {CORES["primaria"]};
    }}
    .hero-descricao {{
        max-width: 700px;
        background-color: #edf2f7;
        border-left: 4px solid {CORES["primaria"]};
        padding: 1.25rem 1.5rem;
        border-radius: 0 8px 8px 0;
        color: {CORES["cinza_escuro"]};
        font-size: 0.95rem;
        line-height: 1.7;
    }}

    /* ---------- Título de seção de projeto ---------- */
    .projeto-header {{
        display: flex;
        justify-content: space-between;
        align-items: flex-end;
        border-bottom: 2px solid #e2e8f0;
        padding-bottom: 0.75rem;
        margin-bottom: 1rem;
        margin-top: 2.5rem;
    }}
    .projeto-titulo {{
        font-size: 1.5rem;
        font-weight: 700;
        color: {CORES["fundo_escuro"]};
        font-family: 'Segoe UI', sans-serif;
    }}
    .projeto-tags {{
        display: flex;
        gap: 0.5rem;
    }}
    .tag {{
        background-color: #e2e8f0;
        color: {CORES["cinza_escuro"]};
        padding: 4px 12px;
        border-radius: 4px;
        font-size: 0.65rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
    }}

    /* ---------- Colunas de igual altura ---------- */
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

    /* ---------- Wrapper do card (tag <a>) ---------- */
    .card-wrapper {{
        display: block;
        height: 100%;
        text-decoration: none !important;
        color: inherit !important;
    }}
    .card-wrapper:hover {{
        text-decoration: none !important;
    }}
    .card-wrapper * {{
        text-decoration: none !important;
    }}

    /* ---------- Cards de projeto ---------- */
    .card {{
        background-color: #ffffff;
        border-radius: 12px;
        overflow: hidden;
        border: 1px solid #e2e8f0;
        transition: all 0.3s ease;
        height: 100%;
        display: flex;
        flex-direction: column;
    }}
    .card:hover {{
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.08);
        transform: translateY(-4px);
    }}
    .card-preview {{
        width: 100%;
        height: 200px;
        object-fit: cover;
        display: block;
    }}
    .card-preview-placeholder {{
        width: 100%;
        height: 200px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 3rem;
    }}
    .card-body {{
        padding: 1.25rem 1.5rem;
        flex: 1;
        display: flex;
        flex-direction: column;
    }}
    .card-tipo {{
        font-size: 0.7rem;
        font-weight: 700;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 0.4rem;
    }}
    .card-tipo.repo {{
        color: {CORES["primaria"]};
    }}
    .card-tipo.dash {{
        color: #059669;
    }}
    .card-nome {{
        font-size: 1.15rem;
        font-weight: 700;
        color: {CORES["fundo_escuro"]};
        margin-bottom: 0.5rem;
    }}
    .card-desc {{
        font-size: 0.85rem;
        color: {CORES["cinza_lilas"]};
        line-height: 1.6;
        flex: 1;
    }}
    .card-link {{
        display: inline-flex;
        align-items: center;
        gap: 6px;
        color: {CORES["primaria"]};
        font-size: 0.85rem;
        font-weight: 600;
        text-decoration: none;
        margin-top: 1rem;
    }}
    .card-link:hover {{
        text-decoration: underline;
    }}

    /* ---------- Borda especial para card de dashboard ---------- */
    .card.dash-card {{
        border: 1px solid rgba(0, 119, 212, 0.15);
    }}

    /* ---------- Rodapé ---------- */
    .rodape {{
        text-align: center;
        padding: 2rem 0;
        margin-top: 4rem;
        border-top: 1px solid #e2e8f0;
        color: {CORES["cinza_lilas"]};
        font-size: 0.75rem;
        letter-spacing: 1px;
    }}

    /* ---------- Esconder elementos padrão do Streamlit ---------- */
    #MainMenu {{visibility: hidden;}}
    header {{visibility: hidden;}}
    footer {{visibility: hidden;}}
</style>
"""

st.markdown(css, unsafe_allow_html=True)


# ============================================================
# DADOS DOS PROJETOS (EDITE AQUI)
# ============================================================
# Cada projeto é um dicionário com os dados do par de links.
# - titulo: nome do projeto
# - tags: lista de tecnologias usadas
# - repo_nome: título do card do repositório
# - repo_desc: descrição breve do repositório
# - repo_url: link do GitHub
# - repo_img: caminho local ou URL de imagem de pré-visualização (ou None)
# - dash_nome: título do card da dashboard
# - dash_desc: descrição breve da dashboard
# - dash_url: link da dashboard (Streamlit/Looker)
# - dash_img: caminho local ou URL de imagem de pré-visualização (ou None)

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
# FUNÇÕES AUXILIARES
# ============================================================

def imagem_para_base64(caminho: str) -> str:
    """Converte imagem local para string base64 para embutir no HTML."""
    dados = Path(caminho).read_bytes()
    return base64.b64encode(dados).decode()


def carregar_foto_perfil() -> str:
    """Retorna a tag <img> com a foto de perfil em base64."""
    caminho_foto = Path(__file__).parent / "alisson.jpeg"
    if caminho_foto.exists():
        b64 = imagem_para_base64(str(caminho_foto))
        return f'<img class="foto-perfil" src="data:image/jpeg;base64,{b64}" alt="Foto de perfil">'
    return '<div style="width:160px;height:160px;border-radius:50%;background:#475569;margin:0 auto 1rem auto;"></div>'


def gerar_preview(imagem, cor_fundo: str, emoji: str) -> str:
    """Gera o HTML de pré-visualização do card (imagem ou placeholder)."""
    if imagem:
        if imagem.startswith("http"):
            return f'<img class="card-preview" src="{imagem}" alt="Preview">'
        else:
            b64 = imagem_para_base64(imagem)
            return f'<img class="card-preview" src="data:image/png;base64,{b64}" alt="Preview">'
    return f'<div class="card-preview-placeholder" style="background-color:{cor_fundo};">{emoji}</div>'


def gerar_card_repo(projeto: dict) -> str:
    """Gera o HTML de um card de repositório GitHub."""
    preview = gerar_preview(projeto["repo_img"], "#e8f0fe", "💻")
    return f"""
    <a href="{projeto["repo_url"]}" target="_blank" class="card-wrapper">
        <div class="card">
            {preview}
            <div class="card-body">
                <div class="card-tipo repo">📂 Repositório Git</div>
                <div class="card-nome">{projeto["repo_nome"]}</div>
                <div class="card-desc">{projeto["repo_desc"]}</div>
                <span class="card-link">Ver código-fonte →</span>
            </div>
        </div>
    </a>
    """


def gerar_card_dash(projeto: dict) -> str:
    """Gera o HTML de um card de dashboard."""
    preview = gerar_preview(projeto["dash_img"], "#ecfdf5", "📊")
    return f"""
    <a href="{projeto["dash_url"]}" target="_blank" class="card-wrapper">
        <div class="card dash-card">
            {preview}
            <div class="card-body">
                <div class="card-tipo dash">📈 Dashboard ao Vivo</div>
                <div class="card-nome">{projeto["dash_nome"]}</div>
                <div class="card-desc">{projeto["dash_desc"]}</div>
                <span class="card-link">Abrir dashboard ↗</span>
            </div>
        </div>
    </a>
    """


# ============================================================
# BARRA LATERAL - PERFIL E CONTATOS
# ============================================================

with st.sidebar:
    # Foto de perfil
    st.markdown(carregar_foto_perfil(), unsafe_allow_html=True)

    # Nome e título
    st.markdown('<div class="sidebar-nome">Alisson Moreira</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="sidebar-titulo">Analista de Dados</div>',
        unsafe_allow_html=True,
    )

    st.divider()

    # Descrição pessoal
    st.markdown(
        """
        <div class="sidebar-sobre">
            Analista de dados com experiência em <strong>tratamento</strong>,
            <strong>modelagem</strong> e <strong>visualização de dados</strong>.
            Transformo bases brutas em insights acionáveis através de pipelines
            em <strong>Python</strong>, <strong>Pandas</strong> e <strong>SQL</strong>, além de dashboards interativas.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    # Contato: Email (com copiar via components.html para JS funcionar)
    components.html(
        f"""
        <style>
            * {{ margin: 0; padding: 0; box-sizing: border-box; font-family: 'Segoe UI', sans-serif; }}
            body {{ background: transparent; }}
            .contato-item {{
                display: flex; align-items: center; gap: 10px;
                padding: 0.6rem 0.9rem; border-radius: 8px;
                background: rgba(255,255,255,0.03); cursor: pointer;
                transition: all 0.2s ease; text-decoration: none; position: relative;
            }}
            .contato-item:hover {{ background: rgba(0,119,212,0.12); transform: translateX(3px); }}
            .contato-icone {{
                width: 32px; height: 32px; border-radius: 8px;
                display: flex; align-items: center; justify-content: center;
                font-size: 0.95rem; flex-shrink: 0; background: rgba(0,119,212,0.15);
            }}
            .contato-texto {{ display: flex; flex-direction: column; }}
            .contato-label {{
                font-size: 0.65rem; font-weight: 600; text-transform: uppercase;
                letter-spacing: 1px; color: {CORES["cinza_lilas"]}; line-height: 1; margin-bottom: 2px;
            }}
            .contato-valor {{ font-size: 0.82rem; color: #e2e8f0; }}
            .copiado-badge {{
                position: absolute; top: -8px; right: 8px;
                background: #059669; color: #fff; font-size: 0.65rem; font-weight: 700;
                padding: 3px 10px; border-radius: 20px;
                opacity: 0; transform: translateY(5px);
                transition: all 0.3s ease; pointer-events: none;
            }}
            .copiado-badge.visivel {{ opacity: 1; transform: translateY(0); }}
        </style>
        <div class="contato-item" id="copiar-email">
            <div class="contato-icone">✉️</div>
            <div class="contato-texto">
                <span class="contato-label">E-mail · clique para copiar</span>
                <span class="contato-valor">am.analistadedados@gmail.com</span>
            </div>
            <span class="copiado-badge" id="copiado-badge">✓ Copiado!</span>
        </div>
        <script>
            document.getElementById('copiar-email').addEventListener('click', function() {{
                var ta = document.createElement('textarea');
                ta.value = 'am.analistadedados@gmail.com';
                ta.style.position = 'fixed';
                ta.style.left = '-9999px';
                document.body.appendChild(ta);
                ta.focus();
                ta.select();
                document.execCommand('copy');
                document.body.removeChild(ta);
                var badge = document.getElementById('copiado-badge');
                badge.classList.add('visivel');
                setTimeout(function() {{ badge.classList.remove('visivel'); }}, 2000);
            }});
        </script>
        """,
        height=50,
    )
    
    # st.divider()
    
    # Contatos restantes (LinkedIn, GitHub, Localização)
    st.markdown(
        
        """
        <a class="contato-item" href="https://linkedin.com/in/seu-perfil" target="_blank">
            <div class="contato-icone linkedin">🔗</div>
            <div class="contato-texto">
                <span class="contato-label">LinkedIn</span>
                <span class="contato-valor">Alisson Moreira</span>
            </div>
        </a>
        <a class="contato-item" href="https://github.com/alisson002" target="_blank">
            <div class="contato-icone github">🧑🏾‍💻</div>
            <div class="contato-texto">
                <span class="contato-label">GitHub</span>
                <span class="contato-valor">alisson002</span>
            </div>
        </a>
        <div class="contato-item" style="cursor:default;">
            <div class="contato-icone local">📍</div>
            <div class="contato-texto">
                <span class="contato-label">Localização</span>
                <span class="contato-valor">Natal - RN</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    # Botão de download do CV (opcional)
    # Para usar, coloque seu CV na mesma pasta com o nome "cv.pdf"
    caminho_cv = Path(__file__).parent / "cv.pdf"
    if caminho_cv.exists():
        with open(caminho_cv, "rb") as f:
            st.download_button(
                label="📄 Baixar Currículo",
                data=f,
                file_name="Alisson_CV.pdf",
                mime="application/pdf",
                use_container_width=True,
            )


# ============================================================
# CONTEÚDO PRINCIPAL - HERO / INTRODUÇÃO
# ============================================================

# st.markdown('<div class="hero-subtitulo">Trabalhos Selecionados</div>', unsafe_allow_html=True)
# st.markdown(
#     '<div class="hero-titulo">Transformando dados brutos em<br><span>insights estratégicos.</span></div>',
#     unsafe_allow_html=True,
# )
# st.markdown(
#     """
#     <div class="hero-descricao">
#         Desenvolvo pipelines de dados e dashboards interativas que não apenas
#         exibem números — elas contam a história por trás dos dados. Meu processo
#         conecta tratamento rigoroso em Python com visualizações claras e objetivas.
#     </div>
#     """,
#     unsafe_allow_html=True,
# )

st.markdown("<br>", unsafe_allow_html=True)


# ============================================================
# CONTEÚDO PRINCIPAL - GALERIA DE PROJETOS
# ============================================================

for projeto in PROJETOS:
    # Cabeçalho do projeto com tags
    tags_html = "".join(f'<span class="tag">{t}</span>' for t in projeto["tags"])
    st.markdown(
        f"""
        <div class="projeto-header">
            <div class="projeto-titulo">{projeto["titulo"]}</div>
            <div class="projeto-tags">{tags_html}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Par de cards lado a lado: Repositório | Dashboard
    col_repo, col_dash = st.columns(2, gap="medium")

    with col_repo:
        st.markdown(gerar_card_repo(projeto), unsafe_allow_html=True)

    with col_dash:
        st.markdown(gerar_card_dash(projeto), unsafe_allow_html=True)


# ============================================================
# RODAPÉ
# ============================================================

st.markdown(
    """
    <div class="rodape">
        © 2026 Alisson Moreira · Portfólio de Analista de Dados
    </div>
    """,
    unsafe_allow_html=True,
)
