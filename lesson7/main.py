import random
import sqlite3

class Gladiator:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, enemy):
        damage = random.randint(0, self.power)

        if random.random() < 0.2:
            damage *= 2
            print(f"{self.name} сделал критический удар")

        if random.random() < 0.1:
            damage = 0
            print(f"{self.name} промахнулся")

        enemy.health -= damage
        print(f"{self.name} ударил {enemy.name} на {damage}. HP {enemy.name}: {max(0, enemy.health)}")


class Tank(Gladiator):
    def __init__(self, name):
        super().__init__(name, 150, 20)


class Archer(Gladiator):
    def __init__(self, name):
        super().__init__(name, 100, 30)


class Berserker(Gladiator):
    def __init__(self, name):
        super().__init__(name, 120, 40)


def battle(g1, g2):
    rounds = 0
    print(f"{g1.name} vs {g2.name}")

    while g1.health > 0 and g2.health > 0:
        rounds += 1
        print(f"\nРаунд {rounds}")

        g1.attack(g2)
        if g2.health <= 0:
            print(f"Победил {g1.name}")
            return g1, g2, rounds

        g2.attack(g1)
        if g1.health <= 0:
            print(f"Победил {g2.name}")
            return g2, g1, rounds


def save_result(winner, loser, rounds):
    conn = sqlite3.connect("gladiators.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        winner TEXT,
        loser TEXT,
        rounds INTEGER
    )
    """)

    cursor.execute(
        "INSERT INTO results (winner, loser, rounds) VALUES (?, ?, ?)",
        (winner.name, loser.name, rounds)
    )

    conn.commit()
    conn.close()

    print("Сохранено")


if __name__ == "__main__":
    g1 = Tank("Танк")
    g2 = Berserker("Берсерк")

    winner, loser, rounds = battle(g1, g2)
    save_result(winner, loser, rounds)