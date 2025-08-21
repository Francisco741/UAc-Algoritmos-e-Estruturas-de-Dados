import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from sistema.sistema_turistico import SistemaTuristico
from interface.input_output import carregar_sistema_turistico
from interface.menu import menu


def main() -> None:
    """
    Função principal do programa que cria um objeto
    que caracteriza o sistema, carrega dados nele
    e chama o menu principal
    """
    st: SistemaTuristico = SistemaTuristico()
    carregar_sistema_turistico(st)
    menu(st)


if __name__ == "__main__":
    main()
