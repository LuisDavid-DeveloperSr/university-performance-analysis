import os
import pandas as pd

from rendimiento.ejercicio3 import plot_temporal_trends


def test_plot_temporal_trends_creates_file(tmp_path, monkeypatch):
    # Cambio el directorio de trabajo a una carpeta temporal para no afectar al proyecto real
    monkeypatch.chdir(tmp_path)

    # Creo la estructura de carpetas necesaria para guardar la imagen
    os.makedirs("src/img", exist_ok=True)

    # Creo un DataFrame de ejemplo con datos mínimos para generar el gráfico
    df = pd.DataFrame({
        "Curs Acadèmic": ["20-21", "21-22"],
        "Branca": ["Ciències", "Ciències"],
        "Taxa rendiment mitjana": [0.85, 0.88],
        "Taxa abandonament mitjana": [0.10, 0.08],
    })

    # Ejecuto la función de visualización
    plot_temporal_trends(df, student_name="test_student")

    # Compruebo que el archivo de imagen se ha creado correctamente
    output_file = "src/img/evolucion_test_student.png"
    assert os.path.exists(output_file)
