/* ===== Tema claro / escuro ===== */
const htmlEl = document.documentElement;
document.getElementById('theme-toggle').addEventListener('click', () => {
    htmlEl.classList.toggle('dark');
    htmlEl.classList.toggle('light');
    try {
        localStorage.setItem('theme', htmlEl.classList.contains('dark') ? 'dark' : 'light');
    } catch (e) { /* localStorage indisponível (modo privado etc.) */ }
});

/* ===== Copiar e-mail (qualquer elemento com data-copy-email) ===== */
function copiarTexto(texto) {
    navigator.clipboard.writeText(texto).catch(() => {
        const ta = document.createElement('textarea');
        ta.value = texto;
        ta.style.position = 'fixed';
        ta.style.left = '-9999px';
        document.body.appendChild(ta);
        ta.select();
        document.execCommand('copy');
        ta.remove();
    });
}

document.querySelectorAll('[data-copy-email]').forEach((el) => {
    el.addEventListener('click', () => {
        copiarTexto(el.dataset.copyEmail);
        const badge = el.querySelector('.copy-badge');
        if (badge) {
            badge.classList.add('show');
            setTimeout(() => badge.classList.remove('show'), 2000);
        }
    });
});

/* ===== Sidebar mobile ===== */
const sidebar = document.getElementById('sidebar');
const overlay = document.getElementById('sidebar-overlay');
document.getElementById('hamburger').addEventListener('click', () => {
    sidebar.classList.toggle('open');
    overlay.classList.toggle('open');
});
overlay.addEventListener('click', () => {
    sidebar.classList.remove('open');
    overlay.classList.remove('open');
});

/* ===== Animação de entrada ao rolar ===== */
const reveals = document.querySelectorAll('.reveal');
const semAnimacao = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
if ('IntersectionObserver' in window && !semAnimacao) {
    const io = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                io.unobserve(entry.target);
            }
        });
    }, { threshold: 0.08 });
    reveals.forEach((el) => io.observe(el));
} else {
    reveals.forEach((el) => el.classList.add('visible'));
}
