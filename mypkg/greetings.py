def say_hello_to(s):
    return "hello {}".format(s)

def productos_por_marca(m):
    if m.lower() == "mabe":
        return [
            {"sku": 12345, "stock":7, "description": "Lavadora Mabe Automatica LMA46101VGAB 16 kg Gris", "image":"https://cdn1.coppel.com/images/catalog/pm/6217653-1.jpg"},
            {"sku": 45678, "stock":7, "description": "Lavadora Mabe Automatica LMA70215VBAB0 20 kg Blanca", "image":"https://cdn1.coppel.com/images/catalog/pm/6371653-1.jpg"},
            {"sku": 90123, "stock":7, "description": "Lavadora Mabe Automatica LMA76112CBAB0 16 kg Blanca", "image":"https://cdn1.coppel.com/images/catalog/pm/6371653-1.jpg"}
        ]
    elif m.lower() == "flexi":
        return [
            {"sku": 62748, "description": "Botas Outdoor Flexi de Piel para Hombre"},
            {"sku": 37462, "description": "Sandalias Casuales Flexi de Piel para Hombre"}

        ]
    else:
        return [
            {"sku": 12345, "stock":7, "description": "Lavadora Mabe Automatica LMA46101VGAB 16 kg Gris", "image":"https://cdn1.coppel.com/images/catalog/pm/6217653-1.jpg"},
            {"sku": 45678, "stock":7, "description": "Lavadora Mabe Automatica LMA70215VBAB0 20 kg Blanca", "image":"https://cdn1.coppel.com/images/catalog/pm/6371653-1.jpg"},
            {"sku": 90123, "stock":7, "description": "Lavadora Mabe Automatica LMA76112CBAB0 16 kg Blanca", "image":"https://cdn1.coppel.com/images/catalog/pm/6371653-1.jpg"},
            {"sku": 62748, "description": "Botas Outdoor Flexi de Piel para Hombre"},
            {"sku": 37462, "description": "Sandalias Casuales Flexi de Piel para Hombre"}
            ]

def descripcion_por_articulo(a):
    if a == 12345:
        return {
            "sku": 12345,
            "description": "Lavadora Mabe Automatica LMA46101VGAB 16 kg Gris",
            "price": 10999,
            "status": "agotado",
            "details": "Durabilidad, confiabilidad y maximo rendimiento para tu hogar. Complementa tu centro de lavado con esta lavadora Mabe LMA46101VGAB."
        }
    elif a == 45678:
        return {
            "sku": 45678,
            "description": "Lavadora Mabe Automatica LMA70215VBAB0 20 kg Blanca",
            "price": 12299,
            "status": "disponible",
            "details": "Ten al alcance de tu familia ropa limpia y cuidada con ayuda de la lavadora Mabe modelo LMA70215VBAB0. Es automatica y tiene capacidad de 20 kg."
        }
    elif a == 90123:
        return {
            "sku": 90123,
            "description": "Lavadora Mabe Automatica LMA76112CBAB0 16 kg Blanca",
            "price": 6999,
            "status": "disponible",
            "details": "Ahorra tiempo, dinero y esfuerzo con esta lavadora Mabe LMA76112BAB0. Este modelo tiene una gran capacidad de 16 kilos y es ideal para familias grandes."
        }
    elif a == 62748:
        return {
            "sku": 62748,
            "description": "Botas Outdoor Flexi de Piel para Hombre",
            "price": 699,
            "status": "agotado",
            "details": "Se trata de un calzado hecho 100% de piel, y cuenta con un par de chinelas en color negro, ambas con hebillas, que les dan un estilo moderno y desenfadado."
        }
    elif a == 37462:
        return {
            "sku": 37462,
            "description": "Sandalias Casuales Flexi de Piel para Hombre",
            "price": 899,
            "status": "disponible",
            "details": "Desempanate adecuadamente en tu lugar de trabajo con estas botas de la marca Flexi. Un calzado especializado para superficies rusticas."
        }
    else:
        return []