from modules.secondary_funtions import time_complete
# modulo de ventas
def opc_ventas(usuarios,ventas,servicios,informes):
    usuarios = list(usuarios)
    ventas = list(ventas)
    servicios = list(servicios)
    informes = list(informes)
    while True:
        choice = -1
        try:
            #opciones
            choice = int(input("""
Modulo de ventas
los cambios solo se guardan cuando termine el programa
ingresa la opcion: 
(1) Registrar venta.
(2) Listar ventas.
(0) Terminar. """))
        
        except Exception:
            print("ese valor no es valido")

        if choice == 1:
            usuarios,ventas,servicios,informes = agregar_ventas(usuarios,ventas,servicios,informes)
        elif choice == 2:
            ventas = listar_ventas(ventas)
        elif choice == 0:
            print("terminando proceso")
            break
    return ventas,informes

# ver si esta disponible
# registrar venta
def agregar_ventas(usuarios,ventas,servicios,informes):
    # definiendo variables
    usuarios = list(usuarios)
    ventas = list(ventas)
    servicios = list(servicios)
    informes = list(informes)
    venta = {}
    usuario = {}
    servicio_encontrado = False
    usuario_encontrado = False
    ya_lo_tinene = True
    # preguntando por la id del producto la cantidad y la id a quien se lo esta vendiendo
    # verificar si la id del servicio existe
    id_servicio = input("ingresa la id del servicio vendido ")
    for i in range(len(servicios)):
        if id_servicio == servicios[i]["id"]:
            venta = servicios[i]
            servicio_encontrado = True
            break
    # verificar si la id del usuario existe
    id_usuario = input("ingresa la id del usuario al que le vendiste el servicio ")
    for i in range(len(usuarios)):
        if id_usuario == usuarios[i]["id"]:
            usuario = usuarios[i]
            usuario_encontrado = True
            break
    # continuar si las dos id's existen
    if servicio_encontrado and usuario_encontrado:
        # preguntar la cantidad de servicio vendido
        try:
            vendido = int(input("ingresa la cantidad de ventas del servicio "))
            if vendido < 0:
                print("los valores negativos no son validos")
                return usuarios,ventas,servicios,informes
        except Exception:
                print("ese valor no es valido")
                return usuarios,ventas,servicios,informes
        # descontar de la cantidad del servicio disponible
        for i in servicios:
            if i["id"] == id_servicio:
                if (i["cantidad"] - vendido) >= 0:
                        i["cantidad"] -= vendido
                        break
                else:
                    print("no hay disponible esa cantidad del servicio")
                    return usuarios,ventas,servicios,informes
        # asignar el servicio adquirido al usuario
        for i in usuarios:
            if i["id"] == id_usuario:
                    if any(i["servicios"]):
                        for j in i["servicios"]:
                            if j == venta["servicio"]:
                                ya_lo_tinene = False
                                break
                        if ya_lo_tinene:
                            i["servicios"].append(venta["servicio"])
                            break
                    else:
                        i["servicios"].append(venta["servicio"])
                        break
        # verificar si ese servicio ya existe informacion de venta, actualizarla y agregar la cantidad vendida
        for i in range(len(ventas)):
            if id_servicio == ventas[i]["id"]:
                ventas[i]["precio"] = venta["precio"]
                ventas[i]["caracteristicas"] = venta["caracteristicas"]
                ventas[i]["vendido"] += vendido
                print("venta registrada")
                # crear el informe de la compra
                informes.append(
                    {
                        "servicio":venta["servicio"],
                        "usuario":usuario["nombre"],
                        "precio": venta["precio"],
                        "caracteristicas":venta["caracteristicas"],
                        "cantidad":vendido,
                        "total":vendido*venta["precio"],
                        "fecha": f"{time_complete()}"
                    }
                )
                return usuarios,ventas,servicios,informes
        # si no existe informacion de venta, crearla de 0
        ventas.append(
            {
                "servicio":venta["servicio"],
                "precio":venta["precio"],
                "caracteristicas":venta["caracteristicas"],
                "vendido":vendido,
                "id":id_servicio
            }
        )
        # crear el informe de la factura
        informes.append(
            {
                "servicio":venta["servicio"],
                "usuario":usuario["nombre"],
                "precio": venta["precio"],
                "caracteristicas":venta["caracteristicas"],
                "cantidad":vendido,
                "total":vendido*venta["precio"],
                "fecha": f"{time_complete()}"
            }
        )
        print("venta registrada")
        return usuarios,ventas,servicios,informes
    # si no existen terminar
    else:
        print("ese servicio/usuario no existen")
        return usuarios,ventas,servicios,informes

# mostrar todas las ventas realizadas
def listar_ventas(ventas):
    ventas = list(ventas)
    for i in ventas:
        for j in i:
            print(j,":",i[j])
        print("")
    return ventas