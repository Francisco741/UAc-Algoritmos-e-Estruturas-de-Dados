from typing import TypeVar, Generic, Optional


T = TypeVar("T")


class DoubleNode(Generic[T]):
    """Nó duplamente ligado"""

    def __init__(self, data: T):
        """
        Define o estado inicial de self

        :param data: dados contidos no nó
        :type data: T
        """
        self._data: T = data
        self._next: Optional[DoubleNode] = None
        self._prev: Optional[DoubleNode] = None


class LinkedList(Generic[T]):
    """TDA Lista baseado em estruturas duplamente ligadas"""

    def __init__(self):
        """Define o estado inicial de self"""
        self._head: Optional[DoubleNode] = None
        self._tail: Optional[DoubleNode] = None

    def __iter__(self):
        """
        Itera sobre a lista

        :yield: dados do nó atual
        :rtype: T
        """
        current: Optional[DoubleNode] = self._head
        while current:
            yield current._data
            current: Optional[DoubleNode] = current._next

    def add(self, data: T) -> None:
        """
        Adiciona um novo nó com determinados dados

        :param data: dados a adicionar
        :type data: T
        """
        new_node: DoubleNode = DoubleNode(data)
        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            new_node._prev = self._tail
            self._tail._next = new_node
            self._tail = new_node

    def remove(self, data: T) -> None:
        """
        Remove um nó da lista

        :param data: dados do nó a ser removido
        :type data: T
        """
        current: Optional[DoubleNode] = self._head
        while current:
            if current._data == data:
                if current._prev:
                    current._prev._next = current._next
                else:
                    self._head = current._next
                if current._next:
                    current._next._prev = current._prev
                else:
                    self._tail = current._prev
                return None
            current: Optional[DoubleNode] = current._next

    def update(self, old_data: T, new_data: T) -> None:
        """
        Alterar os dados de um nó na lista

        :param old_data: dados a serem alterados no nó
        :type old_data: T
        :param new_data: dados a serem inseridos no nó
        :type new_data: T
        """
        current: Optional[DoubleNode] = self._head
        while current:
            if current._data == old_data:
                current._data = new_data
                return None
            current: Optional[DoubleNode] = current._next

    def get(self, data: T) -> Optional[T]:
        """
        Obter o valor de um nó

        :param data: dados contidos no nó
        :type data: T
        :return: _description_
        :rtype: _type_
        """
        current = self._head
        while current:
            if current._data == data:
                return current._data
            current = current._next
        return None
