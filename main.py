from models.book import Book
from repository.db import init_db
from services.libraryService import LibraryService

def seed_data(service: LibraryService) -> tuple:
    author_1 = service.create_author("AMAN")
    author_2 = service.create_author("AMANGELDI")

    student = service.register_student("AMANGELDI12")
    librarian = service.register_librarian("ALISHER")

    b1_id = service.add_book(Book("Python 101", "123456789011121", author_1.id))
    b2_id = service.add_book(Book("JS", "123456799011121", author_1.id))
    b3_id = service.add_book(Book("C++ ", "123456700011121", author_2.id))

    service.borrow_book(student, b1_id)
    service.borrow_book(student, b2_id)
    service.borrow_book(librarian, b3_id)
    service.borrow_book(librarian, b1_id)

    return student, librarian

def main() -> None:
    init_db()
    
    service = LibraryService()

    if not service.get_books():
        seed_data(service)

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