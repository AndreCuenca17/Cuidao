from openpyxl import load_workbook
from .funcionalidades import obtener_ultima_fila
def ConvertirDictToList(dicti: dict, lista: list):
    # Usar una lista de comprensión para reducir la sobrecarga de iteraciones
    for nombre, coordenadas in dicti.items():
        latitud, longitud = map(float, coordenadas[0].split(','))
        lista.append({'name': nombre, 'lat': latitud, 'lng': longitud})


def CargarDataToDict(file_path: str, data_dict: dict, columna1: str, columna2: str):
    # Leer los datos de una vez usando pandas
    dataframe = pd.read_excel(file_path)

    # Usar groupby para agrupar y luego convertir a diccionario de manera eficiente
    grouped = dataframe.groupby(columna1)[columna2].apply(list).to_dict()
    
    # Actualizar el diccionario original
    data_dict.update(grouped)

def ConvertirDictToDicWithTuple(dicti: dict, dicti_tuplas: dict):
    # Usar una lista de comprensión y map para mejorar la conversión
    for nombre, coordenadas in dicti.items():
        latitud, longitud = map(float, coordenadas[0].split(','))
        dicti_tuplas[nombre] = (latitud, longitud)


# Función para guardar los datos en el archivo Excel
def guardar_datos_en_excel(dni, lat, lon, departamento, provincia, distrito, tipo_robo, descripcion, fecha, hora, archivo_excel="data/reportes_delitos.xlsx"):
    try:
        # Cargar el archivo Excel
        workbook = load_workbook(archivo_excel)
        sheet = workbook.active
        
        # Preparar los datos en una lista
        nueva_fila = [dni, lat, lon, departamento, provincia, distrito, tipo_robo, descripcion, fecha, hora]
        
        # Agregar la nueva fila directamente
        sheet.append(nueva_fila)
        
        # Guardar los cambios
        workbook.save(archivo_excel)
        print(f"Datos guardados exitosamente.")
    except FileNotFoundError:
        print("Error: No se encontró el archivo Excel.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def cargar_calles_json(file="data/callePrincipal.geojson"):
    # Cargar archivo geojson
    gdf = gpd.read_file(file)
    G = nx.Graph()

    # Iterar sobre las filas del GeoDataFrame
    for _, row in gdf.iterrows():
        # Procesar solo las geometrías de tipo LineString
        if isinstance(row.geometry, LineString):
            # Extraer y convertir coordenadas (invertir latitud y longitud)
            coords = [(lon, lat) for lat, lon in row.geometry.coords]
            # Agregar aristas al grafo entre nodos consecutivos
            for i in range(len(coords) - 1):
                node1 = coords[i]
                node2 = coords[i + 1]
                # Agregar borde y nombre de calle si existe
                G.add_edge(node1, node2, street_name=row.get("name", "Unknown"))

    return G

