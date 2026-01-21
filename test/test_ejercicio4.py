def test_analyze_dataset_output_structure(tmp_path):
    import pandas as pd
    from rendimiento.ejercicio4 import analyze_dataset

    # Creo un DataFrame de ejemplo con datos mínimos para el análisis estadístico
    df = pd.DataFrame({
        "Curs Acadèmic": ["20-21", "20-21"],
        "Branca": ["Ciències", "Ciències"],
        "Taxa rendiment mitjana": [0.9, 0.8],
        "Taxa abandonament mitjana": [0.1, 0.2]
    })

    # Ejecuto la función de análisis para comprobar que se genera el resultado sin errores
    analyze_dataset(df)
