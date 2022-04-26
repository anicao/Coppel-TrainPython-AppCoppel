# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request

from app.invalid_usage import InvalidUsage
from app.validation import validate_greeting, validate_marca, validate_articulo
from mypkg.greetings import say_hello_to, productos_por_marca, descripcion_por_articulo

app = Flask(__name__)


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

def application(environ, start_response):
  if environ['REQUEST_METHOD'] == 'OPTIONS':
    start_response(
      '200 OK',
      [
        ('Content-Type', 'application/json'),
        ('Access-Control-Allow-Origin', '*'),
        ('Access-Control-Allow-Headers', 'Authorization, Content-Type'),
        ('Access-Control-Allow-Methods', 'POST'),
      ]
    )
    return ''

@app.route("/")
def index() -> str:
    return jsonify({"message": "El servicio esta activo."})


@app.route("/hello", methods=['POST'])
def hello() -> str:
    errors = validate_greeting(request)
    if errors is not None:
        print(errors)
        raise InvalidUsage(errors)
    greetee = request.json.get("greetee", None)
    response = {"message": say_hello_to(greetee)}
    return jsonify(response)

@app.route("/findProductsByBrand", methods=['POST'])
def findProductsByBrand() -> str:
    errors = validate_marca(request)
    if errors is not None:
        print(errors)
        raise InvalidUsage(errors)

    marca = request.json.get("marca", None)
    response = {"productos": productos_por_marca(marca)}
    return jsonify(response)

# -----------------------------------------------------
# Ejercicio:
# Agregar un nuevo punto de entrada llamado productDetail (GET)
# que me permite recuperar el detalle de un articulo a partir de su SKU (entero).
#
# Usar la funci?n: descripcion_por_articulo(a) para recuperar la informaci?n
# Usar la funci?n: validate_articulo(request) para validar la petici?n
# -----------------------------------------------------
@app.route("/productDetail", methods=['GET'])
def productDetail() -> str:
    errors = validate_articulo(request)
    if errors is not None:
        print(errors)
        raise InvalidUsage(errors)

    sku = request.json.get("sku", None)
    response = {"response": descripcion_por_articulo(sku)}
    return jsonify(response)


# These two lines are used only while developing.
# In production this code will be run as a module.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

