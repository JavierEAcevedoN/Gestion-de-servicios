# modulo de ventas
def opc_ventas(ventas,servicios):
    ventas = list(ventas)
    servicios = list(servicios)
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
            ventas,servicios = agregar_ventas(ventas,servicios)
        elif choice == 2:
            ventas = listar_ventas(ventas)
        elif choice == 0:
            print("terminando proceso")
            break
    return ventas

# registrar venta
def agregar_ventas(ventas,servicios):
    ventas = list(ventas)
    servicios = list(servicios)
    venta = {}
    encontrado = False
    id = input("ingresa la id del servicio vendido ")
    for i in range(len(servicios)):
        if id == servicios[i]["id"]:
            venta = servicios[i]
            encontrado = True
            break
    if encontrado:
        try:
            vendido = int(input("ingresa la cantidad de ventas del servicio "))
        except Exception:
                print("ese valor no es valido")
                return ventas,servicios
        for i in servicios:
            if i["id"] == id:
                i["cantidad"] -= vendido
                break
        for i in range(len(ventas)):
            if id == ventas[i]["id"]:
                ventas[i]["precio"] = venta["precio"]
                ventas[i]["caracteristicas"] = venta["caracteristicas"]
                ventas[i]["vendido"] += vendido
                print("venta registrada")
                return ventas,servicios
        ventas.append(
            {
                "servicio":venta["servicio"],
                "precio":venta["precio"],
                "caracteristicas":venta["caracteristicas"],
                "vendido":vendido,
                "id":id
            }
        )
        print("venta registrada")
        return ventas,servicios
    else:
        print("ese servicio no existe")
        return ventas,servicios

# mostrar todas las ventas
def listar_ventas(ventas):
    ventas = list(ventas)
    for i in ventas:
        for j in i:
            print(j,":",i[j])
        print("")
    return ventas