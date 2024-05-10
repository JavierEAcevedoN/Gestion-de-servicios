# modulo de administrador C.R.U.D
def CRUD(datos):
    datos = list(datos) 
    while True:
        choice = -1
        try:
            choice = int(input("""
Modulo de usuarios (Administrador)
los cambios solo se guardan cuando termine el programa
ingresa la opcion: 
(1) Crear usuario.
(2) Leer usuario.
(3) Actualizar usuario.
(4) Eliminar usuario.
(5) Listar usuarios.
(0) Terminar. """))
        
        except Exception:
            print("ese valor no es valido")

        if choice == 1:
            datos = crear_usuario(datos)
        elif choice == 2:
            datos = leer_usuario(datos)
        elif choice == 3:
            datos = actualizar_usuario(datos)
        elif choice == 4:
            datos = eliminar_usuario(datos)
        elif choice == 5:
            datos = listar_usuarios(datos)
        elif choice == 0:
            print("terminando proceso")
            break
    return datos

# crear usuario
def crear_usuario(datos):
    datos = list(datos)
    nombre = input("ingresa el nombre del usuario ")
    id = input("ingresa la id del usuario (no repetir con otra id) ")
    for i in datos:
        if id == i["id"]:
            print("esa id no esta disponible")
            return datos
    direccion = input("ingresa la direccion del usuario ")
    contacto = input("ingresa el contacto del usuario ")
    datos.append(
        {
            "nombre":nombre.capitalize(),
            "id":id,
            "direccion":direccion.capitalize(),
            "contacto":contacto.capitalize(),
            "categoria": "Nuevo",
            "servicios": []
        }
    )
    print("participante resgistrado")
    return datos

# mostrar la informacion del usuario
def leer_usuario(datos):
    datos = list(datos)
    id = input("ingresa la id del usuario ")
    for i in datos:
        if id == i["id"]:
            for j in i:
                print(j,":",i[j])
            return datos
    print("no se encontro el usuario")
    return datos

# actualizar la informacion del usuario (direccion, contacto, categoria)
def actualizar_usuario(datos):
    datos = list(datos)
    choice = "0"
    id = input("ingresa la id del usuario ")
    for i in range(len(datos)):
        if id == datos[i]["id"]:
            choice = input("1 para la informacion, 2 para los servicios ")
            if choice == "1":
                direccion = input("ingresa la direccion del usuario ")
                contacto = input("ingresa el contacto del usuario ")
                categoria = input("ingresa la categoria del usuario (nuevo, regular o leal) ")
                datos[i]["direccion"] = direccion.capitalize()
                datos[i]["contacto"] = contacto.capitalize()
                datos[i]["categoria"] = categoria.capitalize()
                print("informacion del usuario actualizada")
                return datos
            elif choice == "2":
                datos[i]["servicios"].append(input("ingresa el nuevo servicio del usuario "))
    print("no se encontro el usuario")
    return datos

# eliminar usuarios
def eliminar_usuario(datos):
    datos = list(datos)
    id = input("ingresa la id del usuario ")
    for i in range(len(datos)):
        if id == datos[i]["id"]:
            datos.pop(i)
            print("usuario eliminado")
            return datos
    print("no se encontro el usuario")
    return datos

# mostrar todos los usuarios
def listar_usuarios(datos):
    datos = list(datos)
    for i in datos:
        print(i["nombre"])
        print(i["id"])
        print("")
    return datos