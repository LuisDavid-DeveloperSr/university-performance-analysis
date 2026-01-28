import pandas as pd


# --------------------------------------------------
# FUNCIONES DE TRANSFORMACIÓN (PURAS)
# --------------------------------------------------

def rename_abandono_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Renombra las columnas del dataset de abandono para que coincidan
    con el dataset de rendimiento.
    """
    return df.rename(columns={
        "Naturalesa universitat responsable": "Tipus universitat",
        "Universitat Responsable": "Universitat",
        "Sexe Alumne": "Sexe",
        "Tipus de centre": "Integrat S/N",
        "% Abandonament a primer curs": "Taxa abandonament"
    })


def drop_unnecessary_columns(df: pd.DataFrame, dataset_type: str) -> pd.DataFrame:
    """
    Elimina columnas innecesarias según el tipo de dataset.
    """
    cols = ["Universitat", "Unitat"]

    if dataset_type == "rendimiento":
        cols += [
            "Crèdits ordinaris superats",
            "Crèdits ordinaris matriculats"
        ]

    return df.drop(columns=cols, errors="ignore")


def group_by_branch(
    df: pd.DataFrame,
    value_column: str,
    new_column_name: str
) -> pd.DataFrame:
    """
    Agrupa por curso, rama y características comunes y calcula la media.
    """
    group_cols = [
        "Curs Acadèmic",
        "Tipus universitat",
        "Sigles",
        "Tipus Estudi",
        "Branca",
        "Sexe",
        "Integrat S/N"
    ]

    return (
        df.groupby(group_cols, as_index=False)[value_column]
        .mean()
        .rename(columns={value_column: new_column_name})
    )


def merge_datasets(
    df_rendimiento: pd.DataFrame,
    df_abandono: pd.DataFrame
) -> pd.DataFrame:
    """
    Fusiona ambos datasets usando inner merge.
    """
    merge_cols = [
        "Curs Acadèmic",
        "Tipus universitat",
        "Sigles",
        "Tipus Estudi",
        "Branca",
        "Sexe",
        "Integrat S/N"
    ]

    return df_rendimiento.merge(df_abandono, on=merge_cols, how="inner")


# --------------------------------------------------
# PIPELINE COMPLETO (WEB-FRIENDLY)
# --------------------------------------------------

def run_ejercicio_2(
    df_rendimiento: pd.DataFrame,
    df_abandono: pd.DataFrame
) -> pd.DataFrame:
    """
    Ejecuta el proceso completo del Ejercicio 2:
    limpieza, agrupación y fusión de datasets.

    Devuelve el DataFrame final (sin prints).
    """
    # Limpieza dataset abandono
    df_abandono = rename_abandono_columns(df_abandono)
    df_abandono = drop_unnecessary_columns(df_abandono, "abandono")

    # Limpieza dataset rendimiento
    df_rendimiento = drop_unnecessary_columns(df_rendimiento, "rendimiento")

    # Agrupaciones
    df_r_grouped = group_by_branch(
        df_rendimiento,
        "Taxa rendiment",
        "Taxa rendiment mitjana"
    )

    df_a_grouped = group_by_branch(
        df_abandono,
        "Taxa abandonament",
        "Taxa abandonament mitjana"
    )

    # Merge final
    df_final = merge_datasets(df_r_grouped, df_a_grouped)

    return df_final


# --------------------------------------------------
# VERSIÓN CLI (OPCIONAL, PERO MUY PRO)
# --------------------------------------------------

def run_ejercicio_2_cli(
    df_rendimiento: pd.DataFrame,
    df_abandono: pd.DataFrame
) -> pd.DataFrame:
    """
    Versión para consola del Ejercicio 2 (con prints).
    """
    print("\nEjercicio 2 — Limpieza y unión de datasets")

    df_final = run_ejercicio_2(df_rendimiento, df_abandono)

    print("\nPrimeras filas del dataset final:")
    print(df_final.head())

    print("\nDimensiones del dataset final:")
    print(df_final.shape)

    return df_final
