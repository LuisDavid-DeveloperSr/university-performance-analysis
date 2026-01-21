import json
import os
from datetime import datetime

from scipy.stats import linregress, pearsonr


def analyze_dataset(merged_df):
    """
    Realiza un análisis estadístico completo del dataset fusionado
    y guarda los resultados en un archivo JSON.

    Parameters
    ----------
    merged_df : pandas.DataFrame
        Dataset final fusionado (salida del Ejercicio 2)
    """

    # Inicializo el diccionario que contendrá todo el informe
    report = {}

    # Añado información general sobre el análisis realizado
    report["metadata"] = {
        "fecha_analisis": datetime.now().strftime("%Y-%m-%d"),
        "num_registros": len(merged_df),
        "periodo_temporal": sorted(merged_df["Curs Acadèmic"].unique().tolist()),
    }

    # Extraigo las columnas de abandono y rendimiento eliminando valores nulos
    abandono = merged_df["Taxa abandonament mitjana"].dropna()
    rendimiento = merged_df["Taxa rendiment mitjana"].dropna()

    # Calculo la correlación de Pearson entre abandono y rendimiento
    corr, p_value = pearsonr(abandono, rendimiento)

    # Guardo las estadísticas globales en el informe
    report["estadisticas_globales"] = {
        "abandono_medio": abandono.mean(),
        "rendimiento_medio": rendimiento.mean(),
        "correlacion_abandono_rendimiento": {
            "coeficiente": corr,
            "p_value": p_value,
        },
    }

    # Inicializo el bloque de análisis por rama de estudio
    report["analisis_por_rama"] = {}

    for branch in merged_df["Branca"].unique():
        # Filtro los datos correspondientes a la rama actual
        branch_data = merged_df[merged_df["Branca"] == branch]

        # Calculo estadísticas descriptivas del abandono
        abandono_media = branch_data["Taxa abandonament mitjana"].mean()
        abandono_std = branch_data["Taxa abandonament mitjana"].std()

        # Calculo estadísticas descriptivas del rendimiento
        rendimiento_media = branch_data["Taxa rendiment mitjana"].mean()
        rendimiento_std = branch_data["Taxa rendiment mitjana"].std()

        # Agrupo los datos por curso académico para analizar la tendencia temporal
        branch_by_year = (
            branch_data
            .groupby("Curs Acadèmic", as_index=False)
            .agg({"Taxa abandonament mitjana": "mean"})
        )

        # Extraigo los valores medios de abandono por año
        valores_abandono = branch_by_year["Taxa abandonament mitjana"].tolist()

        # Aplico una regresión lineal para detectar la tendencia del abandono
        slope, _, _, _, _ = linregress(
            range(len(valores_abandono)),
            valores_abandono,
        )

        # Interpreto la pendiente para clasificar la tendencia
        if slope > 0.01:
            tendencia = "creciente"
        elif slope < -0.01:
            tendencia = "decreciente"
        else:
            tendencia = "estable"

        # Guardo los resultados del análisis de la rama actual
        report["analisis_por_rama"][branch] = {
            "estadisticas": {
                "abandono": {
                    "media": abandono_media,
                    "desviacion_std": abandono_std,
                },
                "rendimiento": {
                    "media": rendimiento_media,
                    "desviacion_std": rendimiento_std,
                },
            },
            "tendencia_abandono": {
                "pendiente": slope,
                "tipo": tendencia,
            },
        }

    # Calculo los rankings de rendimiento y abandono por rama
    ranking_rend = merged_df.groupby("Branca")["Taxa rendiment mitjana"].mean()
    ranking_aband = merged_df.groupby("Branca")["Taxa abandonament mitjana"].mean()

    # Identifico las ramas con mejores y peores resultados
    report["rankings"] = {
        "mejor_rendimiento": ranking_rend.idxmax(),
        "peor_rendimiento": ranking_rend.idxmin(),
        "mayor_abandono": ranking_aband.idxmax(),
        "menor_abandono": ranking_aband.idxmin(),
    }

    # Creo el directorio de salida si no existe
    output_dir = "src/report"
    os.makedirs(output_dir, exist_ok=True)

    # Defino la ruta del archivo JSON
    output_path = os.path.join(output_dir, "analisi_estadistic.json")

    # Guardo el informe en formato JSON
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4, ensure_ascii=False)

    # Muestro un mensaje indicando dónde se ha guardado el informe
    print(f"\nInforme estadístico guardado en: {output_path}")
