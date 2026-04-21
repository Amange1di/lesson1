from models.baseUser import BaseUser


class User(BaseUser):
    def __init__(self, user_id: int, name: str, user_type: str) -> None:
        super().__init__(user_id, name)
        self.__user_type = user_type

    @property
    def user_type(self) -> str:
        return self.__user_type

    @user_type.setter
    def user_type(self, value: str) -> None:
        if value not in {"student", "librarian"}:
            raise ValueError("user_type must be 'student' or 'librarian'.")
        self.__user_type = value


class Student(User):
    def __init__(self, user_id: int, name: str, max_books: int = 3) -> None:
        super().__init__(user_id, name, "student")
        self.__max_books = max_books

    @property
    def max_books(self) -> int:
        return self.__max_books

    @max_books.setter
    def max_books(self, value: int) -> None:
        if value < 1:
            raise ValueError("max_books must be positive.")
        self.__max_books = value

    def borrow_book(self, book) -> dict:
        return {
            "action": f"Student {self.name} borrowed '{book.title}'.",
            "borrow_days": 14,
        }


class Worker:
    def __init__(self, salary: float = 0.0) -> None:
        self.__salary = salary

    @property
    def salary(self) -> float:
        return self.__salary

    @salary.setter
    def salary(self, value: float) -> None:
        if value < 0:
            raise ValueError("salary cannot be negative.")
        self.__salary = value

    def work(self) -> str:
        return "Librarian is managing catalog operations."


class Librarian(User, Worker):
    def __init__(self, user_id: int, name: str, salary: float = 0.0) -> None:
        User.__init__(self, user_id, name, "librarian")
        Worker.__init__(self, salary)

    def borrow_book(self, book) -> dict:
        return {
            "action": f"Librarian {self.name} issued '{book.title}' to a reader.",
            "borrow_days": 30,
        }
