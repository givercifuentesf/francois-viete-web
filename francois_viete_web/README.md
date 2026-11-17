# François Viète (1540–1603): El nacimiento del álgebra simbólica

Sitio web educativo e interactivo desarrollado en **Python (Flask)**, **HTML5**, **CSS3** y **JavaScript**, con diseño académico inspirado en el Renacimiento francés y rigor histórico respaldado por fuentes académicas verificadas.

## Estructura del proyecto

```text
francois_viete_web/
├── app.py                      # Servidor principal Flask
├── requirements.txt            # Dependencias de Python
├── README.md                   # Guía de instalación y ejecución
├── data/
│   ├── __init__.py
│   └── viete_content.py        # Datos históricos, matemáticos y bibliografía APA 7.ª ed.
├── static/
│   ├── css/
│   │   └── styles.css          # Estilos académicos responsivos (estética Renacimiento)
│   ├── js/
│   │   └── main.js             # Navegación, filtros de línea de tiempo y simulador de Viète
│   └── images/
│       └── viete_portrait.jpg  # Ilustración artística estilo grabado renacentista
└── templates/
    ├── base.html               # Estructura base, cabecera, navegación y pie de página
    ├── index.html              # Integración de las 10 secciones
    └── sections/               # Plantillas modulares por sección
        ├── inicio.html
        ├── biografia.html
        ├── linea_tiempo.html
        ├── aportes.html
        ├── impacto.html
        ├── podcast.html
        ├── juego.html
        ├── curiosidades.html
        ├── fuentes.html
        └── uso_ia.html
```

## Requisitos previos

- Python 3.9 o superior instalado en su equipo.
- Gestor de paquetes `pip`.

## Instalación y ejecución paso a paso

1. **Descomprima** la carpeta `francois_viete_web` y abra una terminal dentro de ella:
   ```bash
   cd francois_viete_web
   ```

2. **(Opcional pero recomendado) Cree y active un entorno virtual:**
   - En **Windows**:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - En **macOS / Linux**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Instale las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecute el servidor Flask:**
   ```bash
   python app.py
   ```
   *(En macOS/Linux, use `python3 app.py` si `python` no apunta a Python 3).*

5. **Abra su navegador** y visite:
   ```text
   http://127.0.0.1:5000
   ```

## Notas sobre recursos y rigor histórico

- La ilustración de François Viète incluida en `static/images/viete_portrait.jpg` es una representación artística de estilo grabado del siglo XVI creada específicamente para este proyecto educativo, libre de restricciones de uso.
- Las fórmulas matemáticas utilizan **MathJax** (con carga desde CDN y representación legible en HTML como respaldo). Si ejecuta el proyecto sin conexión a internet, las fórmulas siguen siendo legibles gracias al marcado HTML semántico incluido.
- Las secciones **Podcast**, **Juego interactivo** y **Uso de inteligencia artificial** están diseñadas visualmente y reservadas para completarse en etapas posteriores del proyecto.
