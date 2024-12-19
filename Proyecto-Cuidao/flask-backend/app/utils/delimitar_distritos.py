import folium
from shapely.geometry import shape, Polygon, MultiPolygon , Point
from .funcionalidades import *

def agregar_distritos_al_mapa(data, mapa):
    # Lista para almacenar los polígonos y evitar múltiples adiciones al mapa
    district_polygons = []
    
    # Pre-calcular la geometría solo una vez y evitar el uso repetido de 'shape' y otras operaciones costosas
    for feature in data['features']:
        # Obtener el nombre del distrito o un valor predeterminado si no está presente
        distrito_nombre = feature['properties'].get('name', 'Distrito desconocido')
        
        # Obtener la geometría del distrito solo una vez
        distrito_poligono = shape(feature['geometry'])

        if isinstance(distrito_poligono, Polygon):
            coords = [(point[1], point[0]) for point in distrito_poligono.exterior.coords]
            district_polygons.append({
                'coords': coords,
                'popup': distrito_nombre
            })
        elif isinstance(distrito_poligono, MultiPolygon):
            for poly in distrito_poligono.geoms:
                coords = [(point[1], point[0]) for point in poly.exterior.coords]
                district_polygons.append({
                    'coords': coords,
                    'popup': distrito_nombre
                })

    # Añadir todos los polígonos al mapa de una sola vez
    for polygon in district_polygons:
        folium.Polygon(
            locations=polygon['coords'],
            weight=2,
            fill=True,
            fill_opacity=0,
            popup=polygon['popup']
        ).add_to(mapa)
        
    print("Distritos cargados correctamente en el mapa")

def delimitar_distritos(mapaCuidao = None):

    if mapaCuidao is None:
        mapaCuidao = crear_mapa_vacio()

    dataGeojson = obtener_geojson_distritos()
    agregar_distritos_al_mapa(dataGeojson , mapaCuidao)

    return mapaCuidao

if __name__ == "__main__":
    delimitar_distritos()
