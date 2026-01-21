# PEC4 

Autor: Luis David Espinal Espinal 
Asignatura: Programación para la Ciencia de Datos  
Curso: 2025–2026  

# Descripción del proyecto

Este proyecto analiza el rendimiento académico y la tasa de abandono de los estudiantes universitarios en Cataluña a partir de datos oficiales publicados por la Generalitat de Catalunya.

El análisis incluye:
- Exploración inicial de los datasets
- Limpieza y fusión de datos
- Análisis visual de tendencias temporales
- Análisis estadístico automatizado con generación de informes

El proyecto se ha desarrollado como un paquete Python modular, ejecutable desde línea de comandos.

# Estructura 

Activity_4/
│
├── LUIS DAVID ESPINAL ESPINAL
├── README.md
├── LICENSE
├── requirements.txt
├── setup.py
├── .pylintrc
├── main.py
│
├── src/
│   ├── rendimiento/
│   │   ├── _init_.py
│   │   ├── ejercicio1.py
│   │   ├── ejercicio2.py
│   │   ├── ejercicio3.py
│   │   └── ejercicio4.py
│   │
│   ├── img/
│   │   └── evolucion_Luis_David_Espinal_Espinal.png
│   │
│   └── report/
│       └── analisi_estadistic.json
│
├── tests/
│   ├── test_ejercicio1.py
│   ├── test_ejercicio2.py
│   ├── test_ejercicio3.py
│   └── test_ejercicio4.py
│
├── doc/
│   ├── src.rendimiento.ejercicio1.html
│   ├── src.rendimiento.ejercicio2.html
│   ├── src.rendimiento.ejercicio3.html
│   └── src.rendimiento.ejercicio4.html
│
└── screenshots/
    ├── coverage.png
    ├── tests.png
    ├── linting.png
    ├── ejecucion.png
    └── documentacion.png

# Instalación

* Instalar dependencias: pip install -r requirements.txt
* Comprobar la instalación: python -m pytest
* Si se ejecutan los test sin errores es una manera para ver si está correcto

* Ejecución del proyecto

Ejecuta todos los ejercicios: python main.py
Ejecuta solo el ejercicio 1: python main.py -ex 1
Ejecuta hasta el Ejercicio 2: python main.py -ex 2
Ejecuta hasta el Ejercicio 3: python main.py -ex 3

* Muestra ayuda: python main.py -h

* Resultados

Gráficos generados en: src/img/

Informe estadístico JSON en: src/report/analisi_estadistic.json

* Tests 

Ejecutar tests: pytest

Ejecutar tests con cobertura: pytest --cov=src --cov-report=term-missing

# Documentación

La documentación HTML se genera automáticamente a partir de los docstrings
utilizando pydoc.
Desde la raíz del proyecto se ejecutan los siguientes comandos:

python -m pydoc -w src.rendimiento.ejercicio1
python -m pydoc -w src.rendimiento.ejercicio2
python -m pydoc -w src.rendimiento.ejercicio3
python -m pydoc -w src.rendimiento.ejercicio4

* Linting 

El código sigue la guía PEP8 y se ha validado con pylint.

Ejecutar: pylint src/rendimiento

* Capturas de pantalla

Las capturas requeridas se encuentran en la carpeta screenshots/:

* Documentación generada

Ejecución de tests y coverage

Ejecución del linter

# Licencia

MIT License

Copyright (c) 2026 Luis David Espinal Espinal

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

