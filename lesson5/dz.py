from abc import ABC, abstractmethod


class Employee(ABC):
	def __init__(self, name: str, salary: float):
		if not self.is_valid_name(name):
			raise ValueError("Имя должно быть минимум 2 символа")
		self._name = name
		self.__salary = 0
		self.set_salary(salary)

	def get_salary(self) -> float:
		return self.__salary

	def set_salary(self, value: float):
		if value < 0:
			raise ValueError("Зарплата не может быть меньше 0")
		self.__salary = value

	@abstractmethod
	def work(self) -> str:
		raise NotImplementedError

	@classmethod
	def create_from_string(cls, data: str):
		parts = data.split(",")
		if len(parts) != 2:
			raise ValueError("Ожидается формат 'Имя,зарплата'")
		name = parts[0].strip()
		try:
			salary = float(parts[1].strip())
		except ValueError:
			raise ValueError("Неверный формат зарплаты")
		return cls(name, salary)

	@staticmethod
	def is_valid_name(name: str) -> bool:
		return isinstance(name, str) and len(name.strip()) >= 2

	def __str__(self) -> str:
		return f"{self._name} - {self.get_salary()}"

	def __len__(self) -> int:
		return len(self._name)

	def __eq__(self, other) -> bool:
		if not isinstance(other, Employee):
			return NotImplemented
		return self.get_salary() == other.get_salary()


class LoggerMixin:
	def log(self, message: str):
		print(f"[LOG] {self._name}: {message}")


class BonusMixin:
	def add_bonus(self, amount: float):
		if amount < 0:
			raise ValueError("Бонус не может быть отрицательным")
		new_salary = self.get_salary() + amount
		self.set_salary(new_salary)


class Developer(Employee, LoggerMixin, BonusMixin):
	def work(self) -> str:
		action = "Пишет код"
		self.log(action)
		return action


class Manager(Employee, LoggerMixin):
	def work(self) -> str:
		action = "Управляет командой"
		self.log(action)
		return action



if __name__ == "__main__":
	dev = Developer("Beka", 15000)
	mgr = Manager("AAAAAAAA", 1500)
	dev2 = Developer.create_from_string("Aman, 1200")

	employees = [dev, mgr, dev2]

	for emp in employees:
		print(emp.work())

	print(str(dev))
	print(len(mgr))
	print(dev == dev2)

	dev.add_bonus(200)
	print(dev.get_salary())

