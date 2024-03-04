class Employee1:
    def name(self):
        print("Harshit is my name")

    def salary(self):
        print("3000 is his salary")

    def age(self):
        print("22 is his age")


class Employee2:
    def name(self):
        print("Rahul is my name")

    def salary(self):
        print("4000 is his salary")

    def age(self):
        print("23 is his age")


def func(obj):
    obj.name()
    obj.salary()
    obj.age()


obj_emp1 = Employee1()
obj_emp2 = Employee2()

func(obj_emp1)
func(obj_emp2)


# Output
# Harshit is my name
# 3000 is his salary
# 22 is his age
# Rahul is my name
# 4000 is his salary
# 23 is his age
