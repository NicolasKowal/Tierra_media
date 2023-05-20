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
    pr = Promociones(promo[0], promo[1], promo[2], promo[3])
    promos.append(pr)

for persona in personas:
    carrito = []
    print("* "*25,f"\nBienvenido {persona.nombre}, tenes {persona.tiempo} horas para divertirte y ${persona.dinero} para gastar\n")
    print(f"Tenemos {len(promos)} promociones para ofrecerte:")
    i = 0
    for promo in promos:
        i +=1
        print(f"{i} - ", promo)
    eleccion = int(input("- ¿Queres alguna? 0 para ninguna "))

    if eleccion == 1:
        for atraccion in atracciones:
            if atraccion.nombre == "Bosque negro":
                precio_bn = atraccion.precio - (20 * atraccion.precio / 100)
                persona.total += precio_bn
                persona.dinero -= precio_bn
                persona.tiempo-= atraccion.tiempo
                atraccion.cupo -= 1
                carrito.append(atraccion.nombre)
            if atraccion.nombre == "Mordor":
                precio_m = atraccion.precio - (20 * atraccion.precio / 100)
                persona.total += precio_m
                persona.dinero -= precio_m
                persona.tiempo-= atraccion.tiempo
                atraccion.cupo -= 1
                carrito.append(atraccion.nombre)
        print(f"\nSubtotal: ${persona.total}. \nDinero restante ${persona.dinero}.\nTiempo disponible {persona.tiempo} horas.\n")
        for atraccion in atracciones:
            if atraccion.tipo == persona.tipo and atraccion.nombre != "Bosque negro" and atraccion.nombre != "Mordor":
                print(f"{atraccion.nombre} sale {atraccion.precio} monedas y quedan {atraccion.cupo} lugares")
                opcion = input("Acepta? S/N: ")
                print("\n")
                if opcion == "S":
                    persona.total += atraccion.precio
                    persona.dinero -= atraccion.precio
                    persona.tiempo-= atraccion.tiempo
                    atraccion.cupo -= 1
                    print(f"Subtotal: ${persona.total}. \nDinero restante ${persona.dinero}.\nTiempo disponible {persona.tiempo} horas.\n")
        for atraccion in atracciones:
            if atraccion.tipo != persona.tipo and atraccion.nombre != "Bosque negro" and atraccion.nombre != "Mordor":
                print(f"{atraccion.nombre} sale {atraccion.precio} monedas y quedan {atraccion.cupo} lugares")
                opcion = input("Acepta? S/N: ")
        print(f"Subtotal: ${persona.total}. \nDinero restante ${persona.dinero}.\nTiempo disponible {persona.tiempo} horas.\n")


    if eleccion == 2:
        for atraccion in atracciones:

            if atraccion.nombre == "Lothlorien":
                persona.total += 18
                persona.dinero -= 18
                persona.tiempo-= atraccion.tiempo
                atraccion.cupo -= 1
                carrito.append(atraccion.nombre)

            if atraccion.nombre == "La comarca":
                persona.total += 18
                persona.dinero -= 18
                persona.tiempo-= atraccion.tiempo
                atraccion.cupo -= 1
                carrito.append(atraccion.nombre)

    if eleccion == 3:
        for atraccion in atracciones:

            if atraccion.nombre == "Minas tirith":
                persona.total += atraccion.precio
                persona.dinero -= atraccion.precio
                persona.tiempo-= atraccion.tiempo
                atraccion.cupo -= 1
                carrito.append(atraccion.nombre)

            if atraccion.nombre == "Abismo de helm":
                persona.total += atraccion.precio
                persona.dinero -= atraccion.precio
                persona.tiempo-= atraccion.tiempo
                atraccion.cupo -= 1
                carrito.append(atraccion.nombre)

            if atraccion.nombre == "Erebor":
                persona.total += 0
                persona.dinero -= 0
                persona.tiempo-= 0
                atraccion.cupo -= 1
                carrito.append(atraccion.nombre)

    print(f"Subtotal: ${persona.total}. \nDinero restante ${persona.dinero}.\nTiempo disponible {persona.tiempo} horas.\n\n")


            







# for persona in personas:
#     
#     for lugar in lugares:
#         if lugar.tipo == persona.tipo:
#            print(f"{lugar.nombre} sale {lugar.precio} monedas y quedan {lugar.cupo} lugares")
#            opcion = input("- Acepta S/N: ")
#            if opcion == "S" and persona.dinero >= lugar.precio and persona.tiempo >= lugar.tiempo:
#                 persona.total += lugar.precio
#                 persona.dinero -= lugar.precio
#                 persona.tiempo-= lugar.tiempo
#                 lugar.cupo -= 1
#                 print(f"SUBTOTAL ${persona.total} DINERO RESTANTE ${persona.dinero} TIEMPO RESTANTE {persona.tiempo} HORAS")
#     for lugar in lugares:
#         if lugar.tipo != persona.tipo:
#            print(f"{lugar.nombre} sale {lugar.precio} monedas y quedan {lugar.cupo} lugares")
#            opcion = input("- Acepta S/N: ")
#            if opcion == "S" and persona.dinero >= lugar.precio and persona.tiempo >= lugar.tiempo:
#                 persona.total += lugar.precio
#                 persona.dinero -= lugar.precio
#                 persona.tiempo-= lugar.tiempo
#                 lugar.cupo -= 1
#                 print(f"SUBTOTAL ${persona.total} DINERO RESTANTE ${persona.dinero} TIEMPO RESTANTE {persona.tiempo} HORAS")
#            else:
#                 print(f"Solo te quedan ${persona.dinero}")
#     print("\n")

# guardar_archivo("atracciones.json", lugares)
# guardar_archivo("perfiles.json", personas)