
from flask import Flask, render_template, request, jsonify, url_for
import cv2
import numpy as np
from werkzeug.utils import redirect
from werkzeug.exceptions import abort
import base64
import random

app = Flask(__name__, template_folder='templates')

templates_folder = app.root_path + '/templates'

@app.route("/")
def inicio():
    return "¡Hola, mundo!123"
    # return app.root_path 
    # return render_template('/home/hp-user/Documentos/python/service-flask/templates/index.html')
    # return render_template(templates_folder + '/index.html')

@app.route("/mostrar/<nombre>", methods=['GET', 'POST'])
def mostrar_nombre(nombre):
    # return "¡Hola, mundo!"
    # return app.root_path 
    # return render_template('/home/hp-user/Documentos/python/service-flask/templates/index.html')
    return render_template('index.html', nombre=nombre)


@app.route("/redireccionar")
def redireccionar():
    return redirect(url_for('mostrar_nombre', nombre='juan'))

@app.route("/salir")
def salir():
    return abort(404)

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template('error404.html', error=error), 404

@app.route('/process_image', methods=['POST'])
# @app.route('/process_image', methods=['GET'])
def process_image():
    try:
#     # Código que puede lanzar una excepción
        # Obtener la imagen de la solicitud POST
        image_file = request.files['image'].read()
        # nombre = request.form.get("nombre")
        
        # decodificar datos de la imagen en un arreglo de bytes
        nparr = np.fromstring(image_file, np.uint8)
        
        # decodificar arreglo de bytes en matriz numpy
        img_array = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        # Convertir la imagen a una matriz numpy usando OpenCV
        # image_array = cv2.imdecode(np.frombuffer(image_file, np.uint8), cv2.IMREAD_COLOR)
        
        # Procesar la imagen con OpenCV
        # Aquí se puede agregar cualquier código de procesamiento de imagen que se desee
        xi, yi, xf, yf = 1, 1, 100, 20
        r = random.randrange(0, 255, 50)
        g = random.randrange(0, 255, 50)
        b = random.randrange(0, 255, 50)
        
        cv2.rectangle(img_array, (xi, yi), (xf, yf), (r, g, b), 3)
        
        # Codificar la imagen en formato jpg
        ret, buffer = cv2.imencode('.jpg', img_array)
        # return 'nise'
        image_64_encode = base64.b64encode(buffer)
        return image_64_encode.decode('utf-8')
        return jsonify({'result': 'success', 'processed_image': image_64_encode.decode('utf-8')})  
    # except ValueError:
    except Exception as e:    
        return jsonify({'result': 'errors', 'type': f"Tipo de excepción: {type(e)}", 'errors': f"Mensaje de error: {e}"})  
    

@app.route('/example', methods=['POST'])
# @app.route('/process_image', methods=['GET'])
def example():
    try:
#     # Código que puede lanzar una excepción
        # Obtener la imagen de la solicitud POST
        image_file = request.files['image'].read()
        # nombre = request.form.get("nombre")
        
        # decodificar datos de la imagen en un arreglo de bytes
        nparr = np.fromstring(image_file, np.uint8)
        
        # decodificar arreglo de bytes en matriz numpy
        img_array = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        # Convertir la imagen a una matriz numpy usando OpenCV
        # image_array = cv2.imdecode(np.frombuffer(image_file, np.uint8), cv2.IMREAD_COLOR)
        
        # Procesar la imagen con OpenCV
        # Aquí se puede agregar cualquier código de procesamiento de imagen que se desee
        xi, yi, xf, yf = 1, 1, 100, 20
        r = random.randrange(0, 255, 50)
        g = random.randrange(0, 255, 50)
        b = random.randrange(0, 255, 50)
        
        cv2.rectangle(img_array, (xi, yi), (xf, yf), (r, g, b), 3)
        
        # Codificar la imagen en formato jpg
        ret, buffer = cv2.imencode('.jpg', img_array)
        # return 'nise'
        image_64_encode = base64.b64encode(buffer)
        return image_64_encode.decode('utf-8')
        return jsonify({'result': 'success', 'processed_image': image_64_encode.decode('utf-8')})  
    # except ValueError:
    except Exception as e:    
        return jsonify({'result': 'errors', 'type': f"Tipo de excepción: {type(e)}", 'errors': f"Mensaje de error: {e}"})  
    

      