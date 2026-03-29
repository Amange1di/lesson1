


# # class Animal:
# #     def speak(self):
# #         print("Животное издает звук")

# # class Dog(Animal):
# #     pass


# # dog = Dog()
# # dog.speak()


# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def info(self):
#         print(f"Name : {self.name}, Slalary: {self.salary}")

# class Developer(Employee):
#     def __init__(self, name, salary, language):
#         super().__init__(name, salary)
#         self.language = language

#     def info(self):
#         print(f"""Name : {self.name}, Salary: 
#         {self.salary}, language : {self.language}""")

# class Manager(Employee):
#     def __init__(self, name, salary, team_size):
#         super().__init__(name, salary)
#         self.team_size = team_size

#     def info(self):
#         print(f"""Name : {self.name}, Salary: 
#         {self.salary}, team_size : {self.team_size}""")

# dev = Developer("Bob", 2000, "Python")
# man = Manager("Alice", 4000, 5)
# dev.info()
# man.info()

# class Dog:
#     def speak(self):
#         return "Gav Gav"
    
# class Cat:
#     def speak(self):
#         return "May May"
    
# animals = [Dog(), Cat()]

# for animal in animals:
#     print(animal.speak())



# класс Shape
# метод area()
#  классы:
# Circle → площадь круга
#  → площадь прямоугольника


class Shape:
    def area(self):
        print("Площадь фигуры")

class Circle(Shape):
    def area(self):
        print("площадь круга")

class Rectangle(Shape):
    def area(self):
        print("площадь прямоугольника")

shapes = [Shape(), Circle(), Rectangle()]

for shape in shapes:
    shape.area()