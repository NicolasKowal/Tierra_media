class Promociones:
    def __init__(self, tipo, clase, atr1, atr2) -> None:
        self.clase = clase
        self.tipo = tipo
        self.atr1 = atr1
        self.atr2 = atr2

    def __str__(self) -> str:
        return f"La promocion del tipo {self.clase}."


class PromocionPorcentual(Promociones):
    def __init__(self, tipo, clase, atr1, atr2, porcentaje) -> None:
        super().__init__(self, clase, atr1, atr2)
        self.porcentaje = porcentaje
        self.tipo = tipo

    def __str__(self) -> str:
        return f"La promocion del tipo {self.clase}, si compras {self.atr1} y {self.atr2}, tienes un {self.porcentaje}% de descuento."


class PromocionAbsoluta(Promociones):
    def __init__(self, tipo, clase, atr1, atr2, precio) -> None:
        super().__init__(self, clase, atr1, atr2)
        self.precio = precio
        self.tipo = tipo

    def __str__(self) -> str:
        return f"La promocion del tipo {self.clase}, compras {self.atr1} y {self.atr2} por {self.precio} monedas."


class PromocionAxB(Promociones):
    def __init__(self, tipo, clase, atr1, atr2, atr3) -> None:
        super().__init__(self, clase, atr1, atr2)
        self.atr3 = atr3
        self.tipo = tipo

    def __str__(self) -> str:
        return f"La promocion del tipo {self.clase}, si compras {self.atr1} y {self.atr2}, tienes {self.atr3} gratis."
