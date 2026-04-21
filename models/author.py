class Author:
    def __init__(self, name: str, author_id: int | None = None) -> None:
        self.__id = author_id
        self.__name = name

    @property
    def id(self) -> int | None:
        return self.__id

    @id.setter
    def id(self, value: int) -> None:
        self.__id = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if not value or not value.strip():
            raise ValueError("name cannot be empty.")
        self.__name = value.strip()
