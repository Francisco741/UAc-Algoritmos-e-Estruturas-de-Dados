import math
from matplotlib import pyplot as plt
from sistema.LinkedList import LinkedList
from sistema.ponto_interesse import PontoInteresse
from sistema.via_circulacao import ViaCirculacao
from sistema.grafo import Graph
from typing import TypeVar, List, Tuple, Union


T = TypeVar("T")


class SistemaTuristico:
    """
    Classe que contém todos os dados dos
    pontos de interesse e da rede de circulação
    """

    def __init__(self):
        """Define o estado inicial de self"""
        self._pontos: LinkedList[PontoInteresse] = LinkedList()
        self._categorias: Tuple[str, str, str] = (
            "natureza",
            "cultura",
            "gastronomia",
        )
        self._rede: List[ViaCirculacao] = []
        self._grafo: Graph = Graph()

    def adicionar_ponto(self, ponto_interesse: PontoInteresse) -> None:
        """
        Adiciona um ponto de interesse ao sistema

        :param ponto_interesse: ponto de interesse a ser adicionado
        :type ponto_interesse: PontoInteresse
        """
        self._pontos.add(ponto_interesse)

    def alterar_ponto(
        self, ponto_interesse: PontoInteresse, categoria: str, acessibilidade: str
    ) -> None:
        """
        Altera a categoria a a acessibilidade de um
        ponto de interesse

        :param ponto_interesse: ponto de interesse a ser alterado
        :type ponto_interesse: PontoInteresse
        :param categoria: nova categoria
        :type categoria: str
        :param acessibilidade: nova acessibilidade
        :type acessibilidade: str
        """
        ponto_interesse._categoria = categoria
        ponto_interesse._acessibilidade = acessibilidade

    def bubble_sort(self, lista: List[Tuple[str, T]]) -> List[Tuple[str, T]]:
        """
        Algorítmo bubble sort para ordenar por ordem alfabética

        :param lista: lista desordenada
        :type lista: List[Tuple[str, T]]
        :return: lista ordenada
        :rtype: List[Tuple[str, T]]
        """
        n: int = len(lista)
        for i in range(n):
            trocas: bool = False
            for j in range(0, n - i - 1):
                if lista[j][0].upper() > lista[j + 1][0].upper():
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
                    trocas: bool = True
            if not trocas:
                break
        return lista

    def pesquisar_pontos(self, categoria: str) -> str:
        """
        Pesquisa todos os pontos de interesse de uma determinada
        categoria e ordena-os por ordem alfabética

        :param categoria: categoria a ser pesquisada
        :type categoria: str
        :return: pontos de interesse pertencente à categoria ordenados
        :rtype: str
        """
        resultados: List[Tuple[str, PontoInteresse]] = []
        resultados_ordenados: str = ""
        for ponto_interesse in self._pontos:
            if ponto_interesse._categoria == categoria:
                resultados.append((ponto_interesse._designacao, ponto_interesse))
        resultados = self.bubble_sort(resultados)
        for i in resultados:
            resultados_ordenados += f"{str(i[1])}\n"
        return resultados_ordenados

    def avaliar_ponto(self, avaliacao: int, ponto_interesse: PontoInteresse) -> None:
        """
        Adiciona uma avaliação ao ponto de interesse
        e incrementa o seu contador de visitas em uma unidade

        :param avaliacao: avaliação dada ao ponto de interesse
        :type avaliacao: int
        :param ponto_interesse: ponto de interesse a ser avaliado
        :type ponto_interesse: PontoInteresse
        """
        ponto_interesse._avaliacao.append(avaliacao)
        ponto_interesse._visitas += 1

    def consultar_estatisticas(self) -> str:
        """
        Consulta todos os pontos de interesse,
        indicando a sua designação, categoria,
        número de visitas e classificação média
        e o gráfico com a distribuição dos pontos de interesse
        pelos valores da escala numérica

        :return: atributos dos pontos de interesse
        :rtype: str
        """
        consulta: str = ""
        total_avaliacoes: List[int] = []
        for ponto_interesse in self._pontos:
            if len(ponto_interesse._avaliacao) > 0:
                media: float = sum(ponto_interesse._avaliacao) / len(
                    ponto_interesse._avaliacao
                )
                for a in ponto_interesse._avaliacao:
                    total_avaliacoes.append(a)
            else:
                media: float = 0.00
            consulta += (
                f"{ponto_interesse._designacao}:\n"
                "Categoria: "
                f"{ponto_interesse._categoria}\n"
                "Número de visitantes: "
                f"{str(ponto_interesse._visitas)}\n"
                "Classificação média: "
                f"{str(round(media, 2))}\n\n"
            )
        contagem_avaliacoes = [
            total_avaliacoes.count(1),
            total_avaliacoes.count(2),
            total_avaliacoes.count(3),
            total_avaliacoes.count(4),
        ]
        escala = [
            "1\nNada Satisfeito",
            "2\nPouco Satisfeito",
            "3\nSatisfeito",
            "4\nMuito Satisfeito",
        ]
        plt.figure(figsize=(8, 6))
        plt.bar(escala, contagem_avaliacoes)
        plt.title("Distribuição dos Pontos de Interesse pela Escala Numérica")
        plt.ylabel("Número de Avaliações")
        plt.yticks(range(0, max(contagem_avaliacoes) + 1))
        plt.show()
        return consulta

    def distancia_terra(
        self, lat1: float, lon1: float, lat2: float, lon2: float
    ) -> float:
        """
        Calcula a distância entre dois pontos no planeta Terra

        :param lat1: latitude do ponto 1
        :type lat1: float
        :param lon1: longitude do ponto 1
        :type lon1: float
        :param lat2: latitude do ponto 2
        :type lat2: float
        :param lon2: longitude do ponto 2
        :type lon2: float
        :return: distância entre os dois pontos
        :rtype: float
        """
        R: int = 6371000
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
        dlat: float = lat2 - lat1
        dlon: float = lon2 - lon1
        a: float = (
            math.sin(dlat / 2) ** 2
            + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        )
        c: float = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        d: float = R * c
        return d

    def quick_sort(
        self, lista: List[Tuple[Union[int, float], T]]
    ) -> List[Tuple[Union[int, float], T]]:
        """
        Algorítmo quick sort para ordenar números por ordem decrescente

        :param lista: lista desordenada
        :type lista: List[Tuple[Union[int, float], T]]
        :return: lista ordenada
        :rtype: List[Tuple[Union[int, float], T]]
        """
        if len(lista) > 1:
            pivot: int = len(lista) // 2
            lista_maior: List[Tuple[Union[int, float], T]] = []
            lista_menor: List[Tuple[Union[int, float], T]] = []
            for i in range(len(lista)):
                if lista[i][0] < lista[pivot][0]:
                    lista_menor.append(lista[i])
                elif i != pivot:
                    lista_maior.append(lista[i])
            return (
                self.quick_sort(lista_maior)
                + [lista[pivot]]
                + self.quick_sort(lista_menor)
            )
        return lista

    def sugestoes_visitas(self, lat: float, lon: float) -> str:
        """
        Mostra os pontos de interesse próximos das coordenadas inseridas,
        organizando-os por ordem decrescente do número de visitas

        :param lat: latitude da coordenada inserida
        :type lat: float
        :param lon: longitude da coordenada inserida
        :type lon: float
        :return: pontos de interesse próximos das coordenadas
        :rtype: str
        """
        pontos_proximos: List[Tuple[Union[int, float], PontoInteresse]] = []
        pontos_ordenados: str = ""
        for ponto_interesse in self._pontos:
            proximidade: float = self.distancia_terra(
                float(lat),
                float(lon),
                float(ponto_interesse._coordenadas._x),
                float(ponto_interesse._coordenadas._y),
            )
            if proximidade <= 5000:
                pontos_proximos.append((ponto_interesse._visitas, ponto_interesse))
        pontos_proximos = self.quick_sort(pontos_proximos)
        for i in pontos_proximos:
            pontos_ordenados += f"{str(i[1])}\n"
        return pontos_ordenados

    def consultar_vertices(self) -> str:
        """
        Consulta todos os pontos pertencentes à rede de circulação

        :return: pontos na rede de circulação
        :rtype: str
        """
        vertices: str = ""
        for v in self._grafo._vertices:
            vertices += f"{v}\n"
        return vertices

    def acrescentar_vertice(self, vertice: str) -> None:
        """
        Adiciona um ponto à rede de circulação

        :param vertice: ponto a ser adicionado
        :type vertice: str
        """
        self._grafo.add_vertex(vertice)

    def remover_vertice(self, vertice: str) -> None:
        """
        Remove um ponto da rede de circulação

        :param vertice: ponto a ser removido
        :type vertice: str
        """
        for a in self._rede:
            if vertice == a._inicio or vertice == a._fim:
                self._rede.remove(a)
        self._grafo.remove_vertex(vertice)

    def consultar_arestas(self) -> str:
        """
        Consulta todas as vias pertencentes à rede de circulação

        :return: vias na rede de circulação
        :rtype: str
        """
        arestas: str = ""
        for a in self._rede:
            arestas += f"{a}\n"
        return arestas

    def acrescentar_aresta(self, aresta: ViaCirculacao) -> None:
        """
        Acrescenta uma via à rede de circulação

        :param vertice: via a ser adicionada
        :type vertice: str
        """
        self._rede.append(aresta)
        self._grafo.add_edges(aresta._inicio, aresta._fim, aresta._distancia)

    def remover_aresta(self, aresta: ViaCirculacao) -> None:
        """
        Remove uma via da rede de circulação

        :param aresta: via a ser removida
        :type aresta: ViaCirculacao
        """
        self._rede.remove(aresta)
        self._grafo.remove_edge(aresta._inicio, aresta._fim)

    def grau_externo(self) -> str:
        """
        Pontos da rede mais críticos, considerando
        a métrica de centralidade grau externo,
        ordenados por ordem decrescente

        :return: pontos ordenados por ordem decrescente do grau externo
        :rtype: str
        """
        pontos_criticos: List[Tuple[Union[int, float], str]] = []
        pontos_ordenados: str = ""
        for v in self._grafo._vertices:
            pontos_criticos.append((len(self._grafo.adjacentes_externo(v)), v))
        pontos_criticos = self.quick_sort(pontos_criticos)
        for p in pontos_criticos:
            pontos_ordenados += (
                f"Ponto da rede: {str(p[1])}\n" f"Grau externo: {str(p[0])}\n\n"
            )
        return pontos_ordenados

    def grau_interno(self) -> str:
        """
        Pontos da rede mais críticos, considerando
        a métrica de centralidade grau interno,
        ordenados por ordem decrescente

        :return: pontos ordenados por ordem decrescente do grau interno
        :rtype: str
        """
        pontos_criticos: List[Tuple[Union[int, float], str]] = []
        pontos_ordenados: str = ""
        for v in self._grafo._vertices:
            pontos_criticos.append((len(self._grafo.adjacentes_interno(v)), v))
        pontos_criticos = self.quick_sort(pontos_criticos)
        for p in pontos_criticos:
            pontos_ordenados += (
                f"Ponto da rede: {str(p[1])}\n" f"Grau interno: {str(p[0])}\n\n"
            )
        return pontos_ordenados

    def proximidade(self) -> str:
        return ""

    def mapa(self) -> None:
        """
        Mostra um mapa com os pontos de interesse
        usando as coordenadas de cada um
        """
        coordenadas: List[Tuple[float, float, str]] = []
        for ponto_interesse in self._pontos:
            coordenadas.append(
                (
                    float(ponto_interesse._coordenadas._x),
                    float(ponto_interesse._coordenadas._y),
                    str(ponto_interesse._designacao),
                )
            )
        plt.figure(figsize=(8, 6))
        for latitude, longitude, designacao in coordenadas:
            plt.scatter(latitude, longitude, label=designacao)
        plt.title("Mapa dos Pontos de Interesse")
        plt.xlabel("Latitude")
        plt.ylabel("Longitude")
        plt.grid(True)
        plt.legend()
        plt.show()
