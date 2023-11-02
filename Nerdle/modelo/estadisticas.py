from matplotlib import pyplot as plt


class Estadisticas:
    datos = ["partidas_perdidas", "partidas_ganadas",
             "ganadas_en_un_intento",
             "ganadas_en_dos_intentos",
             "ganadas_en_tres_intentos",
             "ganadas_en_cuatro_intentos",
             "ganadas_en_mas_de_cinco_intentos"]
    numeros: list = [0, 0, 0, 0, 0, 0, 0]

    def actualizar_estadisticas(self, resultado_partida):
        # Actualiza las estadísticas según el resultado de la partida
        if resultado_partida in Estadisticas.datos:
            index = Estadisticas.datos.index(resultado_partida)
            Estadisticas.numeros[index] += 1

    @staticmethod
    def crear_grafica():
        fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
        ax.bar(Estadisticas.datos, Estadisticas.numeros)
        ax.tick_params(axis='x', labelsize=6)
        ax.tick_params(axis='y', labelsize=8)

        return fig
