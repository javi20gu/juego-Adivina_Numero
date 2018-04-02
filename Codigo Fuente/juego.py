from random import randint
from sys import exit
from ClassJugadores import Jugadores
from ClassJuego import Juego
from Clases_Bases import color


def play():

    """Verifica los Numeros de Jugadores"""
    color.utilizarAzul()
    numero_jugadores = int(input("Introduce el Numero de Jugadores: "))
    numero_jugador = 1
    print()

    while numero_jugador <= numero_jugadores:

        """Agrega a los jugadores de la clase Jugadores un nombre y los asigna a la clase Juego"""

        jugador = Jugadores()
        color.utilizarAzulClarito()
        a = input("Introduce el Nombre del Jugador {}: ".format(numero_jugador))
        jugador.set_jugador_nombre(a)
        juego.set_jugadores(jugador)
        numero_jugador += 1

    for jugador_1 in juego.get_jugadores():

        """Va Iterando sobre todos los jugadores disponibles de uno en uno"""
        print("\n")
        color.utilizarVerde()
        print("Empieza: {}".format(jugador_1.get_jugado_nombre()))
        num1, num2 = juego.get_rangos()
        print("Rango de {} al {}".format(num1, num2))
        intentos = jugador_1.get_jugador_intentos()
        numero_oculto = randint(num1, num2)
        puntos = jugador_1.get_jugador_puntuacion_total()

        """Empieza la partida con 4 Intentos hasta que se quede en 0"""

        while intentos >= 0:
            try:
                color.utilizarVerdeClarito()
                numero = int(input("Introduce un Número: "))
                color.utilizarAmarillo()
                print("Intetos Restantes: {}".format(intentos-1))
                if numero_oculto < numero and intentos != 1:
                    color.utilizarRojoClarito()
                    print("\nEs Demasiado Grande\n")
                    intentos -= 1
                    jugador_1.set_jugador_intentos(intentos)

                elif numero_oculto > numero and intentos != 1:
                    color.utilizarRojoClarito()
                    print("\nEs Demasiado Pequeño\n")
                    intentos -= 1
                    jugador_1.set_jugador_intentos(intentos)

                elif numero == numero_oculto:
                    color.utilizarAzulClarito()
                    print("\nHas Ganado en el {0} intento".format(intentos))
                    puntos += 1
                    jugador_1.set_jugador_puntuacion_total(puntos)
                    input("Pulse enter para continuar...")
                    break

                elif numero != numero_oculto and intentos == 1:
                    color.utilizarVerdeClarito()
                    print("\nEl número era {} :(\n".format(numero_oculto))
                    color.utilizarRojo()
                    print(format("GAME OVER", "-^75"))
                    input("Pulse enter para continuar...")
                    break

            except (ValueError, NameError):
                print("\nError: Tiene que ser un número ...")


def otra_partida():

    """Crea Otra Partida Con los Datos ya Almacenados"""

    for jugador_1 in juego.get_jugadores():

        """Va Iterando sobre todos los jugadores disponibles de uno en uno"""
        color.utilizarVerde()
        print("\nEmpieza: {}".format(jugador_1.get_jugado_nombre()))
        num1, num2 = juego.get_rangos()
        print("Rango de {} al {}".format(num1, num2))
        jugador_1.set_jugador_intentos(4)
        intentos = jugador_1.get_jugador_intentos()
        numero_oculto = randint(num1, num2)
        puntos = jugador_1.get_jugador_puntuacion_total()

        while intentos >= 0:

            """Empieza la partida con 4 Intentos hasta que se quede en 0"""

            try:
                color.utilizarVerde()
                numero = int(input("\nIntroduce un Número: "))
                color.utilizarAmarillo()
                print("Intetos Restantes: {}".format(intentos - 1))
                if numero_oculto < numero and intentos != 1:
                    color.utilizarRojoClarito()
                    print("\nEs Demasiado Grande\n")
                    intentos -= 1
                    jugador_1.set_jugador_intentos(intentos)

                elif numero_oculto > numero and intentos != 1:
                    color.utilizarRojoClarito()
                    print("\nEs Demasiado Pequeño\n")
                    intentos -= 1
                    jugador_1.set_jugador_intentos(intentos)

                elif numero == numero_oculto:
                    color.utilizarAzul()
                    print("\nHas Ganado en el {0} intento".format(intentos))
                    puntos += 1
                    jugador_1.set_jugador_puntuacion_total(puntos)
                    input("Pulse enter para continuar...")
                    break

                elif numero != numero_oculto and intentos == 1:
                    color.utilizarVerdeClarito()
                    print("\nEl número era {} :(\n".format(numero_oculto))
                    color.utilizarRojo()
                    print(format("GAME OVER", "-^75"))
                    input("Pulse enter para continuar...")
                    break

            except (ValueError, NameError):
                print("\nError: Tiene que ser un número ...")


if __name__ == '__main__':
    juego = Juego()
    play()
    juego.puntuacion_de_la_partida()

    while True:
        color.utilizarAmarillo()
        otra_vez = input("\nSeguir Jugando[Y/N]: ")
        if otra_vez.lower() == "y":
            otra_partida()
            juego.puntuacion_de_la_partida()
        else:
            exit()
else:
    print("No se puede importar")
