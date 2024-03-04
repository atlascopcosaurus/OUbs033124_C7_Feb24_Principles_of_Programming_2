class Employee1:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f'Employee(Name: {self.name}, Age: {self.age}, Salary: {self.salary})'


class Employee2:
    def __init__(self, name, age, salary, department=None):
        self.name = names
        self.age = age
        self.salary = salary
        self.department = department  # Added to demonstrate a different attribute

    def __str__(self):
        return f'Employee(Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Department: {self.department})'


class ChildEmployee(Employee1, Employee2):
    def __init__(self, name, age, salary, role, department):
        Employee1.__init__(self, name, age, salary)
        # Since Employee1 and Employee2 have the same attributes, we choose to explicitly call one
        # to avoid ambiguity. For additional attributes from Employee2, set them directly.
        self.role = role
        self.department = department  # Assuming you want to inherit and use this from Employee2

    def __str__(self):
        return f'{super().__str__()}, Role: {self.role}, Department: {self.department}'


# Example usage
emp1 = ChildEmployee('Harshit', 22, 1000, 'Engineer', 'Development')
emp2 = ChildEmployee('HHarshit', 23, 2000, 'Manager', 'HR')

print(emp1)
print(emp2)
