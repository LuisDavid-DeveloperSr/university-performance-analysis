import pandas as pd


def load_dataset(path: str | None = None) -> pd.DataFrame:
    """
    Carga uno de los datasets disponibles y realiza una EDA básica.

    Parameters
    ----------
    path : str, optional
        Ruta al archivo Excel.

    Returns
    -------
    pd.DataFrame
    """

    # Si no se proporciona una ruta pregunto al usuario qué dataset quiere cargar
    if path is None:
        print("Seleccione el dataset que desea cargar:")
        print("1 - Tasa de rendimiento")
        print("2 - Tasa de abandono")
        option = input("Introduzca 1 o 2: ")

        # Asigno la ruta según la opción seleccionada
        if option == "1":
            path = "data/rendiment_estudiants.xlsx"
        elif option == "2":
            path = "data/taxa_abandonament.xlsx"
        else:
            # Imprimo un error si la opción introducida no es válida
            raise ValueError("Opción no válida")

    # Cargo el dataset desde el archivo Excel
    df = pd.read_excel(path)

    # Muestro las primeras filas 
    print("\nPrimeras 5 filas:")
    print(df.head())

    # Muestro las columnas del DataFrame
    print("\nColumnas del DataFrame:")
    print(df.columns.tolist())

    # Muestro información general del DataFrame
    print("\nInformación del DataFrame:")
    df.info()

    return df
