from models.book import Book
from repository.db import init_db
from services.libraryService import LibraryService


def seed_data(service: LibraryService) -> tuple:
    author_1 = service.create_author("Aman")
    author_2 = service.create_author("Amangeldi")

    student = service.register_student("Student Demo")
    librarian = service.register_librarian("Librarian Demo")

    b1_id = service.add_book(Book("Python 101", "9780132350884", author_1.id))
    b2_id = service.add_book(Book("Java Basics", "9780134685991", author_1.id))
    b3_id = service.add_book(Book("C++ Guide", "9780321563842", author_2.id))

    service.borrow_book(student, b1_id)
    service.borrow_book(student, b2_id)
    service.borrow_book(librarian, b3_id)
    service.borrow_book(librarian, b1_id)

    return student, librarian


def ensure_demo_borrows_for_existing_books(service: LibraryService) -> None:
    stats = service.report_books_borrowed_by_each_user()
    has_any_borrow = any(row["books_taken"] > 0 for row in stats)
    books = service.get_books()

    if has_any_borrow or not books:
        return

    student = service.register_student("Student Auto")
    librarian = service.register_librarian("Librarian Auto")

    first_book_id = books[0]["id"]
    service.borrow_book(student, first_book_id)
    service.borrow_book(student, first_book_id)

    if len(books) > 1:
        second_book_id = books[1]["id"]
        service.borrow_book(librarian, second_book_id)
    else:
        service.borrow_book(librarian, first_book_id)


def main() -> None:
    init_db()
    service = LibraryService()

    if not service.get_books():
        seed_data(service)
    else:
        ensure_demo_borrows_for_existing_books(service)

    print("\n--- Список всех книг ---")
    for book in service.get_books():
        print(f"ID: {book['id']} | Название: {book['title']} | ISBN: {book['isbn']}")

    print("\n--- Топ 5 популярных книг ---")
    for row in service.report_top_5_popular_books():
        print(f"Книга: {row['title']} | Выдана раз: {row['borrow_count']}")

    print("\n--- Статистика по пользователям (Среднее и выше) ---")
    for user_stat in service.report_users_above_average_borrows():
        print(user_stat)


if __name__ == "__main__":
    main()
