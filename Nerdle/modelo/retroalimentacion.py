class Retroalimentacion:

    def __init__(self, ecuacion: list):

        self.ecuacion_actual: list = ecuacion

    def verificar_posiciones(self, ingreso: list) -> list:

        lista_retorno: list = ["" for i in ingreso]
        for i in range(len(self.ecuacion_actual)):
            if ingreso[i] not in self.ecuacion_actual:
                lista_retorno[i] = "#808080"
            elif ingreso[i] in self.ecuacion_actual:
                if self.ecuacion_actual[i] != ingreso[i]:
                    lista_retorno[i] = "#E8F65E"
                elif self.ecuacion_actual[i] == ingreso[i]:
                    lista_retorno[i] = "#7ED957"

        return lista_retorno
