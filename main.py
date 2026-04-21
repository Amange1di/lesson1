import sqlite3
import random
import datetime

ENCHANTMENTS = {
    "Огонь": {"урон": 5, "прочность": -1},
    "Лёд": {"меткость": 3, "шанс_крита": 2},
    "Яд": {"урон": 3, "шанс_крита": 5},
    "Сила": {"урон": 7},
    "Точность": {"меткость": 7},
    "Прочность": {"прочность": 10},
}


class Weapon:
    def __init__(self, name, damage, crit_damage, crit_chance, accuracy, durability):
        self.name = name
        self.damage = damage
        self.crit_damage = crit_damage
        self.crit_chance = crit_chance
        self.accuracy = accuracy
        self.durability = durability

    def apply_enchantment(self, enchantment):
        for attr, bonus in ENCHANTMENTS[enchantment].items():
            if hasattr(self, attr):
                setattr(self, attr, getattr(self, attr) + bonus)

    def __str__(self):
        return (
            f"{self.name}: урон={self.damage}, крит. урон={self.crit_damage}, "
            f"шанс крита={self.crit_chance}%, меткость={self.accuracy}, прочность={self.durability}"
        )


def init_db():
    conn = sqlite3.connect("history.db")
    c = conn.cursor()
    c.execute(
        """CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        weapon_name TEXT,
        enchantment TEXT,
        result TEXT
    )"""
    )
    conn.commit()
    conn.close()


def log_action(weapon_name, enchantment, result):
    conn = sqlite3.connect("history.db")
    c = conn.cursor()
    c.execute(
        "INSERT INTO history (timestamp, weapon_name, enchantment, result) VALUES (?, ?, ?, ?)",
        (datetime.datetime.now().isoformat(), weapon_name, enchantment, result),
    )
    conn.commit()
    conn.close()


def show_history():
    conn = sqlite3.connect("history.db")
    c = conn.cursor()
    c.execute("SELECT * FROM history ORDER BY id DESC LIMIT 20")
    rows = c.fetchall()
    for row in rows:
        print(f"[{row[1]}] {row[2]} + {row[3]} => {row[4]}")
    conn.close()


def create_weapon():
    name = input("Введите название оружия: ")
    print("1 — Случайные характеристики, 2 — Ввести вручную")
    mode = input("Выберите режим: ")
    if mode == "1":
        damage = random.randint(10, 20)
        crit_damage = random.randint(20, 40)
        crit_chance = random.randint(5, 25)
        accuracy = random.randint(60, 100)
        durability = random.randint(10, 30)
    else:
        damage = int(input("Урон: "))
        crit_damage = int(input("Крит. урон: "))
        crit_chance = int(input("Шанс крита (%): "))
        accuracy = int(input("Меткость: "))
        durability = int(input("Прочность: "))
    return Weapon(name, damage, crit_damage, crit_chance, accuracy, durability)


def enchant_weapon(weapon):
    print("Доступные зачарования:")
    for i, ench in enumerate(ENCHANTMENTS.keys(), 1):
        print(f"{i}. {ench} (+{ENCHANTMENTS[ench]})")
    idx = int(input("Выберите зачарование: ")) - 1
    enchantment = list(ENCHANTMENTS.keys())[idx]
    print(f"Попытка зачаровать {weapon.name} с помощью {enchantment}...")
    success = random.random() < 0.7  # 70% успеха
    if success:
        weapon.apply_enchantment(enchantment)
        result = "Успех"
        print("Зачарование успешно!")
    else:
        weapon.durability -= random.randint(1, 5)
        result = "Провал (поломка)"
        print("Зачарование не удалось, оружие повреждено!")
    log_action(weapon.name, enchantment, result)
    print(weapon)


def main():
    init_db()
    print("--- Программа зачарования оружия ---")
    while True:
        print("\n1 — Создать оружие и зачаровать")
        print("2 — Показать историю")
        print("0 — Выход")
        choice = input("Выберите действие: ")
        if choice == "1":
            weapon = create_weapon()
            enchant_weapon(weapon)
        elif choice == "2":
            show_history()
        elif choice == "0":
            break
        else:
            print("Некорректный ввод!")


if __name__ == "__main__":
    main()
