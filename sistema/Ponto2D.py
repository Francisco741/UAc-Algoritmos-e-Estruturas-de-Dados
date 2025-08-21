from typing import Union


class Ponto2D:
    """Classe que representa um Ponto 2D, com duas cooordenadas"""

    def __init__(self, x: Union[int, float], y: Union[int, float]):
        """
        Define o estado inicial de self

        :param x: valor para a abcissa
        :type x: Union[int, float]
        :param y: valor para a ordenada
        :type y: Union[int, float]
        """
        self._x: Union[int, float] = x
        self._y: Union[int, float] = y

    def get_x(self) -> Union[int, float]:
        """
        Obter o valor da abcissa do ponto

        :return: valor da abcissa do ponto
        :rtype: Union[int, float]
        """
        return self._x

    def set_x(self, valor: Union[int, float]) -> None:
        """
        Atribui um valor à abcissa do ponto

        :param valor: valor a atribuir
        :type valor: Union[int, float]
        """
        self._x = valor

    def get_y(self) -> Union[int, float]:
        """
        Obter o valor da ordenada do ponto

        :return: valor da ordenada do ponto
        :rtype: Union[int, float]
        """
        return self._y

    def set_y(self, valor: Union[int, float]) -> None:
        """
        Atribui um valor à ordenada do ponto

        :param valor: valor a atribuir
        :type valor: Union[int, float]
        """
        self._y = valor

    def __str__(self) -> str:
        """
        Gerar uma string com o valar da abcissa e da ordenada do ponto

        :return: string com o estado do ponto
        :rtype: str
        """
        return "(" + str(self._x) + ", " + str(self._y) + ")"
