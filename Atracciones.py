class Atraccion:
    def __init__(self, nombre, precio, tiempo, cupo, tipo):
        self.nombre = nombre
        self.precio = precio
        self.tiempo = tiempo
        self.cupo = cupo
        self.tipo = tipo

    def __str__(self) -> str:
        return f"La atraccion {self.nombre} es del tipo {self.tipo}, dura {self.tiempo} horas y cuesta {self.precio} monedas. Actualmente cuenta con {self.cupo} cupos."
