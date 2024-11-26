from flask import Flask
from flask_cors import CORS
from .routes import register_routes  # Importar la función para registrar las rutas

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Registrar las rutas desde routes.py
    register_routes(app)

    return app
