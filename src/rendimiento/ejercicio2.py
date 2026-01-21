import pandas as pd


def rename_abandono_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Renombra las columnas del dataset de abandono para que coincidan
    con el dataset de rendimiento.
    """
    # Renombro las columnas del dataset de abandono 
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
    # Defino las columnas comunes que no se utilizarán en el análisis
    cols = ["Universitat", "Unitat"]

    # Si el dataset es de rendimiento, elimino también columnas de créditos
    if dataset_type == "rendimiento":
        cols += [
            "Crèdits ordinaris superats",
            "Crèdits ordinaris matriculats"
        ]

    # Elimino las columnas indicadas ignorando errores si alguna no existe
    return df.drop(columns=cols, errors="ignore")


def group_by_branch(
    df: pd.DataFrame,
    value_column: str,
    new_column_name: str
) -> pd.DataFrame:
    """
    Agrupa por curso, rama y características comunes y calcula la media.
    """
    # Defino las columnas por las que se van a agrupar los datos
    group_cols = [
        "Curs Acadèmic",
        "Tipus universitat",
        "Sigles",
        "Tipus Estudi",
        "Branca",
        "Sexe",
        "Integrat S/N"
    ]

    # Agrupo los datos y calculo la media de la columna que indico
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
    # Defino las columnas clave comunes a los datasets
    merge_cols = [
        "Curs Acadèmic",
        "Tipus universitat",
        "Sigles",
        "Tipus Estudi",
        "Branca",
        "Sexe",
        "Integrat S/N"
    ]

    # Realizo un merge interno para quedarme solo con las filas que coinciden
    return df_rendimiento.merge(df_abandono, on=merge_cols, how="inner")
