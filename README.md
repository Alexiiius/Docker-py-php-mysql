# Docker Composer con servidores phyton y php conjunto a mysql y phpmyadmin.

## Descripción

Este script automatiza la creacion de dos servidores en phyton y php asi como una base de datos en mysql asociada y acceso mediante phpmyadmin.

## Tabla de Contenidos

- [Instalación](#instalación)
- [Uso](#uso)
- [Datos de Interes](#datos-de-interes)

## Instalación

Para instalar y ejecutar este script, sigue estos pasos:


1. Descargue o clone el repositorio en el directorio donde quiera establecer su entorno de prueba.
   ```bash
   git clone https://github.com/Alexiiius/Docker-py-php-mysql.git
   ```

3. Lance docker-compose en el directorio donde quiera establecer su entorno de prueba.
    ```bash
    docker-compose up
    ```
4. Si ya ha usado alguna imagen que se este empleando en el recurso, es posible que surjan errores, limpie las imagenes y volumenes de su docker en caso de fallos.

## Uso

Una vez lanzado exitosamente, se habran mapeado las carpetas `php` y `phyton` a sus respectivos servidores.
En ambas carpetas se encuentran la raices de los servidores asi como un archivo de prueba. 

Ambos scripts son codigo basura y no recomendado para su uso. Han sido generados parcialmente con Copilot para hacer una prueba rapida. Ambos se conectan a la base de datos, construyen una tabla, la pueblan y la imprimen en pantalla.

Se recomienda borrar estos scripts tras probar su funcionalidad y limpiar la base de datos en caso de haberlos ejecutado.

Por defecto se han mapeado los puertos de los contenedor de la siguiente manera:
  - Php 8080
  - Phyton 8081
  - Phpmyadmin 8084

Parametros de la DB:
  - Root PW: `rootpassword`
  - Usuario: `user`
  - Usuario PW: `password`
  - Esquema por defecto: `mydb`
  - Nombre contenedor: `db`

Cualquier cambio realizado en los Dockerfile requerira que se vuelvan a reconstruir los volumenes para ello borre respectivamente las imagenes y volumenes en su Docker y reconstruyalos.

## Datos de Interes

1. El servidor phyton instala el framework flask y mysql connector por defecto a traves del Dockerfile.
2. Tambien cabe mencionar que el servidor phyton esta atacando a app.py por defecto, esto esta configurado en el Dockerfile.
