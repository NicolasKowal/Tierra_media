class Perfil:
    def __init__(self,nombre, tipo, tiempo, dinero):
        self.nombre = nombre
        self.tipo = tipo
        self.tiempo = tiempo
        self.dinero = dinero
        self.total = 0

    def __str__(self) -> str:
        return f"{self.nombre} es el tipo {self.tipo}, cuenta con {self.tiempo} horas y tiene {self.dinero} monedas"