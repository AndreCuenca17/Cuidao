import folium
from folium.plugins import MarkerCluster
from .funcionalidades import *
import pickle

def agregar_comisarias_al_mapa(
    mapa, lista_comisarias, icon_image="app/static/images/pnp.png", icon_size=(30, 30)
):
    # Crear un MarkerCluster para agrupar los marcadores
    marker_cluster = MarkerCluster().add_to(mapa)
    
    for comisaria in lista_comisarias:
        lat = comisaria["lat"]
        lng = comisaria["lng"]
        nombre = comisaria["name"]
        
        # Crear el marcador y añadirlo al MarkerCluster
        folium.Marker(
            location=[lat, lng],
            popup=nombre,
            tooltip=nombre,
            icon=folium.CustomIcon(icon_image=icon_image, icon_size=icon_size),
        ).add_to(marker_cluster)

    print("Las comisarias fueron cargadas correctamente al mapa")

def cargar_comisarias_desde_cache():
    try:
        with open('cache/comisarias_cache.pkl', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        # Si no hay caché, leer desde el archivo Excel
        datos_excel_comisarias = {}
        CargarDataToDict("data/Comisarias.xlsx", datos_excel_comisarias, "COMISARÍA", "GPS")
        comisarias = []
        ConvertirDictToList(datos_excel_comisarias, comisarias)
        
        # Guardar los datos en caché para la próxima vez
        with open('comisarias_cache.pkl', 'wb') as file:
            pickle.dump(comisarias, file)
        
        return comisarias


def mostrar_comisarias(mapaCuidao=None):
    
    if mapaCuidao is None:
        mapaCuidao = crear_mapa_vacio()

    comisarias = cargar_comisarias_desde_cache()
    agregar_comisarias_al_mapa(mapaCuidao, comisarias)

    return mapaCuidao


if __name__ == "__main__":

    mostrar_comisarias()
