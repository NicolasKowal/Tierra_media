from funciones import *
from Atracciones import *
from Perfiles import *
from Promociones import *

lugares = abir_archivo("atracciones.json")
perfiles = abir_archivo("perfiles.json")
promociones = abir_archivo("promociones.json")

atracciones = []
personas = []
promos = []

for lugar in lugares:
    atrac = Atraccion(lugar[0], lugar[1], lugar[2], lugar[3], lugar[4])
    atracciones.append(atrac)

for perfil in perfiles:
    person = Perfil(perfil[0], perfil[1], perfil[2], perfil[3])
    personas.append(person)

for promo in promociones:
    if promo[0] == 0:
        prom = PromocionPorcentual(
            promo[0], promo[1], promo[2], promo[3], promo[4])
    elif promo[0] == 1:
        prom = PromocionAbsoluta(
            promo[0], promo[1], promo[2], promo[3], promo[4])
    elif promo[0] == 2:
        prom = PromocionAxB(promo[0], promo[1], promo[2], promo[3], promo[4])
    promos.append(prom)

for persona in personas:
    carrito = []
    total = 0
    subtotal = 0
    tiempototal = 0
    print(
        "* "*25, f"\nBienvenido {persona.nombre}, tenes {persona.tiempo} horas para divertirte y {persona.dinero} monedas para gastar\n")

    print(f"Tenemos {len(promos)} promociones para ofrecerte:")
    i = 0

    for promo in promos:
        i += 1
        print(f"{i} - ", promo)

    opcion = limites(
        0, len(promos), "Te interesa alguna? escribi 0 en el caso contrario: ")

    condicion = 0
    x = 0
    for promo in promos:
        if x == opcion - 1:
            condicion = promo.tipo
        x += 1

    if condicion == 0:
        atr1 = promos[opcion-1].atr1
        # nombres de las atracciones de la promo guardadas
        atr2 = promos[opcion-1].atr2
        for atraccion in atracciones:  # se calcula si se tiene tiempo o plata
            if atraccion.nombre == atr1:
                subtotal += atraccion.precio
                tiempototal = atraccion.tiempo
            if atraccion.nombre == atr2:
                subtotal += atraccion.precio
                tiempototal += atraccion.tiempo

        # si tiene tiempo y dinero, se procede con la compra
        if persona.dinero >= subtotal and persona.tiempo >= tiempototal:
            print("Compra confirmada!\n")
            carrito.append(atr1)  # se agrega al carrito las atracciones
            carrito.append(atr2)
            subtotal = 0  # se resetean las variables para reutilizar al final
            tiempototal = 0

            for atraccion in atracciones:
                if atraccion.nombre == atr1:  # se recorren las atracciones para sacar el tiempo y el precio de la primer atraccion
                    subtotal += atraccion.precio
                    persona.tiempo -= atraccion.tiempo
                    atraccion.cupo -= 1
                    tiempototal += atraccion.tiempo
                if atraccion.nombre == atr2:  # se recorren las atracciones para sacar el tiempo y el precio de la segunda atraccion
                    subtotal += atraccion.precio
                    atraccion.cupo -= 1
                    persona.tiempo -= atraccion.tiempo
                    tiempototal += atraccion.tiempo
            # se guarda el descuento  MODIFICAR *-*-*-*-*-*-*-*-*-*-*-*-*
            total = subtotal - subtotal*.2
            persona.dinero -= total
            print(
                f"\nTu total es de {total} monedas, te quedaron {persona.dinero} monedas.\nTu tour va a durar {tiempototal} horas.\n")
        else:
            print("DINERO O TIEMPO INSUFICIENTE")

        for atraccion in atracciones:
            # se muestran atracciones de otro tipo, que no sean de promociones
            if atraccion.tipo == persona.tipo and atraccion.nombre != atr1 and atraccion.nombre != atr2:
                print(atraccion)
                opcion = limites(1, 2, "1.Si\n2.No\nAcepta?: ")
                if opcion == 1:
                    if persona.dinero >= atraccion.precio and persona.tiempo >= atraccion.tiempo:
                        print("\nCompra confirmada!\n")
                        persona.dinero -= atraccion.precio
                        persona.tiempo -= atraccion.tiempo
                        atraccion.cupo -= 1
                        total += atraccion.tiempo
                        subtotal += atraccion.precio
                        tiempototal += atraccion.tiempo
                        carrito.append(atraccion.nombre)
                    elif persona.dinero < atraccion.precio:
                        print(
                            f"Dinero insuficiente! tienes {persona.dinero} monedas y {atraccion.nombre} cuesta {atraccion.precio} monedas")
                    elif persona.tiempo < atraccion.tiempo:
                        print(
                            f"Tiempo insuficiente! tienes {persona.tiempo} horas y {atraccion.nombre} cuesta {atraccion.tiempo} horas")
        for atraccion in atracciones:
            if atraccion.tipo != persona.tipo and atraccion.nombre != atr1 and atraccion.nombre != atr2:
                print(atraccion)
                opcion = limites(1, 2, "1.Si\n2.No\nAcepta?: ")
                if opcion == 1:
                    if persona.dinero >= atraccion.precio and persona.tiempo >= atraccion.tiempo:
                        print("\nCompra confirmada!\n")
                        persona.dinero -= atraccion.precio
                        persona.tiempo -= atraccion.tiempo
                        atraccion.cupo -= 1
                        total += atraccion.tiempo
                        subtotal += atraccion.precio
                        tiempototal += atraccion.tiempo
                        carrito.append(atraccion.nombre)
                    elif persona.dinero < atraccion.precio:
                        print(
                            f"Dinero insuficiente! tienes {persona.dinero} monedas y {atraccion.nombre} cuesta {atraccion.precio} monedas")
                    elif persona.tiempo < atraccion.tiempo:
                        print(
                            f"Tiempo insuficiente! tienes {persona.tiempo} horas y {atraccion.nombre} cuesta {atraccion.tiempo} horas")
        print("Atracciones adquiridas:")
        mostrar(carrito)
        print(
            f"\nTu total es de {total} monedas, te quedaron {persona.dinero} monedas.\nTu tour va a durar {tiempototal} horas.")
