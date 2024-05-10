import json

def cargar_datos_json(ruta):
    datos = {}
    file = open(ruta,"r")
    datos = json.load(file)
    return datos

def guardar_datos_json(datos, ruta):
    datos = list(datos)
    diccionario = json.dumps(datos, indent=4)
    file = open(ruta,"w")
    file.write(diccionario)
    file.close()