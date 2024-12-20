import folium
from .funcionalidades import *


def agregar_marcador_personalizado(
    mapa,
    latitud,
    longitud,
    popup_text="Ubicación Actual",
    tooltip_text="Ubicación Actual",
    icon_image="app/static/images/gps.webp",
    icon_size=(30, 30),
):
    # Usar folium.Marker solo cuando realmente sea necesario
    marker = folium.Marker(
        location=[latitud, longitud],
        popup=popup_text,
        tooltip=tooltip_text,
        icon=folium.CustomIcon(icon_image=icon_image, icon_size=icon_size),
    )
    # Añadir marcador al mapa solo si no está ya en el mapa
    marker.add_to(mapa)

def mostrar_ubicacion_actual(mapaCuidao=None):
    # Obtener la ubicación una sola vez
    ubicacion = obtener_ubicacion()
    latitud, longitud = ubicacion["latitud"], ubicacion["longitud"]
    
    # Solo crear el mapa si no ha sido creado previamente
    if mapaCuidao is None:
        mapaCuidao = crear_mapa_vacio()
    
    # Añadir el marcador de forma eficiente
    agregar_marcador_personalizado(mapaCuidao, latitud, longitud)

    return mapaCuidao



if __name__ == "__main__":

    mostrar_ubicacion_actual()
