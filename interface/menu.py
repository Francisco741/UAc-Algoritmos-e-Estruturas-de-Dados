import interface.input_output as io
from sistema.sistema_turistico import SistemaTuristico


def opcoes_menu() -> str:
    """
    Opções de escolha do menu

    :return: opções disponíveis
    :rtype: str
    """
    return (
        "0 - Apresentação do concelho\n"
        "1 - Adicionar ponto de interesse\n"
        "2 - Alterar ponto de interesse\n"
        "3 - Pesquisar pontos de interesse\n"
        "4 - Assinalar e avaliar visita a ponto de interesse\n"
        "5 - Consultar estatísticas de visitas aos pontos de interesse\n"
        "6 - Obter sugestões de visitas a pontos de interesse\n"
        "7 - Gerir a rede de circulação\n"
        "8 - Consultar a rede de circulação\n"
        "9 - Consultar pontos críticos da via de circulação\n"
        "10 - Interromper via de circulação\n"
        "11 - Obter Itenerário\n"
        "12 - Consultar rotas para percursos de carro\n"
        "13 - Mapa dos pontos de interesse\n"
        "14 - Sair\n"
    )


def menu(st: SistemaTuristico) -> None:
    """
    Executa funções dependendo da opção inserida pelo utilizador

    :param st: objeto que caracteriza o sistema
    :type st: SistemaTuristico
    """
    fim = False
    while not fim:
        print(opcoes_menu())
        op = int(input("Opção: "))
        if op == 0:
            io.apresentacao_concelho()
        elif op == 1:
            print(io.adicionar_ponto_interesse(st))
        elif op == 2:
            print(io.alterar_ponto_interesse(st))
        elif op == 3:
            print(io.pesquisar_pontos_interesse(st))
        elif op == 4:
            print(io.avaliar_ponto_interesse(st))
        elif op == 5:
            print(io.consultar_estatisticas_visitas(st))
        elif op == 6:
            print(io.sugestoes_pontos_interesse(st))
        elif op == 7:
            menu2(st)
        elif op == 8:
            io.consultar_grafico_rede(st)
        elif op == 9:
            menu3(st)
        elif op == 10:
            print(io.interromper_via_circulacao(st))
        elif op == 11:
            print(io.obter_itinerario(st))
        elif op == 12:
            print(io.rotas_percurso_carro(st))
        elif op == 13:
            io.mapa_pontos(st)
        else:
            fim = True


def opcoes_menu2() -> str:
    """
    Opções de escolha do menu

    :return: opções disponíveis
    :rtype: str
    """
    return (
        "1 - Consultar pontos da rede de circulação\n"
        "2 - Acrescentar ponto à rede de circulação\n"
        "3 - Remover ponto da rede de circulação\n"
        "4 - Consultar vias da rede de circulação\n"
        "5 - Acrescentar via à rede de circulação\n"
        "6 - Remover via da rede de circulação\n"
        "7 - Voltar atrás\n"
    )


def menu2(st: SistemaTuristico) -> None:
    """
    Executa funções dependendo da opção inserida pelo utilizador

    :param st: objeto que caracteriza o sistema
    :type st: SistemaTuristico
    """
    fim = False
    while not fim:
        print(opcoes_menu2())
        op = int(input("Opção: "))
        if op == 1:
            print(io.consultar_pontos_rede(st))
        elif op == 2:
            print(io.acrescentar_ponto_rede(st))
        elif op == 3:
            print(io.remover_ponto_rede(st))
        elif op == 4:
            print(io.consultar_vias_rede(st))
        elif op == 5:
            print(io.acrescentar_via_rede(st))
        elif op == 6:
            print(io.remover_via_rede(st))
        else:
            fim = True


# * alterar comentario
def opcoes_menu3() -> str:
    """
    Opções de escolha do menu

    :return: opções disponíveis
    :rtype: str
    """
    return (
        "1 - Consultar pontos críticos pelo seu grau externo\n"
        "2 - Consultar pontos críticos pelo seu grau interno\n"
        "3 - Consultar pontos críticos pela sua proximidade\n"
        "4 - Voltar atrás\n"
    )


def menu3(st: SistemaTuristico) -> None:
    """
    Executa funções dependendo da opção inserida pelo utilizador

    :param st: objeto que caracteriza o sistema
    :type st: SistemaTuristico
    """
    fim = False
    while not fim:
        print(opcoes_menu3())
        op = int(input("Opção:  "))
        if op == 1:
            print(io.pontos_criticos_grau_externo(st))
        elif op == 2:
            print(io.pontos_criticos_grau_interno(st))
        elif op == 3:
            print(io.pontos_criticos_proximidade(st))
        else:
            fim = True
