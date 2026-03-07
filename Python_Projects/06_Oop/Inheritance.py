class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)   # calling parent constructor
        self.salary = salary
"""
emp = Employee("Rayasat", 50000)
print(emp.name, emp.salary)
"""
a=Employee("Rayasat",1500)
print(a.name)