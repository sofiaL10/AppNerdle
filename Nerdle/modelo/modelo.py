from dataclasses import dataclass
from Nerdle.modelo.claseEcuacion import Ecuacion
from Nerdle.modelo.retroalimentacion import Retroalimentacion
from Nerdle.modelo.estadisticas import Estadisticas


@dataclass
class Jugador:
    nombre_jugador: str = ""
    contraseña: str = ""


class Nerdle(Ecuacion):
    def __init__(self):
        super().__init__()
        self.retroalimentacion = None
        self.nombre_jugador: str = ""
        self.contraseña: str = ""
        self.intentos: int = 5
        self.estadisticas: Estadisticas = Estadisticas()

    def registrar_nombre_jugador(self, nombre_jugador: str) -> str:
        self.nombre_jugador = nombre_jugador
        return self.nombre_jugador

    def registrar_correo_jugador(self, contraseña: str) -> str:
        self.contraseñar = contraseña
        return self.contraseña

    """ Se borra el metodo juego nuevo pues no necesitamos mostrar la tabla por consola"""

    """
    El metodo iniciar nuevo juego es el que debe ser llamado cuando el jugador de click en jugar, este genera y retorna
    la ecuacion, y a su vez la imprime en consola
    """

    def iniciar_nuevo_juego(self):
        ecuacion: list = super().generar_ecuacion()
        self.retroalimentacion: Retroalimentacion = Retroalimentacion(ecuacion)
        titulo = "COMIENZA A JUGAR: "

    """El metodo retroalimentar retorna una lista con los colores en hexadecimal segun lo que puso el usuario
    asi solo se tiene que tomar el color y cambiar cada casilla segun la posicion de la lista.
    """

    def retroalimentar(self, ingreso: list):

        lista_de_colores = self.retroalimentacion.verificar_posiciones(ingreso)
        return lista_de_colores

    """ Anunciar y perder, simplemente retornan un mensaje, y si pierde hay que retornarle al usuario 
    la ecuacion real"""

    def anunciar_ganador(self):
        self.estadisticas.numeros[1] += 1
        print("gana")

        if self.intentos >= 5:
            self.estadisticas.numeros[2] += 1
        elif self.intentos >= 4:
            self.estadisticas.numeros[3] += 1
        elif self.intentos >= 3:
            self.estadisticas.numeros[4] += 1
        elif self.intentos >= 2:
            self.estadisticas.numeros[5] += 1
        else:
            self.estadisticas.numeros[6] += 1

    def anunciar_perdedor(self):
        print("pierde")
        self.estadisticas.numeros[0] += 1


    """ Estado del juego se encarga de recibir lo que el usuario ingreso y determinar si, en base a la 
    retroalimentacion, gana, pierde, o disminuyen sus intentos disponibles.

    Este metodo debe llamarse cada que se de click en ingresar y se le debe pasar como argumento una lista que contenga
    los datos que el usuario ingreso."""

    def estado_del_juego(self, ingreso):
        lista = self.retroalimentar(ingreso)

        return lista

