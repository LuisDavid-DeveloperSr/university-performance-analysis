from rendimiento.ejercicio1 import load_dataset


def test_load_dataset_with_path():
    # Compruebo que la función carga correctamente el dataset cuando se pasa una ruta
    df = load_dataset("data/rendiment_estudiants.xlsx")

    # Verifico que el DataFrame resultante no esté vacío
    assert not df.empty
