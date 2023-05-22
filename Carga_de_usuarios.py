from funciones import *


print("ESTRUCTURA: NOMBRE, TIPO DE ATRACCION, TIEMPO, DINERO")
usuarios = abir_archivo("perfiles.json")
while continuar == 1:
    usuario = []

    nombre = input("Nombre: ")
    nombre = nombre.capitalize()
    for user in usuarios:
        if nombre == user[0]:
            print("NOMBRE REPETIDO.")
            break
    else:
        usuario.append(nombre)
        tipodeatraccion = limites(
            1, 3, "1. Aventura\n2. Degustacion\n3. Paisajes\n")
        if tipodeatraccion == 1:
            tipodeatraccion = "Aventura"
        elif tipodeatraccion == 2:
            tipodeatraccion = "Degustacion"
        elif tipodeatraccion == 3:
            tipodeatraccion = "Paisajes"
        usuario.append(tipodeatraccion)
        tiempo = limites(0, 10000, "Tiempo disponible: ")
        usuario.append(tiempo)
        dinero = limites(0, 10000, "Dinero disponible: ")
        usuario.append(dinero)
        continuar = limites(1, 2, "Continuar?\n1. Si\n2. No\n")
        usuarios.append(usuario)
guardar_archivo("perfiles.json", usuarios)
