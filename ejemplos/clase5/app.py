from flask import Flask, jsonify

aplicacion = Flask(__name__)

@aplicacion.route('/')
def home():
    return "Hola"

@aplicacion.route('/datos')
def obtener_datos():
    datos = {"nombre": "Daniel", "cedula": 13213123}
    return jsonify(datos)