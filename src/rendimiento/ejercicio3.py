import os
import matplotlib.pyplot as plt


# --------------------------------------------------
# FUNCIÓN PRINCIPAL (WEB-FRIENDLY)
# --------------------------------------------------

def plot_temporal_trends(df):
    """
    Genera dos gráficos de series temporales:
    1) Evolución del % de abandono por curso académico
    2) Evolución de la tasa de rendimiento por curso académico

    Parameters
    ----------
    df : pandas.DataFrame
        Dataset final fusionado (salida del Ejercicio 2)

    Returns
    -------
    matplotlib.figure.Figure
        Figura generada
    """

    # Ordeno el DataFrame por curso académico
    df = df.sort_values("Curs Acadèmic")

    branches = df["Branca"].unique()
    colors = plt.get_cmap("tab10").colors

    fig, axs = plt.subplots(2, 1, figsize=(14, 10))

    # -------------------------------
    # Gráfico 1 — Abandono
    # -------------------------------
    for i, branch in enumerate(branches):
        data_branch = df[df["Branca"] == branch]

        axs[0].plot(
            data_branch["Curs Acadèmic"],
            data_branch["Taxa abandonament mitjana"],
            label=branch,
            color=colors[i % len(colors)],
        )

    axs[0].set_title("Evolución del % de Abandono por curso académico")
    axs[0].set_ylabel("% Abandono")
    axs[0].grid(True)
    axs[0].legend()

    # -------------------------------
    # Gráfico 2 — Rendimiento
    # -------------------------------
    for i, branch in enumerate(branches):
        data_branch = df[df["Branca"] == branch]

        axs[1].plot(
            data_branch["Curs Acadèmic"],
            data_branch["Taxa rendiment mitjana"],
            label=branch,
            color=colors[i % len(colors)],
        )

    axs[1].set_title("Evolución de la Tasa de Rendimiento por curso académico")
    axs[1].set_ylabel("Tasa de rendimiento")
    axs[1].set_xlabel("Curso académico")
    axs[1].grid(True)
    axs[1].legend()

    plt.xticks(rotation=45)
    plt.tight_layout()

    return fig


# --------------------------------------------------
# VERSIÓN CLI (GUARDA IMAGEN + PRINTS)
# --------------------------------------------------

def plot_temporal_trends_cli(df, mi_nombre: str):
    """
    Versión para consola del Ejercicio 3.
    Guarda el gráfico en disco y muestra mensajes.
    """
    fig = plot_temporal_trends(df)

    output_dir = "src/img"
    os.makedirs(output_dir, exist_ok=True)

    filename = f"evolucion_{mi_nombre}.png"
    filepath = os.path.join(output_dir, filename)

    fig.savefig(filepath, dpi=300)
    plt.close(fig)

    print(f"\nGráfico guardado en: {filepath}")
