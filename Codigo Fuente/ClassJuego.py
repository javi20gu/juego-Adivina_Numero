from colorama import Fore

class Juego:
    """Clase Principal del Juego"""

    __intentos = 4
    __jugadores = []
    __rango1, __rango2 = 1, 100


    def __str__(self):
        return "Bienvenido al Juego, si desea obtener ayuda introduzca el comando help(self)"


    def puntuacion_de_la_partida(self):
        """Muestra el Marcador de la Partida"""
        print(Fore.LIGHTWHITE_EX + "", end='')
        for i in self.__jugadores:
            print("""\nJugador: {}
    Intentos: {}
    Puntuacion: {}""".format(i.get_jugado_nombre(), i.get_jugador_intentos(), i.get_jugador_puntuacion_total()))


    def set_intentos(self, intento: int):
        """Cambia los intentos del Juego"""
        self.__intentos = intento

    def set_jugadores(self, jugador: object):
        """Añade un jugador al Juego"""
        self.__jugadores.append(jugador)

    def set_rangos(self, rango1, rango2):
        """Cambia los rangos del Juego"""
        self.__rango1, self.__rango2 = rango1, rango2
    

    def get_intentos(self) -> int:
        """Obtiene los intentos del Juego"""
        return self.__intentos
    
    def get_jugadores(self) -> list:
        """Obtiene los jugadores del Juego"""
        return self.__jugadores

    def get_rangos(self):
        """Obtiene los rangos del Juego"""
        return self.__rango1, self.__rango2
