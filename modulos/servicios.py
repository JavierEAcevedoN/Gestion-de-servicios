# modulo de servicios
def CRUD_servicios(datos):
    datos = list(datos) 
    while True:
        choice = -1
        try:
            choice = int(input("""
Modulo de servicios
los cambios solo se guardan cuando termine el programa
ingresa la opcion: 
(1) Agregar servicio.
(2) Actualizar servicio.
(3) Eliminar servicio.
(4) Listar servicios.
(0) Terminar. """))
        
        except Exception:
            print("ese valor no es valido")

        if choice == 1:
            datos = agregar_servicios(datos)
        elif choice == 2:
            datos = actualizar_servicio(datos)
        elif choice == 3:
            datos = eliminar_servicio(datos)
        elif choice == 4:
            datos = listar_servicios(datos)
        elif choice == 0:
            print("terminando proceso")
            break
    return datos

# agregar servicio
def agregar_servicios(datos):
    datos = list(datos)
    nombre = input("ingresa el nombre del servicio ")
    id = input("ingresa la id del servicio (no repetir con otra id) ")
    caracteristicas = input("ingresa las caracteristicas del servicio ")
    for i in datos:
        if id == i["id"]:
            print("esa id no esta disponible")
            return datos
    try:
        precio = int(input("ingresa el precio del servicio "))
        cantidad = int(input("ingresa la catidad disponible del servicio "))
    except Exception:
        print("ese valor no es valido")
        return datos
    datos.append(
        {
            "servicio":nombre.capitalize(),
            "precio":precio,
            "caracteristicas":caracteristicas,
            "cantidad":cantidad,
            "id":id
        }
    )
    print("servicio resgistrado")
    return datos

# actualizar la informacion del servicio (precio y cantidad)
def actualizar_servicio(datos):
    datos = list(datos)
    id = input("ingresa la id del servicio ")
    for i in range(len(datos)):
        if id == datos[i]["id"]:
            caracteristicas = input("ingresa las nuevas caracteristicas del servicio ")
            try:
                precio = int(input("ingresa el nuevo precio del servicio "))
                cantidad = int(input("ingresa la nueva catidad disponible del servicio "))
            except Exception:
                print("ese valor no es valido")
                return datos
            datos[i]["precio"] = precio
            datos[i]["caracteristicas"] = caracteristicas
            datos[i]["cantidad"] = cantidad
            print("informacion del servicio actualizada")
            return datos
    print("no se encontro el servicio")
    return datos

# eliminar servicios
def eliminar_servicio(datos):
    datos = list(datos)
    id = input("ingresa la id del servicio ")
    for i in range(len(datos)):
        if id == datos[i]["id"]:
            datos.pop(i)
            print("servicio eliminado")
            return datos
    print("no se encontro el servicio")
    return datos

# mostrar todos los servicios
def listar_servicios(datos):
    datos = list(datos)
    for i in datos:
        for j in i:
            print(j,":",i[j])
        print("")
    return datos