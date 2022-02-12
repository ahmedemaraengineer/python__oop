# Special methods or magic methods allow us emulate some built-in behaviour
# Within python and it's also how we implement operator overloading
# Dunder Methods ...
# (1)- Some special methods are used to overcome the ambiguous representation
# Of the objects

class Employee:
    raise_amount = 1.04
    # __init__ method is one of the special methods that allows us
    # To create objects outside the class .
    def __init__(self, first: str, last: str, pay: int):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = '{}_{}@company.com'.format(first, last)

    def full_name(self):
        return self.first + ' ' + self.last

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # (2)- Returning an informative definition of an object
    def __repr__(self):
        return "Employee('{}', {}, {})".format(self.first, self.last, self.pay)

    # (3)- this is a little more informative that is suitable for the end-user
    def __str__(self):
        return '{} - {}'.format(self.full_name(), self.email)

    # (4)- Here is another Dunder Method that add things together under specific conditions
    # Here we will interpret the addition sign as adding the two pays
    # of two employees
    def __add__(self, other):
        return self.pay + other.pay

    # (5)- Here we want to enable the class to calculate the length
    # of a specific string using one of the magic methods
    def __len__(self):
        return len(self.full_name())


emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "Employee", 60000)

# (1)
# print(emp_1)
# --> <__main__.Employee object at 0x000001E3044F8400>

# (2)
# print(emp_1)
# --> Employee('Corey', Schafer, 50000)

# (3)
# print(emp_1)
# --> Corey Schafer - Corey_Schafer@company.com

# print(str(emp_1))
# print(repr(emp_1))

# print(emp_1.__str__())
# print(emp_1.__repr__())

# (4)
# print(emp_1 + emp_2)
# print(emp_1.__add__(emp_2))

# (5)
# print(len(emp_2))
# print(emp_1.__len__())