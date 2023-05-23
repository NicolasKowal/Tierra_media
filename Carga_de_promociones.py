from funciones import *


promociones = abir_archivo("promociones.json")
atracciones = abir_archivo("atracciones.json")
atraccionesaventura = []
atraccionespaisajes = []
atraccionesbanquete = []
for atraccion in atracciones:
    if atraccion[4] == "Aventura":
        atraccionesaventura.append(atraccion[0])
    elif atraccion[4] == "Paisajes":
        atraccionespaisajes.append(atraccion[0])
    elif atraccion[4] == "Banquete":
        atraccionesbanquete.append(atraccion[0])

continuar = 1

while continuar == 1:
    promo = []
    tipodepromo = limites(
        1, 3, "1. Descuento porcentual.\n2. Precio por las 2 atracciones.\n3. Atraccion gratuita.\n")
    if tipodepromo == 1:
        tipodepromo = 0
        promo.append(tipodepromo)
        print("ESTRUCTURA: TIPO DE PROMOCION, TIPO DE ATRACCION, ATRACCION, ATRACCION, PORCENTAJE")
        tipodeatraccion = limites(
            1, 3, "1. Aventura\n2. Banquete\n3. Paisajes\n")
        if tipodeatraccion == 1:
            tipodeatraccion = "Aventura"
        elif tipodeatraccion == 2:
            tipodeatraccion = "Banquete"
        elif tipodeatraccion == 3:
            tipodeatraccion = "Paisajes"
        promo.append(tipodeatraccion)

        atr3 = input(f"Ingrese Atraccion del tipo {tipodeatraccion}: ")
        atr3 = atr3.capitalize()

        if tipodeatraccion == "Aventura":
            if atr3 in atraccionesaventura:
                promo.append(atr3)
            else:
                print("Atraccion no encontrada o erronea")
                break
        if tipodeatraccion == "Paisajes":
            if atr3 in atraccionespaisajes:
                promo.append(atr3)
            else:
                print("Atraccion no encontrada")
                break
        if tipodeatraccion == "Banquete":
            if atr3 in atraccionesbanquete:
                promo.append(atr3)
            else:
                print("Atraccion no encontrada")
                break

        atr2 = input(f"Ingrese Atraccion del tipo {tipodeatraccion}: ")
        atr2 = atr2.capitalize()

        if tipodeatraccion == "Aventura":
            if atr2 in atraccionesaventura:
                promo.append(atr2)
            else:
                print("Atraccion no encontrada o erronea")
                break
        if tipodeatraccion == "Paisajes":
            if atr2 in atraccionespaisajes:
                promo.append(atr2)
            else:
                print("Atraccion no encontrada")
                break
        if tipodeatraccion == "Banquete":
            if atr2 in atraccionesbanquete:
                promo.append(atr2)
            else:
                print("Atraccion no encontrada")
                break

        total = limites(0, 100, "Porcentaje: ")
        promo.append(total)
        promociones.append(promo)
        continuar = limites(1, 2, "Continuar?\n1. Si\n2. No\n")

    elif tipodepromo == 2:
        tipodepromo = 1

        promo.append(tipodepromo)
        print(
            "ESTRUCTURA: TIPO DE PROMOCION, TIPO DE ATRACCION, ATRACCION, ATRACCION, PRECIO")
        tipodeatraccion = limites(
            1, 3, "1. Aventura\n2. Banquete\n3. Paisajes\n")
        if tipodeatraccion == 1:
            tipodeatraccion = "Aventura"
        elif tipodeatraccion == 2:
            tipodeatraccion = "Banquete"
        elif tipodeatraccion == 3:
            tipodeatraccion = "Paisajes"
        promo.append(tipodeatraccion)

        atr3 = input(f"Ingrese Atraccion del tipo {tipodeatraccion}: ")
        atr3 = atr3.capitalize()

        if tipodeatraccion == "Aventura":
            if atr3 in atraccionesaventura:
                promo.append(atr3)
            else:
                print("Atraccion no encontrada o erronea")
                break
        if tipodeatraccion == "Paisajes":
            if atr3 in atraccionespaisajes:
                promo.append(atr3)
            else:
                print("Atraccion no encontrada")
                break
        if tipodeatraccion == "Banquete":
            if atr3 in atraccionesbanquete:
                promo.append(atr3)
            else:
                print("Atraccion no encontrada")
                break

        atr2 = input(f"Ingrese Atraccion del tipo {tipodeatraccion}: ")
        atr2 = atr2.capitalize()

        if tipodeatraccion == "Aventura":
            if atr2 in atraccionesaventura:
                promo.append(atr2)
            else:
                print("Atraccion no encontrada o erronea")
                break
        if tipodeatraccion == "Paisajes":
            if atr2 in atraccionespaisajes:
                promo.append(atr2)
            else:
                print("Atraccion no encontrada")
                break
        if tipodeatraccion == "Banquete":
            if atr2 in atraccionesbanquete:
                promo.append(atr2)
            else:
                print("Atraccion no encontrada")
                break

        total = limites(0, 100, "Total: ")
        promo.append(total)
        promociones.append(promo)
        continuar = limites(1, 2, "Continuar?\n1. Si\n2. No\n")

    elif tipodepromo == 3:
        tipodepromo = 2
        promo.append(tipodepromo)
        print("ESTRUCTURA: TIPO DE PROMOCION, TIPO DE ATRACCION, ATRACCION, ATRACCION, ATRACCION")
        tipodeatraccion = limites(
            1, 3, "1. Aventura\n2. Banquete\n3. Paisajes\n")
        if tipodeatraccion == 1:
            tipodeatraccion = "Aventura"
        elif tipodeatraccion == 2:
            tipodeatraccion = "Banquete"
        elif tipodeatraccion == 3:
            tipodeatraccion = "Paisajes"
        promo.append(tipodeatraccion)

        atr1 = input(f"Ingrese Atraccion del tipo {tipodeatraccion}: ")
        atr1 = atr1.capitalize()

        if tipodeatraccion == "Aventura":
            if atr1 in atraccionesaventura:
                promo.append(atr1)
            else:
                print("Atraccion no encontrada o erronea")
                break
        if tipodeatraccion == "Paisajes":
            if atr1 in atraccionespaisajes:
                promo.append(atr1)
            else:
                print("Atraccion no encontrada")
                break
        if tipodeatraccion == "Banquete":
            if atr1 in atraccionesbanquete:
                promo.append(atr1)
            else:
                print("Atraccion no encontrada")
                break

        atr2 = input(f"Ingrese Atraccion del tipo {tipodeatraccion}: ")
        atr2 = atr2.capitalize()

        if tipodeatraccion == "Aventura":
            if atr2 in atraccionesaventura:
                promo.append(atr2)
            else:
                print("Atraccion no encontrada o erronea")
                break
        if tipodeatraccion == "Paisajes":
            if atr2 in atraccionespaisajes:
                promo.append(atr2)
            else:
                print("Atraccion no encontrada")
                break
        if tipodeatraccion == "Banquete":
            if atr2 in atraccionesbanquete:
                promo.append(atr2)
            else:
                print("Atraccion no encontrada")
                break

        atr3 = input(f"Ingrese Atraccion del tipo {tipodeatraccion}: ")
        atr3 = atr3.capitalize()

        if tipodeatraccion == "Aventura":
            if atr3 in atraccionesaventura:
                promo.append(atr3)
            else:
                print("Atraccion no encontrada o erronea")
                break
        if tipodeatraccion == "Paisajes":
            if atr3 in atraccionespaisajes:
                promo.append(atr3)
            else:
                print("Atraccion no encontrada")
                break
        if tipodeatraccion == "Banquete":
            if atr3 in atraccionesbanquete:
                promo.append(atr3)
            else:
                print("Atraccion no encontrada")
                break

        promociones.append(promo)
        continuar = limites(1, 2, "Continuar?\n1. Si\n2. No\n")
guardar_archivo("promociones.json", promociones)