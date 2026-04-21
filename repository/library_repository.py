from repository.db import get_connection, init_db


class LibraryRepository:
    def __init__(self) -> None:
        init_db()

    def add_author(self, name: str) -> int:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO authors (name) VALUES (?)", (name,))
            conn.commit()
            return cursor.lastrowid

    def add_user(self, name: str, user_type: str) -> int:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO users (name, user_type) VALUES (?, ?)",
                (name, user_type),
            )
            conn.commit()
            return cursor.lastrowid

    def add_book(self, title: str, isbn: str, author_id: int) -> int:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO books (title, isbn, author_id) VALUES (?, ?, ?)",
                (title, isbn, author_id),
            )
            conn.commit()
            return cursor.lastrowid

    def get_books(self) -> list[dict]:
        with get_connection() as conn:
            cursor = conn.cursor()
            rows = cursor.execute(
                """
                SELECT
                    b.id,
                    b.title,
                    b.isbn,
                    b.author_id,
                    a.name AS author_name
                FROM books b
                JOIN authors a ON a.id = b.author_id
                ORDER BY b.id
                """
            ).fetchall()
            return [dict(row) for row in rows]

    def get_book_by_id(self, book_id: int) -> dict | None:
        with get_connection() as conn:
            cursor = conn.cursor()
            row = cursor.execute(
                "SELECT id, title, isbn, author_id FROM books WHERE id = ?",
                (book_id,),
            ).fetchone()
            return dict(row) if row else None

    def update_book(
        self,
        book_id: int,
        title: str | None = None,
        isbn: str | None = None,
        author_id: int | None = None,
    ) -> None:
        updates = []
        params = []

        if title is not None:
            updates.append("title = ?")
            params.append(title)
        if isbn is not None:
            updates.append("isbn = ?")
            params.append(isbn)
        if author_id is not None:
            updates.append("author_id = ?")
            params.append(author_id)

        if not updates:
            return

        params.append(book_id)

        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(f"UPDATE books SET {', '.join(updates)} WHERE id = ?", params)
            conn.commit()

    def delete_book(self, book_id: int) -> None:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
            conn.commit()

    def add_borrow_record(self, user_id: int, book_id: int, borrowed_days: int) -> int:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO borrow_records (user_id, book_id, borrowed_days)
                VALUES (?, ?, ?)
                """,
                (user_id, book_id, borrowed_days),
            )
            conn.commit()
            return cursor.lastrowid

    def top_5_popular_books(self) -> list[dict]:
        with get_connection() as conn:
            cursor = conn.cursor()
            rows = cursor.execute(
                """
                SELECT
                    b.id,
                    b.title,
                    COUNT(br.id) AS borrow_count
                FROM books b
                LEFT JOIN borrow_records br ON br.book_id = b.id
                GROUP BY b.id, b.title
                ORDER BY borrow_count DESC, b.title ASC
                LIMIT 5
                """
            ).fetchall()
            return [dict(row) for row in rows]

    def books_borrowed_by_each_user(self) -> list[dict]:
        with get_connection() as conn:
            cursor = conn.cursor()
            rows = cursor.execute(
                """
                SELECT
                    u.id,
                    u.name,
                    u.user_type,
                    COUNT(br.id) AS books_taken
                FROM users u
                LEFT JOIN borrow_records br ON br.user_id = u.id
                GROUP BY u.id, u.name, u.user_type
                ORDER BY books_taken DESC, u.name ASC
                """
            ).fetchall()
            return [dict(row) for row in rows]

    def total_borrow_days_by_user(self) -> list[dict]:
        with get_connection() as conn:
            cursor = conn.cursor()
            rows = cursor.execute(
                """
                SELECT
                    u.id,
                    u.name,
                    COALESCE(SUM(br.borrowed_days), 0) AS total_borrow_days
                FROM users u
                LEFT JOIN borrow_records br ON br.user_id = u.id
                GROUP BY u.id, u.name
                ORDER BY total_borrow_days DESC, u.name ASC
                """
            ).fetchall()
            return [dict(row) for row in rows]

    def users_above_average_borrows(self) -> list[dict]:
        with get_connection() as conn:
            cursor = conn.cursor()
            rows = cursor.execute(
                """
                SELECT
                    u.id,
                    u.name,
                    COUNT(br.id) AS borrow_count
                FROM users u
                JOIN borrow_records br ON br.user_id = u.id
                GROUP BY u.id, u.name
                HAVING COUNT(br.id) > (
                    SELECT AVG(user_borrows)
                    FROM (
                        SELECT COUNT(*) AS user_borrows
                        FROM borrow_records
                        GROUP BY user_id
                    )
                )
                ORDER BY borrow_count DESC, u.name ASC
                """
            ).fetchall()
            return [dict(row) for row in rows]

    def get_view_book_borrow_stats(self) -> list[dict]:
        with get_connection() as conn:
            cursor = conn.cursor()
            rows = cursor.execute(
                """
                SELECT book_id, title, borrow_count
                FROM book_borrow_stats
                ORDER BY borrow_count DESC, title ASC
                """
            ).fetchall()
            return [dict(row) for row in rows]
