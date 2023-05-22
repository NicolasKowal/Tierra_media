from funciones import *


print("ESTRUCTURA:  NOMBRE, PRECIO, TIEMPO, CUPO, TIPO")
atracciones = abir_archivo("atracciones.json")
continuar = 1
while continuar == 1:
    atraccion = []

    nombre = input("Nombre: ")
    nombre = nombre.capitalize()
    for user in atracciones:
        if nombre == user[0]:
            print("NOMBRE REPETIDO.")
            break
    else:
        atraccion.append(nombre)
        
        precio = limites(0, 10000, "Precio: ")
        atraccion.append(precio)
        
        tiempo = limites(0, 10000, "Tiempo: ")
        atraccion.append(tiempo)

        cupo = limites(0, 1000, "Cupo: ")
        atraccion.append(cupo)
        
        
        tipodeatraccion = limites(
            1, 3, "1. Aventura\n2. Degustacion\n3. Paisajes\n")
        if tipodeatraccion == 1:
            tipodeatraccion = "Aventura"
        elif tipodeatraccion == 2:
            tipodeatraccion = "Degustacion"
        elif tipodeatraccion == 3:
            tipodeatraccion = "Paisajes"
        atraccion.append(tipodeatraccion)

        continuar = limites(1, 2, "Continuar?\n1. Si\n2. No\n")
        atracciones.append(atraccion)
guardar_archivo("atracciones.json", atracciones)
