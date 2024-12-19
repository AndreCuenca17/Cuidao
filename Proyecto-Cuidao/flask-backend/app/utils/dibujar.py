
def agregar_marcador_personalizado(mapa, latitud, longitud, popup_text="Ubicación Actual", tooltip_text="Ubicación Actual", icon_image="app/static/images/gps.webp", icon_size=(30, 30)):

    """
    Añade un marcador personalizado a un mapa de Folium.

    Parámetros:
    - mapa: El objeto de mapa de Folium donde se añadirá el marcador.
    - latitud: Coordenada de latitud para la ubicación del marcador.
    - longitud: Coordenada de longitud para la ubicación del marcador.
    - popup_text: Texto que aparecerá en el popup al hacer clic en el marcador.
    - tooltip_text: Texto que aparecerá al pasar el cursor sobre el marcador.
    - icon_image: Ruta a la imagen del ícono personalizado para el marcador.
    - icon_size: Tamaño del ícono personalizado (ancho, alto).
    """
    # Añadir el marcador al mapa
    folium.Marker(
        location=[latitud, longitud],
        popup=popup_text,
        tooltip=tooltip_text,
        icon=folium.CustomIcon(icon_image=icon_image, icon_size=icon_size)
    ).add_to(mapa)
    
    print("La ubicacion fue cargada exitosamente en el mapa")

def agregar_comisarias_al_mapa(mapa, lista_comisarias, icon_image="app/static/images/pnp.png", icon_size=(30, 30)):
    """
    Añade marcadores de comisarías al mapa de Folium.

    Parámetros:
    - mapa: El objeto de mapa de Folium donde se añadirán las comisarías.
    - lista_comisarias: Lista de diccionarios, cada uno con 'name', 'lat', y 'lng' para la ubicación y nombre de la comisaría.
    - icon_image: Ruta a la imagen del ícono personalizado para cada comisaría.
    - icon_size: Tamaño del ícono personalizado (ancho, alto).
    """
    for comisaria in lista_comisarias:
        # Obtener los datos de la comisaría
        lat = comisaria['lat']
        lng = comisaria['lng']
        nombre = comisaria['name']

        # Añadir el marcador al mapa
        folium.Marker(
            location=[lat, lng],
            popup=nombre,
            tooltip=nombre,
            icon=folium.CustomIcon(icon_image=icon_image, icon_size=icon_size)
        ).add_to(mapa)
    
    print("Las comisarias fueron cargadas correctamente al mapa")

# Función para crear un mapa con la data de los puntos peligrosos
def crear_mapa_con_puntos(datos, mapa, archivo_salida="app/templates/crimenes.html"):

    # Agregar puntos al mapa
    for dato in datos:
        lat = dato["latitud"]
        lon = dato["longitud"]
        distrito = dato["distrito"]
        tipo_robo = dato["tipo_robo"]

        # Crear un marcador para cada punto
        folium.Marker(
            location=[lat, lon],
            popup=f"Distrito: {distrito}<br>Tipo de Robo: {tipo_robo}",
            icon=folium.CustomIcon(icon_image="app/static/images/danger.webp", icon_size=(30, 30))
        ).add_to(mapa)

    # Guardar el mapa en un archivo HTML
    mapa.save(archivo_salida)
    print("Lugares peligrosos cargados exitosamente al mapa")

def agregar_distritos_al_mapa(data, conteo_distritos, mapa):
    for feature in data['features']:
        # Obtener el nombre del distrito o un valor predeterminado si no está presente
        distrito_nombre = feature['properties'].get('name', 'Distrito desconocido')
        
        # Obtener la geometría del distrito y verificar si es Polygon o MultiPolygon
        distrito_poligono = shape(feature['geometry'])
        
        # Obtener el conteo de incidentes para el distrito
        conteo = conteo_distritos[distrito_nombre]  # Usar el defaultdict, devuelve 0 si no existe
        color = obtener_color(conteo)  # Obtener el color según el conteo

        if isinstance(distrito_poligono, Polygon):
            # Convertir el polígono de Shapely a la lista de coordenadas para Folium
            coords = [(point[1], point[0]) for point in distrito_poligono.exterior.coords]
            folium.Polygon(
                locations=coords,
                color=color,
                weight=2,
                fill=True,
                fill_opacity=0.6,
                popup=distrito_nombre
            ).add_to(mapa)

        elif isinstance(distrito_poligono, MultiPolygon):
            # Iterar sobre cada polígono en el MultiPolygon usando `geoms`
            for poly in distrito_poligono.geoms:
                coords = [(point[1], point[0]) for point in poly.exterior.coords]
                folium.Polygon(
                    locations=coords,
                    color=color,
                    weight=2,
                    fill=True,
                    fill_opacity=0.6,
                    popup=distrito_nombre
                ).add_to(mapa)
    print("Distritos cargados correctamente en el mapa")

def dibujar_ruta_hacia_comisaria_mas_cercana(mapaCuidao, G, mi_ubicacion, comisarias, comisaria_mas_cercana):
    # Coordenadas de puntos de interés
    point1 = mi_ubicacion  # Mi ubicación
    point2 = (next(c['lat'] for c in comisarias if c['name'] == comisaria_mas_cercana),
            next(c['lng'] for c in comisarias if c['name'] == comisaria_mas_cercana))
    

    # Buscar el nodo más cercano
    closest_node1 = find_closest_node(G, point1)
    closest_node2 = find_closest_node(G, point2)

    # Si existe un camino entre los dos nodos más cercanos, dibujarlo
    if nx.has_path(G, source=closest_node1, target=closest_node2):
        path = nx.shortest_path(G, source=closest_node1, target=closest_node2)
        
        # Convertir el camino en una lista de coordenadas
        path_coords = [[node[0], node[1]] for node in path]
        
        # Añadir la ruta al mapa
        folium.PolyLine(locations=path_coords, color="red", weight=5, opacity=0.7,tooltip="Ruta más corta").add_to(mapaCuidao)

        print("Existe un camino entre los dos nodos. Ruta mostrada en el mapa.")
    else:
        print("No existe un camino entre los dos nodos.")
    
def mostrar_mapa():

    # Variables
    
    ubicacion = obtener_ubicacion()
    location = (ubicacion['latitud'], ubicacion['longitud'])
    mapaCuidao = folium.Map(location=[ubicacion['latitud'], ubicacion['longitud']], zoom_start=12)
    latitud,longitud = ubicacion['latitud'], ubicacion['longitud']
    datos_excel_comisarias = {}
    comisarias = []
    datosDistritos,conteo_distritos= cargar_datos_y_contar_distritos()
    G = cargar_calles_json("data/callePrincipal.geojson")

    # Implementación de funciones

    agregar_marcador_personalizado(mapaCuidao, latitud, longitud)
    
    CargarDataToDict("data/Comisarias.xlsx", datos_excel_comisarias, "COMISARÍA", "GPS")
    ConvertirDictToList(datos_excel_comisarias,comisarias)
    
    agregar_comisarias_al_mapa(mapaCuidao,comisarias)
    crear_mapa_con_puntos(datosDistritos,mapaCuidao)


    agregar_distritos_al_mapa(dataGeoJson, conteo_distritos, mapaCuidao)
   
    comisaria_mas_cercana = encontrar_comisaria_mas_cercana(location, comisarias)
    dibujar_ruta_hacia_comisaria_mas_cercana(mapaCuidao, G, location, comisarias, comisaria_mas_cercana)

    return mapaCuidao
    #                             # MAPA DE PARTIDA
    # mapaCuidao = folium.Map(location=[-12.0464, -77.0428], zoom_start=12)

    #                     #Simulando que tenemos la ubicacion del usuario
    # #-----------------------------------------------------------------------------------------------------#
    # latitud,longitud = -12.056695, -77.024096
    # #-----------------------------------------------------------------------------------------------------#

    # # Añadir la ubiacacion del usuario al mapa
    # agregar_marcador_personalizado(mapaCuidao, latitud, longitud)


    # datos_excel_comisarias = {}
    # comisarias = []
    # CargarDataToDict("Data/Comisarias.xlsx", datos_excel_comisarias, "COMISARÍA", "GPS")
    # ConvertirDictToList(datos_excel_comisarias,comisarias)


    # agregar_comisarias_al_mapa(mapaCuidao,comisarias)


    # datosDistritos,conteo_distritos= cargar_datos_y_contar_distritos()
    # crear_mapa_con_puntos(datosDistritos,mapaCuidao)


    # agregar_distritos_al_mapa(dataGeoJson, conteo_distritos, mapaCuidao)
    

    # G = cargar_calles_json("callePrincipal.geojson")
    # comisaria_mas_cercana = encontrar_comisaria_mas_cercana((latitud, longuitud), comisarias)
    # dibujar_ruta_hacia_comisaria_mas_cercana(mapaCuidao, G, (latitud, longuitud), comisarias, comisaria_mas_cercana)


    # return mapaCuidao