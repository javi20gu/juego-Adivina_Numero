from colorama import Fore, init


class Color:

    __AZUL = Fore.BLUE
    __AZUL_CLARITO = Fore.LIGHTBLUE_EX
    __ROJO = Fore.RED
    __ROJO_CLARITO = Fore.LIGHTRED_EX
    __VERDE = Fore.GREEN
    __VERDE_CLARITO = Fore.LIGHTGREEN_EX
    __AMARILLO = Fore.YELLOW
    __AMARILLO_CLARITO = Fore.LIGHTYELLOW_EX
    __MAGENTA = Fore.MAGENTA
    __MAGENTA_CLARITO = Fore.LIGHTMAGENTA_EX
    __BLANCO = Fore.WHITE
    __BLANCO_CLARITO = Fore.LIGHTWHITE_EX
    __NEGRO = Fore.BLACK
    __NEGRO_CLARITO = Fore.LIGHTBLACK_EX
    __CYAN = Fore.CYAN
    __CYAN_CLARITO = Fore.LIGHTCYAN_EX

    def utilizarAzul(self):
        print(self.__AZUL + "", end='')

    def utilizarAzulClarito(self):
        print(self.__AZUL_CLARITO + "", end='')

    def utilizarRojo(self):
        print(self.__ROJO + "", end='')

    def utilizarRojoClarito(self):
        print(self.__ROJO_CLARITO + "", end='')

    def utilizarCyan(self):
        print(self.__CYAN + "", end='')

    def utilizarCyanClarito(self):
        print(self.__CYAN_CLARITO + "", end='')

    def utilizarVerde(self):
        print(self.__VERDE + "", end='')

    def utilizarVerdeClarito(self):
        print(self.__VERDE_CLARITO + "", end='')

    def utilizarAmarillo(self):
        print(self.__AMARILLO + "", end='')

    def utilizarAmarilloClarito(self):
        print(self.__AMARILLO_CLARITO + "", end='')

    def utilizarBlanco(self):
        print(self.__BLANCO + "", end='')

    def utilizarBlancoClarito(self):
        print(self.__BLANCO_CLARITO + "", end='')

    def utilizarNegro(self):
        print(self.__NEGRO + "", end='')

    def utilizarNegroClarito(self):
        print(self.__NEGRO_CLARITO + "", end='')

    def utilizarMagenta(self):
        print(self.__MAGENTA + "", end='')

    def utilizarMagentaClarito(self):
        print(self.__MAGENTA + "", end='')


init()
color = Color()
