

class SuperJugadores:

    """Clase para un Jugador"""

    __nombre_jugador = ''
    __jugador_intentos = 0
    __jugador_puntuacion_total = 0
    __id_de_jugador = 0

    def __str__(self):
        return 'Jugador ({}) con el id {}'.format(self.__nombre_jugador, self.__id_jugador_1)

    def __init__(self):
        SuperJugadores.__id_de_jugador += 1
        self.__id_jugador_1 = self.__id_de_jugador
        self.__id = SuperJugadores.__id_de_jugador

    def set_jugador_nombre(self, nombre: str):
        """Cambia el nombre al jugador"""
        self.__nombre_jugador = nombre
    
    def set_jugador_intentos(self, intentos: int):
        """Cambia los intentos actuales"""
        self.__jugador_intentos = intentos
    
    def set_jugador_puntuacion_total(self, puntuacion: int):
        """Cambia la Puntución Total del Jugador"""
        self.__jugador_puntuacion_total = puntuacion

    def get_jugado_nombre(self) -> str:
        """Obtiene el nombre del jugador"""
        return self.__nombre_jugador
    
    def get_jugador_intentos(self) -> int:
        """Obtiene los intentos actuales"""
        return self.__jugador_intentos
    
    def get_jugador_puntuacion_total(self) -> int:
        """Obtiene la puntuación total del jugador"""
        return self.__jugador_puntuacion_total
    
    def get__id_de_jugador(self) -> int:
        """Obtiene el id del jugador"""
        return self.__id_jugador_1
