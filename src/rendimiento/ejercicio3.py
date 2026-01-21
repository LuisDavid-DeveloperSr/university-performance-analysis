import os
import matplotlib.pyplot as plt


def plot_temporal_trends(df, mi_nombre):
    """
    Genera dos gráficos de series temporales:
    1) Evolución del % de abandono por curso académico
    2) Evolución de la tasa de rendimiento por curso académico

    Parameters
    ----------
    df : pandas.DataFrame
        Dataset final fusionado (salida del Ejercicio 2)
    student_name : str
        Mi nombre
    """

    # Ordeno el DataFrame por curso académico para que las series temporales sean coherentes
    df = df.sort_values("Curs Acadèmic")

    # Cojo las ramas de estudio y una paleta de colores
    branches = df["Branca"].unique()
    colors = plt.get_cmap("tab10").colors

    # Creo la figura con dos subgráficos verticales
    _, axs = plt.subplots(2, 1, figsize=(14, 10))

    # Gráfico 1, de abandono 
    for i, branch in enumerate(branches):
        # Filtro los datos que corresponden a cada rama
        data_branch = df[df["Branca"] == branch]

        # Represento la evolución del abandono para la rama actual
        axs[0].plot(
            data_branch["Curs Acadèmic"],
            data_branch["Taxa abandonament mitjana"],
            label=branch,
            color=colors[i % len(colors)],
        )

    # Configuro títulos, etiquetas y leyenda del primer gráfico
    axs[0].set_title("Evolución del % de Abandono por curso académico")
    axs[0].set_ylabel("% Abandono")
    axs[0].grid(True)
    axs[0].legend()

    # Gráfico 2, de rendimiento
    for i, branch in enumerate(branches):
        # Filtro los datos que corresponden a cada rama
        data_branch = df[df["Branca"] == branch]

        # Represento la evolución del rendimiento para la rama actual
        axs[1].plot(
            data_branch["Curs Acadèmic"],
            data_branch["Taxa rendiment mitjana"],
            label=branch,
            color=colors[i % len(colors)],
        )

    # Configuro títulos, etiquetas y leyenda del segundo gráfico
    axs[1].set_title("Evolución de la Tasa de Rendimiento por curso académico")
    axs[1].set_ylabel("Tasa de rendimiento")
    axs[1].set_xlabel("Curso académico")
    axs[1].grid(True)
    axs[1].legend()

    # Roto las etiquetas del eje X para mejorar la legibilidad
    plt.xticks(rotation=45)

    # Creo la carpeta de salida si no existe
    output_dir = "src/img"
    os.makedirs(output_dir, exist_ok=True)

    # Defino el nombre y la ruta del archivo de salida
    filename = f"evolucion_{mi_nombre}.png"
    filepath = os.path.join(output_dir, filename)

    # Ajusto el diseño, guardo la figura y cierro el gráfico
    plt.tight_layout()
    plt.savefig(filepath, dpi=300)
    plt.close()

    # Muestro un mensaje indicando dónde se ha guardado la imagen
    print(f"\nGráfico guardado en: {filepath}")
