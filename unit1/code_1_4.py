# superclass
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f'Employee(Name: {self.name}, Age: {self.age}, Salary: {self.salary})'


class ChildEmployee1(Employee):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)
        self.name = name
        self.age = age
        self.salary = salary


# second child class
class ChildEmployee2(Employee):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)
        self.name = name
        self.age = age
        self.salary = salary


emp1 = ChildEmployee1('harshit', 22, 1000)
emp2 = ChildEmployee2('HHarshit', 23, 2000)

print(emp1)
print(f'{emp2}')
