class User:
    def __init__(self, username, age):
        self.username = username
        self.age = age

    def hello(self):
        return f"{self.username}  hello!"


user1 = User("Bob", 12)

print(user1.username)
print(user1.age)

print(user1.hello())


class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def info(self):
        return f"{self.brand} едет со скоростью {self.speed}"


car1 = Car("BMW", 120)
print(car1.info())
