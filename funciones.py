import json


def abir_archivo(nombre):
    with open(nombre, 'r') as file:
        contenido = file.read()
    data = json.loads(contenido)
    estruct = data
    return estruct


def guardar_archivo(nombre, lista):
    pass


def mostrar(lista):
    for elemento in lista:
        print(elemento)


def validar_numeros(frase):
    while True:
        try:
            valor = int(input(f"{frase}"))
            break
        except ValueError:
            print("No se ha detectado un numero, vuelva a ingresar.")
    return valor


def limites(inferior, superior, frase="numero"):
    numero = validar_numeros(frase)
    while numero < inferior or numero > superior:
        print(
            f"El numero tiene que ser mayor que {inferior} y menor que {superior}")
        numero = validar_numeros(frase)
    return numero

def calcular_porcentaje(numero, porcentaje):
    return numero - (porcentaje * numero /100)