class Book:
    def __init__(
        self,
        title: str,
        isbn: str,
        author_id: int,
        book_id: int | None = None,
    ) -> None:
        if not self.validate_isbn(isbn):
            raise ValueError("ISBN must contain 10 or 13 digits.")

        self.__id = book_id
        self.__title = title
        self.__isbn = isbn
        self.__author_id = author_id

    @property
    def id(self) -> int | None:
        return self.__id

    @id.setter
    def id(self, value: int) -> None:
        self.__id = value

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, value: str) -> None:
        if not value or not value.strip():
            raise ValueError("title cannot be empty.")
        self.__title = value.strip()

    @property
    def isbn(self) -> str:
        return self.__isbn

    @isbn.setter
    def isbn(self, value: str) -> None:
        if not self.validate_isbn(value):
            raise ValueError("ISBN must contain 10 or 13 digits.")
        self.__isbn = value

    @property
    def author_id(self) -> int:
        return self.__author_id

    @author_id.setter
    def author_id(self, value: int) -> None:
        if value <= 0:
            raise ValueError("author_id must be positive.")
        self.__author_id = value

    def __str__(self) -> str:
        return f"Book(title='{self.__title}', isbn='{self.__isbn}', author_id={self.__author_id})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Book):
            return False
        return self.__isbn == other.__isbn

    @staticmethod
    def validate_isbn(isbn: str) -> bool:
        if not isbn:
            return False
        digits = "".join(ch for ch in isbn if ch.isdigit())
        return len(digits) in {10, 13}

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            title=data["title"],
            isbn=data["isbn"],
            author_id=data["author_id"],
            book_id=data.get("id"),
        )
