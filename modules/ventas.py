# modulo de ventas
def opc_ventas(usuarios,ventas,servicios,informes):
    usuarios = list(usuarios)
    ventas = list(ventas)
    servicios = list(servicios)
    informes = list(informes)
    while True:
        choice = -1
        try:
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

# agregar la fecha a el registro
# ver si esta disponible
# registrar venta
def agregar_ventas(usuarios,ventas,servicios,informes):
    usuarios = list(usuarios)
    ventas = list(ventas)
    servicios = list(servicios)
    informes = list(informes)
    venta = {}
    usuario = {}
    servicio_encontrado = False
    usuario_encontrado = False
    id_servicio = input("ingresa la id del servicio vendido ")
    for i in range(len(servicios)):
        if id_servicio == servicios[i]["id"]:
            venta = servicios[i]
            servicio_encontrado = True
            break
    id_usuario = input("ingresa la id del usuario al que le vendiste el servicio ")
    for i in range(len(usuarios)):
        if id_usuario == usuarios[i]["id"]:
            usuario = usuarios[i]
            usuario_encontrado = True
            break
    if servicio_encontrado and usuario_encontrado:
        try:
            vendido = int(input("ingresa la cantidad de ventas del servicio "))
        except Exception:
                print("ese valor no es valido")
                return usuarios,ventas,servicios,informes
        for i in servicios:
            if i["id"] == id_servicio:
                i["cantidad"] -= vendido
                break
        for i in usuarios:
            if i["id"] == id_usuario:
                    if any(i["servicios"]):
                        for j in i["servicios"]:
                            if j == venta["servicio"]:
                                break
                            else:
                                i["servicios"].append(venta["servicio"])
                                break
                    else:
                        i["servicios"].append(venta["servicio"])
                        break
        for i in range(len(ventas)):
            if id_servicio == ventas[i]["id"]:
                ventas[i]["precio"] = venta["precio"]
                ventas[i]["caracteristicas"] = venta["caracteristicas"]
                ventas[i]["vendido"] += vendido
                print("venta registrada")
                informes.append(
                    {
                        "servicio":venta["servicio"],
                        "usuario":usuario["nombre"],
                        "precio": venta["precio"],
                        "caracteristicas":venta["caracteristicas"],
                        "fecha": "8:34 AM"
                    }
                )
                return usuarios,ventas,servicios,informes
        ventas.append(
            {
                "servicio":venta["servicio"],
                "precio":venta["precio"],
                "caracteristicas":venta["caracteristicas"],
                "vendido":vendido,
                "id":id_servicio
            }
        )
        informes.append(
            {
                "servicio":venta["servicio"],
                "usuario":usuario["nombre"],
                "precio": venta["precio"],
                "caracteristicas":venta["caracteristicas"],
                "fecha": "8:34 AM"
            }
        )
        print("venta registrada")
        return usuarios,ventas,servicios,informes
    else:
        print("ese servicio/usuario no existen")
        return usuarios,ventas,servicios,informes

# mostrar todas las ventas
def listar_ventas(ventas):
    ventas = list(ventas)
    for i in ventas:
        for j in i:
            print(j,":",i[j])
        print("")
    return ventas