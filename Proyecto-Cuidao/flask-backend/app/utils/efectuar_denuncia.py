import folium
import networkx as nx

from .mostrar_ubicacion_actual import *
from .mostrar_comisarias import *
from .mostrar_ultimos_reportes import *
from .delimitar_distritos import *
from .mostrar_mapa_de_calor import *
from .funcionalidades import *


def dibujar_ruta_hacia_comisaria_mas_cercana(
    mapaCuidao, G, mi_ubicacion, comisarias, comisaria_mas_cercana
):
    # Coordenadas de puntos de interés
    point1 = mi_ubicacion  # Mi ubicación
    point2 = (
        next(c["lat"] for c in comisarias if c["name"] == comisaria_mas_cercana),
        next(c["lng"] for c in comisarias if c["name"] == comisaria_mas_cercana),
    )

    # Buscar el nodo más cercano
    closest_node1 = find_closest_node(G, point1)
    closest_node2 = find_closest_node(G, point2)

    # Si existe un camino entre los dos nodos más cercanos, dibujarlo
    if nx.has_path(G, source=closest_node1, target=closest_node2):
        path = nx.shortest_path(G, source=closest_node1, target=closest_node2)

        # Convertir el camino en una lista de coordenadas
        path_coords = [[node[0], node[1]] for node in path]

        # Añadir la ruta al mapa
        folium.PolyLine(
            locations=path_coords,
            color="red",
            weight=5,
            opacity=0.7,
            tooltip="Ruta más corta",
        ).add_to(mapaCuidao)

        print("Existe un camino entre los dos nodos. Ruta mostrada en el mapa.")
    else:
        print("No existe un camino entre los dos nodos.")


def efectuar_denuncia(mapaCuidao=None):
    if mapaCuidao is None:
        mapaCuidao = crear_mapa_vacio()

    mapaCuidao = mostrar_ubicacion_actual(mapaCuidao)
    mapaCuidao = mostrar_comisarias(mapaCuidao)
    mapaCuidao = mostrar_ultimos_reportes(mapaCuidao)
    mapaCuidao = delimitar_distritos(mapaCuidao)
    mapaCuidao = mostrar_mapa_de_calor(mapaCuidao)

    ubicacion = obtener_ubicacion()
    location = (ubicacion["latitud"], ubicacion["longitud"])

    datos_excel_comisarias = {}
    comisarias = []
    CargarDataToDict("data/Comisarias.xlsx", datos_excel_comisarias, "COMISARÍA", "GPS")
    ConvertirDictToList(datos_excel_comisarias, comisarias)
    G = cargar_calles_json("data/callePrincipal.geojson")
    comisaria_mas_cercana = encontrar_comisaria_mas_cercana(location, comisarias)
    dibujar_ruta_hacia_comisaria_mas_cercana(
        mapaCuidao, G, location, comisarias, comisaria_mas_cercana
    )
    mapaCuidao.save("app/templates/efectuar_denuncia.html")
    return mapaCuidao


if __name__ == "__main__":

    efectuar_denuncia()
