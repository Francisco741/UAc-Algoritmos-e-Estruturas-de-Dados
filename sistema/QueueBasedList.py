from typing import TypeVar, Generic, List, Iterator


T = TypeVar("T")


class QueueBasedList(Generic[T]):
    """Implementation of ADT Queue based on Python type list."""

    def __init__(self, source_collection=None):
        """
        Sets the initial state of self, which includes the
        contents of source_collection, if it's present.
        :param source_collection: initial content of self
        """
        self._items: List[T] = list()
        """current elements in queue"""

        self._size: int = 0
        """current size of queue"""

        if source_collection:
            for item in source_collection:
                self.add(item)

    # collection accessor methods

    def is_empty(self) -> bool:
        """
        Tests if self is empty.
        :return: True if len(self) is 0, otherwise False
        """
        return len(self) == 0

    def __len__(self) -> int:
        """
        Gets the number of items in self.
        :return: the number of items in self
        """
        return self._size

    def __str__(self) -> str:
        """
        Builds the string representation of self.
        :return: String representation of self
        """
        return "[" + " ".join(map(str, self)) + "]"

    def __iter__(self) -> Iterator:
        """
        Supports iteration over a view of self.
        :return: an iteration of self
        """
        return iter(self._items)

    # collection mutator methods

    def clear(self) -> None:
        """
        Makes self become empty.
        :return: None
        """
        self._items = list()
        self._size = 0

    # Queue accessor methods

    def peek(self) -> T:
        """
        Gets the item at the top of the queue, assuming the queue is not empty.
        :return: the top item
        """
        return self._items[0]

    # Queue mutator methods

    def add(self, item: T) -> None:
        """
        Inserts item at the rear of the queue.
        :param item: the item to insert
        :return: None
        """
        self._items.append(item)
        self._size += 1

    def pop(self) -> T:
        """
        Removes the item at top of the queue, assuming the queue is not empty
        :return: the item removed
        """
        self._size -= 1
        return self._items.pop(0)
