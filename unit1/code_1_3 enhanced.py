# superclass
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


# first child class
class ChildEmployee1(Employee):
    def __init__(self, name, age, salary, role):
        super().__init__(name, age, salary)
        self.role = role


# second child class
class ChildEmployee2(ChildEmployee1):
    def __init__(self, name, age, salary, role, department):
        super().__init__(name, age, salary, role)
        self.department = department


emp1 = Employee('harshit', 22, 1000)
emp2 = ChildEmployee1('HHarshit', 23, 2000, role="Engineer")

print(emp1.age)
print(f'{emp2.role}')

# Output 
# # 22
# # Engineer
