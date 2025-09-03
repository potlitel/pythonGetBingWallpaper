
# 📸 Bing Wallpaper Downloader 4K

<!-- Badges -->
[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Downloads](https://img.shields.io/badge/downloads-10%2B-blue.svg)](#)

## 🚀 Descripción
Este proyecto es un script en Python que descarga automáticamente la imagen del día de Bing Wallpaper en resolución 4K. Está diseñado para facilitar la descarga segura y eficiente de fondos de pantalla en alta calidad, incorporando funcionalidades para mejorar la experiencia de usuario, como una barra de progreso visual y verificación previa de conexión a Internet.

## ✨Características

- 🐍 Código 100% en Python.
- ⚙️ Fácil de usar y configurar.
- 🌐 Soporte para múltiples plataformas.
- 📖 Documentación completa.
- Python Script que:
  - Descarga la imagen actual de la url **https://bingwallpaper.anerg.com/** y la almacena en una ubicación específica del HDD.
- 🌐 **Verificación de conexión**: Comprueba si hay acceso a Internet antes de iniciar la descarga.
- ⏳ **Barra de progreso**: Muestra el avance de la descarga en tiempo real.
- 🔗 **Navegación web automatizada**: Extrae dinámicamente la URL de la imagen del día.
- 💾 **Guardado organizado**: Descarga la imagen y la guarda en una carpeta específica en el sistema.

## 📝 Requisitos de Software

### 1. Python
- **Versión**: Python 3.7 o superior

#### Instalación de Python en Windows

##### 1. Descargar el instalador de Python

Visita el sitio web oficial de Python: python.org.
Descarga la última versión de Python 3.x para Windows (asegúrate de elegir entre la versión de 32 bits o 64 bits según tu sistema).

##### 2. Ejecutar el instalador

Abre el archivo descargado (por ejemplo, python-3.x.x-amd64.exe).
Asegúrate de marcar la opción "Add Python to PATH" antes de hacer clic en "Install Now".

##### 3. Personalizar la instalación (opcional)

Si deseas personalizar la instalación, selecciona "Customize installation" y elige las características que deseas incluir, como pip, documentación, etc.

##### 4. Verificar la instalación

Abre el símbolo del sistema (cmd) y ejecuta el siguiente comando para verificar que Python se haya instalado correctamente:

  ```bash
  python --version
  ```

#### Instalación de Python en linux

##### 1: Usar el gestor de paquetes

Abre la terminal y ejecuta el siguiente comando según tu distribución:

  * Ubuntu/Debian:

      ```bash
      sudo apt-get install python3
      ```

  * Fedora:

      ```bash
      sudo dnf install python3
      ```

##### 2: Verificar la instalación

Ejecuta el siguiente comando en la terminal:

   ```bash
  python3 --version
  ```

#### Instalación de Python en Mac

##### 1. Descargar el instalador de Python

Ve a python.org y descarga la versión más reciente de Python para macOS.

##### 2. Ejecutar el instalador

Localiza el archivo descargado en tu carpeta de Descargas y haz doble clic en él para iniciar la instalación.
Sigue las instrucciones en pantalla para completar la instalación.

##### 3. Verificar la instalación

Abre la Terminal y ejecuta:

  ```bash
  python3 --version
  ```

#### Instalación de pip 

##### 1. Verificar si pip está instalado

Después de instalar Python, pip generalmente se instala automáticamente. Verifica su instalación ejecutando:

  ```bash
  pip --version
  ```

##### 2. Instalar pip (si no está instalado)

Si pip no está instalado, puedes instalarlo usando el script get-pip.py. Sigue estos pasos:

###### 1. Descarga el script

  ```bash
  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
  ```

###### 2. Ejecuta el script

  ```bash
  python get-pip.py
  ```

## 🛠️ Para instalar el proyecto, sigue estos pasos:

1. Clona el repositorio:
   
   ```bash
   git clone https://github.com/potlitel/pythonGetBingWallpaper.git
   ```

2. Navega al directorio del proyecto:
   
   ```bash
   cd tu_repositorio
   ```

3. Crear un Entorno Virtual (**opcional pero recomendado**): Esto ayuda a manejar las dependencias sin afectar tu instalación global de Python.

   ```bash
   python -m venv venv
   ```

4. Activar el Entorno Virtual:

    * En Windows:

        ```bash
        venv\Scripts\activate
        ```

    * En Linux/Mac

        ```bash
        source venv/bin/activate
        ```
5. Instalar las Dependencias:

    ```bash
    pip install -r requirements.txt
    ```

## ▶️ Uso

Ejecuta el script principal. Este descargará la imagen de fondo del día, mostrando el progreso y notificando cualquier problema, como falta de conexión:

```bash
    python BingTodayWallpaper.py
```

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si deseas ayudar a mejorar este proyecto, puedes hacerlo siguiendo estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama con tu feature o corrección: `git checkout -b nombre-de-tu-rama`
3. Realiza tus cambios y realiza commits claros y descriptivos.
4. Envía un pull request describiendo detalladamente tus modificaciones.

Por favor, asegúrate de que tu código sigue las buenas prácticas, y si haces mejoras significativas, considera incluir pruebas o documentación adicional.

---

## 📝 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

## 🙏 Agradecimiento y contacto

¡Gracias por visitar y usar este proyecto! ✨  
Si tienes dudas, sugerencias o quieres contribuir, no dudes en abrir un issue 📥 o contactarme directamente:  

- GitHub: [potlitel](https://github.com/potlitel) 👨‍💻  
- Email: potlitel@gmail.com ✉️  

¡Espero tus aportes y comentarios! 💬😊

