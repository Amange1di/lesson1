import sqlite3
from typing import Optional, List, Tuple


DATABASE_NAME = "users.db"


def get_connection():
    return sqlite3.connect(DATABASE_NAME)


def init_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE,
            age INTEGER
        )
    """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT,
            user_id INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        )
    """
    )

    conn.commit()
    conn.close()




def create_user(name: str, email: str, age: Optional[int] = None) -> int:
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO users (name, email, age)
            VALUES (?, ?, ?)
        """,
            (name, email, age),
        )
        conn.commit()
        user_id = cursor.lastrowid
        print(f"Пользователь создан: {name} (ID: {user_id})")
        return user_id
    except sqlite3.IntegrityError as e:
        print(f"Ошибка: {e}")
        return -1
    finally:
        conn.close()


def get_users() -> List[Tuple]:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, email, age FROM users")
    users = cursor.fetchall()
    conn.close()

    return users


def get_user(user_id: int) -> Optional[Tuple]:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, email, age FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    conn.close()

    return user


def update_user(user_id: int, name: str, email: str, age: Optional[int] = None) -> bool:
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            UPDATE users
            SET name = ?, email = ?, age = ?
            WHERE id = ?
        """,
            (name, email, age, user_id),
        )
        conn.commit()

        if cursor.rowcount > 0:
            print(f"Пользователь {user_id} обновлен")
            return True
        else:
            print(f" Пользователь {user_id} не найден")
            return False
    except sqlite3.IntegrityError as e:
        print(f"Ошибка: {e}")
        return False
    finally:
        conn.close()


def delete_user(user_id: int) -> bool:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()

    if cursor.rowcount > 0:
        print(f"Пользователь {user_id} удален")
        result = True
    else:
        print(f" Пользователь {user_id} не найден")
        result = False

    conn.close()
    return result




def create_post(title: str, content: str, user_id: int) -> int:
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO posts (title, content, user_id)
            VALUES (?, ?, ?)
        """,
            (title, content, user_id),
        )
        conn.commit()
        post_id = cursor.lastrowid
        print(f"Пост создан: {title} (ID: {post_id})")
        return post_id
    except sqlite3.IntegrityError as e:
        print(f"Ошибка: {e}")
        return -1
    finally:
        conn.close()


def get_posts_by_user(user_id: int) -> List[Tuple]:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, title, content, user_id FROM posts WHERE user_id = ?
    """,
        (user_id,),
    )
    posts = cursor.fetchall()
    conn.close()

    return posts


def get_all_posts() -> List[Tuple]:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, title, content, user_id FROM posts")
    posts = cursor.fetchall()
    conn.close()

    return posts




def print_separator(title: str = ""):
    if title:
        print(f"\n{'=' * 50}")
        print(f"  {title}")
        print(f"{'=' * 50}")
    else:
        print()


if __name__ == "__main__":
    init_database()
    print("База данных инициализирована\n")

    print("\n1. Создание пользователей:")
    create_user("Alex", "alex@gmail.com", 20)
    create_user("Bob", "bob@gmail.com", 25)

    print("\n2. Все пользователи:")
    users = get_users()
    for user in users:
        print(f"   ID: {user[0]}, Name: {user[1]}, Email: {user[2]}, Age: {user[3]}")

    print("\n3. Обновление пользователя (ID=1):")
    update_user(1, "Alex Updated", "alex2@gmail.com", 21)

    print("\n4. Получение пользователя (ID=1):")
    user = get_user(1)
    if user:
        print(f"   ID: {user[0]}, Name: {user[1]}, Email: {user[2]}, Age: {user[3]}")

    print("\n5. Удаление пользователя (ID=2):")
    delete_user(2)

    print("\n6. Пользователи после удаления:")
    users = get_users()
    for user in users:
        print(f"   ID: {user[0]}, Name: {user[1]}, Email: {user[2]}, Age: {user[3]}")


    print("\n1. Создание дополнительных пользователей:")
    create_user("Charlie", "charlie@gmail.com", 30)
    create_user("Diana", "diana@gmail.com", 28)

    print("\n2. Создание постов:")
    create_post("Python основы", "Введение в Python", 1)
    create_post("Flask туториал", "Создание веб-приложения", 1)
    create_post("Django advanced", "Продвинутые техники", 3)
    create_post("SQL запросы", "Оптимизация SQL", 4)

    print("\n3. Посты пользователя (ID=1, Alex):")
    posts = get_posts_by_user(1)
    for post in posts:
        print(f"   ID: {post[0]}, Title: {post[1]}, Content: {post[2]}")

    print("\n4. Посты пользователя (ID=3, Charlie):")
    posts = get_posts_by_user(3)
    for post in posts:
        print(f"   ID: {post[0]}, Title: {post[1]}, Content: {post[2]}")

    print("\n5. Все посты в системе:")
    all_posts = get_all_posts()
    for post in all_posts:
        print(f"   ID: {post[0]}, User ID: {post[3]}, Title: {post[1]}")

    print_separator()
    print("Все тесты успешно выполнены!\n")


