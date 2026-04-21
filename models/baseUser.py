from abc import ABC, abstractmethod


class BaseUser(ABC):
    def __init__(self, user_id: int, name: str) -> None:
        self._id = user_id
        self._name = name

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not value or not value.strip():
            raise ValueError("Name cannot be empty.")
        self._name = value.strip()

    @abstractmethod
    def borrow_book(self, book):
        raise NotImplementedError
