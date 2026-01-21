import pandas as pd

from rendimiento.ejercicio2 import (
    rename_abandono_columns,
    drop_unnecessary_columns,
    group_by_branch,
    merge_datasets,
)


def test_rename_abandono_columns():
    # Creo un DataFrame de ejemplo con los nombres originales del dataset de abandono
    df = pd.DataFrame({
        "Naturalesa universitat responsable": ["PÚBLICA"],
        "Universitat Responsable": ["UB"],
        "Sexe Alumne": ["HOME"],
        "Tipus de centre": ["Integrat"],
        "% Abandonament a primer curs": [0.1],
    })

    # Aplico la función de renombrado de columnas
    df_renamed = rename_abandono_columns(df)

    # Compruebo que las columnas han sido renombradas correctamente
    assert "Tipus universitat" in df_renamed.columns
    assert "Universitat" in df_renamed.columns
    assert "Sexe" in df_renamed.columns
    assert "Integrat S/N" in df_renamed.columns
    assert "Taxa abandonament" in df_renamed.columns


def test_drop_unnecessary_columns_rendimiento():
    # Creo un DataFrame con columnas que deben eliminarse en el dataset de rendimiento
    df = pd.DataFrame({
        "Universitat": ["UB"],
        "Unitat": ["Facultat"],
        "Crèdits ordinaris superats": [30],
        "Crèdits ordinaris matriculats": [60],
        "Taxa rendiment": [0.5],
    })

    # Elimino las columnas innecesarias
    df_clean = drop_unnecessary_columns(df, dataset_type="rendimiento")

    # Verifico que las columnas no relevantes han sido eliminadas
    assert "Universitat" not in df_clean.columns
    assert "Unitat" not in df_clean.columns
    assert "Crèdits ordinaris superats" not in df_clean.columns
    assert "Crèdits ordinaris matriculats" not in df_clean.columns

    # Compruebo que la columna importante se mantiene
    assert "Taxa rendiment" in df_clean.columns


def test_group_by_branch():
    # Creo un DataFrame de ejemplo con dos registros del mismo estudio pero distinto sexo
    df = pd.DataFrame({
        "Curs Acadèmic": ["20-21", "20-21"],
        "Tipus universitat": ["PÚBLICA", "PÚBLICA"],
        "Sigles": ["UB", "UB"],
        "Tipus Estudi": ["Grau", "Grau"],
        "Branca": ["Economia", "Economia"],
        "Sexe": ["HOME", "DONA"],
        "Integrat S/N": ["Integrat", "Integrat"],
        "Taxa rendiment": [0.8, 0.9],
    })

    # Agrupo los datos por las columnas clave y calculo la media del rendimiento
    result = group_by_branch(
        df,
        value_column="Taxa rendiment",
        new_column_name="Taxa rendiment mitjana",
    )

    # Compruebo que se mantienen los grupos separados por sexo
    assert len(result) == 2
    assert 0.8 in result["Taxa rendiment mitjana"].values
    assert 0.9 in result["Taxa rendiment mitjana"].values


def test_merge_datasets():
    # Creo un DataFrame de rendimiento ya agrupado
    df_r = pd.DataFrame({
        "Curs Acadèmic": ["20-21"],
        "Tipus universitat": ["PÚBLICA"],
        "Sigles": ["UB"],
        "Tipus Estudi": ["Grau"],
        "Branca": ["Economia"],
        "Sexe": ["HOME"],
        "Integrat S/N": ["Integrat"],
        "Taxa rendiment mitjana": [0.85],
    })

    # Creo un DataFrame de abandono ya agrupado
    df_a = pd.DataFrame({
        "Curs Acadèmic": ["20-21"],
        "Tipus universitat": ["PÚBLICA"],
        "Sigles": ["UB"],
        "Tipus Estudi": ["Grau"],
        "Branca": ["Economia"],
        "Sexe": ["HOME"],
        "Integrat S/N": ["Integrat"],
        "Taxa abandonament mitjana": [0.10],
    })

    # Fusiono ambos datasets
    merged = merge_datasets(df_r, df_a)

    # Verifico que la fusión es correcta y contiene ambas métricas
    assert len(merged) == 1
    assert "Taxa rendiment mitjana" in merged.columns
    assert "Taxa abandonament mitjana" in merged.columns
