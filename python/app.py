# El script de python que se ejecutará en el contenedor de docker esta corriendo en el puerto 80 localmente indicado en app.run permitiendo cualquier ip de origen con host
# Se esta usando el framework de flask ya que facilita la creación de aplicaciones web y servicios web con python
# Esta instalado flash a traves del dockerfile

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hola mundo desde phyton en docker!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)