import json
import os
from datetime import datetime

from scipy.stats import linregress, pearsonr


# --------------------------------------------------
# FUNCIÓN PRINCIPAL (WEB-FRIENDLY)
# --------------------------------------------------

def analyze_dataset(merged_df) -> dict:
    """
    Realiza un análisis estadístico completo del dataset fusionado
    y devuelve el informe como diccionario.

    Parameters
    ----------
    merged_df : pandas.DataFrame
        Dataset final fusionado (salida del Ejercicio 2)

    Returns
    -------
    dict
        Informe estadístico completo
    """

    report = {}

    # -------------------------------
    # Metadata
    # -------------------------------
    report["metadata"] = {
        "fecha_analisis": datetime.now().strftime("%Y-%m-%d"),
        "num_registros": int(len(merged_df)),
        "periodo_temporal": sorted(
            merged_df["Curs Acadèmic"].unique().tolist()
        ),
    }

    abandono = merged_df["Taxa abandonament mitjana"].dropna()
    rendimiento = merged_df["Taxa rendiment mitjana"].dropna()

    corr, p_value = pearsonr(abandono, rendimiento)

    report["estadisticas_globales"] = {
        "abandono_medio": float(abandono.mean()),
        "rendimiento_medio": float(rendimiento.mean()),
        "correlacion_abandono_rendimiento": {
            "coeficiente": float(corr),
            "p_value": float(p_value),
        },
    }

    # -------------------------------
    # Análisis por rama
    # -------------------------------
    report["analisis_por_rama"] = {}

    for branch in merged_df["Branca"].unique():
        branch_data = merged_df[merged_df["Branca"] == branch]

        abandono_media = branch_data["Taxa abandonament mitjana"].mean()
        abandono_std = branch_data["Taxa abandonament mitjana"].std()

        rendimiento_media = branch_data["Taxa rendiment mitjana"].mean()
        rendimiento_std = branch_data["Taxa rendiment mitjana"].std()

        branch_by_year = (
            branch_data
            .groupby("Curs Acadèmic", as_index=False)
            .agg({"Taxa abandonament mitjana": "mean"})
        )

        valores_abandono = branch_by_year[
            "Taxa abandonament mitjana"
        ].tolist()

        slope, _, _, _, _ = linregress(
            range(len(valores_abandono)),
            valores_abandono
        )

        if slope > 0.01:
            tendencia = "creciente"
        elif slope < -0.01:
            tendencia = "decreciente"
        else:
            tendencia = "estable"

        report["analisis_por_rama"][branch] = {
            "estadisticas": {
                "abandono": {
                    "media": float(abandono_media),
                    "desviacion_std": float(abandono_std),
                },
                "rendimiento": {
                    "media": float(rendimiento_media),
                    "desviacion_std": float(rendimiento_std),
                },
            },
            "tendencia_abandono": {
                "pendiente": float(slope),
                "tipo": tendencia,
            },
        }

    # -------------------------------
    # Rankings
    # -------------------------------
    ranking_rend = merged_df.groupby("Branca")[
        "Taxa rendiment mitjana"
    ].mean()

    ranking_aband = merged_df.groupby("Branca")[
        "Taxa abandonament mitjana"
    ].mean()

    report["rankings"] = {
        "mejor_rendimiento": ranking_rend.idxmax(),
        "peor_rendimiento": ranking_rend.idxmin(),
        "mayor_abandono": ranking_aband.idxmax(),
        "menor_abandono": ranking_aband.idxmin(),
    }

    return report


# --------------------------------------------------
# VERSIÓN CLI (GUARDA JSON + PRINT)
# --------------------------------------------------

def analyze_dataset_cli(merged_df):
    """
    Versión para consola del Ejercicio 4.
    Guarda el informe estadístico en un archivo JSON.
    """
    report = analyze_dataset(merged_df)

    output_dir = "src/report"
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(
        output_dir,
        "analisi_estadistic.json"
    )

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4, ensure_ascii=False)

    print(f"\nInforme estadístico guardado en: {output_path}")

    return report
