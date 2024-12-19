import folium
from shapely.geometry import shape, Polygon, MultiPolygon, Point
from .funcionalidades import *


def obtener_color(conteo, total_reportes):
    # Evitar el cálculo de porcentaje repetido. Utilizamos umbrales de manera directa
    porcentaje = (conteo / total_reportes) * 100 if total_reportes else 0

    if porcentaje >= 10:
        return "red"  # Zonas más peligrosas (10% o más de los reportes)
    elif porcentaje >= 3:
        return "orange"  # Zonas de peligro moderado (entre 3% y 10% de los reportes)
    else:
        return "green"  # Zonas menos peligrosas (menos del 3% de los reportes)

def agregar_distritos_al_mapa(data, conteo_distritos, mapa):
    # Precalcular el total de reportes
    total_reportes = sum(conteo_distritos.values())
    
    # Utilizamos una lista para acumular todos los polígonos y agregarlos de una sola vez
    polygons = []

    # Iteramos sobre los distritos, procesando las geometrías de forma eficiente
    for feature in data["features"]:
        distrito_nombre = feature["properties"].get("name", "Distrito desconocido")
        distrito_poligono = shape(feature["geometry"])
        conteo = conteo_distritos.get(distrito_nombre, 0)  # Usamos `.get` en lugar de `[]` para evitar errores
        color = obtener_color(conteo, total_reportes)  # Pasamos el total de reportes

        if isinstance(distrito_poligono, Polygon):
            coords = [(point[1], point[0]) for point in distrito_poligono.exterior.coords]
            polygons.append((coords, color, distrito_nombre))
        elif isinstance(distrito_poligono, MultiPolygon):
            # Procesamos todos los polígonos dentro del MultiPolygon
            for poly in distrito_poligono.geoms:
                coords = [(point[1], point[0]) for point in poly.exterior.coords]
                polygons.append((coords, color, distrito_nombre))

    # Agregar todos los polígonos de una vez al mapa, reduciendo las llamadas a `folium.Polygon`
    for coords, color, distrito_nombre in polygons:
        folium.Polygon(
            locations=coords,
            color=color,
            weight=2,
            fill=True,
            fill_opacity=0.3,
            popup=distrito_nombre,
        ).add_to(mapa)

    print("Mapa de calor cargado correctamente en el mapa")

def mostrar_mapa_de_calor(mapaCuidao=None):

    if mapaCuidao is None:
        mapaCuidao = crear_mapa_vacio()

    _, conteo_distritos = cargar_datos_y_contar_distritos()
    dataGeojson = obtener_geojson_distritos()
    agregar_distritos_al_mapa(dataGeojson, conteo_distritos, mapaCuidao)

    return mapaCuidao


if __name__ == "__main__":
    mostrar_mapa_de_calor()
