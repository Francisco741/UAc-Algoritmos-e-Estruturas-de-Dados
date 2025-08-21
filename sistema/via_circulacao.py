from math import floor


class ViaCirculacao:
    """Via de uma rede de circulação de um determinado concelho"""

    def __init__(
        self,
        inicio: str,
        fim: str,
        distancia: float,
        velocidade_minima: float,
        velocidade_maxima: float,
    ):
        """
        Define o estado inicial de self

        :param inicio: ponto do início da via
        :type inicio: str
        :param fim: ponto do fim da via
        :type fim: str
        :param distancia: distância da via
        :type distancia: float
        :param velocidade_minima: velocidade mínima da via
        :type velocidade_minima: float
        :param velocidade_maxima: velocidade máxima da via
        :type velocidade_maxima: float
        """
        self._inicio: str = inicio
        self._fim: str = fim
        self._distancia: float = distancia
        self._velocidade_minima: float = velocidade_minima
        self._velocidade_maxima: float = velocidade_maxima
        self._tempo_a_pe: float = distancia / 5
        self._tempo_carro: float = distancia / (
            (velocidade_maxima + velocidade_minima) / 2
        )

    def __str__(self) -> str:
        """
        Gerar uma string com todos os atributos da via

        :return: string com os atributos da via
        :rtype: str
        """
        horas_a_pe: int = floor(self._tempo_a_pe)
        minutos_a_pe: int = round((self._tempo_a_pe - horas_a_pe) * 60)
        horas_carro: int = floor(self._tempo_carro)
        minutos_carro: int = round((self._tempo_carro - horas_carro) * 60)
        return (
            f"Ponto do início da via: {self._inicio}\n"
            f"Ponto do fim da via: {self._fim}\n"
            f"Distância (km): {round(self._distancia, 3)}\n"
            f"Velocidade mínima (km/h): {round(self._velocidade_minima, 3)}\n"
            f"Velocidade máxima (km/h): {round(self._velocidade_maxima, 3)}\n"
            f"Tempo estimado para percorrer a pé: "
            f"{horas_a_pe}h {minutos_a_pe}m\n"
            f"Tempo estimado para percorrer de carro: "
            f"{horas_carro}h {minutos_carro}m\n"
        )
