import folium
from .funcionalidades import *


def crear_mapa_con_puntos(datos, mapa):
    # Preprocesar íconos para tipos de robo
    iconos = {
        "Robo": "app/static/images/robo.png",
        "Hurto": "app/static/images/hurto.png",
        "default": "app/static/images/danger.webp",
    }

    # Crear marcadores y agregarlos al mapa
    for dato in datos:
        lat = dato["latitud"]
        lon = dato["longitud"]
        distrito = dato["distrito"]
        tipo_robo = dato["tipo_robo"] if dato["tipo_robo"] != "Otros" else dato["descripcion"]
        
        # Determinar el ícono adecuado
        icon_image = iconos.get(tipo_robo, iconos["default"])

        # Crear el marcador y añadirlo al mapa
        folium.Marker(
            location=[lat, lon],
            popup=f"Distrito: {distrito}<br>Tipo de Robo: {tipo_robo}",
            icon=folium.CustomIcon(icon_image, icon_size=(30, 30)),
        ).add_to(mapa)

    print("Lugares peligrosos cargados exitosamente al mapa")


def mostrar_ultimos_reportes(mapaCuidao=None):

    if mapaCuidao is None:
        mapaCuidao = crear_mapa_vacio()
    datosDistritos, _ = cargar_datos_y_contar_distritos()
    crear_mapa_con_puntos(datosDistritos, mapaCuidao)
    
    return mapaCuidao


if __name__ == "__main__":

    mostrar_ultimos_reportes()
