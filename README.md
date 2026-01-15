### Hytale Launcher 🎮
Un lanzador ligero y minimalista para Hytale, desarrollado en Python utilizando la librería CustomTkinter. Este proyecto permite gestionar el nombre de usuario, verificar dependencias del sistema y ejecutar el juego de forma sencilla.

## ✨ Características
Interfaz Moderna: Diseño oscuro y minimalista con estética profesional.

Multi-idioma: Soporte nativo para Español e Inglés.

Gestión de Usuario: Permite cambiar el nickname directamente desde la interfaz, actualizando automáticamente el script de arranque.

Información del Sistema: Muestra detalles en tiempo real sobre tu CPU, GPU, Sistema Operativo y Versión del Kernel.

Verificación de Dependencias: En sistemas Linux, comprueba automáticamente si tienes instaladas las librerías críticas (libpng, libSDL2).

Logs Integrados: Consola interna para visualizar el progreso del lanzamiento y posibles errores.

## 📸 Vista Previa

<img width="540" height="640" alt="image" src="https://github.com/user-attachments/assets/25c4fc84-1b23-46fa-bae8-7bd02c8ce171" />



### IMPORTANTE

PONER EL ARCHIVO launcher.py en la carpeta de hytale.


### 🚀 Requisitos
una canaima con linux (opcional)

Dependencias de Python
Para ejecutar el launcher, necesitas tener instalado Python 3.x y las siguientes librerías:


pip install customtkinter pillow
Dependencias del Sistema (Linux)
El launcher verificará la presencia de:

libpng

libSDL2


### 🛠️ Uso
Asegúrate de que el archivo hytale.sh esté en la misma carpeta que launcher.py.

Ejecuta el launcher:

python launcher.py
Introduce tu nombre de usuario (ars es el nombre predeterminado).

Haz clic en "Lanzar Aplicación".

Nota: En sistemas Linux, el launcher intentará dar permisos de ejecución (chmod +x) al archivo hytale.sh automáticamente antes de iniciar.
