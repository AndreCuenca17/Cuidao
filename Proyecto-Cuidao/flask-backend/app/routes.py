from flask import render_template, jsonify, request

# import app.utils.funcionalidades as fun -> Opcion 1
import google.generativeai as genai
from app.utils.delimitar_distritos import *
from app.utils.dibujar import *
from app.utils.funcionalidades import *
from app.utils.manejar_data import *
from app.utils.mostrar_comisarias import *
from app.utils.mostrar_mapa_de_calor import *
from app.utils.mostrar_ubicacion_actual import *
from app.utils.mostrar_ultimos_reportes import *
from app.utils.reportar_crimen import *
from app.utils.combinaciones import *
from app.utils.efectuar_denuncia import *
from app.utils.registrar_denuncia import *
from app.utils.reportar_crimen import *
from threading import Thread
from decouple import config
import threading

# Variables globales para controlar la ejecución única
update_lock = threading.Lock()
is_updating = False  # Estado de actualización

genai.configure(api_key=config('API_KEY'))

def actualizar_datos_crimenes():
    global is_updating
    try:
        print("Actualizando datos de crímenes...")
        mostrar_ultimos_reportes().save("app/templates/crimenes.html")
        ubicacion_crimenes()
        crimenes_distritos()
        crimenes_calor()
        ubicacion_crimenes_distritos()
        ubicacion_crimenes_calor()
        crimenes_distritos_calor()
        ubicacion_crimenes_distritos_calor()
        crimenes_comisarias()
        ubicacion_crimenes_comisarias()
        crimenes_comisarias_distritos()
        crimenes_comisarias_calor()
        ubicacion_crimenes_comisarias_distritos()
        ubicacion_crimenes_comisarias_calor()
        crimenes_comisarias_distritos_calor()
        ubicacion_crimenes_comisarias_distritos_calor()
        efectuar_denuncia()
        print("Crímenes actualizados correctamente")
    except Exception as e:
        print(f"Error al actualizar datos: {e}")
    finally:
        is_updating = False  # Restablecer estado de actualización
        update_lock.release()  # Liberar el bloqueo


def register_routes(app):
    """Registrar todas las rutas en la aplicación Flask."""

    @app.route("/", methods=["POST"])
    def post_ubicacion_actual():

        try:
            # Obtener los datos enviados desde el frontend
            data = request.get_json()
            latitud = data.get("latitud")
            longitud = data.get("longitud")

            if latitud is None or longitud is None:
                return jsonify({"error": "Faltan datos de latitud o longitud"}), 400

            # Almacenar en la variable global
            global geolocalizacion
            geolocalizacion["latitud"] = latitud
            geolocalizacion["longitud"] = longitud
            print(geolocalizacion)
            return jsonify({"message": "Coordenadas almacenadas correctamente"})
        except Exception as e:
            print(e)
            return jsonify({"error": str(e)}), 500

    @app.route("/", methods=["GET"])
    def get_generar_mapas():
        try:
            # Generar el mapa vacío y guardarlo como HTML
            crear_mapa_vacio().save("app/templates/mapa_vacio.html")  # mapa_vacio.html
            mostrar_ubicacion_actual().save(
                "app/templates/ubicacion.html"
            )  # ubicacion.html
            mostrar_comisarias().save(
                "app/templates/comisarias.html"
            )  # comisarias.html
            mostrar_mapa_de_calor().save("app/templates/calor.html")  # calor.html
            delimitar_distritos().save("app/templates/distritos.html")  # distritos.html
            ubicacion_comisarias()  # ubicacion_comisarias.html
            ubicacion_distritos()  # ubicacion_distritos.html
            ubicacion_calor()  # ubicacion_calor.html
            comisarias_distritos()  # comisarias_distritos.html
            comisarias_calor()  # comisarias_calor.html
            distritos_calor()  # distritos_calor.html
            ubicacion_comisarias_distritos()  # ubicacion_comisarias_distritos.html
            ubicacion_comisarias_calor()  # ubicacion_comisarias_calor.html
            ubicacion_distritos_calor()  # ubicacion_distritos_calor.html
            comisarias_distritos_calor()  # comisarias_distritos_calor.html
            ubicacion_comisarias_distritos_calor()  # ubicacion_comisarias_distritos_calor.html
            efectuar_denuncia()  # efectuar_denuncia.html
            mapa_modificado()  # reportar_crimen.html

            # Mapas que se volveran a generar en /map
            # mostrar_ultimos_reportes().save("app/templates/crimenes.html")
           

            # ubicacion_crimenes()  # ubicacion_crimenes.html
            
            # crimenes_comisarias()  # crimenes_comisarias.html
            # crimenes_distritos()  # crimenes_distritos.html
            # crimenes_calor()  # crimenes_calor.html
            
            
            # ubicacion_crimenes_comisarias()  # ubicacion_crimenes_comisarias.html
            # ubicacion_crimenes_distritos()  # ubicacion_crimenes_distritos.html
            # ubicacion_crimenes_calor()  # ubicacion_crimenes_calor.html
            
           
            # crimenes_comisarias_distritos()  # crimenes_comisarias_distritos.html
            # crimenes_comisarias_calor()  # crimenes_comisarias_calor.html
            # crimenes_distritos_calor()  # crimenes_distritos_calor.html
            
            # ubicacion_crimenes_comisarias_distritos()  # ubicacion_crimenes_comisarias_distritos.html
            # ubicacion_crimenes_comisarias_calor()  # ubicacion_crimenes_comisarias_calor.html
            # ubicacion_crimenes_distritos_calor()  # ubicacion_crimenes_distritos_calor.html
            
            # crimenes_comisarias_distritos_calor()  # crimenes_comisarias_distritos_calor.html
            # ubicacion_crimenes_comisarias_distritos_calor()  # ubicacion_crimenes_comisarias_distritos_calor.html
            print("Mapas generados correctamente")
            return jsonify({"message": "Mapas generados correctamente"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route("/map")
    def mostrar_mapas_actualizados():
        global is_updating
        
        # Obtener las opciones enviadas desde el frontend
        ubicacion = request.args.get("ubicacion") == "true"
        crimenes = request.args.get("crimenes") == "true"
        comisarias = request.args.get("comisarias") == "true"
        distritos = request.args.get("distritos") == "true"
        calor = request.args.get("calor") == "true"

        # Diccionario para mapear combinaciones a templates
        template_mapping = {
            (False, False, False, False, False): "mapa_vacio.html",
            (True, False, False, False, False): "ubicacion.html",
            (False, True, False, False, False): "crimenes.html",
            (False, False, True, False, False): "comisarias.html",
            (False, False, False, True, False): "distritos.html",
            (False, False, False, False, True): "calor.html",
            (True, True, False, False, False): "ubicacion_crimenes.html",
            (True, False, True, False, False): "ubicacion_comisarias.html",
            (True, False, False, True, False): "ubicacion_distritos.html",
            (True, False, False, False, True): "ubicacion_calor.html",
            (False, True, True, False, False): "crimenes_comisarias.html",
            (False, True, False, True, False): "crimenes_distritos.html",
            (False, True, False, False, True): "crimenes_calor.html",
            (False, False, True, True, False): "comisarias_distritos.html",
            (False, False, True, False, True): "comisarias_calor.html",
            (False, False, False, True, True): "distritos_calor.html",
            (True, True, True, False, False): "ubicacion_crimenes_comisarias.html",
            (True, True, False, True, False): "ubicacion_crimenes_distritos.html",
            (True, True, False, False, True): "ubicacion_crimenes_calor.html",
            (True, False, True, True, False): "ubicacion_comisarias_distritos.html",
            (True, False, True, False, True): "ubicacion_comisarias_calor.html",
            (True, False, False, True, True): "ubicacion_distritos_calor.html",
            (False, True, True, True, False): "crimenes_comisarias_distritos.html",
            (False, True, True, False, True): "crimenes_comisarias_calor.html",
            (False, True, False, True, True): "crimenes_distritos_calor.html",
            (False, False, True, True, True): "comisarias_distritos_calor.html",
            (
                True,
                True,
                True,
                True,
                False,
            ): "ubicacion_crimenes_comisarias_distritos.html",
            (True, True, True, False, True): "ubicacion_crimenes_comisarias_calor.html",
            (True, True, False, True, True): "ubicacion_crimenes_distritos_calor.html",
            (
                True,
                False,
                True,
                True,
                True,
            ): "ubicacion_comisarias_distritos_calor.html",
            (False, True, True, True, True): "crimenes_comisarias_distritos_calor.html",
            (
                True,
                True,
                True,
                True,
                True,
            ): "ubicacion_crimenes_comisarias_distritos_calor.html",
        }

        # Generar la clave basada en las opciones y obtener el template
        template_key = (ubicacion, crimenes, comisarias, distritos, calor)
        template = template_mapping.get(template_key, "mapa_vacio.html")

            # Verificar si ya se está ejecutando la actualización
        if not is_updating:
            if update_lock.acquire(blocking=False):  # Intentar adquirir el lock
                is_updating = True  # Marcar actualización en progreso
                thread = threading.Thread(target=actualizar_datos_crimenes)
                thread.start()
            else:
                print("Actualización ya en curso.")

        return render_template(template)

    @app.route("/efectuar-denuncia")
    def mostrar_efectuar_denuncia():

        return render_template("efectuar_denuncia.html")

    @app.route("/reportar-crimen", methods=["POST"])
    def post_guardar_crimen():
        """
        Recibe los datos de un crimen desde el frontend y los almacena en un archivo Excel.
        """
        try:
            # Obtener los datos enviados desde el frontend
            data = request.get_json()
            dni = data.get("dni")
            latitud = ubicacion_seleccionada["latitud"]
            longitud = ubicacion_seleccionada["longitud"]
            departamento = "Lima"
            provincia = "Lima"
            distrito = data.get("distrito")
            tipo_robo = data.get("tipoDelito")
            descripcion = data.get("otroDelito") or tipo_robo

            fecha = data.get("fecha")
            hora = data.get("hora")

            if (
                latitud is None
                or longitud is None
                or distrito is None
                or tipo_robo is None
            ):
                return (
                    jsonify(
                        {
                            "error": "Faltan datos de latitud, longitud, distrito o tipo de robo"
                        }
                    ),
                    400,
                )

            # Guardar los datos en el archivo Excel
            guardar_datos_en_excel(
                dni,
                latitud,
                longitud,
                departamento,
                provincia,
                distrito,
                tipo_robo,
                descripcion,
                fecha,
                hora,
            )
            print("Se ejecutó correctamente la función guardar_datos_en_excel")
            return jsonify({"message": "Crimen reportado correctamente"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route("/prueba")
    def prueba():
        mapa_modificado()
        return jsonify({"message": "Crimen reportado correctamente"})

    @app.route("/reportar-crimen")
    def reportar_crimen():

        return render_template("reportar_crimen.html")

    @app.route("/guardar-coordenadas", methods=["POST"])
    def post_guardar_ubicacion_seleccionada():
        # Obtener los datos JSON enviados desde el frontend
        datos = request.get_json()

        # Extraer latitud y longitud
        latitud = datos.get("latitud")
        longitud = datos.get("longitud")

        global ubicacion_seleccionada
        ubicacion_seleccionada["latitud"] = latitud
        ubicacion_seleccionada["longitud"] = longitud

        # Aquí puedes procesar las coordenadas, guardarlas en la base de datos, etc.
        print(
            f"Coordenadas recibidas: Latitud: {ubicacion_seleccionada["latitud"]}, Longitud: {ubicacion_seleccionada["longitud"]}"
        )

        # Respuesta de éxito
        return jsonify(
            {
                "mensaje": "Coordenadas guardadas exitosamente",
                "latitud": latitud,
                "longitud": longitud,
            }
        )

    @app.route("/settear-distrito", methods=["GET"])
    def get_settear_distrito():

        lat, lon = ubicacion_seleccionada["latitud"], ubicacion_seleccionada["longitud"]
        print(lat, lon)
        distrito = obtener_distrito_de_punto(
            (lat, lon), obtener_geojson_distritos()
        )  # Aquí asignas el distrito que ya tienes, o lo obtienes de donde corresponda

        
        # Imprimir el distrito recibido (para depuración)
        print(f"Distrito enviado al frontend: {distrito}")

        # Respuesta de éxito con el distrito
        return jsonify({"distrito": distrito})
        # Posible error las tildes
    
    @app.route('/generate', methods=['POST'])
    def generate_content():
        try:
            # Obtener el mensaje del cliente
            data = request.json
            prompt = data.get("prompt", "")

            # Conectar con el modelo y generar respuesta
            model = genai.GenerativeModel(model_name=config('MODEL_NAME'))
            result = model.generate_content(prompt)

            # Responder al frontend
            return jsonify({"response": result.text})
        except Exception as e:
            return jsonify({"error": str(e)}), 500