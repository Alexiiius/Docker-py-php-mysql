# El script de python que se ejecutará en el contenedor de docker esta corriendo en el puerto 80 localmente indicado en app.run permitiendo cualquier ip de origen con host
# Se esta usando el framework de flask ya que facilita la creación de aplicaciones web y servicios web con python
# Esta instalado flash a traves del dockerfile

from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Conectar a la base de datos
    cnx = mysql.connector.connect(user='user', password='password',
                                  host='db',
                                  database='mydb')

    # Crear un cursor
    cursor = cnx.cursor()


## SI NO QUIERES QUE EL SCRIPT CREE Y INSERTE BORRA LA CREACION Y INSERTADO DE DATOS Y SOLAMENTE LEERA. BORRA DESDE LINEA 22 A LINEA 32
    # Crear la tabla si no existe
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS MyTable (
            id INT AUTO_INCREMENT PRIMARY KEY,
            firstname VARCHAR(40),
            lastname VARCHAR(40)
        )
    """)
    # Insertar datos aleatorios
    cursor.execute("INSERT INTO MyTable (firstname, lastname) VALUES ('Alex', 'Sanchez')")

    # Hacer commit de la transacción
    cnx.commit()

    # Seleccionar y mostrar los datos
    cursor.execute("SELECT id, firstname, lastname FROM MyTable")

    # Recoger los resultados
    results = cursor.fetchall()

    # Cerrar la conexión
    cnx.close()

    # Devolver los resultados como una cadena
    return 'Hola mundo desde phyton en docker! Aquí están tus datos de la DB: ' + str(results)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)