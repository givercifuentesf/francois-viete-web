/**
 * Lógica interactiva del sitio web educativo sobre François Viète.
 * Incluye:
 *  1. Menú de navegación responsive y resaltado de sección activa.
 *  2. Filtrado interactivo de la línea de tiempo histórica.
 *  3. Simulador del producto infinito de Viète para π.
 *  4. Laboratorio interactivo de las Fórmulas de Viète (raíces y coeficientes).
 *  5. Animaciones moderadas de aparición al desplazarse.
 */

document.addEventListener("DOMContentLoaded", () => {
    initMobileMenu();
    initActiveNavHighlight();
    initTimelineFilters();
    initPiCalculator();
    initVieteRootsLab();
    initRevealAnimations();
});

function initMobileMenu() {
    const toggle = document.getElementById("navToggle");
    const nav = document.getElementById("mainNav");
    if (!toggle || !nav) return;

    toggle.addEventListener("click", () => {
        const isOpen = nav.classList.toggle("open");
        toggle.setAttribute("aria-expanded", String(isOpen));
    });

    nav.querySelectorAll(".nav-link").forEach((link) => {
        link.addEventListener("click", () => {
            nav.classList.remove("open");
            toggle.setAttribute("aria-expanded", "false");
        });
    });
}

function initActiveNavHighlight() {
    const sections = document.querySelectorAll("main section[id]");
    const links = document.querySelectorAll(".nav-link");
    if (!sections.length || !links.length) return;

    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (!entry.isIntersecting) return;
                const currentId = entry.target.getAttribute("id");
                links.forEach((link) => {
                    link.classList.toggle(
                        "active",
                        link.getAttribute("href") === `#${currentId}`
                    );
                });
            });
        },
        { rootMargin: "-35% 0px -55% 0px" }
    );

    sections.forEach((sec) => observer.observe(sec));
}

function initTimelineFilters() {
    const buttons = document.querySelectorAll(".filter-btn");
    const items = document.querySelectorAll(".timeline-item");
    if (!buttons.length || !items.length) return;

    buttons.forEach((btn) => {
        btn.addEventListener("click", () => {
            const filter = btn.dataset.filter;
            buttons.forEach((b) => b.classList.remove("active"));
            btn.classList.add("active");

            items.forEach((item) => {
                const matches = filter === "all" || item.dataset.era === filter;
                item.classList.toggle("hidden", !matches);
            });
        });
    });
}

function initPiCalculator() {
    const range = document.getElementById("piTermsRange");
    const termsLabel = document.getElementById("piTermsValue");
    const approxOutput = document.getElementById("piApproxOutput");
    const errorOutput = document.getElementById("piErrorOutput");
    if (!range || !termsLabel || !approxOutput || !errorOutput) return;

    const updatePi = () => {
        const n = parseInt(range.value, 10);
        termsLabel.textContent = String(n);

        // Producto infinito de Viète: 2/pi = prod_{k=1..n} (a_k / 2)
        let product = 1;
        let radical = Math.sqrt(2);
        for (let i = 0; i < n; i++) {
            product *= radical / 2;
            radical = Math.sqrt(2 + radical);
        }

        const approx = 2 / product;
        const absError = Math.abs(Math.PI - approx);
        approxOutput.textContent = approx.toFixed(8);
        errorOutput.textContent = absError.toExponential(3);
    };

    range.addEventListener("input", updatePi);
    updatePi();
}

function initVieteRootsLab() {
    const r1Input = document.getElementById("root1Input");
    const r2Input = document.getElementById("root2Input");
    const output = document.getElementById("vieteLabOutput");
    if (!r1Input || !r2Input || !output) return;

    const renderLab = () => {
        const r1 = Math.max(1, parseInt(r1Input.value, 10) || 1);
        const r2 = Math.max(1, parseInt(r2Input.value, 10) || 1);
        const sum = r1 + r2;
        const prod = r1 * r2;

        output.innerHTML = `
            <div><strong>1. Suma de raíces (r₁ + r₂):</strong> ${r1} + ${r2} = <strong>${sum}</strong></div>
            <div><strong>2. Producto de raíces (r₁ · r₂):</strong> ${r1} × ${r2} = <strong>${prod}</strong></div>
            <div><strong>3. Ecuación resultante:</strong> x² − ${sum}x + ${prod} = 0</div>
            <div><strong>4. Notación homogénea de Viète:</strong> A² − B·A + C² = 0 (con B = ${sum}, C² = ${prod})</div>
        `;
    };

    r1Input.addEventListener("input", renderLab);
    r2Input.addEventListener("input", renderLab);
    renderLab();
}

function initRevealAnimations() {
    const reveals = document.querySelectorAll(".reveal");
    if (!reveals.length) return;

    if (!("IntersectionObserver" in window)) {
        reveals.forEach((el) => el.classList.add("is-visible"));
        return;
    }

    const observer = new IntersectionObserver(
        (entries, obs) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("is-visible");
                    obs.unobserve(entry.target);
                }
            });
        },
        { threshold: 0.08 }
    );

    reveals.forEach((el) => observer.observe(el));
}
