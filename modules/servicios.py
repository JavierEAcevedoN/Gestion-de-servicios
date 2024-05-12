from modules.secondary_funtions import exeptions

def CRUD_servicios(datos):
    # comprobar contraseña para continuar
    while True:
        password = input("ingresa la contraseña, para regresar escribe 'salir' ")
        if password == "administradorClaro312":
            break
        elif password == "salir":
            return datos

    # modulo de servicios
    datos = list(datos) 
    while True:
        choice = -1
        try:
            choice = int(input("""
Modulo de productos/servicios
los cambios solo se guardan cuando termine el programa
ingresa la opcion: 
(1) Agregar producto/servicio.
(2) Actualizar producto/servicio.
(3) Eliminar producto/servicio.
(4) Listar productos/servicios.
(0) Terminar. """))
        
        except Exception as e:
            exeptions(repr(e))
            print("ese valor no es valido")

        try:
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
        except Exception as e:
            exeptions(repr(e))
            print("hubo un error en los modulos")
    return datos

# agregar producto/servicio
def agregar_servicios(datos):
    datos = list(datos)

    # pedir la informacion sobre el producto/servicio
    nombre = input("ingresa el nombre del producto/servicio ")
    id = input("ingresa la id del producto/servicio (no repetir con otra id) ")
    caracteristicas = input("ingresa las caracteristicas del producto/servicio ")

    # verificar si esa id ya esta en uso
    for i in datos:
        if id == i["id"]:
            print("esa id no esta disponible")
            return datos
    try:
        precio = int(input("ingresa el precio del producto/servicio "))
        cantidad = int(input("ingresa la catidad disponible del producto/servicio "))
        if precio < 0 or cantidad < 0:
            print("los valores negativos no son validos")
            return datos
    except Exception as e:
        exeptions(repr(e))
        print("ese valor no es valido")
        return datos

    # agregando el nuevo producto/servicio
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

# actualizar la informacion del producto/servicio (precio y cantidad)
def actualizar_servicio(datos):
    datos = list(datos)

    # buscar el producto/servicio por medio de la id
    id = input("ingresa la id del producto/servicio ")
    for i in range(len(datos)):
        if id == datos[i]["id"]:

            # pedir la nueva informacion del producto/servicio
            caracteristicas = input("ingresa las nuevas caracteristicas del producto/servicio ")
            try:
                precio = int(input("ingresa el nuevo precio del producto/servicio "))
                cantidad = int(input("ingresa la nueva catidad disponible del producto/servicio "))
                if precio < 0 or cantidad < 0:
                    print("los valores negativos no son validos")
                    return datos
            except Exception as e:
                exeptions(repr(e))
                print("ese valor no es valido")
                return datos

            # actualizar la informacion
            datos[i]["precio"] = precio
            datos[i]["caracteristicas"] = caracteristicas
            datos[i]["cantidad"] = cantidad
            print("informacion del producto/servicio actualizada")
            return datos

    # si no se encontro la id
    print("no se encontro el producto/servicio")
    return datos

# eliminar productos/servicios por medio de la id
def eliminar_servicio(datos):
    datos = list(datos)
    id = input("ingresa la id del producto/servicio ")

    # verificar si existe la id
    for i in range(len(datos)):
        if id == datos[i]["id"]:
            datos.pop(i)
            print("producto/servicio eliminado")
            return datos

    # si no existe la id
    print("no se encontro el producto/servicio")
    return datos

# mostrar todos los productos/servicios
def listar_servicios(datos):
    datos = list(datos)
    for i in datos:
        for j in i:
            print(j,":",i[j])
        print("")
    return datos