"""
Contenido académico y matemático verificado sobre François Viète (1540–1603).

Todas las fechas, hechos biográficos, citas y referencias bibliográficas
proceden de fuentes académicas contrastadas (MacTutor History of Mathematics,
Encyclopædia Britannica, The Galileo Project de Rice University, arXiv e IMPA).
Cuando existe incertidumbre o discrepancia documental, se indica expresamente.
"""

SITE_META = {
    "title": "François Viète (1540–1603) | Padre del Álgebra Simbólica",
    "subtitle": "Seigneur de la Bigotière · Franciscus Vieta",
    "quote_latin": "Nullum non problema solvere.",
    "quote_spanish": "«No dejar ningún problema sin resolver.»",
    "quote_source": "Lema final de In artem analyticen isagoge (Tours, 1591).",
    "secondary_quote": (
        "«Yo, que no profeso ser matemático, pero que, siempre que hay ocio, "
        "me deleito en los estudios matemáticos…»"
    ),
    "secondary_quote_source": "Introducción de Viète a su respuesta a Adriaan van Roomen (1595), citado en MacTutor.",
}

NAV_ITEMS = [
    {"id": "inicio", "label": "Inicio"},
    {"id": "biografia", "label": "Biografía"},
    {"id": "linea-tiempo", "label": "Línea de tiempo"},
    {"id": "aportes", "label": "Aportes"},
    {"id": "impacto", "label": "Impacto actual"},
    {"id": "podcast", "label": "Podcast"},
    {"id": "juego", "label": "Juego"},
    {"id": "curiosidades", "label": "Curiosidades"},
    {"id": "fuentes", "label": "Fuentes"},
    {"id": "uso-ia", "label": "Uso de IA"},
]

BIOGRAPHY_DATA = {
    "vital_facts": [
        {
            "label": "Nombre completo y título",
            "value": "François Viète (en latín: Franciscus Vieta), Seigneur de la Bigotière.",
        },
        {
            "label": "Nacimiento",
            "value": (
                "1540 en Fontenay-le-Comte, Poitou (actual departamento de Vendée), Francia. "
                "Nota documental: el día y el mes exactos no constan en los registros conservados."
            ),
        },
        {
            "label": "Fallecimiento",
            "value": (
                "1603 en París, Francia. Nota de rigor histórico: las fuentes académicas registran "
                "dos fechas distintas para el día exacto: 23 de febrero de 1603 (The Galileo Project, "
                "Rice University) y 13 de diciembre de 1603 (MacTutor History of Mathematics)."
            ),
        },
        {
            "label": "Formación académica",
            "value": (
                "Estudios iniciales en Fontenay-le-Comte; ingresó hacia 1555 en la Universidad de "
                "Poitiers, donde se graduó en Derecho (licenciatura para ejercer la abogacía) en 1560."
            ),
        },
        {
            "label": "Profesión y cargos",
            "value": (
                "Abogado, consejero del Parlamento de Bretaña en Rennes (1573), maître des requêtes "
                "y consejero privado de los reyes Enrique III y Enrique IV de Francia, además de "
                "criptoanalista real. Nunca ejerció como matemático profesional asalariado."
            ),
        },
    ],
    "narrative": [
        {
            "title": "Orígenes y formación jurídica",
            "text": (
                "Hijo de Étienne Viète —abogado y notario en Fontenay-le-Comte— y de Marguerite "
                "Dupont, François Viète siguió inicialmente la tradición jurídica familiar. Tras "
                "graduarse en Derecho en Poitiers en 1560, ejerció cuatro años como abogado en su "
                "ciudad natal, atendiendo asuntos relevantes como la gestión de intereses de María "
                "Estuardo, reina de Escocia, y de la viuda de Francisco I."
            ),
        },
        {
            "title": "Tutoría científica y servicio en la corte",
            "text": (
                "En 1564 pasó al servicio de Antoinette d'Aubeterre como secretario y preceptor de su "
                "hija Catherine de Parthenay, a quien instruyó en astronomía y trigonometría. En 1570 "
                "se trasladó a París, donde en 1571 comenzó a publicar su Canon Mathematicus. En octubre "
                "de 1573 Carlos IX lo nombró consejero del Parlamento de Bretaña (Rennes), y en marzo de "
                "1580 Enrique III lo designó consejero privado en el Parlamento de París."
            ),
        },
        {
            "title": "Exilio en Beauvoir-sur-Mer y plenitud matemática",
            "text": (
                "Entre 1584 y 1589, en medio de las Guerras de Religión y bajo presión de la Liga "
                "Católica por su cercanía con círculos hugonotes, Viète fue apartado de la corte. "
                "Se retiró a Beauvoir-sur-Mer y Fontenay. Ese periodo sin cargos públicos le permitió "
                "dedicarse por entero a la investigación matemática y gestar su obra cumbre: "
                "In artem analyticen isagoge (1591)."
            ),
        },
        {
            "title": "Criptoanalista de Enrique IV y últimos años",
            "text": (
                "Llamado de regreso en 1589 por Enrique III en Tours, tras el asesinato del monarca pasó "
                "a servir a Enrique IV. Descifró complejos mensajes encriptados de la Corona española "
                "dirigidos a Felipe II. En 1593 resolvió el célebre desafío de grado 45 de Adriaan van "
                "Roomen. Fue relevado de su servicio real el 14 de diciembre de 1602 y falleció en París en 1603."
            ),
        },
    ],
    "context_cards": [
        {
            "title": "Contexto político y religioso",
            "text": (
                "Francia vivió entre 1562 y 1598 las Guerras de Religión entre católicos (Liga Católica, "
                "respaldada por Felipe II de España) y protestantes hugonotes, incluyendo la Masacre de "
                "San Bartolomé (23 de agosto de 1572). Viète, vinculado inicialmente a los hugonotes, "
                "siguió el ejemplo de Enrique IV al convertirse al catolicismo en 1593."
            ),
        },
        {
            "title": "Contexto científico del Renacimiento",
            "text": (
                "El álgebra del siglo XVI oscilaba entre reglas aritméticas dispersas (escuela italiana "
                "de Cardano, Tartaglia y Bombelli; tradición cósica alemana) y la geometría euclidiana "
                "clásica. Viète unificó ambos mundos mediante una notación literal sistemática basada en "
                "las proporciones y la homogeneidad dimensional."
            ),
        },
    ],
    "historical_figures": [
        {
            "name": "Catherine de Parthenay",
            "role": "Alumna y mecenas intelectual",
            "relation": "Viète fue su preceptor desde 1564 y redactó para ella tratados de astronomía y trigonometría.",
        },
        {
            "name": "Enrique III y Enrique IV de Francia",
            "role": "Monarcas franceses",
            "relation": "Ambos reyes lo nombraron consejero privado; para Enrique IV actuó además como criptoanalista clave.",
        },
        {
            "name": "Felipe II de España",
            "role": "Monarca español y adversario político",
            "relation": "Viète descifró en 1590 los despachos secretos enviados al rey español por el comandante Moreo.",
        },
        {
            "name": "Adriaan van Roomen",
            "role": "Matemático flamenco",
            "relation": "Propuso la ecuación de grado 45 que Viète resolvió trigonométricamente, iniciando una gran amistad.",
        },
        {
            "name": "Thomas Harriot",
            "role": "Matemático y astrónomo inglés",
            "relation": "Corresponsal de Viète; desarrolló y perfeccionó la notación y teoría de ecuaciones a partir de su obra.",
        },
        {
            "name": "Joseph Justus Scaliger",
            "role": "Erudito y polemista",
            "relation": "Sostuvo una célebre controversia con Viète tras afirmar erróneamente haber cuadrado el círculo.",
        },
    ],
}

TIMELINE_EVENTS = [
    {
        "year": "1540",
        "era": "formacion",
        "era_label": "Formación y primeros años",
        "title": "Nacimiento en Fontenay-le-Comte",
        "description": (
            "Nace en Fontenay-le-Comte, región de Poitou (Francia). El día y mes exactos "
            "no están documentados en las fuentes históricas conservadas."
        ),
        "verified": True,
    },
    {
        "year": "1555–1560",
        "era": "formacion",
        "era_label": "Formación y primeros años",
        "title": "Estudios de Derecho en Poitiers",
        "description": (
            "Cursa estudios jurídicos en la Universidad de Poitiers y obtiene su licenciatura "
            "en Derecho en 1560, ejerciendo como abogado hasta 1564."
        ),
        "verified": True,
    },
    {
        "year": "1564–1570",
        "era": "formacion",
        "era_label": "Formación y primeros años",
        "title": "Tutor de Catherine de Parthenay",
        "description": (
            "Trabaja al servicio de Antoinette d'Aubeterre y enseña matemáticas y astronomía "
            "a su hija Catherine en el entorno de La Rochelle."
        ),
        "verified": True,
    },
    {
        "year": "1571",
        "era": "obra",
        "era_label": "Obra matemática cumbre",
        "title": "Inicio de publicación del Canon Mathematicus",
        "description": (
            "Comienza a publicar en París su obra trigonométrica y astronómica con tablas de "
            "alta precisión y resolución sistemática de triángulos planos y esféricos."
        ),
        "verified": True,
    },
    {
        "year": "1573–1580",
        "era": "servicio",
        "era_label": "Servicio real y exilio",
        "title": "Ascenso como consejero real",
        "description": (
            "Nombrado consejero del Parlamento de Bretaña en Rennes (1573) por Carlos IX y "
            "consejero privado en París (25 de marzo de 1580) por Enrique III."
        ),
        "verified": True,
    },
    {
        "year": "1584–1589",
        "era": "servicio",
        "era_label": "Servicio real y exilio",
        "title": "Retiro forzado en Beauvoir-sur-Mer",
        "description": (
            "Apartado de la corte por presiones de la Liga Católica, dedica cinco años "
            "exclusivos a las matemáticas y concibe su nueva álgebra simbólica."
        ),
        "verified": True,
    },
    {
        "year": "1589–1590",
        "era": "servicio",
        "era_label": "Servicio real y exilio",
        "title": "Desciframiento del código español",
        "description": (
            "El 15 de marzo de 1590 entrega a Enrique IV el desciframiento completo de la "
            "carta secreta del comandante Moreo dirigida a Felipe II de España."
        ),
        "verified": True,
    },
    {
        "year": "1591",
        "era": "obra",
        "era_label": "Obra matemática cumbre",
        "title": "Publicación de In artem analyticen isagoge",
        "description": (
            "Publica en Tours la obra fundacional del álgebra simbólica (logistica speciosa), "
            "introduciendo letras para representar tanto incógnitas como parámetros conocidos."
        ),
        "verified": True,
    },
    {
        "year": "1593",
        "era": "obra",
        "era_label": "Obra matemática cumbre",
        "title": "Producto infinito para π y Supplementum geometriae",
        "description": (
            "Calcula π con 10 decimales usando un polígono de 393 216 lados y formula el "
            "primer producto infinito de la historia para π. Publica además estudios sobre "
            "duplicación del cubo y trisección del ángulo."
        ),
        "verified": True,
    },
    {
        "year": "1593–1595",
        "era": "obra",
        "era_label": "Obra matemática cumbre",
        "title": "Desafío de Adriaan van Roomen",
        "description": (
            "Resuelve la ecuación de grado 45 propuesta por Van Roomen reconociendo su "
            "relación trigonométrica entre sin(x) y sin(x/45), y publica su respuesta en 1595."
        ),
        "verified": True,
    },
    {
        "year": "1600",
        "era": "obra",
        "era_label": "Obra matemática cumbre",
        "title": "Apollonius Gallus y De numerosa potestatum",
        "description": (
            "Publica su solución geométrica con regla y compás al problema de los tres círculos "
            "de Apolonio y su método numérico de aproximación de raíces de ecuaciones."
        ),
        "verified": True,
    },
    {
        "year": "1603",
        "era": "servicio",
        "era_label": "Servicio real y exilio",
        "title": "Fallecimiento en París",
        "description": (
            "Muere en París tras cesar en el servicio real en diciembre de 1602. Las fuentes "
            "académicas difieren en el día exacto: 23 de febrero de 1603 (Galileo Project) o "
            "13 de diciembre de 1603 (MacTutor)."
        ),
    },
]

CONTRIBUTIONS_DATA = {
    "pillars": [
        {
            "id": "logistica-speciosa",
            "tag": "Fundamento",
            "title": "Del álgebra numérica al álgebra simbólica (Logistica Speciosa)",
            "summary": (
                "En In artem analyticen isagoge (1591), Viète diferenció la logistica numerosa "
                "(operar con números concretos) de la logistica speciosa (operar con símbolos o "
                "especies). Estructuró la resolución de problemas en tres fases: Zetética "
                "(plantear la ecuación), Porística (analizar sus propiedades y resolverla) y "
                "Exegética (interpretar la solución numérica o geométrica)."
            ),
        },
        {
            "id": "letras-parametros",
            "tag": "Notación",
            "title": "Vocales para incógnitas y consonantes para parámetros",
            "summary": (
                "Fue el primero en emplear letras sistemáticamente tanto para las cantidades "
                "desconocidas (vocales A, E, I, O, U, Y) como para las conocidas o parámetros "
                "(consonantes B, C, D, G, Z…). Esto permitió estudiar familias enteras de "
                "ecuaciones en lugar de casos aislados. (La convención actual x, y, z / a, b, c "
                "fue introducida después por René Descartes en 1637)."
            ),
        },
        {
            "id": "resolucion-ecuaciones",
            "tag": "Teoría de ecuaciones",
            "title": "Resolución algebraica, numérica y ley de homogeneidad",
            "summary": (
                "Presentó métodos generales para ecuaciones de segundo, tercer y cuarto grado "
                "respetando la ley de homogeneidad dimensional (solo sumar magnitudes de igual "
                "dimensión, p. ej., A³ + B²A = B²Z). En De numerosa potestatum (1600) propuso "
                "un método iterativo dígito a dígito para aproximar raíces reales positivas."
            ),
        },
        {
            "id": "relaciones-raices",
            "tag": "Fórmulas de Viète",
            "title": "Relación entre raíces y coeficientes de un polinomio",
            "summary": (
                "En De aequationum recognitione et emendatione (publicada póstumamente en 1615), "
                "demostró cómo las sumas y productos elementales de las raíces positivas de un "
                "polinomio determinan directamente sus coeficientes. Además, acuñó el término "
                "matemático «coeficiente»."
            ),
        },
        {
            "id": "trigonometria-pi",
            "tag": "Trigonometría y π",
            "title": "Trigonometría analítica y primer producto infinito para π",
            "summary": (
                "En el Canon Mathematicus (1571–1579) sistematizó las seis funciones trigonométricas "
                "para resolver triángulos planos y esféricos. En 1593 descubrió fórmulas para el "
                "seno y coseno de ángulos múltiples y halló el primer producto infinito de la historia "
                "para π, calculándolo con 10 cifras decimales exactas."
            ),
        },
    ],
    "pi_formula_latex": (
        r"\frac{2}{\pi} = \frac{\sqrt{2}}{2} \cdot \frac{\sqrt{2 + \sqrt{2}}}{2} \cdot "
        r"\frac{\sqrt{2 + \sqrt{2 + \sqrt{2}}}}{2} \cdots"
    ),
    "worked_example": {
        "title": "Ejemplo resuelto paso a paso: Las Fórmulas de Viète en una ecuación cuadrática",
        "intro": (
            "Consideremos la ecuación cuadrática mónica con raíces reales positivas: "
            "x² − 7x + 12 = 0. Veamos cómo la abordaría el método de Viète y cómo se verifican "
            "sus relaciones entre raíces y coeficientes."
        ),
        "steps": [
            {
                "step": "Paso 1 · Forma simbólica y homogeneidad (Notación de Viète vs. moderna)",
                "math": "En notación moderna: x² − bx + c = 0. En notación homogénea de Viète: A² − BA + C² = 0 (donde A es la incógnita y B, C son parámetros conocidos).",
                "explanation": (
                    "Viète exigía que cada término tuviera dimensión 2 (un área) para mantener "
                    "coherencia geométrica: A² es un cuadrado, BA es un rectángulo y C² es otro cuadrado."
                ),
            },
            {
                "step": "Paso 2 · Factorización simbólica por raíces",
                "math": "(x − r₁)(x − r₂) = x² − (r₁ + r₂)x + r₁·r₂ = 0",
                "explanation": (
                    "Si r₁ y r₂ son las raíces positivas de la ecuación, al expandir el producto "
                    "se obtienen directamente los coeficientes como funciones simétricas de las raíces."
                ),
            },
            {
                "step": "Paso 3 · Igualación de coeficientes (Fórmulas de Viète)",
                "math": "r₁ + r₂ = −(−7)/1 = 7   y   r₁ · r₂ = 12/1 = 12",
                "explanation": (
                    "Para x² − 7x + 12 = 0, la suma de las dos raíces debe ser 7 y su producto debe ser 12."
                ),
            },
            {
                "step": "Paso 4 · Resolución y verificación",
                "math": "r₁ = 3,  r₂ = 4   ⇒   3 + 4 = 7   y   3 × 4 = 12",
                "explanation": (
                    "Sustituyendo en la ecuación original: 3² − 7(3) + 12 = 9 − 21 + 12 = 0, "
                    "y 4² − 7(4) + 12 = 16 − 28 + 12 = 0. Ambas raíces positivas quedan verificadas."
                ),
            },
        ],
    },
}

IMPACT_DATA = [
    {
        "area": "Matemáticas modernas",
        "type": "Influencia histórica directa",
        "description": (
            "Al sustituir casos numéricos particulares por letras paramétricas, Viète abrió el "
            "camino directo hacia la geometría analítica de Descartes y Fermat, la teoría de "
            "ecuaciones polinómicas y el álgebra abstracta contemporánea."
        ),
    },
    {
        "area": "Ingeniería y ciencias",
        "type": "Aplicación moderna de sus conceptos",
        "description": (
            "Las leyes físicas y modelos de ingeniería (como F = m·a o ecuaciones estructurales) "
            "dependen de la distinción simbólica entre constantes/parámetros conocidos y variables "
            "desconocidas que Viète sistematizó por primera vez."
        ),
    },
    {
        "area": "Programación y computación",
        "type": "Aplicación moderna de sus conceptos",
        "description": (
            "Aunque Viète no diseñó máquinas de cálculo, su logistica speciosa anticipó la "
            "abstracción de variables y parámetros en lenguajes de programación y es la base "
            "conceptual de los sistemas de álgebra computacional (CAS) como SymPy o Mathematica."
        ),
    },
    {
        "area": "Desarrollo de algoritmos",
        "type": "Influencia histórica y aplicación moderna",
        "description": (
            "Su algoritmo numérico iterativo en De numerosa potestatum (1600) para aproximar raíces "
            "es un precursor histórico de métodos iterativos modernos (como Horner y Newton-Raphson). "
            "Asimismo, su criptoanálisis de 1590 aplicó análisis sistemático de patrones."
        ),
    },
    {
        "area": "Modelamiento matemático",
        "type": "Influencia histórica directa",
        "description": (
            "Permitió pasar de resolver un problema aislado a formular modelos generales válidos "
            "para infinitos escenarios mediante parámetros simbólicos, esencia de la ciencia de "
            "datos, la optimización y la estadística actual."
        ),
    },
]

CURIOSITIES_DATA = [
    {
        "title": "Acusado de «magia negra» por el rey de España",
        "fact": (
            "En 1590, Viète descifró una compleja carta cifrada enviada al rey Felipe II de España "
            "con cientos de símbolos de sustitución y homófonos. Al descubrir que Francia conocía "
            "sus planes militares, Felipe II protestó ante el Papa alegando que se empleaba magia negra."
        ),
        "source": "MacTutor History of Mathematics (2000)",
    },
    {
        "title": "Resolvió una ecuación de grado 45 junto a una ventana",
        "fact": (
            "En 1593, el embajador de los Países Bajos afirmó ante Enrique IV que ningún matemático "
            "francés figuraba en la lista de sabios de Adriaan van Roomen. Tras recibir el reto "
            "de grado 45, Viète se apoyó en una ventana, identificó la identidad trigonométrica entre "
            "sin(x) y sin(x/45) y halló soluciones de inmediato, resumiendo: «Ut legi, ut solvi» "
            "(«Lo leí, lo resolví»)."
        ),
        "source": "Wikipedia / MacTutor History of Mathematics",
    },
    {
        "title": "Hospitalidad con su rival convertido en amigo",
        "fact": (
            "Impresionado por la solución de Viète al problema de los tres círculos de Apolonio "
            "(Apollonius Gallus, 1600), Adriaan van Roomen viajó desde Würzburg hasta Fontenay-le-Comte. "
            "Según el historiador De Thou, Viète lo hospedó durante un mes para enseñarle su nueva "
            "álgebra y pagó todos sus gastos de regreso."
        ),
        "source": "MacTutor / Jacques-Auguste de Thou",
    },
    {
        "title": "Creador del término «coeficiente»",
        "fact": (
            "Además de su notación simbólica, Viète introdujo vocabulario matemático que perdura "
            "hasta hoy en las aulas de todo el mundo, entre ellos la palabra «coeficiente» "
            "(del latín coëfficiens)."
        ),
        "source": "MacTutor History of Mathematics (2000)",
    },
    {
        "title": "Un cráter en la Luna y una calle en París",
        "fact": (
            "En reconocimiento a su legado en astronomía y matemáticas, un cráter lunar lleva "
            "oficialmente el nombre de «Vieta», y el distrito 17 de París cuenta con la «Rue Viète»."
        ),
        "source": "MacTutor History of Mathematics (2000)",
    },
]

BIBLIOGRAPHY_APA = [
    {
        "citation": (
            "Storypie. (s.f.). Biografía de François Viète para niños: Historia, "
            "datos y actividades."
        ),
        "url": "https://mystorypie.com/learn/es/biography/francois-viete/",
    },
    {
        "citation": (
            "IMPA — Instituto de Matemática Pura e Aplicada. (2021, 27 de octubre). "
            "In Folha, Viète and the birth of modern algebra."
        ),
        "url": "https://impa.br/notices/in-folha-viete-and-the-birth-of-modern-algebra/?lang=en",
    },
    {
        "citation": (
            "Boyé, A. (s.f.). ¿François Viète, inventor del álgebra? (S. Toledo, Trad.). "
            "En Seminario «Orotava» de Historia de la Ciencia - Año XI-XII (pp. 259–276). "
            "Fundación Canaria Orotava de Historia de la Ciencia."
        ),
        "url": "https://fundacionorotava.org/media/web/publication_files/publication29__11.pdf",
    },
   {
        "citation": (
            "Secretaría de Educación Pública. (2025, 6 de febrero). "
            "François Viète y el álgebra simbólica. Nueva Escuela Mexicana Digital."
        ),
        "url": "https://nuevaescuelamexicana.sep.gob.mx/contenido/coleccion/francois-viete-y-el-algebra-simbolica/",
    },
    {
        "citation": (
            "The Edward Worth Library. (s.f.). Viète — Notation. Trinity College Dublin / "
            "Edward Worth Library."
        ),
        "url": "https://mathematics.edwardworthlibrary.ie/notation/viete/",
    },
    {
        "citation": (
            "Westfall, R. S. (s.f.). Viète, François. The Galileo Project, Rice University."
        ),
        "url": "https://galileo.library.rice.edu/Catalog/NewFiles/viete.html",
    },
]
