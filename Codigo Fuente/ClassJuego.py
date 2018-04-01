from Clases_Bases import SuperJuego


class Juego(SuperJuego):
    """Clase Principal del Juego"""

    def __init__(self):
        self.set_intentos(4)
        self.set_rangos(1, 100)
