from flask import Flask
import sys
sys.path.append('controllers')

from controlador import example_bp
from controller_camera import camera_bp

app = Flask(__name__)

# Registra la vista "inicio" en la aplicación Flask
app.register_blueprint(example_bp)
app.register_blueprint(camera_bp)


