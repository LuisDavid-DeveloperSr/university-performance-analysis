import pandas as pd


def load_dataset(path: str) -> pd.DataFrame:
    """
    Carga un dataset desde un archivo Excel.

    Parameters
    ----------
    path : str
        Ruta al archivo Excel.

    Returns
    -------
    pd.DataFrame
    """
    return pd.read_excel(path)


def eda_basic(df: pd.DataFrame) -> dict:
    """
    Realiza una EDA básica y devuelve la información.

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    dict
        Diccionario con head, columnas y shape
    """
    return {
        "head": df.head(),
        "columns": df.columns.tolist(),
        "shape": df.shape,
        "dtypes": df.dtypes
    }


# ⚠️ OPCIONAL (solo si quieres mantener CLI)
def load_dataset_cli(path: str | None = None) -> pd.DataFrame:
    """
    Versión CLI del cargador de datasets (consola).
    """
    if path is None:
        print("Seleccione el dataset que desea cargar:")
        print("1 - Tasa de rendimiento")
        print("2 - Tasa de abandono")
        option = input("Introduzca 1 o 2: ")

        if option == "1":
            path = "data/rendiment_estudiants.xlsx"
        elif option == "2":
            path = "data/taxa_abandonament.xlsx"
        else:
            raise ValueError("Opción no válida")

    df = pd.read_excel(path)

    print("\nPrimeras 5 filas:")
    print(df.head())

    print("\nColumnas:")
    print(df.columns.tolist())

    print("\nInformación:")
    df.info()

    return df
