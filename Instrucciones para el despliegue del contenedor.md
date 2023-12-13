# Instrucciones para el despliegue del contenedor

Esta guía contiene todas las instrucciones necesarias para lanzar Xtreme Biking en Docker. La aplicación debe funcionar igual que en la página web: https://test-xtreme-web.onrender.com/. Al final de la guía se recogen errores comunes a la hora de lanzar el sistema e información relevante sobre la configuración del mismo.

## Tabla de contenidos

- [Instrucciones para el despliegue del contenedor](#instrucciones-para-el-despliegue-del-contenedor)
  - [Tabla de contenidos](#tabla-de-contenidos)
  - [1. Instalación de Docker y Docker Compose](#1-instalación-de-docker-y-docker-compose)
    - [Windows](#windows)
      - [Paso 1: Instalar Docker Desktop para Windows](#paso-1-instalar-docker-desktop-para-windows)
      - [Paso 2: Verificar la Instalación](#paso-2-verificar-la-instalación)
      - [Paso 3: Instalar Docker Compose](#paso-3-instalar-docker-compose)
    - [Mac](#mac)
      - [Paso 1: Instalar Docker Desktop para Mac](#paso-1-instalar-docker-desktop-para-mac)
      - [Paso 2: Verificar la Instalación](#paso-2-verificar-la-instalación-1)
      - [Paso 3: Instalar Docker Compose](#paso-3-instalar-docker-compose-1)
    - [Linux](#linux)
      - [Paso 1: Instalar Docker](#paso-1-instalar-docker)
      - [Paso 2: Verificar la Instalación](#paso-2-verificar-la-instalación-2)
      - [Paso 3: Instalar Docker Compose](#paso-3-instalar-docker-compose-2)
      - [Paso 4: Verificar la Instalación de Docker Compose](#paso-4-verificar-la-instalación-de-docker-compose)
  - [2. Despliegue de los contenedores](#2-despliegue-de-los-contenedores)
    - [2.1. Cargar las imágenes proporcionadas](#21-cargar-las-imágenes-proporcionadas)
    - [2.2. Lanzar los contenedores](#22-lanzar-los-contenedores)
  - [3. Guía de navegación por la web](#3-guía-de-navegación-por-la-web)


## 1. Instalación de Docker y Docker Compose

### Windows

#### Paso 1: Instalar Docker Desktop para Windows
1. Visita la página oficial de Docker en [Docker Hub](https://hub.docker.com/).
2. Regístrate o inicia sesión.
3. Descarga Docker Desktop para Windows.
4. Ejecuta el instalador y sigue las instrucciones en pantalla.

#### Paso 2: Verificar la Instalación
1. Abre una ventana de PowerShell.
2. Escribe `docker --version` para verificar que Docker se haya instalado correctamente.

#### Paso 3: Instalar Docker Compose
- Docker Compose ya viene incluido en Docker Desktop para Windows. No es necesario instalarlo por separado.

### Mac

#### Paso 1: Instalar Docker Desktop para Mac
1. Visita la página oficial de Docker en [Docker Hub](https://hub.docker.com/).
2. Regístrate o inicia sesión.
3. Descarga Docker Desktop para Mac.
4. Abre el archivo `.dmg` y arrastra Docker a la carpeta de Aplicaciones.

#### Paso 2: Verificar la Instalación
1. Abre una terminal.
2. Escribe `docker --version` para verificar que Docker se haya instalado correctamente.

#### Paso 3: Instalar Docker Compose
- Docker Compose ya viene incluido en Docker Desktop para Mac. No es necesario instalarlo por separado.

### Linux

#### Paso 1: Instalar Docker
1. Abre una terminal.
2. Actualiza el índice de paquetes: `sudo apt-get update`.
3. Instala paquetes necesarios para permitir el uso de un repositorio sobre HTTPS:
   ```bash
   sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
   ```
4. Añade la clave GPG oficial de Docker:
   ```bash
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
   ```
5. Añade el repositorio de Docker:
   ```bash
   sudo add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) \
    stable"
   ```
6. Actualiza el índice de paquetes y luego instala Docker:
   ```bash
   sudo apt-get update
   sudo apt-get install docker-ce docker-ce-cli containerd.io
   ```

#### Paso 2: Verificar la Instalación
1. Ejecuta `docker --version` para verificar que Docker se haya instalado correctamente.

#### Paso 3: Instalar Docker Compose
1. Descarga la versión actual de Docker Compose:
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   ```
2. Aplica permisos ejecutables al binario:
   ```bash
   sudo chmod +x /usr/local/bin/docker-compose
   ```

#### Paso 4: Verificar la Instalación de Docker Compose
1. Ejecuta `docker-compose --version` para verificar que Docker Compose se haya instalado correctamente.

## 2. Despliegue de los contenedores

Para desplegar los contenedores que proveen los servicios necesarios para el sistema pueden construirse las imágenes a partir de los ficheros proporcionados o cargar las imágenes previamente construidas que se adjuntan junto al resto de archivos. En caso de optar por construir las imágenes dirígete directamente al segundo conjunto de instrucciones de esta sección.

### 2.1. Cargar las imágenes proporcionadas
1. Descomprime el archivo .zip que contiene los ficheros necesarios para el despliegue.
2. Abre una terminal.
3. Dirígete al directorio `images` dentro de la carpeta que acabas de descomprimir.
4. Carga las imágenes en tu máquina ejecutando los siguienes comandos
   ```bash
   docker load -i imagen.tar
   docker load -i imagen.tar
   docker load -i imagen.tar
   ```

   > NOTA: En caso de no poder ejecutar los comandos anteriores, es posible que tengas que ejecutarlos con permisos de superusuario.

### 2.2. Lanzar los contenedores
1. Si has seguido los pasos de las instrucciones 2.1 salta al paso 5. de este conjunto de instrucciones.
2. Descomprime el archivo .zip que contiene los ficheros necesarios para el despliegue.
3. Abre una terminal.
4. Dirígete al directorio `docker` dentro de la carpeta que acabas de descomprimir.
5. Verifica que en el directorio actual se encuentra el fichero `docker-compose.yml` Para ello puedes ejecutar el comando `ls` que lista los ficheros y directorios del directorio actual.
6. Ejecuta el siguiente comando
   ```bash
   docker-compose up
   ```

El contenedor lanzará, entre otros servicios, un servidor web que espera peticiones al puerto 8000 de la dirección loopback de tu máquina.

Para acceder al servicio web introduce alguna de las siguientes direcciones en el navegador de tu elección:

```
http://localhost:8000
```

```
http://127.0.0.1:8000
```

## 3. Guía de navegación por la web
* Primero podemos ver el escaparate, que incluye los productos destacados. En la cabecera podemos ver el logo de la empresa, y podemos inciar sesión, registrarnos o ver el carrito en la parte superior derecha. 
* En la cabecera, encontramos un menú dónde podemos acceder al inicio, sobre Nosotros, al catálogo y al seguimiento de un pedido, esto es posible desde casi todas las vistas.
* Si el usuario está logueado puede acceder desde la gestión de su perfil (icono de usuario en la parte superior derecha), podremos desde está vista escribir reclamaciones y valoraciones de los pedidos asociados a la cuenta, crear y editar direcciones y modificar la modalidad de pago. También en este mismo botón tendremos la opción de cerrar sesión.
* Desde seguimiento podemos ver los detalles de cada pedido, así como su estado, para ello hay que introducir su ID, que se puede obtener desde el correo enviado tras finalizar la compra o si estás logueado también desde la gestión de tus pedidos.
* Si entramos en catálogo, los productos están ordenados por categorías. En el botón mostrar más, accedemos a la categoría completa. En el margen izquierdo podemos filtrar por precio los productos de esa categoría.
* En la parte derecha de la cabecera, encontramos el buscador para buscar productos por su título o por su categoría.
* Desde el carrito podemos finalizar la compra, seleccionando dirección y modo de pago.