import json

def abir_archivo(nombre):
    with open(nombre, 'r') as file:
        contenido = file.read()

    data = json.loads(contenido)
    estruct = data
    return estruct

def guardar_archivo(nombre,lista):
    pass

def mostrar(lista):
    for elemento in lista:
        print(elemento)