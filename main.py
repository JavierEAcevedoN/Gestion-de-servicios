from modules.datos_json import *
from modules.crud import CRUD 
from modules.servicios import CRUD_servicios
from modules.ventas import opc_ventas
from modules.reportes import opc_reportes

# importe de los datos
usuarios = cargar_datos_json("JSON/usuarios.json")
servicios = cargar_datos_json("JSON/servicios.json")
ventas = cargar_datos_json("JSON/ventas.json")
informes = cargar_datos_json("JSON/informes.json")

# menu de seleccion
while True:
    choice = -1
    try:
        # opciones
        choice = int(input("""
Menu general
ingresa la opcion: 
(1) Modulo de usuarios (Administrador).
(2) Modulo gestion de servicios.
(3) Modulo de reportes.
(4) Modulo de ventas.
(0) Terminar. """))
    
    except Exception:
        print("ese valor no es valido")

    if choice == 1:
        usuarios = CRUD(usuarios)
    elif choice == 2:
        servicios = CRUD_servicios(servicios)
    elif choice == 3:
        ventas,servicios,informes = opc_reportes(ventas,servicios,informes)
    elif choice == 4:
        ventas,informes = opc_ventas(usuarios,ventas,servicios,informes)
    elif choice == 0:
        print("terminando proceso")
        break
    # guardado de los datos
    guardar_datos_json(usuarios,"JSON/usuarios.json")
    guardar_datos_json(servicios,"JSON/servicios.json")
    guardar_datos_json(ventas,"JSON/ventas.json")
    guardar_datos_json(informes,"JSON/informes.json")