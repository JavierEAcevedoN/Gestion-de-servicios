from modulos.datos_json import *
from modulos.crud import CRUD 
from modulos.servicios import CRUD_servicios
from modulos.ventas import opc_ventas

usuarios = cargar_datos_json("JSON/usuarios.json")
servicios = cargar_datos_json("JSON/servicios.json")
ventas = cargar_datos_json("JSON/ventas.json")

while True:
    choice = -1
    try:
        choice = int(input("""
Menu general
los cambios solo se guardan cuando termine el programa
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
        None
    elif choice == 4:
        ventas = opc_ventas(ventas,servicios)
    elif choice == 0:
        print("terminando proceso")
        break
    guardar_datos_json(usuarios,"JSON/usuarios.json")
    guardar_datos_json(servicios,"JSON/servicios.json")
    guardar_datos_json(ventas,"JSON/ventas.json")