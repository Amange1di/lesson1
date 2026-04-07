# HelloWorld(print)


# class A:
#     def method_a(self):
#         print("A")


# class B:
#     def method_b(self):
#         print("B")


# class C(A, B):
#     pass


# obj = C()
# obj.method_a()
# obj.method_b()


# class A:
#     def __init__(self):
#         print(" A")
#         super().__init__()


# class B:
#     def __init__(self):
#         print(" B")
#         super().__init__()


# class C(A, B):
#     def __init__(self):
#         print("C")
#         super().__init__()


# obj = C()
# obj.__init__()

# print(C.mro())


# class Printer:
#     def print_text(self):
#         print("Печать докмента")

# class Scanner:
#     def scan(self):
#         print("Сканирование докмента")


# class MFP (Printer, Scanner):
#     pass


# device = MFP()
# device.print_text()
# device.scan()


# class MyClass:
#     value: 0

#     @classmethod
#     def set_value(cls, v):
#         cls.value = v


# MyClass.set_value(10)
# print(MyClass.value)


# class Book:
#     def __init__(self, title):
#         self.title = title

#     def __str__(self):
#         return f"Book: {self.title}"


# print(Book("Python 101"))


# class User:
#     @staticmethod

#     def is_valid_email(email):
#         return "@" in email

# print(User.is_valid_email("test@gmail.com"))  
# print(User.is_valid_email("invalid-email"))    


