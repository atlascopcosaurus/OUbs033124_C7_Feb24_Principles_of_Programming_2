class Employee:
    def __init__(self, name, age, id, salary):
        # self is an instance of a class
        self.name = name
        self.age = age
        self.id = id
        self.salary = salary


emp1 = Employee("harshit", 22, 1000, 1234)
emp2 = Employee("arjun", 23, 2000, 2234)

print(emp1.__dict__)
