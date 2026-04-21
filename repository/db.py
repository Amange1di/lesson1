import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "repository.db"


def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def init_db() -> None:
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                user_type TEXT NOT NULL CHECK(user_type IN ('student', 'librarian'))
            )
            """
        )

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS authors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
            """
        )

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                isbn TEXT NOT NULL UNIQUE,
                author_id INTEGER NOT NULL,
                FOREIGN KEY(author_id) REFERENCES authors(id) ON DELETE CASCADE
            )
            """
        )

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS borrow_records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                book_id INTEGER NOT NULL,
                borrowed_days INTEGER NOT NULL DEFAULT 14,
                borrowed_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE,
                FOREIGN KEY(book_id) REFERENCES books(id) ON DELETE CASCADE
            )
            """
        )

        cursor.execute(
            """
            CREATE VIEW IF NOT EXISTS book_borrow_stats AS
            SELECT
                b.id AS book_id,
                b.title AS title,
                COUNT(br.id) AS borrow_count
            FROM books b
            LEFT JOIN borrow_records br ON br.book_id = b.id
            GROUP BY b.id, b.title
            """
        )

        conn.commit()
