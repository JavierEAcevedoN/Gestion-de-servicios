import csv

def cargar_datos_diccionario_csv(ruta):
    datos = {}
    file = open(ruta,"r")
    datos = csv.DictReader(file)
    datos = list(datos)
    return datos

def guardar_datos_csv(datos, ruta):
    datos = list(datos)
    file = open(ruta,"a",newline="")
    escritor = csv.writer(file)
    for i in datos:
        escritor.writerows(datos)
    file.close()