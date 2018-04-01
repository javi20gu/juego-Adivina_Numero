from Clases_Bases import SuperJugadores


class Jugadores(SuperJugadores):
    """Clase para un Jugador"""

    def __init__(self):
        super().__init__()
        self.set_jugador_intentos(4)
