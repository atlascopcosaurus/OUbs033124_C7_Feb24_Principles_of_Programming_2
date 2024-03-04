class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f'Employee(Name: {self.name}, Age: {self.age}, Salary: {self.salary})'

class ChildEmployee1(Employee):
    def __init__(self, name, age, salary, role):
        super().__init__(name, age, salary)
        self.role = role

    def __str__(self):
        return super().__str__() + f', Role: {self.role}'

class ChildEmployee2(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.department = department

    def __str__(self):
        return super().__str__() + f', Department: {self.department}'

# Example usage
emp1 = ChildEmployee1('Harshit', 22, 1000, 'Engineer')
emp2 = ChildEmployee2('HHarshit', 23, 2000, 'HR')

print(emp1)
print(emp2)


# Output
# Employee(Name: Harshit, Age: 22, Salary: 1000), Role: Engineer
# Employee(Name: HHarshit, Age: 23, Salary: 2000), Department: HR