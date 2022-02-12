# Inheritance allows us to inherit attributes from a parent class
# Now that is useful because we can create subclasses and get
# All of the functionalities of the parent class and we can override or add
# completely new functionality without affecting the parent class .

class Employee:
    raise_amount = 1.04

    def __init__(self, first: str, last: str, pay: int):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = '{}_{}@company.com'.format(first, last)

    def full_name(self):
        return self.first + ' ' + self.last

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


# (1)- We want to create a subclass that inherits from the Employee class ;
class Developer(Employee):
    # (2)- We can now change our class variable just in here without affecting the parent class
    raise_amount = 1.10

    # (3)- What if we wanted to add an extra attribute that doesn't exist
    # In our parent class (eg, Programming_language)
    def __init__(self, first, last, pay, prog_lang):
        # We want now the parent class handle the already-known data
        # Which are (first, last, pay)
        super().__init__(first, last, pay)
        # Now we want to handle the added feature
        self.prog_lang = prog_lang


# (4)- We want now to create a new subclass called(manager) :
class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print("--->", emp.full_name())


# So whether we create our instance using the parent class or the subclass
# We will see the same results
# (1)
# dev_1 = Employee("Corey", "Schafer", 50000)
# dev_2 = Employee("Test", "employee", 60000)
# dev_1 = Developer("Corey", "Schafer", 50000)
# dev_2 = Developer("Test", "employee", 60000)
# print(dev_1.email)
# print(dev_2.email)

# print(help(Developer))

# (2)
# print(dev_1.pay)
# We can use on of our methods that is in our parent class in our instance
# That is inherited from the parent class
# dev_1.apply_raise()
# print(dev_1.pay)

# (3)
# We can now make use of our new feature that is defined in our subclass
# And has nothing to do with the parent class
# dev_1 = Developer("Corey", "Schafer", 50000, 'python')
# dev_2 = Developer("Test", "employee", 60000, 'java')
# print(dev_1.email)
# print(dev_2.prog_lang)

# (4)
# mgr_1 = Manager('Sue', 'Smith', '90000', [dev_1])
# print(mgr_1.email)
# mgr_1.add_employee(dev_2)
# mgr_1.print_emp()

# Suppose that we want to assure if a given object is an instance of a specific class or not
# print(isinstance(mgr_1, Manager))
# print(isinstance(mgr_1, Developer))
# print(issubclass(Developer, Employee))
# print(issubclass(Manager, Developer))
