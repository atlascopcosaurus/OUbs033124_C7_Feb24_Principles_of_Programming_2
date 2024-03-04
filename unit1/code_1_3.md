Inheritance is a way to form new classes using classes that have already been defined. The newly formed classes are called derived classes, subclasses, or child classes, and the classes that we derive from are called base classes or parent classes. Let's break down the code and explain it in detail.

### Superclass: Employee
The `Employee` class is defined as a superclass or parent class. It has an `__init__` method (constructor) that initializes three attributes: `name`, `age`, and `salary` for an Employee object. This class is the base class from which other classes will inherit.

```python
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
```

### First Child Class: ChildEmployee1
`ChildEmployee1` is a subclass or child class of the `Employee` class. It inherits from `Employee` and also has an `__init__` method. Within this method, it calls `super().__init__(name, age, salary)` to initialize the inherited attributes. This use of `super()` is a way to call the parent class's constructor and ensures that the `name`, `age`, and `salary` attributes are initialized in the same way as the parent class. After calling `super()`, the attributes are redundantly set again, which is actually unnecessary because `super().__init__` already does this.

```python
class ChildEmployee1(Employee):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)
        # The following lines are unnecessary since super() already does the job
        self.name = name
        self.age = age
        self.salary = salary
```

### Second Child Class: ChildEmployee2
`ChildEmployee2` is a subclass of `ChildEmployee1`, making it a grandchild of the `Employee` class. It follows the same pattern as `ChildEmployee1`, using `super().__init__` to call its parent class's constructor, which in turn calls the constructor of `Employee`. Similar to `ChildEmployee1`, it unnecessarily sets the attributes again after they have already been initialized by the parent class's constructor.

```python
class ChildEmployee2(ChildEmployee1):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)
        # Again, these lines are unnecessary
        self.name = name
        self.age = age
        self.salary = salary
```

### Instances and Prints
Two instances of the classes are created, `emp1` of `Employee` and `emp2` of `ChildEmployee1`, and the `age` attribute of each is printed. This demonstrates that instances of both parent and child classes can be created and used to access attributes defined in the parent class.

```python
emp1 = Employee('harshit', 22, 1000)
emp2 = ChildEmployee1('harshit', 23, 2000)

print(emp1.age)  # Prints 22
print(f'{emp2.age}')  # Prints 23 using formatted string
```

### Type of Inheritance
The type of inheritance demonstrated here is **multilevel inheritance**, where a class is derived from another derived class, forming a "grandparent-parent-child" relationship. `Employee` is the base class, `ChildEmployee1` is derived from `Employee`, and `ChildEmployee2` is derived from `ChildEmployee1`.

### Note on Redundant Code
The redundant setting of attributes in both `ChildEmployee1` and `ChildEmployee2` after calling `super().__init__` is unnecessary and not recommended in practice since it introduces extra lines of code without adding any value.