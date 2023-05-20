class Atraccion:
    def __init__(self, nombre, precio, tiempo, cupo, tipo) -> None:
        self.nombre = nombre
        self.precio = precio
        self.tiempo = tiempo
        self.cupo = cupo
        self.tipo = tipo
        
    def __str__(self) -> str:
         return f"{self.nombre}"