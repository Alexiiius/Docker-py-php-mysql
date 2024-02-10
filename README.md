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

2. Lance docker-compose en el directorio donde quiera establecer su entorno de prueba.
    ```bash
    docker-compose up
    ```
3. Si ha usado alguna imagen que se este empleando en el recurso, es posible que surjan errores, limpie las imagenes de su docker en caso de fallos.

## Uso

Una vez lanzado exitosamente, se habran mapeado las carpetas `php` y `phyton` a sus respectivos servidores.
En ambas carpetas se encuentran la raices de los servidores asi como un archivo de prueba. 

Por defecto se han mapeado los puertos de los contenedor de la siguiente manera:
  - Php 8080
  - Phyton 8081
  - Phpmyadmin 8084

## Datos de Interes

1. El servidor phyton instala el framework flask por defecto a traves del dockerfile.
2. El servidor php no esta configurado, si se quiere emplear pdo o alguna otra extension, se deben de aplicar a mano.
