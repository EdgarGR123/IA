import subprocess
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Configurar CORS para que acepte solicitudes desde cualquier origen
CORS(app, resources={r"/*": {"origins": "*"}})

# Configurar logging
logging.basicConfig(level=logging.INFO)

@app.route('/')
def hello_world():
    return '¡Hola, mundo desde Flask en cPanel!'

@app.route('/peticion_IA', methods=['POST'])
def peticion_ia():
    print(data)

    data = request.get_json()
    if 'titulo' in data:
        titulo_producto = data['titulo']
        logging.info(f"Título recibido: {titulo_producto}")
        
        # Ejecutar el script de IA en xvfb
        command = f"xvfb-run python /workspaces/IA/IA2.py \"{titulo_producto}\""  # Añadir comillas para manejar espacios
        try:
            # Ejecuta el comando y obtiene la salida
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
            return jsonify({'message': output.decode('utf-8')}), 200
        except subprocess.CalledProcessError as e:
            return jsonify({'error': 'No se pudo generar la descripción con IA', 'details': e.output.decode('utf-8')}), 500
    else:
        return jsonify({'error': 'Falta el campo "titulo" en los datos'}), 400

if __name__ == "__main__":
    app.run(port=5215)
