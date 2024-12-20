from .manejar_data import *
from .funcionalidades import *
from shapely.geometry import shape, Point

ubicacion_seleccionada = {"latitud": None, "longitud": None}


# Convertir el punto a un objeto Point de Shapely (Maneja mejor el espacio) para encontrar el distrito en el que está
def obtener_distrito_de_punto(punto, data):
    punto_obj = Point(
        punto[1], punto[0]
    )  # (longitud, latitud) asi lo manejan las librerias xd

    # Iterar sobre los distritos en los datos
    for feature in data["features"]:
        distrito_nombre = feature["properties"].get("name", "Distrito desconocido")
        distrito_geometria = shape(feature["geometry"])

        # Verificar si el punto está dentro del distrito
        if distrito_geometria.contains(punto_obj):
            return distrito_nombre
    # Si no se encontró ningún distrito, devolver 'Distrito desconocido'
    return "Distrito desconocido"
