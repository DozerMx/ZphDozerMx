# ZphDozerMx

ZphDozerMx es una herramienta de phishing actualizada en 2024, de momento solo cuenta con soporte para Facebook, pero en el futuro traerá más variedad. Se trata de una herramienta de clonación de páginas web, en este caso, de Facebook. Esta es su primera versión, y pronto seguirán mejoras y actualizaciones más avanzadas.

## Instalación

Sigue los pasos a continuación para instalar y configurar ZphDozerMx en Termux.

### Requisitos

Asegúrate de tener Termux instalado en tu dispositivo Android.

### Pasos de instalación

1. Aquí tienes los comandos de instalación:

1. **Actualizar paquetes y herramientas de Termux**:

   ```bash
   pkg update -y && pkg upgrade -y
   ```
2. **Instalar Git*
   ```bash
   pkg install git -y
   ```

4. **Instalar Python**:

   ```bash
   pkg install python -y
   ```

5. **Instalar OpenSSH** (para utilizar Serveo):

   ```bash
   pkg install openssh -y
   ```

6. **Clonar el repositorio**:

   ```bash
   git clone https://github.com/DozerMx/ZphDozerMx.git
   ```

7. **Cambiar al directorio del proyecto**:

   ```bash
   cd ZphDozerMx
   ```

8. **Instalar las dependencias de Python**:

   ```bash
   pip install -r requirements.txt
   ```

9. **Ejecutar el script**:

   ```bash
   python zphdozer.py
   ```

10. **Seleccionar la opción 1 en la terminal** para elegir el login de Facebook.


# instalacion en kali Linux.



```markdown
# Instalación en Kali Linux

Sigue estos pasos para instalar y configurar ZphDozerMx en Kali Linux.

### Requisitos

- Kali Linux
- Conexión a Internet

### Pasos de instalación

1. **Actualizar el sistema**:

   ```bash
   sudo apt update
   sudo apt upgrade
   ```

2. **Instalar Git, Python y pip**:

   ```bash
   sudo apt install git python3 python3-pip
   ```

3. **Clonar el repositorio**:

   ```bash
   git clone https://github.com/DozerMx/ZphDozerMx.git
   ```

4. **Cambiar al directorio del proyecto**:

   ```bash
   cd ZphDozerMx
   ```

5. **Crear y activar un entorno virtual (opcional, pero recomendado)**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

6. **Instalar las dependencias**:

   ```bash
   pip install -r requirements.txt
   ```

7. **Ejecutar el script**:

   ```bash
   python3 zphdozer.py
   ```

8. **Seleccionar la opción 1 en la terminal** para elegir el login de Facebook.
