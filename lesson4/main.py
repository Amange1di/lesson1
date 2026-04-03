from abc import ABC, abstractmethod


class User:
    def __init__(self, user_id, name, balance=0):
        self.id = user_id
        self.name = name
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def add_balance(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Баланс пополнен. {amount} add ")

    def spend(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return True
        return False





class Product:
    def __init__(self, product_id, name, price):
        self.id = product_id
        self.name = name
        self.price = price

    def get_info(self):
        return f"Товар: {self.name} | Цена: {self.price}"


class Electronics(Product):
    def __init__(self, product_id, name, price, warranty):
        super().__init__(product_id, name, price)
        self.warranty = warranty

    def get_info(self):
        return f"Электроника: {self.name} | Цена: {self.price} | Гарантия: {self.warranty} мес."


class Clothing(Product):
    def __init__(self, product_id, name, price, size):
        super().__init__(product_id, name, price)
        self.size = size

    def get_info(self):
        return f"Одежда: {self.name} | Цена: {self.price} | Размер: {self.size}"


class Cart:
    def __init__(self, user):
        self.user = user
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Добавлено: {product.name}")

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
            print(f"Удалено: {product.name}")

    def get_total_price(self):
        return sum(p.price for p in self.products)

    def clear(self):
        self.products = []


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CardPayment(Payment):
    def pay(self, amount):
        print(f"Оплата {amount} CardPayment  ")


class CryptoPayment(Payment):
    def pay(self, amount):
        print(f"Оплата {amount} CryptoPayment")



def checkout(cart, payment_method):
    total = cart.get_total_price()

    if not cart.products:
        print("Корзина пуста")
        return

    if not cart.user.spend(total):
        print("Недостаточно средств!")
        return

    if payment_method.pay(total):
        print("Оплата успешна ✅")
        cart.clear()


user1 = User(1, "Aman", 1000000)
print(f"Пользователь: {user1.name}, Баланс: {user1.balance}")
user1.add_balance(450)
print(user1.balance)


catalog = [
    Electronics(1, "Смартфон", 5000, 12),
    Electronics(2, "Ноутбук", 90000, 24),
    Clothing(3, "Футболка", 1500, "L"),
    Clothing(4, "Джинсы", 3500, "M"),
    Clothing(5, "Худи", 4500, "XL"),
]

for product in catalog:
    print(product.get_info())

cart = Cart(user1)
cart.add_product(catalog[0])
cart.add_product(catalog[0])
print(f" Cтоимость: {cart.get_total_price()}")
cart.remove_product(catalog[0])
print(f"Стоимость после удаления: {cart.get_total_price()}")
checkout(cart, CardPayment())
print(user1.balance)