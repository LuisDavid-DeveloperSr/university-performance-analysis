import argparse

from rendimiento.ejercicio1 import load_dataset
from rendimiento.ejercicio2 import (
    rename_abandono_columns,
    drop_unnecessary_columns,
    group_by_branch,
    merge_datasets
)
from rendimiento.ejercicio3 import plot_temporal_trends
from rendimiento.ejercicio4 import analyze_dataset


def run_ejercicio_2(df_r, df_a):
    """
    Ejecuta el proceso completo del Ejercicio 2:
    limpieza, agrupación y fusión de datasets.
    """
    print("\nEjercicio 2, limpieza y unión")

    # Renombro las columnas del dataset de abandono
    df_a = rename_abandono_columns(df_a)

    # Elimino columnas innecesarias en ambos datasets
    df_r = drop_unnecessary_columns(df_r, "rendimiento")
    df_a = drop_unnecessary_columns(df_a, "abandono")

    # Agrupo el dataset de rendimiento por rama y características comunes
    df_r_grouped = group_by_branch(
        df_r,
        "Taxa rendiment",
        "Taxa rendiment mitjana"
    )

    # Agrupo el dataset de abandono por rama y características comunes
    df_a_grouped = group_by_branch(
        df_a,
        "Taxa abandonament",
        "Taxa abandonament mitjana"
    )

    # Fusiono ambos datasets agrupados
    df_final = merge_datasets(df_r_grouped, df_a_grouped)

    # Muestro las primeras filas del dataset final
    print("\nDataset final con las primeras filas:")
    print(df_final.head())

    return df_final


# PUNTO DE ENTRADA DEL PROGRAMA
if __name__ == "__main__":
    # Configuro los argumentos de línea de comandos
    parser = argparse.ArgumentParser(
        description="Análisis del rendimiento universitario en Cataluña"
    )

    parser.add_argument(
        "-ex",
        type=int,
        default=4,
        help="Ejecutar ejercicios desde 1 hasta el número indicado"
    )

    args = parser.parse_args()

    # Cargo los datasets originales
    df_r = load_dataset("data/rendiment_estudiants.xlsx")
    df_a = load_dataset("data/taxa_abandonament.xlsx")

    # Ejecuto el Ejercicio 2 si corresponde
    if args.ex >= 2:
        df_final = run_ejercicio_2(df_r, df_a)

    # Ejecuto el Ejercicio 3 si corresponde
    if args.ex >= 3:
        plot_temporal_trends(
            df_final,
            mi_nombre="Luis_David_Espinal_Espinal"
        )

    # Ejecuto el Ejercicio 4 si corresponde
    if args.ex >= 4:
        analyze_dataset(df_final)
