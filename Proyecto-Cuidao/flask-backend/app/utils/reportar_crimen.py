import folium
from .mostrar_comisarias import mostrar_comisarias
from .mostrar_ubicacion_actual import mostrar_ubicacion_actual
from folium import IFrame
from .funcionalidades import obtener_geojson_distritos
ubicacion_seleccionada = {"latitud": None, "longitud": None}

def mapa_modificado():
    # Inyectar el script JavaScript dentro del mapa
    m = mostrar_ubicacion_actual()
    m = mostrar_comisarias(m)

    # Obtener el ID del mapa
    map_id = m.get_name()

    # Usar una cadena multilínea para evitar conflictos con las llaves de formato
    script = f"""
        <script>
            document.addEventListener('DOMContentLoaded', function () {{
                // Obtener el mapa generado por Folium
                var map = window.{map_id};  // Usar el mapa generado automáticamente por Folium

                // Verificar si el mapa está correctamente definido
                if (!map) {{
                    console.error('El mapa no se ha cargado correctamente.');
                    return;
                }}

                // Variable para almacenar el marcador temporal
                var tempMarker = null;

                // Agregar el evento de clic al mapa existente
                map.on('click', function(e) {{
                    var lat = e.latlng.lat;
                    var lon = e.latlng.lng;

                    // Eliminar el marcador anterior si existe
                    if (tempMarker) {{
                        map.removeLayer(tempMarker);
                    }}

                    // Crear un nuevo marcador en la ubicación seleccionada
                    tempMarker = L.marker([lat, lon]).addTo(map);

                    // Enviar las coordenadas al backend
                    fetch('/guardar-coordenadas', {{
                        method: 'POST',
                        headers: {{
                            'Content-Type': 'application/json',
                        }},
                        body: JSON.stringify({{
                            latitud: lat,
                            longitud: lon
                        }})
                    }})
                    .then(response => response.json())
                    .then(data => {{
                        console.log('Coordenadas guardadas:', data);

                        // Enviar un mensaje al frontend para que solicite el distrito
                        window.parent.postMessage({{ type: "coordinatesSaved" }}, "*");
                    }})
                    .catch(error => {{
                        console.error('Error al guardar coordenadas:', error);
                    }});
                }});
            }});
        </script>
    """

    # Inyectar el script generado en el HTML del mapa
    m.get_root().html.add_child(folium.Element(script))

    # Guardar el mapa como archivo HTML
    m.save("app/templates/reportar_crimen.html")

# def devolver_distrito():
#     global ubicacion_seleccionada
#     lat, lon = ubicacion_seleccionada["latitud"], ubicacion_seleccionada["longitud"]
#     distrito =  obtener_distrito_de_punto((lat,lon),obtener_geojson_distritos())
#     return distrito



