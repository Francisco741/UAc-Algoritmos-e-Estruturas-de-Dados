import networkx as nx
from typing import List, Tuple
from matplotlib.pyplot import show, figure
from sistema.QueueBasedList import QueueBasedList
from sistema.StackBasedList import StackListBased


class Graph:
    """TDA Grafo"""

    def __init__(self):
        """Define o estado inicial de self"""
        self._vertices: dict[str, dict[str, float]] = {}

    def is_empty(self) -> bool:
        """
        Verifica se o grafo não tem vértices

        :return: True se não tiver vértices e False se tiver
        :rtype: bool
        """
        return len(self._vertices) == 0

    def __len__(self) -> int:
        """
        Verifica o número de vértices pertencentes ao grafo

        :return: número de vértices
        :rtype: int
        """
        return len(self._vertices)

    def __str__(self) -> str:
        """
        Gera uma string com todos os vértices e arestas do grafo

        :return: vértices e arestas do grafo
        :rtype: str
        """
        s: str = ""
        for v in sorted(self._vertices):
            s += "\nVértice: " + str(v)
            s += "\nArestas: "
            for adj in self._vertices[v]:
                s += str(adj) + " / "
            s += "\n"
        return s

    def clear(self) -> None:
        """Elimina todos os dados do grafo"""
        self._vertices: dict[str, dict[str, float]] = {}

    def adjacentes_externo(self, label: str) -> set[str]:
        """
        Recebe um vértice do grafo e retorna o conjunto de todos
        os vértices em que este aponta

        :param label: vertice do grafo
        :type label: str
        :return: conjunto de vértices adjacentes externamente
        :rtype: set[str]
        """
        if label in self._vertices:
            return set(self._vertices[label])
        return set()

    def adjacentes_interno(self, label: str) -> set[str]:
        """
        Recebe um vértice do grafo e retorna o conjunto de todos
        os vértices que apontam para este

        :param label: vertice do grafo
        :type label: str
        :return: conjunto de vértices adjacentes internamente
        :rtype: set[str]
        """
        adjacentes: set[str] = set()
        if label in self._vertices:
            for v, i in self._vertices.items():
                if label in i:
                    adjacentes.add(v)
        return adjacentes

    def add_vertex(self, label: str) -> None:
        """
        Adiciona um vértice ao grafo

        :param label: vértice a ser adicionado
        :type label: str
        """
        if label not in self._vertices:
            self._vertices[label] = {}

    def add_edges(self, from_label: str, to_label: str, weight: float) -> None:
        """
        Adiciona uma aresta ao grafo

        :param from_label: vertice do inicio da aresta
        :type from_label: str
        :param to_label: vertice do fim da aresta
        :type to_label: str
        :param weight: peso da aresta
        :type weight: float
        """
        if (
            to_label in self._vertices
            and from_label in self._vertices
            and to_label not in self._vertices[from_label]
            and from_label not in self._vertices[to_label]
        ):
            self._vertices[from_label][to_label] = weight

    def remove_vertex(self, vertex: str) -> None:
        """
        Remove um vértice e todas as arestas conetadas a este do grafo

        :param vertex: vértice a ser removido
        :type vertex: str
        """
        if vertex in self._vertices:
            self._vertices.pop(vertex)
            for v in self._vertices.values():
                if vertex in v:
                    v.pop(vertex)

    def remove_edge(self, from_label: str, to_label: str) -> None:
        """
        Remove uma aresta do grafo

        :param from_label: vertice do inicio da aresta
        :type from_label: str
        :param to_label: vertice do fim da aresta
        :type to_label: str
        """
        if from_label in self._vertices and to_label in self._vertices:
            if to_label in self._vertices[from_label]:
                self._vertices[from_label].pop(to_label)

    def size_edges(self) -> int:
        """
        Conta o número de arestas existentes no grafo

        :return: número de arestas no grafo
        :rtype: int
        """
        count: int = 0
        for v in self._vertices:
            count += len(self._vertices[v])
        return count

    def get_vertices(self) -> set[str]:
        """
        Obtém um conjunto de todos os vértices do grafo

        :return: conjunto dos vértices do grafo
        :rtype: set[str]
        """
        return set(self._vertices)

    def get_edges(self) -> set[tuple[str, str]]:
        """
        Obtém um conjunto de todas as arestas do grafo

        :return: conjunto das arestas do grafo
        :rtype: set[tuple[str, str]]
        """
        edges: set[tuple[str, str]] = set()
        for v in self._vertices:
            for adj in self.adjacentes_externo(v):
                if (v, adj) not in edges and (adj, v) not in edges:
                    edges.add((v, adj))
        return edges

    def get_weight(self, from_label: str, to_label: str) -> float:
        """
        Obtém o peso de uma aresta

        :param from_label: vertice do inicio da aresta
        :type from_label: str
        :param to_label: vertice do fim da aresta
        :type to_label: str
        :return: peso da aresta
        :rtype: float
        """
        if from_label in self._vertices and to_label in self._vertices[from_label]:
            return self._vertices[from_label][to_label]
        return -1

    def draw_graph(self) -> None:
        """Visualiza o grafo em modo gráfico"""
        figure(figsize=(8, 6))
        g: nx.DiGraph = nx.DiGraph()
        nodes: set[str] = self.get_vertices()
        g.add_nodes_from(nodes)
        edges: set[tuple[str, str]] = self.get_edges()
        g.add_edges_from(edges)
        pos = nx.shell_layout(g)
        weights: dict[tuple[str, str], float] = {}
        for from_label, to_label in edges:
            weights[(from_label, to_label)] = self.get_weight(from_label, to_label)
        nx.draw_networkx_nodes(g, pos)
        nx.draw_networkx_edges(g, pos, arrows=True)
        nx.draw_networkx_labels(g, pos)
        nx.draw_networkx_edge_labels(g, pos, edge_labels=weights, label_pos=0.7)
        show()

    def total_caminhos(self, inicio: str, fim: str) -> List[List[str]]:
        """
        Realiza uma travessia em largura e retorna
        uma lista de todos os caminhos possíveis

        :param inicio: vértice inicial
        :type inicio: str
        :param fim: vértice final
        :type fim: str
        :return: lista de todos os caminhos possíveis
        :rtype: List[List[str]]
        """
        if inicio == fim:
            return [[inicio]]
        total: List[List[str]] = []
        por_visitar: QueueBasedList = QueueBasedList()
        por_visitar.add([inicio])
        while not por_visitar.is_empty():
            caminho: List[str] = por_visitar.pop()
            ponto_fim: str = caminho[-1]
            if ponto_fim == fim:
                total.append(caminho)
            for adjacente in self._vertices[ponto_fim]:
                if adjacente not in caminho:
                    novo_caminho: List[str] = list(caminho)
                    novo_caminho.append(adjacente)
                    por_visitar.add(novo_caminho)
        return total

    def distancia_caminhos(
        self, caminhos: List[List[str]]
    ) -> List[Tuple[float, List[str]]]:
        """
        Calcula o peso total de cada caminho

        :param caminhos: caminhos a serem calculados
        :type caminhos: List[List[str]]
        :return: lista dos caminhos com o seu peso total
        :rtype: List[Tuple[float, List[str]]]
        """
        distancia_dos_caminhos: List[Tuple[float, List[str]]] = []
        for caminho in caminhos:
            distancia_total: float = 0.0
            for i in range(len(caminho) - 1):
                distancia_total += self.get_weight(caminho[i], caminho[i + 1])
            distancia_dos_caminhos.append((distancia_total, caminho))
        return distancia_dos_caminhos

    def draw_tree(self) -> None:
        """Visualiza a árvore em modo gráfico"""
        figure(figsize=(8, 6))
        g: nx.DiGraph = nx.DiGraph()
        nodes: set[str] = self.get_vertices()
        g.add_nodes_from(nodes)
        edges: set[tuple[str, str]] = self.get_edges()
        g.add_edges_from(edges)
        pos = nx.spring_layout(g)
        weights: dict[tuple[str, str], float] = {}
        for from_label, to_label in edges:
            weights[(from_label, to_label)] = self.get_weight(from_label, to_label)
        nx.draw_networkx_nodes(g, pos)
        nx.draw_networkx_edges(g, pos, arrows=True)
        nx.draw_networkx_labels(g, pos)
        nx.draw_networkx_edge_labels(g, pos, edge_labels=weights, label_pos=0.7)
        show()

    def construir_arvore(self, inicio: str) -> None:
        """
        Realiza uma travessia em profundidade e retorna
        o gráfico da árvore construida

        :param inicio: vértice inicial
        :type inicio: str
        :return: gráfico da árvore
        """
        arvore: Graph = Graph()
        visitados: set[str] = set()
        pilha: StackListBased = StackListBased()
        pilha.push(inicio)
        while pilha:
            ponto: str = pilha.pop()
            arvore.add_vertex(ponto)
            visitados.add(ponto)
            for adjacente in self._vertices[ponto]:
                if adjacente not in visitados:
                    pilha.push(adjacente)
                    visitados.add(adjacente)
                    arvore.add_vertex(adjacente)
                    arvore.add_edges(
                        ponto, adjacente, self.get_weight(ponto, adjacente)
                    )
        return arvore.draw_tree()
