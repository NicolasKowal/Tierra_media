class Promociones:
    def __init__(self, nombre, atr1, atr2, condicion) -> None:
        self.nombre = nombre
        self.atr1 = atr1
        self.atr2 = atr2
        self.condicion = condicion
    
    def __str__(self) -> str:
        return f"La promocion {self.nombre} ofrece una promocion por {self.atr1} y {self.atr2}, {self.condicion}."