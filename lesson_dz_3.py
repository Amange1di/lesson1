from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, owner, currency, initial_balance):
        self.owner = owner
        self._currency = currency
        self.__balance = initial_balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self.__balance = value
        else:
            print("Ошибка: баланс не может быть отрицательным")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Пополнение: +{amount} {self._currency}")

    def withdraw(self, amount):
        if self.can_withdraw(amount):
            self.__balance -= amount
            print(f"Снятие: -{amount} {self._currency}")
        else:
            print("Отказ: недостаточно средств или неверная сумма")

    @abstractmethod
    def can_withdraw(self, amount):
        pass

class PersonalAccount(BankAccount):
    def can_withdraw(self, amount):
        return 0 < amount <= self.balance

class AuthSystem(ABC):
    @abstractmethod
    def login(self, username, password):
        pass

class EmailAuth(AuthSystem):
    def login(self, username, password):
        return f"Login Email: {username} / {password}"

class GoogleAuth(AuthSystem):
    def login(self, username, password):
        return f"Login Google: {username} / {password}"

class TelegramAuth(AuthSystem):
    def login(self, username, password):
        return f"Login Telegram: {username} / {password}"

if __name__ == "__main__":
    acc = PersonalAccount("Aman", "som", 100000)
    print(f"Владелец: {acc.owner}")
    print(f"Начальный баланс: {acc.balance} {acc._currency}")
    
    acc.deposit(500)
    acc.withdraw(200)
    print(f"Итоговый баланс: {acc.balance}")
    
    acc.balance = -100
    
    print("-" * 30)
    
    auth_methods = [EmailAuth(), GoogleAuth(), TelegramAuth()]
    for auth in auth_methods:
        print(auth.login("user_test", "qwerty123"))