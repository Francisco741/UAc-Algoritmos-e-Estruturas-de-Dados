from typing import List
from sistema.Ponto2D import Ponto2D


class PontoInteresse:
    """Ponto de interesse turístico de um determinado concelho"""

    def __init__(
        self,
        designacao: str,
        morada: str,
        coordenadas: Ponto2D,
        categoria: str,
        acessibilidade: str,
        atividades: str,
    ):
        """
        Define o estado inicial de self

        :param designacao: designação do ponto de interesse
        :type designacao: str
        :param morada: morada do ponto de interesse
        :type morada: str
        :param coordenadas: coordenadas do ponto de interesse
        :type coordenadas: Ponto2D
        :param categoria: categoria do ponto de interesse
        :type categoria: str
        :param acessibilidade: informação sobre as acessibilidades
        do ponto de interesse
        :type acessibilidade: str
        :param atividades: informação sobre as atividades
        do ponto de interesse
        :type atividades: str
        """
        self._designacao: str = designacao
        self._morada: str = morada
        self._coordenadas: Ponto2D = coordenadas
        self._categoria: str = categoria
        self._acessibilidade: str = acessibilidade
        self._atividades: str = atividades
        self._avaliacao: List[int] = []
        self._visitas: int = 0

    def __str__(self) -> str:
        """
        Gerar uma string com todos os atributos do ponto de interesse

        :return: string com os atributos do ponto de interesse
        :rtype: str
        """
        if len(self._avaliacao) > 0:
            media: float = sum(self._avaliacao) / len(self._avaliacao)
        else:
            media: float = 0.00
        return (
            f"Designação: {self._designacao}\n"
            f"Morada: {self._morada}\n"
            f"Coordenadas: {self._coordenadas}\n"
            f"Categoria: {self._categoria}\n"
            f"Acessibilidade: {self._acessibilidade}\n"
            f"Atividades: {self._atividades}\n"
            f"Classificação média: {str(round(media, 2))}\n"
            f"Visitas: {self._visitas}\n"
        )
