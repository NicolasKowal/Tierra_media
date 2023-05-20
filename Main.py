import json
from funciones import *
from Atracciones import *
from Perfiles import *

atracciones = abir_archivo("atracciones.json")
perfiles = abir_archivo("perfiles.json")

lugares = []
personas = []

for atraccion in atracciones:
    atrac = Atraccion(atraccion["nombre"], atraccion["precio"], atraccion["tiempo"], atraccion["cupo"], atraccion["tipo"])
    lugares.append(atrac)

for perfil in perfiles:
    person = Perfil(perfil["nombre"], perfil["tipo"], perfil["tiempo"], perfil["dinero"])
    personas.append(person)
    
for persona in personas:
    print("* "*25,f"\nBienvenido {persona.nombre}, tenes {persona.tiempo} horas para divertirte y ${persona.dinero} para gastar")
    for lugar in lugares:
        if lugar.tipo == persona.tipo:
           print(f"{lugar.nombre} sale {lugar.precio} monedas y quedan {lugar.cupo} lugares")
           opcion = input("- Acepta S/N: ")
           if opcion == "S" and persona.dinero >= lugar.precio and persona.tiempo >= lugar.tiempo:
                persona.total += lugar.precio
                persona.dinero -= lugar.precio
                persona.tiempo-= lugar.tiempo
                lugar.cupo -= 1
                print(f"SUBTOTAL ${persona.total} DINERO RESTANTE ${persona.dinero} TIEMPO RESTANTE {persona.tiempo} HORAS")

    for lugar in lugares:
        if lugar.tipo != persona.tipo:
           print(f"{lugar.nombre} sale {lugar.precio} monedas y quedan {lugar.cupo} lugares")
           opcion = input("- Acepta S/N: ")
           if opcion == "S" and persona.dinero >= lugar.precio and persona.tiempo >= lugar.tiempo:
                persona.total += lugar.precio
                persona.dinero -= lugar.precio
                persona.tiempo-= lugar.tiempo
                lugar.cupo -= 1
                print(f"SUBTOTAL ${persona.total} DINERO RESTANTE ${persona.dinero} TIEMPO RESTANTE {persona.tiempo} HORAS")
    print("\n")