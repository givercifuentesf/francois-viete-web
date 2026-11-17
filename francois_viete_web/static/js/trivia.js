/**
 * Trivia educativa: El reto del arte analítico (Sección 07)
 * Lógica aislada con banco de 18 preguntas verificables sobre François Viète.
 */

document.addEventListener("DOMContentLoaded", () => {
    const triviaRoot = document.getElementById("triviaApp");
    if (!triviaRoot) return;

    const QUESTIONS_BANK = [
        {
            category: "Biografía",
            question: "¿En qué ciudad francesa nació François Viète en 1540?",
            options: [
                "París",
                "Fontenay-le-Comte",
                "Lyon",
                "Marsella"
            ],
            correctIndex: 1,
            explanation: "François Viète nació en 1540 en Fontenay-le-Comte, en la región de Poitou (actual departamento de Vendée), Francia."
        },
        {
            category: "Formación académica",
            question: "¿Qué carrera universitaria estudió François Viète en la Universidad de Poitiers?",
            options: [
                "Medicina",
                "Teología",
                "Derecho",
                "Ingeniería militar"
            ],
            correctIndex: 2,
            explanation: "Siguiendo la profesión de su padre Étienne Viète, estudió Derecho en la Universidad de Poitiers y se graduó en 1560."
        },
        {
            category: "Trayectoria profesional",
            question: "¿Cuál fue la relación laboral de Viète con las matemáticas durante su vida?",
            options: [
                "Fue catedrático de matemáticas en la Sorbona",
                "Fue abogado y consejero real que investigaba matemáticas en su tiempo libre",
                "Fue astrónomo oficial contratado por el Vaticano",
                "Fue contador comercial en Venecia"
            ],
            correctIndex: 1,
            explanation: "Viète nunca ejerció como matemático profesional asalariado; fue abogado, consejero del Parlamento y consejero privado de los reyes Enrique III y Enrique IV."
        },
        {
            category: "Personajes históricos",
            question: "¿Para qué alumna escribió Viète tratados de astronomía y trigonometría entre 1564 y 1568?",
            options: [
                "Catherine de Parthenay",
                "María Estuardo",
                "Émilie du Châtelet",
                "Margarita de Valois"
            ],
            correctIndex: 0,
            explanation: "En 1564 entró al servicio de Antoinette d'Aubeterre como secretario y preceptor de su hija Catherine de Parthenay."
        },
        {
            category: "Contexto histórico",
            question: "¿Por qué periodo político fue apartado Viète de la corte entre 1584 y 1589?",
            options: [
                "La Guerra de los Cien Años",
                "La Revolución Francesa",
                "Las Guerras de Religión en Francia y la presión de la Liga Católica",
                "La Guerra de Sucesión Española"
            ],
            correctIndex: 2,
            explanation: "Debido a su cercanía con los hugonotes durante las Guerras de Religión, la Liga Católica logró apartarlo de la corte; durante su retiro en Beauvoir-sur-Mer gestó su nueva álgebra."
        },
        {
            category: "Curiosidades históricas",
            question: "¿Qué hazaña realizó Viète en 1590 al servicio del rey Enrique IV?",
            options: [
                "Diseñó el primer telégrafo óptico",
                "Descifró una compleja carta encriptada dirigida a Felipe II de España",
                "Construyó un observatorio astronómico en Tours",
                "Redactó el primer código civil francés"
            ],
            correctIndex: 1,
            explanation: "Viète descifró los despachos secretos del comandante Moreo dirigidos a Felipe II; al descubrirlo, el rey español se quejó ante el Papa de que Francia usaba «magia negra»."
        },
        {
            category: "Obras matemáticas",
            question: "¿Cuál es la obra publicada en 1591 donde Viète presentó sistemáticamente el álgebra simbólica?",
            options: [
                "Principia Mathematica",
                "In artem analyticen isagoge",
                "Ars Magna",
                "La Géométrie"
            ],
            correctIndex: 1,
            explanation: "En In artem analyticen isagoge (Tours, 1591), Viète expuso la logistica speciosa, obra fundacional del álgebra simbólica."
        },
        {
            category: "Frase histórica",
            question: "¿Qué significa el lema latino «Nullum non problema solvere» con el que cierra su Isagoge (1591)?",
            options: [
                "«Todo número es geometría»",
                "«No dejar ningún problema sin resolver»",
                "«La razón supera a la experiencia»",
                "«Solo lo exacto es verdadero»"
            ],
            correctIndex: 1,
            explanation: "Viète cerró su tratado de 1591 con la aspiración de «No dejar ningún problema sin resolver» gracias al nuevo arte analítico."
        },
        {
            category: "Álgebra simbólica",
            question: "En la notación de Viète, ¿qué tipo de letras representaban las cantidades desconocidas (incógnitas)?",
            options: [
                "Las últimas letras del alfabeto (x, y, z)",
                "Las letras griegas (α, β, γ)",
                "Las vocales (A, E, I, O, U, Y)",
                "Las consonantes (B, C, D, G, Z)"
            ],
            correctIndex: 2,
            explanation: "Viète utilizó vocales para las cantidades desconocidas y consonantes para las conocidas o parámetros."
        },
        {
            category: "Influencia histórica",
            question: "¿Qué matemático introdujo posteriormente la convención actual de usar x, y, z para incógnitas y a, b, c para conocidas?",
            options: [
                "René Descartes.",
                "Isaac Newton",
                "Leonhard Euler",
                "Carl Friedrich Gauss"
            ],
            correctIndex: 0,
            explanation: "René Descartes introdujo la convención moderna de las primeras letras para parámetros y las últimas para incógnitas en La Géométrie (1637)."
        },
        {
            category: "Álgebra simbólica",
            question: "¿Cómo llamó Viète al cálculo que opera con símbolos generales (especies) en lugar de números concretos?",
            options: [
                "Logistica numerosa",
                "Logistica speciosa.",
                "Aritmética retórica",
                "Cálculo diferencial"
            ],
            correctIndex: 1,
            explanation: "Viète distinguió entre logistica numerosa (cálculo con números) y logistica speciosa (cálculo con símbolos o especies)."
        },
        {
            category: "Método analítico",
            question: "¿Cuáles son las tres etapas en que Viète dividió la resolución de un problema matemático?",
            options: [
                "Hipótesis, antítesis y síntesis",
                "Zetética, Porística y Exegética.",
                "Inducción, deducción y prueba",
                "Derivación, integración y límite"
            ],
            correctIndex: 1,
            explanation: "En la Zetética se plantea la ecuación, en la Porística se analizan sus propiedades y se resuelve, y en la Exegética se interpreta la solución."
        },
        {
            category: "Teoría de ecuaciones",
            question: "¿Qué exigía la «ley de homogeneidad» en las ecuaciones escritas por Viète?",
            options: [
                "Que todas las raíces fueran negativas",
                "Que todos los términos de una igualdad tuvieran la misma dimensión geométrica",
                "Que solo se usaran números primos como coeficientes",
                "Que toda ecuación tuviera exactamente tres incógnitas"
            ],
            correctIndex: 1,
            explanation: "Por herencia geométrica, Viète exigía comparar magnitudes homogéneas (por ejemplo, áreas con áreas o volúmenes con volúmenes)."
        },
        {
            category: "Fórmulas de Viète",
            question: "¿Qué relacionan las célebres «Fórmulas de Viète» en un polinomio?",
            options: [
                "El área de un círculo con su radio",
                "Los coeficientes del polinomio con las sumas y productos de sus raíces",
                "Los ángulos internos de un triángulo esférico",
                "Los logaritmos naturales con las potencias de 10"
            ],
            correctIndex: 1,
            explanation: "En De aequationum recognitione et emendatione (1615), Viète mostró cómo los coeficientes se expresan mediante sumas y productos elementales de las raíces positivas."
        },
        {
            category: "Vocabulario matemático",
            question: "¿Qué término matemático de uso cotidiano en las ecuaciones fue acuñado por François Viète?",
            options: [
                "Matriz",
                "Coeficiente",
                "Integral",
                "Vector"
            ],
            correctIndex: 1,
            explanation: "Viète introdujo el término «coeficiente» (del latín coëfficiens) en sus trabajos sobre ecuaciones."
        },
        {
            category: "Desafíos matemáticos",
            question: "¿Cómo resolvió Viète la ecuación de grado 45 propuesta por el matemático flamenco Adriaan van Roomen?",
            options: [
                "Usando una calculadora mecánica de madera",
                "Reconociendo una relación trigonométrica entre sin(x) y sin(x/45)",
                "Aplicando series de Taylor",
                "Demostrando que no tenía ninguna solución real"
            ],
            correctIndex: 1,
            explanation: "Viète identificó al instante que el polinomio de grado 45 correspondía a la relación trigonométrica de división de ángulos, hallando soluciones de inmediato."
        },
        {
            category: "Trigonometría y π",
            question: "¿Qué logro histórico alcanzó Viète en 1593 respecto al número π?",
            options: [
                "Demostró que π es un número racional",
                "Formuló el primer producto infinito de la historia para π y lo calculó con 10 decimales",
                "Calculó el primer millón de cifras decimales de π",
                "Introdujo la letra griega π como símbolo universal"
            ],
            correctIndex: 1,
            explanation: "En 1593 halló la primera expresión mediante producto infinito para π y obtuvo 10 decimales exactos usando un polígono de 393 216 lados."
        },
        {
            category: "Legado y homenajes",
            question: "¿Qué reconocimiento astronómico y urbano honra la memoria de François Viète en la actualidad?",
            options: [
                "Un planeta enano llamado Vieta",
                "Un cráter lunar llamado Vieta y la Rue Viète en París",
                "Un satélite artificial de la ESA",
                "La torre más alta de Poitiers"
            ],
            correctIndex: 1,
            explanation: "La Unión Astronómica Internacional nombró el cráter lunar Vieta en su honor, y el distrito 17 de París cuenta con la Rue Viète."
        }
    ];

    const TOTAL_PER_ROUND = 5;
    const LETTERS = ["A", "B", "C", "D"];

    // Referencias del DOM
    const elCounter = document.getElementById("triviaCounter");
    const elProgressFill = document.getElementById("triviaProgressFill");
    const elScore = document.getElementById("triviaScore");
    const elDots = document.querySelectorAll("#triviaDots .trivia-dot");

    const elQuestionView = document.getElementById("triviaQuestionView");
    const elResultsView = document.getElementById("triviaResultsView");
    const elCategory = document.getElementById("triviaCategory");
    const elQuestionText = document.getElementById("triviaQuestionText");
    const elOptions = document.getElementById("triviaOptions");
    const elWarning = document.getElementById("triviaWarning");

    const elFeedback = document.getElementById("triviaFeedback");
    const elFeedbackTitle = document.getElementById("feedbackTitle");
    const elFeedbackCorrect = document.getElementById("feedbackCorrectAnswer");
    const elFeedbackExp = document.getElementById("feedbackExplanation");

    const btnCheck = document.getElementById("btnCheckAnswer");
    const btnNext = document.getElementById("btnNextQuestion");
    const btnPlayAgain = document.getElementById("btnPlayAgain");

    const elResScore = document.getElementById("resFinalScore");
    const elResCorrect = document.getElementById("resCorrectCount");
    const elResWrong = document.getElementById("resWrongCount");
    const elResPercent = document.getElementById("resPercentage");
    const elResMessage = document.getElementById("resCustomMessage");

    // Estado de la partida
    let roundQuestions = [];
    let currentIndex = 0;
    let score = 0;
    let selectedOption = null;
    let answered = false;
    let lastRoundIndices = [];

    function shuffleArray(arr) {
        const copy = [...arr];
        for (let i = copy.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [copy[i], copy[j]] = [copy[j], copy[i]];
        }
        return copy;
    }

    function pickRoundQuestions() {
        const allIndices = QUESTIONS_BANK.map((_, idx) => idx);
        // Priorizar preguntas que no aparecieron en la partida inmediatamente anterior
        const freshIndices = allIndices.filter((idx) => !lastRoundIndices.includes(idx));
        const pool = freshIndices.length >= TOTAL_PER_ROUND
            ? shuffleArray(freshIndices)
            : shuffleArray(allIndices);

        const chosenIndices = pool.slice(0, TOTAL_PER_ROUND);
        lastRoundIndices = chosenIndices;
        return chosenIndices.map((idx) => QUESTIONS_BANK[idx]);
    }

    function startNewRound() {
        roundQuestions = pickRoundQuestions();
        currentIndex = 0;
        score = 0;
        selectedOption = null;
        answered = false;

        elScore.textContent = `0 / ${TOTAL_PER_ROUND}`;
        elProgressFill.style.width = "0%";
        elDots.forEach((dot) => {
            dot.classList.remove("current", "correct", "wrong");
        });

        elResultsView.classList.add("hidden");
        elQuestionView.classList.remove("hidden");
        renderQuestion();
    }

    function renderQuestion() {
        const q = roundQuestions[currentIndex];
        selectedOption = null;
        answered = false;

        elCounter.textContent = `Pregunta ${currentIndex + 1} de ${TOTAL_PER_ROUND}`;
        elCategory.textContent = q.category;
        elQuestionText.textContent = q.question;

        elDots.forEach((dot, idx) => {
            dot.classList.toggle("current", idx === currentIndex);
        });

        elOptions.innerHTML = "";
        q.options.forEach((optText, idx) => {
            const btn = document.createElement("button");
            btn.type = "button";
            btn.className = "trivia-option-btn";
            btn.setAttribute("role", "radio");
            btn.setAttribute("aria-checked", "false");
            btn.innerHTML = `
                <span class="option-letter">${LETTERS[idx]}</span>
                <span class="option-text">${optText}</span>
            `;
            btn.addEventListener("click", () => selectOption(idx, btn));
            elOptions.appendChild(btn);
        });

        elWarning.classList.add("hidden");
        elFeedback.classList.add("hidden");
        elFeedback.classList.remove("feedback-success", "feedback-error");
        elFeedbackCorrect.classList.add("hidden");

        btnCheck.classList.remove("hidden");
        btnNext.classList.add("hidden");
        btnNext.textContent =
            currentIndex === TOTAL_PER_ROUND - 1 ? "Ver resultados" : "Siguiente pregunta";
    }

    function selectOption(idx) {
        if (answered) return;
        selectedOption = idx;
        elWarning.classList.add("hidden");

        const allBtns = elOptions.querySelectorAll(".trivia-option-btn");
        allBtns.forEach((b, i) => {
            const isSelected = i === idx;
            b.classList.toggle("selected", isSelected);
            b.setAttribute("aria-checked", String(isSelected));
        });
    }

    function checkAnswer() {
        if (answered) return;
        if (selectedOption === null) {
            elWarning.classList.remove("hidden");
            return;
        }

        answered = true;
        const q = roundQuestions[currentIndex];
        const isCorrect = selectedOption === q.correctIndex;
        const allBtns = elOptions.querySelectorAll(".trivia-option-btn");

        allBtns.forEach((btn, idx) => {
            btn.disabled = true;
            if (idx === q.correctIndex) {
                btn.classList.add("is-correct");
            } else if (idx === selectedOption && !isCorrect) {
                btn.classList.add("is-wrong");
            }
        });

        const currentDot = elDots[currentIndex];
        currentDot.classList.remove("current");

        if (isCorrect) {
            score += 1;
            currentDot.classList.add("correct");
            elFeedback.classList.add("feedback-success");
            elFeedbackTitle.textContent = "¡Excelente! Respuesta correcta.";
            elFeedbackCorrect.classList.add("hidden");
        } else {
            currentDot.classList.add("wrong");
            elFeedback.classList.add("feedback-error");
            elFeedbackTitle.textContent = "Respuesta incorrecta.";
            elFeedbackCorrect.textContent = `La opción correcta era ${LETTERS[q.correctIndex]}: ${q.options[q.correctIndex]}`;
            elFeedbackCorrect.classList.remove("hidden");
        }

        elFeedbackExp.textContent = q.explanation;
        elFeedback.classList.remove("hidden");

        elScore.textContent = `${score} / ${TOTAL_PER_ROUND}`;
        const progressPct = ((currentIndex + 1) / TOTAL_PER_ROUND) * 100;
        elProgressFill.style.width = `${progressPct}%`;

        btnCheck.classList.add("hidden");
        btnNext.classList.remove("hidden");
    }

    function nextStep() {
        if (currentIndex < TOTAL_PER_ROUND - 1) {
            currentIndex += 1;
            renderQuestion();
        } else {
            showResults();
        }
    }

    function getEvaluationMessage(finalScore) {
        if (finalScore === 5) {
            return "¡Excelente! Dominas el arte analítico de François Viète.";
        }
        if (finalScore === 4) {
            return "¡Muy bien! Tienes un gran conocimiento sobre su legado.";
        }
        if (finalScore === 3) {
            return "¡Buen trabajo! Has aprendido sobre sus aportes, pero puedes seguir mejorando.";
        }
        if (finalScore >= 1) {
            return "¡Sigue intentándolo! Repasa la historia y los aportes de François Viète.";
        }
        return "¡No te desanimes! Esta es una oportunidad para aprender algo nuevo.";
    }

    function showResults() {
        const wrongCount = TOTAL_PER_ROUND - score;
        const percentage = Math.round((score / TOTAL_PER_ROUND) * 100);

        elResScore.textContent = `${score} / ${TOTAL_PER_ROUND}`;
        elResCorrect.textContent = String(score);
        elResWrong.textContent = String(wrongCount);
        elResPercent.textContent = `${percentage}%`;
        elResMessage.textContent = getEvaluationMessage(score);

        elQuestionView.classList.add("hidden");
        elResultsView.classList.remove("hidden");
    }

    btnCheck.addEventListener("click", checkAnswer);
    btnNext.addEventListener("click", nextStep);
    btnPlayAgain.addEventListener("click", startNewRound);

    startNewRound();
});