class Library:
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__books = []
        self.__users = []

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if not value or not value.strip():
            raise ValueError("Library name cannot be empty.")
        self.__name = value.strip()

    @property
    def books(self) -> list:
        return list(self.__books)

    @books.setter
    def books(self, value: list) -> None:
        self.__books = list(value)

    @property
    def users(self) -> list:
        return list(self.__users)

    @users.setter
    def users(self, value: list) -> None:
        self.__users = list(value)

    def add_book(self, book) -> None:
        self.__books.append(book)

    def add_user(self, user) -> None:
        self.__users.append(user)

    def __len__(self) -> int:
        return len(self.__books)
