from models.author import Author
from models.book import Book
from models.user import Librarian, Student
from repository.library_repository import LibraryRepository


class LibraryService:
    def __init__(self, repository: LibraryRepository | None = None) -> None:
        self.repository = repository or LibraryRepository()

    def register_student(self, name: str) -> Student:
        user_id = self.repository.add_user(name, "student")
        return Student(user_id=user_id, name=name)

    def register_librarian(self, name: str, salary: float = 0.0) -> Librarian:
        user_id = self.repository.add_user(name, "librarian")
        return Librarian(user_id=user_id, name=name, salary=salary)

    def create_author(self, name: str) -> Author:
        author_id = self.repository.add_author(name)
        return Author(name=name, author_id=author_id)

    def add_book(self, book: Book) -> int:
        return self.repository.add_book(
            title=book.title,
            isbn=book.isbn,
            author_id=book.author_id,
        )

    def add_book_from_dict(self, payload: dict) -> int:
        book = Book.from_dict(payload)
        return self.add_book(book)

    def get_books(self) -> list[dict]:
        return self.repository.get_books()

    def update_book(
        self,
        book_id: int,
        title: str | None = None,
        isbn: str | None = None,
        author_id: int | None = None,
    ) -> None:
        if isbn is not None and not Book.validate_isbn(isbn):
            raise ValueError("Invalid ISBN format.")
        self.repository.update_book(book_id, title=title, isbn=isbn, author_id=author_id)

    def delete_book(self, book_id: int) -> None:
        self.repository.delete_book(book_id)

    def borrow_book(self, user, book_id: int) -> dict:
        book_row = self.repository.get_book_by_id(book_id)
        if not book_row:
            raise ValueError(f"Book with id={book_id} was not found.")

        book = Book.from_dict(book_row)
        action_result = user.borrow_book(book)
        record_id = self.repository.add_borrow_record(
            user_id=user.id,
            book_id=book_id,
            borrowed_days=action_result["borrow_days"],
        )
        return {
            "record_id": record_id,
            "message": action_result["action"],
            "borrow_days": action_result["borrow_days"],
        }

    def report_top_5_popular_books(self) -> list[dict]:
        return self.repository.top_5_popular_books()

    def report_books_borrowed_by_each_user(self) -> list[dict]:
        return self.repository.books_borrowed_by_each_user()

    def report_total_borrow_days_by_user(self) -> list[dict]:
        return self.repository.total_borrow_days_by_user()

    def report_users_above_average_borrows(self) -> list[dict]:
        return self.repository.users_above_average_borrows()

    def report_book_borrow_view(self) -> list[dict]:
        return self.repository.get_view_book_borrow_stats()
