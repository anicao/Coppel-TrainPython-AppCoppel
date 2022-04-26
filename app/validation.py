from flask_inputs import Inputs
from flask_inputs.validators import JsonSchema

# https://pythonhosted.org/Flask-Inputs/#module-flask_inputs
# https://json-schema.org/understanding-json-schema/
# noinspection SpellCheckingInspection
greeting_schema = {
    'type': 'object',
    'properties': {
        'greetee': {
            'type': 'string',
        }
    },
    'required': ['greetee']
}

marca_schema = {
    'type': 'object',
    'properties': {
        'marca': {
            'type': 'string',
        }
    },
    'required': ['marca']
}

articulo_schema = {
    'type': 'object',
    'properties': {
        'sku': {
            'type': 'number',
        }
    },
    'required': ['sku']
}

class GreetingInputs(Inputs):
    json = [JsonSchema(schema=greeting_schema)]

class MarcaInputs(Inputs):
    json = [JsonSchema(schema=marca_schema)]

class ArticuloInputs(Inputs):
    json = [JsonSchema(schema=articulo_schema)]

def validate_greeting(request):
    inputs = GreetingInputs(request)
    if inputs.validate():
        return None
    else:
        return inputs.errors

def validate_marca(request):
    inputs = MarcaInputs(request)
    if inputs.validate():
        return None
    else:
        return inputs.errors

def validate_articulo(request):
    inputs = ArticuloInputs(request)
    if inputs.validate():
        return None
    else:
        return inputs.errors