import webbrowser
from os import path
from json import load, dump
from typing import List, Tuple, Union
from math import floor
from sistema.sistema_turistico import SistemaTuristico
from sistema.ponto_interesse import PontoInteresse
from sistema.via_circulacao import ViaCirculacao
from sistema.Ponto2D import Ponto2D


def carregar_sistema_turistico(st: SistemaTuristico) -> None:
    """
    Carrega os dados do ficheiro json para o objeto da classe SistemaTuristico

    :param st: objeto que caracteriza o sistema
    :type st: SistemaTuristico
    """
    current_dir = path.dirname(path.abspath(__file__))
    relative_path = path.join("..", "sistema", "sistema_turistico.json")
    file_path = path.join(current_dir, relative_path)
    with open(file_path, "r", encoding="UTF-8") as f:
        dados: dict = load(f)
        for ponto in dados["pontos"]:
            ponto_interesse: PontoInteresse = PontoInteresse(
                ponto["designacao"],
                ponto["morada"],
                Ponto2D(ponto["coordenadas"]["x"], ponto["coordenadas"]["y"]),
                ponto["categoria"],
                ponto["acessibilidade"],
                ponto["atividades"],
            )
            ponto_interesse._avaliacao = ponto["avaliacao"]
            ponto_interesse._visitas = ponto["visitas"]
            st.adicionar_ponto(ponto_interesse)
        for via in dados["rede"]:
            via_circulacao: ViaCirculacao = ViaCirculacao(
                via["inicio"],
                via["fim"],
                via["distancia"],
                via["velocidade_minima"],
                via["velocidade_maxima"],
            )
            st._rede.append(via_circulacao)
        for p, a in dados["grafo"].items():
            st._grafo._vertices[p] = a


def gravar_sistema_turistico(st: SistemaTuristico) -> None:
    """
    Grava os dados do objeto da classe SistemaTuristico no ficheiro json

    :param st: objeto que caracteriza o sistema
    :type st: SistemaTuristico
    """
    sistema_turistico: dict = {
        "pontos": [
            {
                "designacao": ponto_interesse._designacao,
                "morada": ponto_interesse._morada,
                "coordenadas": {
                    "x": ponto_interesse._coordenadas._x,
                    "y": ponto_interesse._coordenadas._y,
                },
                "categoria": ponto_interesse._categoria,
                "acessibilidade": ponto_interesse._acessibilidade,
                "atividades": ponto_interesse._atividades,
                "avaliacao": ponto_interesse._avaliacao,
                "visitas": ponto_interesse._visitas,
            }
            for ponto_interesse in st._pontos
        ],
        "rede": [
            {
                "inicio": via._inicio,
                "fim": via._fim,
                "distancia": via._distancia,
                "velocidade_minima": via._velocidade_minima,
                "velocidade_maxima": via._velocidade_maxima,
            }
            for via in st._rede
        ],
        "grafo": st._grafo._vertices,
    }
    current_dir = path.dirname(path.abspath(__file__))
    relative_path = path.join("..", "sistema", "sistema_turistico.json")
    file_path = path.join(current_dir, relative_path)
    with open(file_path, "w", encoding="UTF-8") as f:
        dump(sistema_turistico, f, indent=4)


def apresentacao_concelho() -> None:
    """
    Apresenta o concelho e pede ao utilizador se quer
    abrir o link para obter mais informações
    """
    url: str = "https://angradoheroismo.pt/"
    print(
        "O concelho de Angra do Heroísmo está localizado na ilha "
        "Terceira, nos Açores, Portugal, e é uma área com uma "
        "rica história e cultura.\nA cidade de Angra do Heroísmo, "
        "a sua capital, foi fundada em 1534 e é um importante "
        "centro de comércio, turismo, cultura e património.\n"
        "A cidade possui muitos edifícios históricos bem "
        "preservados, como a Catedral de Angra do Heroísmo "
        "e a Fortaleza de São João Baptista, e foi declarada "
        "Património Mundial pela UNESCO em 1983.\nAlém disso, "
        "o concelho de Angra do Heroísmo é conhecido pelas "
        "suas paisagens naturais deslumbrantes, pelas suas "
        "tradições culturais e pela sua gastronomia única, "
        "tornando-se um destino turístico muito popular.\n"
        f"Mais informações em {url}\n"
    )
    abrir: str = str(input("Deseja abrir o link? (S/N): "))
    if abrir.upper() == "S":
        webbrowser.open(url)


def adicionar_ponto_interesse(st: SistemaTuristico) -> str:
    """
    Pede ao utilizador os atributos do ponto de interesse
    a adicionar ao objeto da classe SistemaTuristico

    :param st: objeto que caracteriza o sistema
    :type st: SistemaTuristico
    :return: mensagem de sucesso ou de erro na operação
    :rtype: str
    """
    designacao: str = str(input("Insira a designação do ponto de interesse: "))
    for pontos_interesse in st._pontos:
        if designacao == pontos_interesse._designacao:
            return "Já existe um ponto de interesse com esta designação\n"
    morada: str = str(input("Insira a morada do ponto de interesse: "))
    latitude: float = float(input("Insira a latitude do ponto de interesse: "))
    longitude: float = float(input("Insira a longitude do ponto de interesse: "))
    coordenadas: Ponto2D = Ponto2D(latitude, longitude)
    categoria: str = str(input("Insira a categoria do ponto de interesse: "))
    if categoria.lower() not in st._categorias:
        return "Categoria não existente no sistema \n"
    acessibilidade: str = str(
        input("Insira informação sobre as " "acessibilidades do ponto de interesse: ")
    )
    atividades: str = str(
        input(
            "Insira informação sobre as atividades "
            "existentes no ponto de interesse: "
        )
    )
    st.adicionar_ponto(
        PontoInteresse(
            designacao,
            morada,
            coordenadas,
            categoria.lower(),
            acessibilidade,
            atividades,
        )
    )
    gravar_sistema_turistico(st)
    return "Ponto de interesse adicionado com sucesso\n"


def alterar_ponto_interesse(st: SistemaTuristico) -> str:
    """
    Pede ao utilizador alterações à categoria e à
    acessibilidade de um ponto de interesse específico

    :param st: objeto que caracteriza o sistema
    :type st: SistemaTuristico
    :return: mensagem de sucesso ou de erro na operação
    :rtype: str
    """
    designacao: str = str(
        input("Insira a designação do ponto de interesse que deseja alterar: ")
    )
    for ponto_interesse in st._pontos:
        if designacao == ponto_interesse._designacao:
            categoria: str = str(
                input("Insira a nova categoria do ponto de interesse: ")
            )
            if categoria.lower() not in st._categorias:
                return "Categoria não existente no sistema\n"
            acessibilidade: str = str(
                input(
                    "Insira informação sobre as novas "
                    "acessibilidades do ponto de interesse: "
                )
            )
            st.alterar_ponto(ponto_interesse, categoria, acessibilidade)
            gravar_sistema_turistico(st)
            return "Ponto de interesse alterado com sucesso\n"
    return "Não foi encontrado nenhum ponto de interesse com esta designação\n"


def pesquisar_pontos_interesse(st: SistemaTuristico) -> str:
    """
    Pede ao utilizador qual a categoria dos
    pontos de interesse que deseja pesquisar
    e mostra todos os pontos da categoria

    :param st: objeto que caracteriza o sistema
    :type st: SistemaTuristico
    :return: pontos de interesse da categoria selecionada
    ordenados por ordem alfabética
    :rtype: str
    """
    categoria: str = str(
        input("Insira a categoria dos pontos de interesse " "que pretende pesquisar: ")
    )
    if categoria.lower() not in st._categorias:
        return "Categoria não existente no sistema\n"
    return (
        f"Pontos de interesse da categoria {categoria}:\n\n"
        f"{st.pesquisar_pontos(categoria)}"
    )


def avaliar_ponto_interesse(st: SistemaTuristico) -> str:
    """
    Pede ao utilizador para avaliar um determinado
    ponto de interesse que este visitou e incrementa
    o contador de visitas do ponto de interesse em uma unidade

    :param st: objeto que caracteriza o sistema
    :type st: SistemaTuristico
    :return: mensagem de sucesso ou de erro na operação
    :rtype: str
    """
    escala: List[int] = [1, 2, 3, 4]
    designacao: str = str(
        input("Insira a designação do ponto turístico que quer avaliar: ")
    )
    for ponto_interesse in st._pontos:
        if ponto_interesse._designacao == designacao:
            print(
                "1 - Nada Satisfeito\n"
                "2 - Pouco Satisfeito\n"
                "3 - Satisfeito\n"
                "4 - Muito Satisfeito\n"
            )
            avaliacao: int = int(input("Avalie a sua visita: "))
            while avaliacao not in escala:
                print("Insira um número que esteja na escala numérica\n")
                avaliacao: int = int(input("Avalie a sua visita: "))
            st.avaliar_ponto(avaliacao, ponto_interesse)
            gravar_sistema_turistico(st)
            return "Avaliação feita com sucesso!\n"
    return "Não foi encontrado nenhum ponto de interesse com esta designação\n"


def consultar_estatisticas_visitas(st: SistemaTuristico) -> str:
    """
    Consulta todos os pontos de interesse,
    indicando a sua designação, categoria,
    número de visitas e classificação média
    e o gráfico com a distribuição dos pontos de interesse
    pelos valores da escala numérica

    :param st: objeto que caracteriza o sistema
    :type st: SistemaTuristico
    :return: atributos dos pontos de interesse
    :rtype: str
    """
    return st.consultar_estatisticas()


def sugestoes_pontos_interesse(st: SistemaTuristico) -> str:
    """
    Pede ao utilizador uma certa latitude e longitude
    e sugere pontos de interesse na proximidade

    :param st: objeto que caracteriza o sistema
    :type st: SistemaTuristico
    :return: pontos de interesse próximos das coordenadas inseridas,
    mostrados por ordem decrescente do número de visitas
    :rtype: str
    """
    latitude: float = float(input("Insira uma latitude: "))
    longitude: float = float(input("Insira uma longitude: "))
    if st.sugestoes_visitas(latitude, longitude):
        return (
            f"Pontos de interesse próximos da localização:\n\n"
            f"{st.sugestoes_visitas(latitude, longitude)}"
        )
    return "Não foram encontrados pontos de interesse " "próximos desta localização\n"


def consultar_pontos_rede(st: SistemaTuristico) -> str:
    """
    Consulta todos os pontos de interesse pertencentes à rede de circulação

    :param st: objeto que caracteriza o sistema
    :type st: SistemaTuristico
    :return: pontos de interesse na rede de circulação
    :rtype: str
    """
    return (
        f"Pontos de interesse na rede de circulação:\n\n" f"{st.consultar_vertices()}"
    )


def acrescentar_ponto_rede(st: SistemaTuristico) -> str:
    """
    Acrescenta um ponto de interesse à rede de circulação

    :param st: objeto que caracteriza o sistema
    :type st: SistemaTuristico
    :return: mensagem de sucesso ou de erro na operação
    :rtype: str
    """
    designacao: str = str(
        input(
            "Insira a designação do ponto de interesse "
            "que deseja acrescentar à rede: "
        )
    )
    for ponto_interesse in st._pontos:
        if designacao == ponto_interesse._designacao:
            if designacao not in st._grafo._vertices:
                st.acrescentar_vertice(designacao)
                gravar_sistema_turistico(st)
                return "Ponto de interesse adicionado à rede com sucesso\n"
            return "Já existe um ponto de interesse com esta designação na rede\n"
    return "Não foi encontrado nenhum ponto de interesse com esta designação \n"


def remover_ponto_rede(st: SistemaTuristico) -> str:
    """
    Remove um ponto de interesse da rede de circulação

    :param st: objeto que caracteriza o sistema
    :type st: SistemaTuristico
    :return: mensagem de sucesso ou de erro na operação
    :rtype: str
    """
    designacao: str = str(
        input(
            "Insira a designação do ponto de interesse " "que deseja remover da rede: "
        )
    )
    if designacao in st._grafo._vertices:
        st.remover_vertice(designacao)
        gravar_sistema_turistico(st)
        return "Ponto de interesse removido da rede com sucesso\n"
    return (
        "Não foi encontrado nenhum ponto de interesse " "com esta designação na rede\n"
    )


def consultar_vias_rede(st: SistemaTuristico) -> str:
    """
    Consulta todas as vias pertencentes à rede de circulação

    :param st: objeto que caracteriza o sistema
    :type st: SistemaTuristico
    :return: vias na rede de circulação
    :rtype: str
    """
    return f"Vias na rede de circulação:\n\n" f"{st.consultar_arestas()}"


def acrescentar_via_rede(st: SistemaTuristico) -> str:
    """
    Acrescenta uma via à rede de circulação

    :param st: objeto que caracteriza o sistema
    :type st: SistemaTuristico
    :return: mensagem de sucesso ou de erro na operação
    :rtype: str
    """
    inicio: str = str(
        input(
            "Insira a designação do ponto do inicio da via "
            "que deseja acrescentar à rede: "
        )
    )
    fim: str = str(
        input(
            "Insira a designação do ponto do fim da via "
            "que deseja acrescentar à rede: "
        )
    )
    if inicio == fim:
        return "Pontos da via não podem ser iguais\n"
    inicio_encontrado: bool = False
    fim_encontrado: bool = False
    lat_inicio: float = 0
    lon_inicio: float = 0
    lat_fim: float = 0
    lon_fim: float = 0
    for ponto_interesse in st._pontos:
        if inicio == ponto_interesse._designacao:
            inicio_encontrado: bool = True
            lat_inicio: float = ponto_interesse._coordenadas._x
            lon_inicio: float = ponto_interesse._coordenadas._y
        elif fim == ponto_interesse._designacao:
            fim_encontrado: bool = True
            lat_fim: float = ponto_interesse._coordenadas._x
            lon_fim: float = ponto_interesse._coordenadas._y
    if inicio_encontrado and fim_encontrado:
        if inicio in st._grafo._vertices and fim in st._grafo._vertices:
            if (
                inicio not in st._grafo._vertices[fim]
                and fim not in st._grafo._vertices[inicio]
            ):
                distancia_coordenadas: float = st.distancia_terra(
                    lat_inicio, lon_inicio, lat_fim, lon_fim
                )
                distancia: float = float(input("Insira a distância da via (km): "))
                if distancia <= 0:
                    return "Distância tem de ser um número positivo\n"
                elif distancia < (distancia_coordenadas / 1000):
                    return (
                        "Distância não pode ser inferior à distância "
                        "entre as coordenadas geográficas dos seus vértices\n"
                    )
                velocidade_minima: float = float(
                    input("Insira a velocidade mínima da via (km/h): ")
                )
                if velocidade_minima < 0:
                    return "Velocidade mínima tem de ser " "um número positivo ou 0\n"
                velocidade_maxima: float = float(
                    input("Insira a velocidade máxima da via (km/h): ")
                )
                if velocidade_maxima <= 0:
                    return "Velocidade máxima tem de ser " "um número positivo\n"
                elif velocidade_maxima <= velocidade_minima:
                    return (
                        "Velocidade máxima tem de ser "
                        "maior do que a velocidade mínima\n"
                    )
                st.acrescentar_aresta(
                    ViaCirculacao(
                        inicio, fim, distancia, velocidade_minima, velocidade_maxima
                    )
                )
                gravar_sistema_turistico(st)
                return "Via adicionada à rede com sucesso\n"
            return "Via já existe na rede\n"
        return "Pontos de interesse não estão via de circulação"
    elif inicio_encontrado and not fim_encontrado:
        return "Ponto de interesse do fim da via não encontrado\n"
    elif not inicio_encontrado and fim_encontrado:
        return "Ponto de interesse do início da via não encontrado\n"
    else:
        return "Nenhum Ponto de interesse encontrado\n"


def remover_via_rede(st: SistemaTuristico) -> str:
    """
    Remove uma via da rede de circulação

    :param st: objeto que caracteriza o sistema
    :type st: SistemaTuristico
    :return: mensagem de sucesso ou de erro na operação
    :rtype: str
    """
    inicio: str = str(
        input(
            "Insira a designação do ponto do inicio da via "
            "que deseja remover da rede: "
        )
    )
    fim: str = str(
        input(
            "Insira a designação do ponto do fim da via " "que deseja remover da rede: "
        )
    )
    for via in st._rede:
        if via._inicio == inicio and via._fim == fim:
            st.remover_aresta(via)
            gravar_sistema_turistico(st)
            return "Via removida da rede de circulação com sucesso\n"
    return "Via não existe na rede de circulação \n"


def consultar_grafico_rede(st: SistemaTuristico) -> None:
    """
    Visualizar a rede completa em modo gráfico

    :param st: objeto que caracteriza o sistema
    :type st: SistemaTuristico
    """
    st._grafo.draw_graph()


def pontos_criticos_grau_externo(st: SistemaTuristico) -> str:
    """
    Pontos da rede mais críticos, considerando
    a métrica de centralidade grau externo,
    ordenados por ordem decrescente

    :param st: objeto que caracteriza o sistema
    :type st: SistemaTuristico
    :return: pontos ordenados por ordem decrescente do grau externo
    :rtype: str
    """
    return st.grau_externo()


def pontos_criticos_grau_interno(st: SistemaTuristico) -> str:
    """
    Pontos da rede mais críticos, considerando
    a métrica de centralidade grau interno,
    ordenados por ordem decrescente

    :param st: objeto que caracteriza o sistema
    :type st: SistemaTuristico
    :return: pontos ordenados por ordem decrescente do grau interno
    :rtype: str
    """
    return st.grau_interno()


def pontos_criticos_proximidade(st: SistemaTuristico) -> str:
    return st.proximidade()


def interromper_via_circulacao(st: SistemaTuristico) -> str:
    """
    Seleciona uma ou mais vias de circulação para interromper
    temporariamente a circulação viária, indicando os
    caminhos alternativos entre os dois pontos da via interrompida,
    ordenados por ordem crescente da distância

    :param st: objeto que caracteriza o sistema
    :type st: SistemaTuristico
    :return: caminhos alternativos entre os dois pontos da via interrompida
    ordenados por ordem crescente da distância
    :rtype: str
    """
    inicio: str = str(
        input(
            "Insira a designação do ponto do inicio da via " "que deseja interromper: "
        )
    )
    fim: str = str(
        input("Insira a designação do ponto do fim da via " "que deseja interromper: ")
    )
    for via in st._rede:
        if via._inicio == inicio and via._fim == fim:
            st.remover_aresta(via)
            while len(st._rede) > 0:
                decisao: str = str(input("Deseja interromper mais alguma via? (S/N): "))
                if decisao.upper() != "S":
                    break
                inicio_extra: str = str(
                    input(
                        "Insira a designação do ponto do inicio da via "
                        "que deseja interromper: "
                    )
                )
                fim_extra: str = str(
                    input(
                        "Insira a designação do ponto do fim da via "
                        "que deseja interromper: "
                    )
                )
                removido: bool = False
                for vias in st._rede:
                    if vias._inicio == inicio_extra and vias._fim == fim_extra:
                        st.remover_aresta(vias)
                        removido: bool = True
                if not removido:
                    return "Via não existe na rede de circulação\n"
            if st._grafo.total_caminhos(inicio, fim):
                caminhos: List[Tuple[Union[int, float], List[str]]] = st.quick_sort(
                    st._grafo.distancia_caminhos(st._grafo.total_caminhos(inicio, fim))
                )
                caminhos.reverse()
                caminhos_ordenados: str = ""
                for c in caminhos:
                    caminhos_ordenados += (
                        f"Caminho: {str(c[1])}\n" f"Distância: {str(c[0])}\n\n"
                    )
                return caminhos_ordenados
            else:
                return "Não existem caminhos\n"
    return "Via não existe na rede de circulação\n"


def obter_itinerario(st: SistemaTuristico) -> str:
    """
    Pede ao utilizador para selecionar dois pontos de interesse,
    mostrando o caminho mais curto entre o ponto de origem e o
    ponto de destino, indicando também a distância a percorrer e o
    tempo estimado a pé e de carro.

    :param st: objeto que caracteriza o sistema
    :type st: SistemaTuristico
    :return: caminho mais curto entre os pontos, indicando também
    a distância a percorrer e o tempo estimado a pé e de carro
    :rtype: str
    """
    inicio: str = str(input("Insira a designação do ponto de origem: "))
    fim: str = str(input("Insira a designação do ponto de destino: "))
    if inicio in st._grafo._vertices and fim in st._grafo._vertices:
        caminho: Tuple[Union[int, float], List[str]] = st.quick_sort(
            st._grafo.distancia_caminhos(st._grafo.total_caminhos(inicio, fim))
        )[-1]
        tempo_a_pe: float = 0.0
        tempo_carro: float = 0.0
        for i in range(len(caminho[1]) - 1):
            for v in st._rede:
                if caminho[1][i] == v._inicio and caminho[1][i + 1] == v._fim:
                    tempo_a_pe += v._tempo_a_pe
                    tempo_carro += v._tempo_carro
        horas_a_pe: int = floor(tempo_a_pe)
        minutos_a_pe: int = round((tempo_a_pe - horas_a_pe) * 60)
        horas_carro: int = floor(tempo_carro)
        minutos_carro: int = round((tempo_carro - horas_carro) * 60)
        return (
            f"Caminho: {str(caminho[1])}\n"
            f"Distância (km): {str(caminho[0])}\n"
            f"Tempo a percorrer a pé: {horas_a_pe}h {minutos_a_pe}m\n"
            f"Tempo a percorrer de carro: {horas_carro}h {minutos_carro}m\n"
        )
    return "Pontos de interesse não encontrados\n"


def rotas_percurso_carro(st: SistemaTuristico) -> str:
    """
    Pede ao utilizador para escolher dois pontos de interesse
    e compara o grau externo destes, escolhendo o com maior valor.
    Retorna um gráfico da árvore com origem nesse ponto

    :param st: objeto que caracteriza o sistema
    :type st: SistemaTuristico
    :return: mensagem de sucesso ou de erro na operação
    :rtype: str
    """
    designacao1: str = str(input("Insira a designação de um ponto de origem:  "))
    for ponto_interesse1 in st._grafo._vertices:
        if ponto_interesse1 == designacao1:
            designacao2: str = str(
                input("Insira a designação de outro ponto de origem:  ")
            )
            for ponto_interesse2 in st._grafo._vertices:
                if ponto_interesse2 == designacao2:
                    if len(st._grafo.adjacentes_externo(ponto_interesse1)) >= len(
                        st._grafo.adjacentes_externo(ponto_interesse2)
                    ):
                        designacao = ponto_interesse1
                    else:
                        designacao = ponto_interesse2
                    st._grafo.construir_arvore(designacao)
                    return "A mostrar gráfico da árvore...\n"
            return (
                "Não foi encontrado nenhum ponto " "de interesse com esta designação \n"
            )
    return "Não foi encontrado nenhum ponto de interesse com esta designação \n"


def mapa_pontos(st: SistemaTuristico) -> None:
    """
    Mostra um mapa com os pontos de interesse
    usando as coordenadas de cada um

    :param st: objeto que caracteriza o sistema
    :type st: SistemaTuristico
    """
    st.mapa()
