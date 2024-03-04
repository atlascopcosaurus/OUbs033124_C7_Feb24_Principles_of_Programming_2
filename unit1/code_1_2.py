class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


class ChildEmployee(Employee):
    def __init__(self, name, age, salary, id):
        super().__init__(name, age, salary)
        self.name = name
        self.age = age
        self.salary = salary
        self.id = id


emp1 = Employee('harshit', 22, 1000)
childEmp = ChildEmployee('Doosan', 36, 2500, 3087)

print(emp1.age)

print(f'Hello {childEmp.id}')
