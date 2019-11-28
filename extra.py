        info = """
        {
            "1": {
                "cantidad": 5058,
                "dinero_acumulado": 126450.0,
                "id_catalogo": 1,
                "nombre": "refresco",
                "precio": 25.0
            },
            "2": {
                "cantidad": 5004,
                "dinero_acumulado": 150120.0,
                "id_catalogo": 2,
                "nombre": "agua fresca",
                "precio": 30.0
            },
            "3": {
                "cantidad": 5010,
                "dinero_acumulado": 175350.0,
                "id_catalogo": 3,
                "nombre": "cerveza",
                "precio": 35.0
            },
            "4": {
                "cantidad": 4926,
                "dinero_acumulado": 197040.0,
                "id_catalogo": 4,
                "nombre": "orden tacos de pastor",
                "precio": 40.0
            },
            "5": {
                "cantidad": 5001,
                "dinero_acumulado": 250050.0,
                "id_catalogo": 5,
                "nombre": "orden tacos de bistec",
                "precio": 50.0
            },
            "6": {
                "cantidad": 4863,
                "dinero_acumulado": 291780.0,
                "id_catalogo": 6,
                "nombre": "orden de alambre",
                "precio": 60.0
            },
            "7": {
                "cantidad": 5072,
                "dinero_acumulado": 126800.0,
                "id_catalogo": 7,
                "nombre": "taco pastor",
                "precio": 25.0
            },
            "8": {
                "cantidad":5024,
                "dinero_acumulado": 150720.0,
                "id_catalogo": 8,
                "nombre": "taco de bistec",
                "precio": 30.0
            },
            "9": {
                "cantidad": 4939,
                "dinero_acumulado": 172865.0,
                "id_catalogo": 9,
                "nombre": "quesadilla",
                "precio": 35.0
            },
            "10": {
                "cantidad": 5113,
                "dinero_acumulado": 281215.0,
                "id_catalogo": 10,
                "nombre": "queso fundido",
                "precio": 55.0
            }
        }
        """
import json

d = json.loads(info)
print(d['13'])