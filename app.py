import streamlit as st

from src.rendimiento.ejercicio1 import load_dataset, eda_basic
from src.rendimiento.ejercicio2 import run_ejercicio_2
from src.rendimiento.ejercicio3 import plot_temporal_trends
from src.rendimiento.ejercicio4 import analyze_dataset

def load_css(path: str):
    with open(path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


load_css("assets/style.css")

# Configuración general
st.set_page_config(
    page_title="Rendimiento universitario en Cataluña",
    layout="wide"
)

# Cabecera
st.title("Rendimiento académico y abandono universitario")
st.caption(
    "Aplicación para el análisis de datos universitarios "
    "basados en fuentes oficiales de la Generalitat de Catalunya."
)

# Navegación
st.sidebar.title("Secciones")

opcion = st.sidebar.radio(
    "Explorar",
    [
        "Inicio",
        "Exploración de datos",
        "Preparación de datos",
        "Análisis temporal",
        "Análisis estadístico"
    ]
)

# INICIO
if opcion == "Inicio":
    st.header("Visión general")

    st.write("""
Esta aplicación permite analizar la relación entre el **rendimiento académico**
y la **tasa de abandono universitario** en Cataluña a lo largo del tiempo y
entre distintas ramas de estudio.

El flujo de análisis está diseñado para ser explorado de forma interactiva,
permitiendo entender los datos desde su origen hasta las métricas finales.
""")

    st.subheader("Qué puedes hacer aquí")
    st.write("""
- Explorar los datasets originales
- Preparar y fusionar distintas fuentes de datos
- Visualizar tendencias temporales
- Analizar métricas y rankings clave
""")

# EXPLORACIÓN
elif opcion == "Exploración de datos":
    st.header("Exploración de datos")

    datasets = {
        "Rendimiento académico": "data/rendiment_estudiants.xlsx",
        "Tasa de abandono": "data/taxa_abandonament.xlsx"
    }

    dataset_name = st.selectbox(
        "Selecciona un dataset",
        list(datasets.keys())
    )

    df = load_dataset(datasets[dataset_name])
    eda = eda_basic(df)

    st.dataframe(eda["head"], use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Filas", eda["shape"][0])
    with col2:
        st.metric("Columnas", eda["shape"][1])

    st.subheader("Estructura del dataset")
    st.write(eda["columns"])

# PREPARACIÓN
elif opcion == "Preparación de datos":
    st.header("Preparación y fusión")

    if st.button("Ejecutar preparación"):
        with st.spinner("Preparando datos..."):
            df_r = load_dataset("data/rendiment_estudiants.xlsx")
            df_a = load_dataset("data/taxa_abandonament.xlsx")
            df_final = run_ejercicio_2(df_r, df_a)
            st.session_state["df_final"] = df_final

        st.success("Datos preparados correctamente")

        st.subheader("Vista rápida")
        st.dataframe(df_final.head(), use_container_width=True)

        st.subheader("Dataset completo")
        st.dataframe(df_final, use_container_width=True)

# TEMPORAL
elif opcion == "Análisis temporal":
    st.header("Análisis temporal")

    if "df_final" not in st.session_state:
        st.warning("Primero prepara los datos.")
        st.stop()

    if st.button("Generar análisis temporal"):
        with st.spinner("Generando gráficos..."):
            fig = plot_temporal_trends(st.session_state["df_final"])
        st.pyplot(fig)

# ESTADÍSTICO
elif opcion == "Análisis estadístico":
    st.header("Análisis estadístico")

    if "df_final" not in st.session_state:
        st.warning("Primero prepara los datos.")
        st.stop()

    if st.button("Calcular métricas"):
        with st.spinner("Calculando métricas..."):
            report = analyze_dataset(st.session_state["df_final"])
            st.session_state["report"] = report

    if "report" in st.session_state:
        report = st.session_state["report"]

        tabs = st.tabs([
            "Métricas",
            "Rankings",
            "Informe completo"
        ])

        with tabs[0]:
            col1, col2, col3 = st.columns(3)
            col1.metric("Abandono medio", f"{report['estadisticas_globales']['abandono_medio']:.2f}")
            col2.metric("Rendimiento medio", f"{report['estadisticas_globales']['rendimiento_medio']:.2f}")
            col3.metric(
                "Correlación",
                f"{report['estadisticas_globales']['correlacion_abandono_rendimiento']['coeficiente']:.2f}"
            )

        with tabs[1]:
            st.write(report["rankings"])

        with tabs[2]:
            st.json(report)
