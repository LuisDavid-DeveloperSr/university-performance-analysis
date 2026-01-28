# Rendimiento académico y abandono universitario en Cataluña

# Autor: Luis David Espinal Espinal

# Descripción del proyecto

Este proyecto analiza el rendimiento académico y la tasa de abandono de los estudiantes universitarios en Cataluña a partir de datos oficiales publicados por la Generalitat de Catalunya.

El objetivo principal es estudiar la relación entre ambas variables, identificar tendencias temporales, y obtener métricas estadísticas que permitan interpretar la evolución del sistema universitario por ramas de estudio.

El proyecto se ha desarrollado siguiendo una arquitectura modular en Python, con dos formas de uso claramente diferenciadas:

🔹 Ejecución por línea de comandos (CLI)

🔹 Dashboard web interactivo con Streamlit

🔍 Contenido del análisis

El análisis incluye las siguientes fases:

- Exploración inicial de los datasets originales

- Limpieza y normalización de los datos

- Agrupación por rama de estudio y características comunes

- Fusión de múltiples fuentes de datos

- Análisis visual de tendencias temporales

- Análisis estadístico automatizado

- Generación de informes en formato JSON

🌐 Aplicación web (Streamlit)

Además de la ejecución por consola, el proyecto incluye una aplicación web interactiva desarrollada con Streamlit, que permite explorar el análisis de forma visual y dinámica.

Características del dashboard:

- Navegación por secciones del análisis

- Exploración interactiva de los datasets

- Visualización de tendencias temporales

- Métricas estadísticas tipo KPI

- Rankings por rama de estudio

- Visualización del informe estadístico completo en JSON

- Estilo visual personalizado con CSS externo

- Soporte automático para modo claro y oscuro

La lógica del análisis y el estilo visual están desacoplados, permitiendo modificar el diseño sin afectar al funcionamiento del programa.

# Ejecución de la aplicación web

Desde la raíz del proyecto:

streamlit run app.py

Esto abrirá el dashboard en el navegador por defecto.

# Ejecución por línea de comandos (CLI)

El proyecto puede ejecutarse íntegramente desde la terminal mediante main.py.

Ejecutar todos los ejercicios:
python main.py

Ejecutar solo el ejercicio 1:
python main.py -ex 1

Ejecutar hasta el ejercicio 2:
python main.py -ex 2

Ejecutar hasta el ejercicio 3:
python main.py -ex 3

Mostrar ayuda:
python main.py -h

# Estructura del proyecto

Activity_4/
├── app.py                  # Aplicación web (Streamlit)
├── assets/
│   └── style.css           # Estilos y animaciones del dashboard
├── main.py                 # Punto de entrada CLI
├── requirements.txt
├── setup.py
├── .pylintrc
├── src/
│   └── rendimiento/
│       ├── __init__.py
│       ├── ejercicio1.py   # Exploración de datos
│       ├── ejercicio2.py   # Limpieza y fusión
│       ├── ejercicio3.py   # Análisis temporal
│       ├── ejercicio4.py   # Análisis estadístico
│       ├── img/
│       │   └── evolucion_Luis_David_Espinal_Espinal.png
│       └── report/
│           └── analisi_estadistic.json
├── tests/
│   ├── test_ejercicio1.py
│   ├── test_ejercicio2.py
│   ├── test_ejercicio3.py
│   └── test_ejercicio4.py
├── doc/
│   ├── src.rendimiento.ejercicio1.html
│   ├── src.rendimiento.ejercicio2.html
│   ├── src.rendimiento.ejercicio3.html
│   └── src.rendimiento.ejercicio4.html
└── screenshots/
    ├── coverage.png
    ├── tests.png
    ├── linting.png
    ├── ejecucion.png
    └── documentacion.png

# Instalación

Instalar las dependencias del proyecto:

pip install -r requirements.txt

# Tests

Ejecutar todos los tests:

pytest


Ejecutar tests con cobertura:

pytest --cov=src --cov-report=term-missing

# Documentación

La documentación HTML se genera automáticamente a partir de los docstrings utilizando pydoc.

Desde la raíz del proyecto:

python -m pydoc -w src.rendimiento.ejercicio1
python -m pydoc -w src.rendimiento.ejercicio2
python -m pydoc -w src.rendimiento.ejercicio3
python -m pydoc -w src.rendimiento.ejercicio4

# Linting

El código sigue la guía PEP8 y se ha validado con pylint.

pylint src/rendimiento

# Resultados generados

Gráficos:
src/rendimiento/img/

Informe estadístico en JSON:
src/rendimiento/report/analisi_estadistic.json

# Licencia

Este proyecto se distribuye bajo la licencia MIT.
Consulta el archivo LICENSE para más información.

# Demo en vivo

La aplicación está desplegada públicamente en Streamlit Cloud:
https://university-performance-analysis-v4yyylcpfginmumyk6ic2a.streamlit.app/
