# superclass
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


# first child class
class ChildEmployee1(Employee):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)
        self.name = name
        self.age = age
        self.salary = salary


# second child class
class ChildEmployee2(ChildEmployee1):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)
        self.name = name
        self.age = age
        self.salary = salary


emp1 = Employee('harshit', 22, 1000)
emp2 = ChildEmployee1('harshit', 23, 2000)

print(emp1.age)
print(f'{emp2.age}')
