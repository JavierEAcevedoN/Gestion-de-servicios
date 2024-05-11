# modulo de reportes
def opc_reportes(ventas,servicios,informes):
    ventas = list(ventas)
    servicios = list(servicios)
    informes = list(informes)
    while True:
        choice = -1
        try:
            choice = int(input("""
Modulo de reportes
ingresa la opcion: 
(1) Reporte de cantidad de productos/servicios ofrecidos.
(2) Reporte de productos/servicios populares.
(3) informes de usuarios adquiriendo productos/servicios.
(0) Terminar. """))
        
        except Exception:
            print("ese valor no es valido")

        if choice == 1:
            servicios = reporte_cantidad(servicios)
        elif choice == 2:
            ventas = reporte_popularidad(ventas)
        elif choice == 3:
            informes = informe_servicios_usuarios(informes)
        elif choice == 0:
            print("terminando proceso")
            break
    return ventas,servicios,informes

# mostrar todos los servicios ofrecidos
def reporte_cantidad(datos):
    datos = list(datos)
    for i in datos:
        print("")
        print(f"esta disponible el servicio {i['servicio']}")
        print(f"con una cantidad de {i['cantidad']} dispociciones")
    return datos

# mostrar de mayor a manor los servicios mas populares
def reporte_popularidad(datos):
    datos = list(datos)
    popular = {}
    popular = list(popular)
    count = 0
    for i in datos:
        popular.append(i["vendido"])
    popular.sort(reverse=True)
    for i in popular:
        for j in datos:
            if i == j["vendido"]:
                count += 1
                print(f"el {count}º servicio mas popular es {j['servicio']} con {j['vendido']} ventas")
    return datos

# informe de las compras de los usuarios
def informe_servicios_usuarios(datos):
    datos = list(datos)
    print("")
    for i in datos:
        for j in i:
            print(j,":",i[j])
        print("")
    return datos