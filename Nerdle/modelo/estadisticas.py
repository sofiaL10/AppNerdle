from matplotlib import pyplot as plt


class Estadisticas:
    def __init__(self):
        self.datos = ["partidas_perdidas", "partidas_ganadas",
                      "ganadas_en_un_intento",
                      "ganadas_en_dos_intentos",
                      "ganadas_en_tres_intentos",
                      "ganadas_en_cuatro_intentos",
                      "ganadas_en_mas_de_cinco_intentos"]
        self.numeros = [0] * len(self.datos)

    def actualizar_estadisticas(self, resultado_partida):
        # Actualiza las estadísticas según el resultado de la partida
        if resultado_partida in self.datos:
            index = self.datos.index(resultado_partida)
            self.numeros[index] += 1

    def crear_grafica(self):
        fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
        ax.bar(self.datos, self.numeros)
        ax.tick_params(axis='x', labelsize=6)
        ax.tick_params(axis='y', labelsize=8)

        return fig
