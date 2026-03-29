


class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, target):
        pass

    def info(self):
        print(f"Имя: {self.name}, Здоровье: {self.health}")

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} получил {damage} урона. Осталось {self.health} ")

        if self.health <= 0:
            print(f"{self.name} погиб ")




class Warrior(Character):
    def __init__(self, name, health, strength):
        super().__init__(name, health)
        self.strength = strength

    def attack(self, target):
        damage = self.strength
        print(f"Воин наносит удар мечом с силой {self.strength}")
        target.take_damage(damage)


class Mage(Character):
    def __init__(self, name, health, mana):
        super().__init__(name, health)
        self.mana = mana

    def attack(self, target):
        damage = self.mana
        print(f"Маг использует заклинание, тратя {self.mana} маны")
        target.take_damage(damage)


class Archer(Character):
    def __init__(self, name, health, arrows):
        super().__init__(name, health)
        self.arrows = arrows

    def attack(self, target):
        if self.arrows > 0:
            self.arrows -= 1
            damage = 15
            print(f"Лучник стреляет стрелой. Осталось стрел: {self.arrows}")
            target.take_damage(damage)
        else:
            print("У лучника нет стрел ")


warrior = Warrior("Aa1B", 90, 20)
mage = Mage("Aa2M", 80, 40)
archer = Archer("Aa3A", 80, 3)

characters = [warrior, mage, archer]

for char in characters:
    char.attack(warrior)


print("\n=== () ===")
warrior.attack(mage)
mage.attack(warrior)
archer.attack(warrior)
