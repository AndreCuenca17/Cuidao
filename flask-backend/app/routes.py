from flask import render_template, jsonify, request
from app.utils.funcionalidades import crear_mapa_vacio

def register_routes(app):
    """Registrar todas las rutas en la aplicación Flask."""

    @app.route('/')
    def home():
        return jsonify({"message": "Bienvenido al backend Flask"})

    @app.route('/generate-map', methods=['GET'])
    def generate_map():
        # Generar el mapa vacío y guardarlo como HTML
        mapa = crear_mapa_vacio()
        mapa.save('app/templates/mapa_vacio.html')
        return render_template('mapa_vacio.html')

    @app.route("/map")
    def get_map():
        # Obtener las opciones enviadas desde el frontend
        ubicacion = request.args.get("ubicacion") == "true"
        crimenes = request.args.get("crimenes") == "true"
        comisarias = request.args.get("comisarias") == "true"
        distritos = request.args.get("distritos") == "true"
        calor = request.args.get("calor") == "true"

        # Lógica para servir el template mapa_vacio.html si 'ubicacion' es True
        if comisarias:
            return render_template('comisarias.html') 

        else:  
            # Si no se selecciona "ubicacion", genera un mapa de ejemplo
            map_html = f"""
            <html>
            <body>
                <h1>Mapa de ejemplo</h1>
                <p>Opciones seleccionadas:</p>
                <ul>
                    <li>Ubicación: {'Sí' if ubicacion else 'No'}</li>
                    <li>Crímenes: {'Sí' if crimenes else 'No'}</li>
                    <li>Comisarías: {'Sí' if comisarias else 'No'}</li>
                    <li>Distritos: {'Sí' if distritos else 'No'}</li>
                    <li>Mapa de calor: {'Sí' if calor else 'No'}</li>
                </ul>
            </body>
            </html>
            """
            return map_html

  