from modules.secondary_funtions import *

# modulo de servicio al cliente
def opc_servicio_al_cliente(usuarios,interacciones):
    try:
        usuarios = list(usuarios)
        interacciones = list(interacciones)
    except Exception as e:
        exeptions(repr(e))
        print("error en las variables")

    while True:
        choice = -1
        try:
            #opciones
            choice = int(input("""
Modulo de ventas
los cambios solo se guardan cuando termine el programa
ingresa la opcion: 
(1) Consulta.
(2) Servicio al cliente.
(3) Reclamaciones.
(4) Sugerencias.
(0) Terminar. """))
        
        except Exception as e:
            exeptions(repr(e))
            print("ese valor no es valido")

        if choice == 1:
            usuarios,interacciones = agregar_interacccion(usuarios,interacciones,1)
        elif choice == 2:
            usuarios,interacciones = agregar_interacccion(usuarios,interacciones,2)
        elif choice == 3:
            usuarios,interacciones = agregar_interacccion(usuarios,interacciones,3)
        elif choice == 4:
            usuarios,interacciones = agregar_interacccion(usuarios,interacciones,4)
        elif choice == 0:
            print("terminando proceso")
            break

    return usuarios,interacciones

# registrar interaccion
def agregar_interacccion(usuarios,interacciones,opc):
    try:
        # definiendo variables
        usuarios = list(usuarios)
        interacciones = list(interacciones)
        opc = int(opc)
        usuario = {}
        usuario_encontrado = False
        ya_lo_tinene = True
        interaccion = ""
        mensaje = ""
    except Exception as e:
        exeptions(repr(e))
        print("error en las variables")
    
    # verificar si la id del usuario existe
    id_usuario = input("ingresa tu id de usuario ")
    for i in range(len(usuarios)):
        if id_usuario == usuarios[i]["id"]:
            usuario = usuarios[i]
            usuario_encontrado = True
            break

    
    # continuar si la id existe
    if usuario_encontrado:
        
        # que tipo de interaccion es
        if opc == 1:
            interaccion = "Consulta"
            mensaje = input("ingresa tu consulta aqui ")
        elif opc == 2:
            interaccion = "Servicio al cliente"
            mensaje = input("no hay servicio al cliente, pero deja tu mensaje aqui ")
        elif opc == 3:
            interaccion = "Reclamacion"
            mensaje = input("ingresa tu reclamacion aqui ")
        elif opc == 4:
            interaccion = "Sugerencia"
            mensaje = input("ingresa tu sugerencia aqui ")

        # asignar la interaccion del usuario
        for i in usuarios:
            if i["id"] == id_usuario:
                    if any(i["interacciones"]):
                        for j in i["interacciones"]:
                            if j == interaccion:
                                ya_lo_tinene = False
                                break
                        if ya_lo_tinene:
                            i["interacciones"].append(interaccion)
                            break
                    else:
                        i["interacciones"].append(interaccion)
                        break

        # crear el informe de la interaccion
        interacciones.append(
            {
                "usuario":usuario["nombre"],
                "id":usuario["id"],
                "interaccion":f"({interaccion}), {mensaje}",
                "contacto":usuario["contacto"],
                "categoria":usuario["categoria"],
                "fecha": f"{time_complete()}"
            }
        )
        print("interaccion registrada")
        return usuarios,interacciones

    # si no existe terminar
    else:
        print("ese usuario no existe")
        return usuarios,interacciones