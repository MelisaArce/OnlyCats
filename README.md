# OnlyCats

<img src="img/logo.jpeg">

OnlyCats es una aplicación web desarrollada en Python con Flask, Gunicorn y SQLAlchemy que te permite publicar gatos en adopción y recibir donaciones para su cuidado, ya sea en refugios o en hogares. La interfaz de la aplicación está diseñada para ser similar a la de Facebook, facilitando la experiencia de los usuarios al interactuar con adorables gatos y encontrar formas de ayudar.


## Características

OnlyCats ofrece las siguientes características principales:

- Registro y inicio de sesión de usuarios: Los usuarios pueden crear cuentas, iniciar sesión y gestionar sus perfiles.
- Publicación de gatos en adopción: Los usuarios pueden crear y compartir publicaciones sobre gatos que necesitan un nuevo hogar.
- Recepción de donaciones: Los usuarios pueden donar dinero para ayudar en el cuidado de los gatos en adopción.
- Búsqueda y filtrado de publicaciones: Los usuarios pueden buscar gatos por diferentes criterios, como ubicación o categoría.
- Comentarios y me gusta en las publicaciones: Los usuarios pueden interactuar con las publicaciones dejando comentarios y dando "me gusta".

## Requisitos Previos

Antes de comenzar, asegúrate de tener instalados los siguientes requisitos previos:

- Python 3.x: [Descarga Python](https://www.python.org/downloads/)
- Virtualenv (recomendado): `pip install virtualenv`
- Gunicorn: `pip install gunicorn`
- Bibliotecas requeridas: Puedes instalarlas usando `pip install -r requirements.txt`

## Instalación

Sigue estos pasos para instalar y configurar OnlyCats en tu entorno local:

1. Clona el repositorio:

```bash
git clone https://github.com/MelisaArce/OnlyCats.git
cd OnlyCats
```
2. Crea un entorno virtual (opcional pero recomendado):

```bash
python -m venv venv
source venv/bin/activate  # En sistemas Unix
venv\Scripts\activate  # En Windows
```
3. Instala las bibliotecas requeridas:

bash:

```bash
pip install -r requirements.txt
```
3. Inicia la aplicación con Gunicorn:

```bash
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

## Levantando con Docker

Si prefieres utilizar Docker para ejecutar el proyecto, aquí tienes los pasos:

1. Asegúrate de tener Docker instalado en tu sistema. Puedes descargarlo desde [Docker's website](https://www.docker.com/get-started).

2. Clona el repositorio de OnlyCats si aún no lo has hecho:

```bash
git clone https://github.com/MelisaArce/OnlyCats.git
cd OnlyCats
```
3. Ejecuta el siguiente comando para construir la imagen de Docker:

```bash
docker build -t onlycats .
```
4. Una vez que la imagen se ha construido con éxito, puedes ejecutar un contenedor Docker con el siguiente comando:

```bash
docker run -p 8000:5000 onlycats
```

La aplicación estará disponible en http://localhost:8000.

## Uso
* Accede a la aplicación en tu navegador web y regístrate como usuario.
* Publica gatos en adopción y busca gatos que necesitan un hogar.
* Realiza donaciones para ayudar en el cuidado de los gatos.
* Interactúa con otras publicaciones dejando comentarios y dando "me gusta".

## Estado del Proyecto
OnlyCats está en constante desarrollo. Siempre estamos trabajando en mejoras y nuevas funcionalidades. No dudes en informar sobre problemas o proponer nuevas ideas.




