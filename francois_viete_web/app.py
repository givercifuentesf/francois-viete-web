"""
Aplicación web educativa sobre el matemático francés François Viète (1540–1603).

Servidor principal desarrollado con Flask que sirve la página única modular
con navegación por secciones y expone los datos históricos y matemáticos
verificados desde el módulo `data.viete_content`.
"""

from flask import Flask, render_template, jsonify
from data.viete_content import (
    SITE_META,
    NAV_ITEMS,
    BIOGRAPHY_DATA,
    TIMELINE_EVENTS,
    CONTRIBUTIONS_DATA,
    IMPACT_DATA,
    CURIOSITIES_DATA,
    BIBLIOGRAPHY_APA,
)

app = Flask(__name__)


@app.route("/")
def index():
    """Renderiza la página principal con todas las secciones educativas."""
    return render_template(
        "index.html",
        meta=SITE_META,
        nav_items=NAV_ITEMS,
        biography=BIOGRAPHY_DATA,
        timeline=TIMELINE_EVENTS,
        contributions=CONTRIBUTIONS_DATA,
        impact=IMPACT_DATA,
        curiosities=CURIOSITIES_DATA,
        bibliography=BIBLIOGRAPHY_APA,
    )


@app.route("/api/timeline")
def api_timeline():
    """Endpoint JSON opcional para consultar los hitos de la línea de tiempo."""
    return jsonify(TIMELINE_EVENTS)


if __name__ == "__main__":
    # Ejecutar en modo desarrollo local
    app.run(host="127.0.0.1", port=5000, debug=True)
