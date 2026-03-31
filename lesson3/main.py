# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance

#     def get_balance(self):
#         return self.__balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount

# acc = BankAccount(1000)
# print(acc.get_balance())

# acc.withdraw(400)
# print(acc.get_balance())

# acc.deposit(1000)
# print(acc.get_balance())


# class User:
#     def __init__(self, username, password, age):
#         self.username = username
#         self._age = age
#         self.__password = password

#     @property
#     def password(self):
#         return "нельзя посмотреть пароль!"

#     @password.setter
#     def password(self, new_password):
#         if len(new_password) < 6:
#             print("Слишком короткий пароль!")
#             return
#         self.__password = new_password

#     def check_password(self, password):
#         return self.__password == password

#     @property
#     def age(self):
#         return self._age

#     @age.setter
#     def age(self, age):
#         if age < 0:
#             print("Возраст не должен быть отрицательным!")
#             return
#         self._age = age


# user = User("bob", "12345678", 19)

# print(user.username)
# print(user.password)
# user.password = "qwertyu"
# print(user.check_password("qwertyu"))
# user.age = 20
# print(user.age)
# user.age = -5
# print(user.age)


from abc import ABC, abstractmethod


class AuthSystem(ABC):
    @abstractmethod
    def login(self, username, password):
        pass


class EmailAuth(AuthSystem):
    def login(self, username, password):
        return f"Login  Email: {username} \ {password}"


class GoogleAuth(AuthSystem):
    def login(self, username, password):
        return f"Login  Google: {username} \  {password}"


class TelegramAuth(AuthSystem):
    def login(self, username, password):
        return f"Login  Telegram: {username} \  {password}"


email_auth = EmailAuth()
google_auth = GoogleAuth()
telegram_auth = TelegramAuth()


print(email_auth.login("user1", "pass123"))
print(google_auth.login("user2", "pass456"))
print(telegram_auth.login("user3", "pass789"))
